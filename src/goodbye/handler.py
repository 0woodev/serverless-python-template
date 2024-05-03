import json


def lambda_handler(event, context):
    request_body_params = json.loads(event.get('body', '{}'))
    name = request_body_params.get('name', 'Anonymous')

    body = {
        "message": f"Goodbye! {name}",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
