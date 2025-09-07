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

arak = {
    "konnektor": 3000,
    "lampa": 2500,
    "kapcsolo": 2000,
    "amper": 15000,
    "eloszto": 8000,
    "villanytuzhely": 12000,
    "bojler": 15000,
    "fi-rele": 5000,
    "foldeles": 20000,
    "vezetekcsere": 30000,
    "ujkiadas": 100000,
    "terv": 20000,
    "meres": 10000,
    "ai-asszisztens": 50000,
    "okos-kamera": 25000,
    "telefonos-vezerles": 30000,
    "automatizalas": 35000,
    "okos-kapcsolo": 15000,
    "szenzorok": 20000,
    "helyiseg-vezerles": 25000,
    "futes": 30000
}

@app.route('/', methods=["GET", "POST"])
def index():
    selected_fazis = None
    osszeg = 0
    if request.method == "POST":
        selected_fazis = request.form.get('fazis')
        # Számítás
        for name in names:
            if name in request.form:
                print(name)
                osszeg += arak[name]
        if selected_fazis == "3":
            osszeg = osszeg * 2
        egyedi=request.form.get("egyedi-kert")
        print(egyedi)
        print(f"Számított összeg: {osszeg}")
  
    return render_template('index.html', osszeg=osszeg)

if __name__ == '__main__':
    app.run(debug=True)
