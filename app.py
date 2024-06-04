from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return "¡Bienvenido a la Aplicación 'Saludo' de Salvador Flores!"

@app.route('/saludo', methods=['GET', 'POST'])
def saludo():
    if request.method == 'POST':
        usuario = request.form['usuario']
        fecha_nacimiento = request.form['fecha_nacimiento']
        return f"¡Hola, {usuario}! Le damos la bienvenida a nuestro servicio exclusivo.<br>Su fecha de nacimiento es {fecha_nacimiento}."
    return '''
        <title>saludo</title>
        <form method="post">
            Usuario: <input type="text" name="usuario"><br>
            Fecha de Nacimiento: <input type="date" name="fecha_nacimiento"><br>
            <input type="submit" value="Enviar">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
