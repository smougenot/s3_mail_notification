variable "bucket_name" {
  description = "The bucket to setup for the s3 notification."
  type        = string
}
variable "lambda_function_name" {
  description = "The lambda function to be triggered on notification."
  type        = string
}
variable "events_to_notify" {
  description = "List of events tot rigger notification for. Default is on creation. See aws_s3_bucket_notification attribute events for more details."
  default     = ["s3:ObjectCreated:*"]
}
