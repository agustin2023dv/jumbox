from . import CategoriaProducto
import sqlite3
class Producto:
    """
    Clase que representa un producto en una base de datos.

    Atributos:
        - id_producto (int): Identificador único del producto.
        - nombre (str): Nombre del producto.
        - descripcion (str): Descripción del producto.
        - precio (float): Precio del producto.
        - categoria (CategoriaProducto): Categoría a la que pertenece el producto. En la base de datos, categoria sería FK en la tabla producto.

    Métodos:
        - __init__(self, id_producto, nombre, descripcion, precio, categoria): Inicializa un objeto Producto.
        - __str__(self): Devuelve una representación en cadena de los atributos del producto.
        - guardar(self, db): Guarda el producto en la base de datos.
        - actualizar(self, db): Actualiza el producto en la base de datos.
        - eliminar(self, db): Elimina el producto de la base de datos.
        - obtener_por_id(cls, db, id_producto): Obtiene un producto por su ID desde la base de datos.

    Uso:
        Esta clase se utiliza para representar y gestionar productos en una base de datos.
    """

    def __init__(self, id_producto, nombre, descripcion, precio, categoria):
        """
        Inicializa un objeto Producto con los atributos proporcionados.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
    
    def __init__(self):
        """
        Inicializa un objeto Producto con los atributos proporcionados.
        """
        
        self.nombre = ""
        self.descripcion = ""
        self.precio = 1
    
    def __init__(self, id_producto, nombre, descripcion, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio


    def __str__(self):
        """
        Devuelve una representación en cadena del producto.
        """
     
        return f"ID Producto: {self.id_producto}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Descripción: {self.descripcion}\n" \
               f"Precio: {self.precio}\n" \
             

    def guardar(self, nombre, descripcion, precio, categoria):
        """
        Guarda el producto en la base de datos.
        """
        # Verificar que el precio sea un número válido y mayor a 0
        try:
            precio = float(precio)
            if precio <= 0:
                return "El precio debe ser un número válido mayor que 0"
        except ValueError:
            return "El precio debe ser un número válido mayor que 0"

        # Verificar que el nombre y la descripción no estén en blanco
        if not nombre.strip() or not descripcion.strip():
            return "El nombre y la descripción no pueden estar en blanco"

        conn = sqlite3.connect('jumbox.db')
        cursor = conn.cursor()

        try:
            consulta = "INSERT INTO producto (nombre, descripcion, precio, categoria_id) VALUES (?, ?, ?, ?)"
            parametros = (nombre, descripcion, precio, categoria)
            cursor.execute(consulta, parametros)
            conn.commit()
            conn.close()
            return 'Producto guardado exitosamente'
        except Exception as e:
            print(f"Error al guardar el producto: {str(e)}")
            return "Error al guardar el producto en la base de datos"


    class Producto:
        def __init__(self, id_producto, nombre, descripcion, precio):
            self.id_producto = id_producto
            self.nombre = nombre
            self.descripcion = descripcion
            self.precio = precio

    def actualizar(self, nombre, descripcion, precio, categoria, id_producto):
        # Intenta convertir el valor de precio a float y verifica si es válido
        try:
            precio = float(precio)
            if precio <= 0:
                print("El precio debe ser mayor que 0")
                return None
            else:
                if precio > 0:
                    try:
                        conexion = sqlite3.connect('jumbox.db')
                        cursor = conexion.cursor()

                        cursor.execute("UPDATE producto SET nombre=?, descripcion=?, precio=?, categoria_id=? WHERE id_producto=?",
                                    (nombre, descripcion, precio, categoria, id_producto))
                        conexion.commit()
                        conexion.close()

                    except Exception as e:
                        print(f"Error al actualizar el producto: {str(e)}")
        except ValueError:
            print("El precio debe ser un número válido")
            return None

  


    def eliminar(self, db):
        """
        Elimina el producto de la base de datos.
        """
        try:
            consulta = "DELETE FROM producto WHERE id_producto = ?"
            parametros = (self.id_producto,)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al eliminar el producto: {str(e)}")

    @classmethod
    def obtener_por_id(cls, db, id_producto):
        """
        Obtiene un producto por su ID desde la base de datos.
        """
        try:
            consulta = "SELECT * FROM producto WHERE id_producto = ?"
            parametros = (id_producto,)
            resultado = db.ejecutar_consulta(consulta, parametros)
            if resultado:
                fila = resultado.fetchone()
                if fila:
                    categoria = CategoriaProducto.obtener_por_id(db, fila[4])
                    return cls(fila[0], fila[1], fila[2], fila[3], categoria)
        except Exception as e:
            print(f"Error al obtener el producto por ID: {str(e)}")
        return None