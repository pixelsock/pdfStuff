from flask import Flask, render_template, request, redirect, url_for, send_file
from ocr import extract_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    output_format = request.form['output_format']
    output_data = extract_data(file, output_format)
    return redirect(url_for('download', data=output_data))

@app.route('/download')
def download():
    data = request.args.get('data')
    return send_file(data, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)