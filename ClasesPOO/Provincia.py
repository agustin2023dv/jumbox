class Provincia:
    """
    Clase que representa una provincia en una base de datos.

    Atributos:
        - id_provincia (int): Identificador único de la provincia.
        - nombre_provincia (str): Nombre de la provincia.

    Métodos:
        - __init__(self, id_provincia, nombre_provincia): Inicializa un objeto Provincia.
        - __str__(self): Devuelve una representación en cadena de los atributos de la provincia.
        - guardar(self, db): Guarda la provincia en la base de datos.
        - actualizar(self, db): Actualiza la provincia en la base de datos.
        - eliminar(self, db): Elimina la provincia de la base de datos.
        - obtener_por_id(cls, db, id_provincia): Obtiene una provincia por su ID desde la base de datos.

    Uso:
        Esta clase se utiliza para representar y gestionar provincias en una base de datos.
    """

    def __init__(self, id_provincia, nombre_provincia):
        """
        Inicializa un objeto Provincia con los atributos proporcionados.
        """
        self.id_provincia = id_provincia
        self.nombre_provincia = nombre_provincia

    def __str__(self):
        """
        Devuelve una representación en cadena de la provincia.
        """
        return f"ID Provincia: {self.id_provincia}\n" \
               f"Nombre Provincia: {self.nombre_provincia}"

    def guardar(self, db):
        """
        Guarda la provincia en la base de datos.
        """
        try:
            consulta = "INSERT INTO provincia (nombre_provincia) VALUES (?)"
            parametros = (self.nombre_provincia,)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al guardar la provincia: {str(e)}")

    def actualizar(self, db):
        """
        Actualiza la provincia en la base de datos.
        """
        try:
            consulta = "UPDATE provincia SET nombre_provincia=? WHERE id_provincia=?"
            parametros = (self.nombre_provincia, self.id_provincia)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar la provincia: {str(e)}")

    def eliminar(self, db):
        """
        Elimina la provincia de la base de datos.
        """
        try:
            consulta = "DELETE FROM provincia WHERE id_provincia = ?"
            parametros = (self.id_provincia,)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al eliminar la provincia: {str(e)}")

    @classmethod
    def obtener_por_id(cls, db, id_provincia):
        """
        Obtiene una provincia por su ID desde la base de datos.
        """
        try:
            consulta = "SELECT * FROM provincia WHERE id_provincia = ?"
            parametros = (id_provincia,)
            resultado = db.ejecutar_consulta(consulta, parametros)
            if resultado:
                fila = resultado.fetchone()
                if fila:
                    return cls(*fila)
        except Exception as e:
            print(f"Error al obtener la provincia por ID: {str(e)}")
        return None
