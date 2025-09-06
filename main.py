from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.', static_folder='.')


names = [
    "konnektor",
    "lampa",
    "kapcsolo",
    "amper",
    "eloszto",
    "villanytuzhely",
    "bojler",
    "fi-rele",
    "foldeles",
    "vezetekcsere",
    "ujkiadas",
    "terv",
    "meres",
    "ai-asszisztens",
    "okos-kamera",
    "telefonos-vezerles",
    "automatizalas",
    "okos-kapcsolo",
    "szenzorok",
    "helyiseg-vezerles",
    "futes"
]


@app.route('/', methods=["GET", "POST"])
def index():
    global names
    
    if request.method == "POST":
        selected_fazis = request.form.get('fazis')
    if selected_fazis:
        print(f"A kiválasztott fázis: {selected_fazis}")
    else:
        print("Nem lett kiválasztva fázis.")
    for name in names:
        if name in request.form:
        # Csak kiírjuk a name-ot, ha be van pipálva
            print (f"A bejelölt checkbox neve: {name}")
    

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
