#from typing import any
class ResponseApi:
    def __init__(self, statusCode, body, message):
        self.statusCode = statusCode
        self.body = body
        self.message = message
        
    def to_dict(self):
        return {
            'statusCode':self.statusCode,
            'message':self.message,
            'body':self.body
        }