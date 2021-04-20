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
    return render_template("cuenta.html")

@app.route('/libro/')
def libro():
    return render_template("libro.html")
app.run(debug=True)
