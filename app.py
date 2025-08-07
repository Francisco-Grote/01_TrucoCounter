from flask import Flask, render_template, request, redirect, url_for
import operaciones

app = Flask(__name__)

@app.route("/")
def inicio():
    nosotros_palitos = operaciones.numero_a_palitos(operaciones.total_nosotros)
    ellos_palitos = operaciones.numero_a_palitos(operaciones.total_ellos)
    return render_template('index.html', nosotros=nosotros_palitos, ellos=ellos_palitos, nombre_grupo=operaciones.nombre)

@app.route("/suma_nosotros")
def suma_nosotros():
    operaciones.suma_nosotros()
    nosotros_palitos = operaciones.numero_a_palitos(operaciones.total_nosotros)
    ellos_palitos = operaciones.numero_a_palitos(operaciones.total_ellos)
    return render_template('index.html', nosotros=nosotros_palitos, ellos=ellos_palitos, nombre_grupo=operaciones.nombre)

@app.route("/resta_nosotros")
def resta_nosotros():
    operaciones.resta_nosotros()
    nosotros_palitos = operaciones.numero_a_palitos(operaciones.total_nosotros)
    ellos_palitos = operaciones.numero_a_palitos(operaciones.total_ellos)
    return render_template('index.html', nosotros=nosotros_palitos, ellos=ellos_palitos, nombre_grupo=operaciones.nombre)

@app.route("/suma_ellos")
def suma_ellos():
    operaciones.suma_ellos()
    nosotros_palitos = operaciones.numero_a_palitos(operaciones.total_nosotros)
    ellos_palitos = operaciones.numero_a_palitos(operaciones.total_ellos)
    return render_template('index.html', nosotros=nosotros_palitos, ellos=ellos_palitos, nombre_grupo=operaciones.nombre)

@app.route("/resta_ellos")
def resta_ellos():
    operaciones.resta_ellos()
    nosotros_palitos = operaciones.numero_a_palitos(operaciones.total_nosotros)
    ellos_palitos = operaciones.numero_a_palitos(operaciones.total_ellos)
    return render_template('index.html', nosotros=nosotros_palitos, ellos=ellos_palitos, nombre_grupo=operaciones.nombre)

@app.route("/boton_reiniciar")
def boton_reiniciar():
    operaciones.boton_reiniciar()
    nosotros_palitos = operaciones.numero_a_palitos(operaciones.total_nosotros)
    ellos_palitos = operaciones.numero_a_palitos(operaciones.total_ellos)
    return render_template('index.html', nosotros=nosotros_palitos, ellos=ellos_palitos, nombre_grupo=operaciones.nombre)

@app.route("/guardar_nombre", methods=["POST"])
def guardar_nombre():
    operaciones.nombre = request.form["nombre_grupo"]
    return redirect(url_for("inicio"))

app.run()