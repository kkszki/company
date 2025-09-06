from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

# Külön útvonal a favicon-hoz
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'logo.png', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
