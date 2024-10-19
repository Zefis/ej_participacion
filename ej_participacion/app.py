from flask import Flask, render_template, redirect, request, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'unaclavesecreta'  # Necesario para manejar las sesiones

#usaremos un diccionario
users = {
    "Zefis": "1234",
    "user_2": "1234",
    "user_3": "1234"
}

# Ruta para el inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificar si el usuario está en nuestra el diccionario
        if username in users and users[username] == password:
            # Almacenar información en la sesión
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.')
            return redirect(url_for('login'))
    return render_template('login.html')

# Ruta para la página de bienvenida después de iniciar sesión
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    else:
        flash('Inicia sesión para acceder a esta página.')
        return redirect(url_for('login'))

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminar el nombre de usuario de la sesión
    flash('Has cerrado sesión exitosamente.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
