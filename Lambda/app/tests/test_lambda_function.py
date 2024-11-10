from unittest.mock import patch
import pytest

with patch("src.sqs.SQSService"):
    with patch("src.dynamo.DynamoService"):
        from lambda_function import lambda_handler


@patch("lambda_function.process")
def test_lambda_function_success(mock_process, payload_sucesso):
    mock_process.return_value = "Registro inserido com sucesso"
    result = lambda_handler(payload_sucesso, "")
    assert result == "Registro inserido com sucesso"

@patch("src.lambda_processor.process")
def test_lambda_function_error(mock_process,payload_error):
    mock_process.return_value = Exception("Erro interno")

    mock_process.setattr("lambda_function.process", mock_process)

    with pytest.raises(Exception):
        result = lambda_handler(payload_error, "")
