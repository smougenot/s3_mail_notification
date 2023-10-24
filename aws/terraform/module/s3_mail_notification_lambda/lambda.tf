
variable "cloudwatch_log_retention_in_days" {
  default = 7
}

locals {
  description = "created by terraform module github.com/dirt-simple/terraform-aws-s3-event-bus"
  name        = "dirt-simple-s3-event-bus"
}

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
  runtime                        = "python3.6"
  handler                        = "index.handler"
  memory_size                    = 128
  reserved_concurrent_executions = 15
  publish                        = true
  description                    = local.description
  tags                           = var.tags

  environment {
    variables = {
      S3_EVENT_BUS_TOPIC_ARN = aws_sns_topic.event_bus_topic.arn
    }
  }
}

resource "aws_cloudwatch_log_group" "lambda" {
  name              = "/aws/lambda/${local.name}"
  retention_in_days = var.cloudwatch_log_retention_in_days
  tags              = var.tags
}

output "s3_event_bus_topic_arn" {
  value = aws_sns_topic.event_bus_topic.arn
}

output "s3_event_bus_topic_name" {
  value = aws_sns_topic.event_bus_topic.name
}
