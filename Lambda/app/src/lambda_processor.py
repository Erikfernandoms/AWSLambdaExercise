from src.sqs import SQSService
from src.dynamo import DynamoService


def process(event, params, sqs_service: SQSService, dynamo_service: DynamoService):
    sqs_service.send_msg(event["Message"]["Sqs"])

    if event["Message"]["Operacao"] == "inserir":
        item = {
                'id':{'S': event["Message"]["Dynamo"]["Id"]},
                'nome':{'S':event["Message"]["Dynamo"]["Nome"]},
                'idade':{'S': event["Message"]["Dynamo"]["Idade"]}
             }
        result = dynamo_service.put_item(item=item)
    elif event["Message"]["Operacao"] == "atualizar":
        key={
        'id': event["Message"]["Dynamo"]["Id"],
        },
        UpdateExpression="set nome = :nome",
        ExpressionAttributeValues={
            ':nome': event["Message"]["Dynamo"]["Nome"],
        }
        result = dynamo_service.update_item(key=key, update_expression=UpdateExpression, att_values=ExpressionAttributeValues)
    elif event["Message"]["Operacao"] == "consultar":
        result = dynamo_service.get_item(key={"Id": {"S": event["Message"]["Dynamo"]["Id"]}})
    else:
        raise Exception("Operacao invalida ou não informada")
    return result
    