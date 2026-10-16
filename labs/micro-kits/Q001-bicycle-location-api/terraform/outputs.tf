output "api_url" {
  description = "HTTP API endpoint protected with AWS_IAM."
  value = "${aws_apigatewayv2_api.http.api_endpoint}/locations"
}
output "lambda_function_name" {
  value = aws_lambda_function.receiver.function_name
}
output "cloudwatch_log_group" {
  value = aws_cloudwatch_log_group.lambda.name
}
