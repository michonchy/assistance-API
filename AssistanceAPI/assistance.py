import json

def json_response(code:int,body:dict):
    return{
    "statusCode": code,
    "headers":{
        "Content-Type": "application/json"
    },
    "body":json.dumps(body)
    }