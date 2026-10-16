variable "aws_region" {
  description = "Region selected after reviewing cost and eligibility."
  type = string
  default = "eu-central-1"
}
variable "lab_name_suffix" {
  description = "Unique lower-case suffix: do not reuse another person's resources."
  type = string
  default = "study"
  validation {
    condition = can(regex("^[a-z0-9-]{1,15}$", var.lab_name_suffix))
    error_message = "Use 1–15 lowercase letters, digits or hyphens."
  }
}
