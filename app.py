from flask import Flask, request, json,jsonify

from db import insert_response, get_responses
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/',methods=['GET'])
def get_response():
    responses = get_responses()
    return jsonify(responses)
@app.route('/response',methods=['POST'])
def send_reponse():
    data = request.get_json()
    print(data)
    string_response = json.dumps(data)
    insert_response(sender="safaricom",response=string_response)
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

