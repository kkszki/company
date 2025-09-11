from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.', static_folder='.')

names = {
    "konnektor": "Konnektor bekötés",
    "lampa": "Lámpa bekötés",
    "kapcsolo": "Kapcsoló bekötés",
    "amper": "Amper bővítés",
    "eloszto": "Elosztó tábla csere / bővítés",
    "villanytuzhely": "Villanytűzhely bekötés",
    "bojler": "Villanybojler bekötés",
    "fi-rele": "FI-relé beépítés",
    "foldeles": "Földelés kiépítése",
    "vezetekcsere": "Vezetékcsere / újrahúzás",
    "ujkiadas": "Teljes új kiépítés",
    "terv": "Tervezés / dokumentáció",
    "meres": "Érintésvédelmi / szabványossági mérés",
    "ai-asszisztens": "AI asszisztens / hangvezérlés",
    "okos-kamera": "Okos kamera / megfigyelés",
    "telefonos-vezerles": "Telefonos vezérlés (app)",
    "automatizalas": "Automatizálás (időzítés, jelenlét)",
    "okos-kapcsolo": "Okos kapcsolók / relék",
    "szenzorok": "Szenzorok (mozgás, füst, hőmérséklet)",
    "helyiseg-vezerles": "Helyiségek szerinti vezérlés",
    "futes": "Fűtés vezérlés"
}

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

@app.route('/calc', methods=["GET", "POST"])
def calc():
    rendelt = []
    selected_fazis = None
    osszeg = 0
    egyedi = ""
    if request.method == "POST":
        selected_fazis = request.form.get('fazis')
        for name, magyarul in names.items():
            if name in request.form:
                osszeg += arak[name]
                rendelt.append(magyarul)
        if selected_fazis == "3":
            osszeg *= 2
        egyedi = request.form.get("egyedi-kert", "")
    return render_template('calc.html', osszeg=osszeg, rendelt=rendelt, egyedi=egyedi)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rolunk')
def rolunk():
    return render_template('rolunk.html')

if __name__ == '__main__':
    app.run(debug=True)
