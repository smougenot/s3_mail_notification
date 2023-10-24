variable "lambda_name" {
  default     = "dirt-simple-s3-event-bus"
  type        = string
  description = "Lambda name"
}

variable "cloudwatch_log_retention_in_days" {
  type    = number
  default = 7
}

variable "lambda_runtime" {
  default     = "python3.10"
  type        = string
  description = "Lambda runtime declaration."
}

variable "lambda_handler" {
  default     = "index.handler"
  type        = string
  description = "Lambda handler declaration."
}

variable "lambda_reserved_concurrent_executions" {
  default     = 3
  description = "Lambda reserved_concurrent_executions declaration."
  type        = number
}

variable "lambda_memory_size" {
  default     = 128
  type        = number
  description = "Lambda memory size declaration"
}
