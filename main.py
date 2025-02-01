from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello2', methods=['GET'])
def hello_world2():
    return jsonify({'message': 'Hello, Aruni'})

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Missing parameters'}), 400
    
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 + num2 + 2
        return jsonify({'sum': result})
    except ValueError:
        return jsonify({'error': 'Invalid input, numbers expected'}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
