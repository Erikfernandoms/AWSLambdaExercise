import os

def get_os_params():
    return {
        "QueueUrl": os.environ.get("QueueUrl"),
        "DynamoTable": os.environ.get("DynamoTable")
    }