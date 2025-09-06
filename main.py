from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        valasztasok = {
            "fazis": request.form.get("fazis"),
            }
        print( f"Bejelölt opciók: {valasztasok}")
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
