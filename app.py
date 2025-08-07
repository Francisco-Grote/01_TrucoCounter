from flask import Flask, render_template, request, redirect, url_for, session
import operaciones

app = Flask(__name__)
app.secret_key = 'truco_counter_secret_key_2024'  # Necesario para sessions

@app.route("/")
def inicio():
    if 'session_started' not in session:
        operaciones.nombre = ""
        operaciones.total_nosotros = 0
        operaciones.total_ellos = 0
        session['session_started'] = True
    
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
    session['nombre_configurado'] = True
    return redirect(url_for("inicio"))

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)