class CategoriaProducto:
    """
    Clase que representa una categoría de productos en un supermercado.

    Atributos:
        - id_categoria (int): Identificador único de la categoría.
        - nombre (str): Nombre de la categoría.
        - descripcion (str): Descripción de la categoría.

    Métodos:
        - __init__(self, id_categoria, nombre, descripcion): Inicializa un objeto CategoriaProducto.
        - __str__(self): Devuelve una representación en cadena de los atributos de la categoría.
        - guardar(self, db): Guarda la categoría en la base de datos.
        - actualizar(self, db): Actualiza la categoría en la base de datos.
        - eliminar(self, db): Elimina la categoría de la base de datos.
        - obtener_por_id(cls, db, id_categoria): Obtiene una categoría por su ID desde la base de datos.

    Uso:
        Esta clase se utiliza para representar y gestionar categorías de productos en un supermercado.
    """

    def __init__(self, id_categoria, nombre, descripcion):
        """
        Inicializa un objeto CategoriaProducto con los atributos proporcionados.
        """
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        """
        Devuelve una representación en cadena de la categoría.
        """
        return f"ID Categoría: {self.id_categoria}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Descripción: {self.descripcion}"

    def guardar(self, db):
        """
        Guarda la categoría en la base de datos.
        """
        consulta = "INSERT INTO categoria_producto (nombre, descripcion) VALUES (?, ?)"
        parametros = (self.nombre, self.descripcion)
        db.ejecutar_consulta(consulta, parametros)
        db.conexion.commit()

    def actualizar(self, db):
        """
        Actualiza la categoría en la base de datos.
        """
        consulta = "UPDATE categoria_producto SET nombre=?, descripcion=? WHERE id_categoria_producto=?"
        parametros = (self.nombre, self.descripcion, self.id_categoria)
        db.ejecutar_consulta(consulta, parametros)
        db.conexion.commit()

    def eliminar(self, db):
        """
        Elimina la categoría de la base de datos.
        """
        consulta = "DELETE FROM categoria_producto WHERE id_categoria_producto = ?"
        parametros = (self.id_categoria,)
        db.ejecutar_consulta(consulta, parametros)
        db.conexion.commit()

    @classmethod
    def obtener_por_id(cls, db, id_categoria):
        """
        Obtiene una categoría por su ID desde la base de datos.
        """
        consulta = "SELECT * FROM categoria_producto WHERE id_categoria_producto = ?"
        parametros = (id_categoria,)
        resultado = db.ejecutar_consulta(consulta, parametros)
        if resultado:
            fila = resultado.fetchone()
            if fila:
                return cls(*fila)
        return None
