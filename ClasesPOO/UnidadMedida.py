class UnidadMedida:
    """
    Clase que representa una unidad de medida en una base de datos.

    Atributos:
        - id_unidad (int): Identificador único de la unidad de medida.
        - nombre (str): Nombre de la unidad de medida.
        - descripcion (str): Descripción de la unidad de medida.

    Métodos:
        - __init__(self, id_unidad, nombre, descripcion): Inicializa un objeto UnidadMedida.
        - __str__(self): Devuelve una representación en cadena de los atributos de la unidad de medida.
        - guardar(self, db): Guarda la unidad de medida en la base de datos.
        - actualizar(self, db): Actualiza la unidad de medida en la base de datos.
        - eliminar(self, db): Elimina la unidad de medida de la base de datos.
        - obtener_por_id(cls, db, id_unidad): Obtiene una unidad de medida por su ID desde la base de datos.

    Uso:
        Esta clase se utiliza para representar y gestionar unidades de medida en una base de datos.
    """

    def __init__(self, id_unidad, nombre, descripcion):
        """
        Inicializa un objeto UnidadMedida con los atributos proporcionados.
        """
        self.id_unidad = id_unidad
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        """
        Devuelve una representación en cadena de la unidad de medida.
        """
        return f"ID Unidad de Medida: {self.id_unidad}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Descripción: {self.descripcion}"

    def guardar(self, db):
        """
        Guarda la unidad de medida en la base de datos.
        """
        try:
            consulta = "INSERT INTO unidad_medida (nombre, descripcion) VALUES (?, ?)"
            parametros = (self.nombre, self.descripcion)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al guardar la unidad de medida: {str(e)}")

    def actualizar(self, db):
        """
        Actualiza la unidad de medida en la base de datos.
        """
        try:
            consulta = "UPDATE unidad_medida SET nombre=?, descripcion=? WHERE id_unidad_medida=?"
            parametros = (self.nombre, self.descripcion, self.id_unidad)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar la unidad de medida: {str(e)}")

    def eliminar(self, db):
        """
        Elimina la unidad de medida de la base de datos.
        """
        try:
            consulta = "DELETE FROM unidad_medida WHERE id_unidad_medida = ?"
            parametros = (self.id_unidad,)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al eliminar la unidad de medida: {str(e)}")

    @classmethod
    def obtener_por_id(cls, db, id_unidad):
        """
        Obtiene una unidad de medida por su ID desde la base de datos.
        """
        try:
            consulta = "SELECT * FROM unidad_medida WHERE id_unidad_medida = ?"
            parametros = (id_unidad,)
            resultado = db.ejecutar_consulta(consulta, parametros)
            if resultado:
                fila = resultado.fetchone()
                if fila:
                    return cls(fila[0], fila[1], fila[2])
        except Exception as e:
            print(f"Error al obtener la unidad de medida por ID: {str(e)}")
        return None
