from flask import Flask, render_template, request, jsonify
from google.cloud import vision
from google.oauth2 import service_account
from werkzeug.utils import secure_filename
import os
import re
import csv


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Přihlašovací údaje ke Google Vision API
creds = service_account.Credentials.from_service_account_file("credentials.json")
client = vision.ImageAnnotatorClient(credentials=creds)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' not in request.files:
        return 'No file part', 400
    file = request.files['photo']
    if file.filename == '':
        return 'No selected file', 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    with open(filepath, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations

    if not texts:
        return jsonify({"recognized_number": None})

    full_text = texts[0].description
    match = re.search(r'\b\d{6}\b', full_text)
    number = match.group(0) if match else None

    return jsonify({"recognized_number": number})

@app.route('/save', methods=['POST'])
def save():
    number = request.form.get('number')
    if not number:
        return jsonify({"error": "Missing number"}), 400

    try:
        with open('output.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([number])
        # Vrátit JSON s uloženým číslem
        return jsonify({"saved_number": number}), 200
    except Exception as e:
        print(f"Error saving number: {e}")
        return jsonify({"error": "Error saving number"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)