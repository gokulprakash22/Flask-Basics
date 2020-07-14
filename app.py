from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/path')
def path():
    return render_template('path.html')

@app.route('/path/<path_variable>')
def get_path_variable(path_variable):
    return render_template('path.html',path_variable=path_variable)

@app.route('/pdf')
def show_pdf():
    with open('./flask_tutorial.pdf', 'rb') as static_file:
        return send_file(static_file, attachment_filename='file.pdf')

if __name__=="__main__":
    app.run(debug=True)