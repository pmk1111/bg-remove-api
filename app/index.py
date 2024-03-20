from flask import Flask, jsonify, request
from flask_cors import CORS
from rembg import remove

app = Flask(__name__)
CORS(app)  # 모든 출처에서의 요청을 허용합니다.

@app.route('/hello', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json()
        result = {"message": "Hello, world!"}
        return jsonify(result)
    
@app.route('/removebg', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return "No image provided", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected image", 400

    image_data = file.read()
    processed_image_data = remove(image_data)

if __name__ == '__main__':
    app.run(debug=True, port=9500)

