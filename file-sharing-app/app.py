from flask import Flask, request, send_from_directory, render_template
import os
import tempfile

app = Flask(__name__)

# Use a temporary directory for uploads to handle Vercel's immutable storage
UPLOAD_FOLDER = tempfile.gettempdir()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # List all files in the temporary uploads directory
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
    except Exception:
        files = []  # Return an empty list if directory is inaccessible
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded!", 400
    file = request.files['file']
    if file and file.filename:
        # Save the file to the temporary upload folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return "File uploaded successfully!", 200
    return "Invalid file!", 400

@app.route('/uploads/<filename>')
def download_file(filename):
    # Serve files from the temporary uploads directory
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except Exception:
        return "File not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
