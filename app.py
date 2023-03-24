from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, Snowpack!'

@app.route('/', methods=['POST'])
def post_request():
    data = request.get_json()
    return data['message']

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
