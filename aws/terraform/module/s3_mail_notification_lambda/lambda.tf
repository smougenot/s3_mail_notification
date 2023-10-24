locals {
  description = "created by terraform module github.com/dirt-simple/terraform-aws-s3-event-bus"
  name        = var.lambda_name
}
#TODO allow to choose archive
data "archive_file" "lambda" {
  type        = "zip"
  output_path = "${path.module}/.zip/lambda.zip"
  source_dir  = "${path.module}/lambda"

}

resource "aws_lambda_function" "lambda" {
  function_name                  = local.name
  filename                       = data.archive_file.lambda.output_path
  source_code_hash               = data.archive_file.lambda.output_base64sha256
  role                           = aws_iam_role.lambda.arn
  runtime                        = var.lambda_runtime
  handler                        = var.lambda_handler
  memory_size                    = var.lambda_memory_size
  reserved_concurrent_executions = var.lambda_reserved_concurrent_executions
  publish                        = true
  description                    = local.description

  environment {
    variables = {
      # TODO define mail environment variables
      NEED_MAIl_SETUP = ""
    }
  }
}

resource "aws_cloudwatch_log_group" "lambda" {
  name              = "/aws/lambda/${local.name}"
  retention_in_days = var.cloudwatch_log_retention_in_days
}

output "s3_event_bus_topic_arn" {
  value = aws_sns_topic.event_bus_topic.arn
}

output "s3_event_bus_topic_name" {
  value = aws_sns_topic.event_bus_topic.name
}
