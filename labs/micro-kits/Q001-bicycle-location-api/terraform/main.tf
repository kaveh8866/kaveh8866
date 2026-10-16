locals {
  prefix = "aws-micro-q001"
  function_name = "${local.prefix}-receiver-${var.lab_name_suffix}"
}
data "archive_file" "lambda" {
  type = "zip"
  source_file = "${path.module}/../lambda/handler.py"
  output_path = "${path.module}/.q001-handler.zip"
}
resource "aws_iam_role" "lambda" {
  name = "${local.prefix}-lambda-role-${var.lab_name_suffix}"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = "sts:AssumeRole"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}
resource "aws_iam_role_policy_attachment" "logs" {
  role = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
resource "aws_cloudwatch_log_group" "lambda" {
  name = "/aws/lambda/${local.function_name}"
  retention_in_days = 1
}
resource "aws_lambda_function" "receiver" {
  function_name = local.function_name
  role = aws_iam_role.lambda.arn
  runtime = "python3.12"
  handler = "handler.lambda_handler"
  memory_size = 128
  timeout = 5
  filename = data.archive_file.lambda.output_path
  source_code_hash = data.archive_file.lambda.output_base64sha256
  depends_on = [aws_iam_role_policy_attachment.logs, aws_cloudwatch_log_group.lambda]
}
resource "aws_apigatewayv2_api" "http" {
  name = "${local.prefix}-http-${var.lab_name_suffix}"
  protocol_type = "HTTP"
}
resource "aws_apigatewayv2_integration" "lambda" {
  api_id = aws_apigatewayv2_api.http.id
  integration_type = "AWS_PROXY"
  integration_uri = aws_lambda_function.receiver.invoke_arn
  integration_method = "POST"
  payload_format_version = "2.0"
}
resource "aws_apigatewayv2_route" "post" {
  api_id = aws_apigatewayv2_api.http.id
  route_key = "POST /locations"
  target = "integrations/${aws_apigatewayv2_integration.lambda.id}"
  authorization_type = "AWS_IAM"
}
resource "aws_apigatewayv2_stage" "default" {
  api_id = aws_apigatewayv2_api.http.id
  name = "$default"
  auto_deploy = true
  default_route_settings {
    throttling_burst_limit = 2
    throttling_rate_limit = 1
  }
  depends_on = [aws_apigatewayv2_route.post]
}
resource "aws_lambda_permission" "gateway" {
  statement_id = "AllowInvokeOnlyQ001Post"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.receiver.function_name
  principal = "apigateway.amazonaws.com"
  source_arn = "${aws_apigatewayv2_api.http.execution_arn}/*/POST/locations"
}
