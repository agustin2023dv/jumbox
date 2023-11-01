class Ciudad:
    """
    Clase que representa una ciudad en una base de datos.

    Atributos:
        - id_ciudad (int): Identificador único de la ciudad.
        - nombre_ciudad (str): Nombre de la ciudad.
        - provincia_id (int): ID de la provincia a la que pertenece la ciudad.

    Métodos:
        - __init__(self, id_ciudad, nombre_ciudad, provincia_id): Inicializa un objeto Ciudad.
        - __str__(self): Devuelve una representación en cadena de los atributos de la ciudad.
        - guardar(self, db): Guarda la ciudad en la base de datos.
        - actualizar(self, db): Actualiza la ciudad en la base de datos.
        - eliminar(self, db): Elimina la ciudad de la base de datos.
        - obtener_por_id(cls, db, id_ciudad): Obtiene una ciudad por su ID desde la base de datos.

    Uso:
        Esta clase se utiliza para representar y gestionar ciudades en una base de datos.
    """

    def __init__(self, id_ciudad, nombre_ciudad, provincia_id):
        """
        Inicializa un objeto Ciudad con los atributos proporcionados.
        """
        self.id_ciudad = id_ciudad
        self.nombre_ciudad = nombre_ciudad
        self.provincia_id = provincia_id

    def __str__(self):
        """
        Devuelve una representación en cadena de la ciudad.
        """
        return f"ID Ciudad: {self.id_ciudad}\n" \
               f"Nombre Ciudad: {self.nombre_ciudad}\n" \
               f"Provincia ID: {self.provincia_id}"

    def guardar(self, db):
        """
        Guarda la ciudad en la base de datos.
        """
        try:
            consulta = "INSERT INTO ciudad (nombre, provincia_id) VALUES (?, ?)"
            parametros = (self.nombre_ciudad, self.provincia_id)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al guardar la ciudad: {str(e)}")

    def actualizar(self, db):
        """
        Actualiza la ciudad en la base de datos.
        """
        try:
            consulta = "UPDATE ciudad SET nombre=?, provincia_id=? WHERE id_ciudad=?"
            parametros = (self.nombre_ciudad, self.provincia_id, self.id_ciudad)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar la ciudad: {str(e)}")

    def eliminar(self, db):
        """
        Elimina la ciudad de la base de datos.
        """
        try:
            consulta = "DELETE FROM ciudad WHERE id_ciudad = ?"
            parametros = (self.id_ciudad,)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al eliminar la ciudad: {str(e)}")

    @classmethod
    def obtener_por_id(cls, db, id_ciudad):
        """
        Obtiene una ciudad por su ID desde la base de datos.
        """
        try:
            consulta = "SELECT * FROM ciudad WHERE id_ciudad = ?"
            parametros = (id_ciudad,)
            resultado = db.ejecutar_consulta(consulta, parametros)
            if resultado:
                fila = resultado.fetchone()
                if fila:
                    return cls(*fila)
        except Exception as e:
            print(f"Error al obtener la ciudad por ID: {str(e)}")
        return None