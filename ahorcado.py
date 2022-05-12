from csv import list_dialects
import random
from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "Esto no debería ir aqui."

@app.route("/")
def index():
    session["listaLetras"] = []
    session["fallos"] = 0
    #return render_template("elegirPalabra.html", nombre = "khe onda")
    return render_template("inicio.html")


@app.route("/elegir_palabra")
def elegir_palabra():
    lista = ["spiderman", "Batman", "Capitan America", "Hulk"]
    session["palabra"] = random.choice(lista).lower()
    print(session["listaLetras"])
    return render_template("ahorcado.html", palabraElegida = session["palabra"], lista_letras = session["listaLetras"], fallos = session["fallos"])

@app.route("/elegir_letra/<letra>")
def elegir_letra(letra):
    contador = 0
    letra = letra.lower()
    listaLetras =  session["listaLetras"]
    listaLetras.append(letra)
    session["listaLetras"] = listaLetras
    palabra = session["palabra"]
    if letra in palabra:
        for i in palabra:
            if (i in listaLetras):
                contador += 1
        palabra2 = palabra.replace(" ","")
        if (contador == len(palabra2)):
            return render_template("ganaste.html")
    else:
        session["fallos"] +=1
        if session["fallos"] > 6:
             return render_template("perdiste.html")
    return render_template("ahorcado.html", palabraElegida = palabra, lista_letras = listaLetras, fallos = session["fallos"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)