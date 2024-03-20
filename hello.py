from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json()

        result = {"message": "Hello, world!"}

        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=9500)
