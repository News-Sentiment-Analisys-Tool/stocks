from flask import Flask
from flask import request
import json
from yahooquery import Ticker

app = Flask(__name__)

@app.route('/stock',methods=['GET'])
def run():

    code = request.args.get('code')
    start = request.args.get('start')
    end = request.args.get('end')

    ticker = Ticker("${}.SA".format(code))

    df = ticker.history(start=start, end=end)

    body = df.to_json(orient = 'table')

    return json.dumps(json.loads(body)['data'])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)