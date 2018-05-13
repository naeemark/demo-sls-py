import json


def hello(event, context):

    body = dict()

    try:
        body['method'] = event['httpMethod']
        if event['httpMethod'] == 'POST':
            body['message'] = "Called POST Method"
            body['input'] = event['body']
        else:
            body['message'] = "Go Serverless v1.0! Your function executed successfully!"
            body['input'] = event
    except Exception as e:
        body['message'] = str(e)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
