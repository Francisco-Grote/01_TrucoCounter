total_nosotros = 0
total_ellos = 0
nombre = ""
mensaje_finalizacion = "La partida se ha terminado"

def nombre_del_grupo():
    global nombre
    return nombre

def suma_nosotros():
    global total_nosotros
    total_nosotros += 1
    finalizar_partida_automaticamente()

def resta_nosotros():
    global total_nosotros
    if total_nosotros > 0:  # Evitar números negativos
        total_nosotros -= 1

def suma_ellos():
    global total_ellos
    total_ellos += 1
    finalizar_partida_automaticamente()

def resta_ellos():
    global total_ellos
    if total_ellos > 0:  # Evitar números negativos
        total_ellos -= 1

def boton_reiniciar():
    global total_nosotros, total_ellos
    total_ellos = 0
    total_nosotros = 0

def finalizar_partida_automaticamente():
    global total_ellos, total_nosotros, mensaje_finalizacion
    if total_nosotros >= 30 or total_ellos >= 30:
        boton_reiniciar()
        return mensaje_finalizacion
    
def numero_a_palitos(numero):
    grupos_de_5 = numero // 5
    palitos_sueltos = numero % 5
    
    html = ""
    
    for i in range(grupos_de_5):
        html += '<div class="grupo-cinco"></div>'
    
    if palitos_sueltos > 0:
        html += f'<div class="palitos-sueltos" data-count="{palitos_sueltos}"></div>'
    
    return html