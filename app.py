from flask import Flask, render_template, request, redirect, url_for
from ClasesPOO.CategoriaProducto import CategoriaProducto
from ClasesPOO.Producto import Producto
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

    return render_template('admin_dashboard.html', productos=productos)

@app.route('/editar_producto/<int:id_producto>', methods=['GET', 'POST'])
def editar_producto(id_producto):
    # Obtén el producto por su ID desde la base de datos
    conn = sqlite3.connect('jumbox.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM producto WHERE id_producto = ?", (id_producto,))
    producto_data = cursor.fetchone()
    conn.close()

    if producto_data:
        if request.method == 'POST':
            # Actualiza los datos del producto en la base de datos
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            precio = request.form['precio']
            conn = sqlite3.connect('jumbox.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE producto SET nombre = ?, descripcion = ?, precio = ? WHERE id_producto = ?", (nombre, descripcion, precio, id_producto))
            conn.commit()
            conn.close()
            return redirect(url_for('admin_dashboard'))

        return render_template('editar_producto.html', producto=producto_data)

    return 'Producto no encontrado', 404

@app.route('/eliminar_producto/<int:id_producto>')
def eliminar_producto(id_producto):
    # Elimina el producto de la base de datos
    conn = sqlite3.connect('jumbox.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producto WHERE id_producto = ?", (id_producto,))
    conn.commit()
    conn.close()
    return 'Producto eliminado exitosamente'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
