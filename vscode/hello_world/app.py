import json
import socket

# import requests

import ptvsd
import sys

ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
print("waiting for debugger to attach...")
sys.stdout.flush()
ptvsd.wait_for_attach()


def lambda_handler(event, context):
  
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    print("VS Debug test")
    ip = socket.gethostbyname(socket.gethostname())
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip.replace("\n", "")
        }),
    }
