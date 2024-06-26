from flask import Flask, request, json,jsonify

from db import insert_response, get_responses

app = Flask(__name__)

app.route('/',methods=['GET',])
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


if __name__ == '__main__':
    app.run()
