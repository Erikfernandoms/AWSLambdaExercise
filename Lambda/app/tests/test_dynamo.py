from src.dynamo import DynamoService
import boto3
from moto import mock_aws

@mock_aws
def test_get_item():
    client = boto3.client('dynamodb', 'sa-east-1')
    client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'Id',
                'AttributeType': 'S'
            },
        ],
        TableName="tabelateste",
        KeySchema=[
        {
            'AttributeName': 'Id',
            'KeyType': 'HASH'
        }
        ],
        ProvisionedThroughput={
        'ReadCapacityUnits': 123,
        'WriteCapacityUnits': 123
        },
    )

    client.put_item(TableName="tabelateste",Item={
                'Id':{'S': "1"},
                'nome':{'S': "Erik"},
                'idade':{'S': "23"}
            })
    client.put_item(TableName="tabelateste",Item={
                'Id':{'S': "2"},
                'nome':{'S': "Well"},
                'idade':{'S': "74"}
            })
    client.put_item(TableName="tabelateste",Item={
                'Id':{'S': "3"},
                'nome':{'S': "Caique"},
                'idade':{'S': "42"}
            })
    
    
    dynamo_service = DynamoService(boto3.session.Session(region_name="sa-east-1"), "tabelateste")
    result = dynamo_service.get_item(key = {'Id': {"S": "1"}})
    assert result["Item"]["nome"]["S"] == "Erik"
    result = dynamo_service.get_item(key = {'Id': {"S": "2"}})
    assert result["Item"]["nome"]["S"] == "Well"
    result = dynamo_service.get_item(key = {'Id': {"S": "3"}})
    assert result["Item"]["nome"]["S"] == "Caique"


def test_update_item():
    pass

def test_put_item():
    pass