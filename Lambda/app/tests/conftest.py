from pytest import fixture


@fixture
def payload_sucesso():
    return {
        "Message": {
            "Sqs": "Está é uma mensagem teste",
            "Dynamo": {
                    "Id": 1,
                    "Nome": "Erik",
                    "Idade": "23"
            },
            "Operacao": "inserir"
        }
    }

@fixture
def payload_error():
    return {
        "Message": {
            "Sqs": "Está é uma mensagem teste",
            "Dynamo": {
                    "Id": 1,
                    "Nome": "Erik",
                    "Idade": "23"
            },
            "Operacao": ""
        }
    }