from src.lambda_processor import process
from src.config import get_os_params
from src.sqs import SQSService
from src.dynamo import DynamoService
import boto3
import boto3.session

# Create your own session
session = boto3.session.Session()
params = get_os_params()
sqs_service = SQSService(session, params["QueueUrl"])
dynamo_service = DynamoService(session, params["DynamoTable"])

def lambda_handler(event, context):
    try:
        result = process(event, params, sqs_service, dynamo_service)
        return result
    except Exception as e:
        raise e