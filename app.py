from flask import Flask, request, json

from db import insert_response

app = Flask(__name__)


@app.route('/',methods=['POST'])
def get_reponse():
    data = request.get_json()
    string_response = json.dumps(data)
    insert_response(sender="safaricom",response=string_response)
    return data


if __name__ == '__main__':
    app.run()
