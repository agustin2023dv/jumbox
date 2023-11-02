from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin_dashboard')
def admin_dashboard():

# Conectar a la base de datos SQLite3 (reemplaza 'tu_base_de_datos.db' con tu base de datos real)
    conn = sqlite3.connect('jumbox.db')
    cursor = conn.cursor()

    # Ejecuta una consulta para obtener los productos desde la base de datos
    cursor.execute("SELECT nombre, precio, descripcion FROM producto")
    productos = cursor.fetchall()

    # Cierra la conexión a la base de datos
    conn.close()

    return render_template('admin_dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
