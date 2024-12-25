from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

# Path to the folder containing your pre-loaded files
FILES_FOLDER = './files'
app.config['FILES_FOLDER'] = FILES_FOLDER

@app.route('/')
def index():
    # Get the list of available files in the 'files' folder
    try:
        files = os.listdir(app.config['FILES_FOLDER'])
    except FileNotFoundError:
        files = []
    return render_template('index.html', files=files)

@app.route('/files/<filename>')
def download_file(filename):
    try:
        return send_from_directory(app.config['FILES_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)
