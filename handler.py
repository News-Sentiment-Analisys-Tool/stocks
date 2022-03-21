import json
from yahooquery import Ticker

def run(event, context):
    data = event['queryStringParameters']
    
    code = data['code']
    start = data['start']
    end = data['end']

    ticker = Ticker("${}.SA".format(code))

    df = ticker.history(start=start, end=end)

    body = df.to_json(orient = 'table')

    response = {
        "statusCode": 200,
        "body": json.dumps(json.loads(body)['data']),
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*',
        },
    }

    return response

run({
    'queryStringParameters': {
        "start": "2022-03-10",
        "end": "2022-03-20",
        "code": "PETR4"
    }
}, {})