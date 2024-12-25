from flask import Flask, request, send_from_directory, render_template
import os
import tempfile

UPLOAD_FOLDER = tempfile.gettempdir()

app = Flask(__name__)

# Directory to save uploaded files
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # List all files in the uploads folder
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        print(f"Files in uploads folder: {files}")  # Debugging line
    except Exception as e:
        print(f"Error listing files: {e}")
        files = []
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        print("No file part in the request")  # Debugging line
        return "No file uploaded!", 400
    file = request.files['file']
    if file and file.filename:
        try:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            print(f"File saved successfully at {filepath}")  # Debugging line
        except Exception as e:
            print(f"Error saving file: {e}")
            return "File upload failed!", 500
        return "File uploaded successfully!", 200
    else:
        return "Invalid file!", 400

@app.route('/uploads/<filename>')
def download_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except Exception as e:
        print(f"Error downloading file: {e}")
        return "File not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
