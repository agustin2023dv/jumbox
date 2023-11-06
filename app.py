
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_args
from ClasesPOO.Producto import Producto  # Importacion la clase Producto desde un módulo externo
import sqlite3

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define la ruta principal que renderiza la plantilla 'index.html'
@app.route('/')
def index():
    return render_template('index.html')

# Define la ruta '/admin_dashboard' para la página de administración del dashboard
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

    # Configura la paginación
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(productos)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    # Divide la lista de productos en páginas
    productos_paginados = productos[offset: offset + per_page]

    # Renderiza la plantilla 'admin_dashboard.html' con los productos paginados
    return render_template('admin_dashboard.html', productos=productos_paginados, pagination=pagination)

# Define una función para obtener todos los productos desde la base de datos
def obtener_todos_los_productos():
    # Conectar a la base de datos SQLite3
    conn = sqlite3.connect('jumbox.db')
    cursor = conn.cursor()
    
    # Ejecuta una consulta para obtener los productos desde la base de datos
    cursor.execute("SELECT nombre, precio, descripcion, id_producto, categoria_id FROM producto")
    productos = cursor.fetchall()

    # Se cierra la conexión a la base de datos
    conn.close()

    return productos

# Define la ruta '/lista_productos' para mostrar una lista paginada de productos
@app.route('/lista_productos', methods=['GET'])
def lista_productos():
    # Configura la paginación
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    
    # Obtén la lista completa de productos desde la base de datos
    productos = obtener_todos_los_productos()

    # Calcula el número total de páginas
    total = len(productos)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    
    # Divide la lista de productos en páginas
    productos_paginados = productos[offset: offset + per_page]

    # Renderiza la plantilla 'lista_productos.html' con los productos paginados y la paginación
    return render_template('lista_productos.html', productos=productos_paginados, pagination=pagination)

# Define la ruta '/editar_producto/<int:id_producto>' para editar un producto por su ID
@app.route('/editar_producto/<int:id_producto>', methods=['GET', 'POST'])
def editar_producto(id_producto):
    # Obtener el producto por su ID desde la base de datos
    print(f'ID del producto a editar: {id_producto}')
    conn = sqlite3.connect('jumbox.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM producto WHERE id_producto = ?", (id_producto,))
    producto_data = cursor.fetchone()

    # Ejecuta una consulta para obtener las categorías de productos
    cursor.execute("SELECT nombre, id_categoria_producto FROM categoria_producto")
    categorias_producto = cursor.fetchall()
   
    conn.close()

    if producto_data:
        if request.method == 'POST':
            # Obtener los nuevos valores desde el formulario
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            precio = request.form['precio']
            categoria_id = request.form['categoria_id']

            print(f"Nombre: {nombre}, Descripción: {descripcion}, Precio: {precio}, Categoría ID: {categoria_id}, ID Producto: {id_producto}")
            
            # Crear un objeto Producto y actualizar sus atributos
            producto = Producto(id_producto, nombre, descripcion, precio)
            producto.actualizar(nombre, descripcion, precio, categoria_id, id_producto)
            
            # Redirigir al panel de administración ('admin_dashboard') después de la edición
            return redirect(url_for('admin_dashboard'))

        # Renderiza la plantilla 'editar_producto.html' con los datos del producto y categorías
        return render_template('editar_producto.html', producto=producto_data, categorias=categorias_producto)
    
    return 'Producto no encontrado', 404

# Define la ruta '/eliminar_producto/<int:id_producto>' para eliminar un producto por su ID
@app.route('/eliminar_producto/<int:id_producto>')
def eliminar_producto(id_producto):
    # Elimina el producto de la base de datos
    conn = sqlite3.connect('jumbox.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producto WHERE id_producto = ?", (id_producto,))
    conn.commit()
    conn.close()
    return 'Producto eliminado exitosamente'

@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('jumbox.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, id_categoria_producto FROM categoria_producto")
    categorias_producto = cursor.fetchall()
    conn.commit()
    conn.close()
    if request.method == 'POST':
        # Obtener los valores del formulario
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        categoria_id = request.form['categoria_id']
        
        # Validar los valores (por ejemplo, asegurándote de que el precio sea válido)
        try:
            precio = float(precio)
            if precio <= 0:
                return "El precio debe ser un número válido mayor que 0"
        except ValueError:
            return "El precio debe ser un número válido mayor que 0"


        # Insertar el nuevo producto en la base de datos
        producto_nuevo= Producto(nombre,descripcion,precio,categoria_id)
        producto_nuevo.guardar(nombre,descripcion,precio,categoria_id)
        # Redirigir al panel de administración ('admin_dashboard') después de la edición
        return redirect(url_for('admin_dashboard'))
        


    
    return render_template('agregar_producto.html', categorias=categorias_producto)

@app.route('/login')
def login():
    return render_template('login.html')
# Ejecuta la aplicación Flask si este archivo es el punto de entrada principal
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
