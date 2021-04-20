from flask import Flask, render_template,abort
from lxml import etree

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
    doc = etree.parse('libros.xml')
    codigo=123
    libro=doc.xpath('//libro/codigo[text()="%i"]/../titulo/text()' % codigo)
    autor=doc.xpath('//libro/codigo[text()="%i"]/../autor/text()' % codigo)
    return render_template("libro.html",libro=libro[0],autor=autor[0])

@app.route('/libro/<int:numero>')
def buscalibro(numero):
    doc = etree.parse('libros.xml')
    codigo=numero
    libro=doc.xpath('//libro/codigo[text()="%i"]/../titulo/text()' % codigo)
    autor=doc.xpath('//libro/codigo[text()="%i"]/../autor/text()' % codigo)
    if len(libro)  == 0:
        abort(404)
    return render_template("libro.html",libro=libro[0],autor=autor[0])
app.run(debug=True)