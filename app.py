from flask import Flask, render_template,abort

app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/potencia/')
def potencia():
    base=0
    exponente=0
    return render_template("potencia.html",base=base,exponente=exponente,resultado=base**exponente)

@app.route('/potencia/<int:num1>/<num2>')
def calculapotencia(num1,num2):
    base=num1
    exponente=int(num2)
    if exponente >0:
        resultado= base**exponente
    if exponente == 0:
        resultado=1
    if exponente < 0:
        resultado=1/base**exponente
    return render_template("potencia.html",base=base,exponente=exponente,resultado=resultado)

@app.route('/cuenta/')
def cuenta():
    palabra="hola"
    letra="h"
    if len(letra) > 1:
        abort(404)
    resultado=palabra.count(letra)
    return render_template("cuenta.html",palabra=palabra,letra=letra,resultado=resultado)
    
@app.route('/cuenta/<cadena1>/<cadena2>')
def hacecuenta(cadena1,cadena2):
    palabra=cadena1
    letra=cadena2
    if len(letra) > 1:
        abort(404)
    resultado=palabra.count(letra)
    return render_template("cuenta.html",palabra=palabra,letra=letra,resultado=resultado)

@app.route('/libro/')
def libro():
    return render_template("libro.html")
app.run(debug=True)
