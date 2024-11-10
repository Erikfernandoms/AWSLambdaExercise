

class SQSService:
    def __init__(self, session, url):
        self.client = session.client('sqs')
        self.url = url
    
    def send_msg(self, msg):
        response = self.client.send_message(QueueUrl=self.url,MessageBody=msg)
        return response