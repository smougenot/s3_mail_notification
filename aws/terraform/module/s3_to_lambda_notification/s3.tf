data "aws_lambda_function" "lambda_function" {
  # Lambda function must exists
  function_name = var.lambda_function_name
}

data "aws_s3_bucket" "s3_bucket" {
  # Bucket must exists
  bucket = var.bucket_name
}

resource "aws_s3_bucket_notification" "s3_event_bus" {
  bucket = var.bucket_name
  lambda_function {
    id                  = data.aws_s3_bucket.s3_bucket.bucket
    lambda_function_arn = data.aws_lambda_function.lambda_function.arn
    events              = var.events_to_notify
  }
}

resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowBucket-${data.aws_s3_bucket.s3_bucket.bucket}"
  action        = "lambda:InvokeFunction"
  function_name = data.aws_lambda_function.lambda_function.arn
  principal     = "s3.amazonaws.com"
  source_arn    = "arn:aws:s3:::${data.aws_s3_bucket.s3_bucket.bucket}"
}
