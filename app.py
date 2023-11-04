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
    # Conectar a la base de datos SQLite3 
    conn = sqlite3.connect('jumbox.db')
    cursor = conn.cursor()
    
    # Ejecuta una consulta para obtener los productos desde la base de datos
    cursor.execute("SELECT nombre, precio, descripcion, id_producto, categoria_id FROM producto")
    productos = cursor.fetchall()

    # Se cierra la conexión a la base de datos
    conn.close()

    return render_template('admin_dashboard.html', productos=productos)

@app.route('/editar_producto/<int:id_producto>', methods=['GET', 'POST'])
def editar_producto(id_producto):
    # Obtener el producto por su ID desde la base de datos
    print(f'ID del producto a editar: {id_producto}')
    conn = sqlite3.connect('jumbox.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM producto WHERE id_producto = ?", (id_producto,))
    producto_data = cursor.fetchone()
    conn.close()

    if producto_data:
        if request.method == 'POST':
            # Obtener los nuevos valores desde el formulario
            nombre = request.form['nombre']
            
            descripcion = request.form['descripcion']
            precio = request.form['precio']
            categoria_id = request.form['categoria_id']
            

            print(f"Nombre: {nombre}, Descripción: {descripcion}, Precio: {precio}, Categoría ID: {categoria_id}, ID Producto: {id_producto}")
            producto = Producto(id_producto,nombre,descripcion,precio)

            producto.actualizar(nombre, descripcion, precio, categoria_id, id_producto)

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
