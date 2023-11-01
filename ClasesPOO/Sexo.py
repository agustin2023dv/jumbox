class Sexo:
    """
    Clase que representa el género de una persona en una base de datos.

    Atributos:
        - id_sexo (int): Identificador único del género.
        - nombre (str): Nombre del género (por ejemplo, "Masculino" o "Femenino").

    Métodos:
        - __init__(self, id_sexo, nombre): Inicializa un objeto Sexo.
        - __str__(self): Devuelve una representación en cadena del género.
        - guardar(self, db): Guarda el género en la base de datos.
        - actualizar(self, db): Actualiza el género en la base de datos.
        - eliminar(self, db): Elimina el género de la base de datos.
        - obtener_por_id(cls, db, id_sexo): Obtiene un género por su ID desde la base de datos.

    Uso:
        Esta clase se utiliza para representar y gestionar información sobre el género de una persona en una base de datos.
    """

    def __init__(self, id_sexo, nombre):
        """
        Inicializa un objeto Sexo con los atributos proporcionados.
        """
        self.id_sexo = id_sexo
        self.nombre = nombre

    def __str__(self):
        """
        Devuelve una representación en cadena del género.
        """
        return f"ID Género: {self.id_sexo}\n" \
               f"Nombre: {self.nombre}"

    def guardar(self, db):
        """
        Guarda el género en la base de datos.
        """
        try:
            consulta = "INSERT INTO sexo (nombre) VALUES (?)"
            parametros = (self.nombre,)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al guardar el género: {str(e)}")

    def actualizar(self, db):
        """
        Actualiza el género en la base de datos.
        """
        try:
            consulta = "UPDATE sexo SET nombre=? WHERE id_sexo=?"
            parametros = (self.nombre, self.id_sexo)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar el género: {str(e)}")

    def eliminar(self, db):
        """
        Elimina el género de la base de datos.
        """
        try:
            consulta = "DELETE FROM sexo WHERE id_sexo = ?"
            parametros = (self.id_sexo,)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al eliminar el género: {str(e)}")

    @classmethod
    def obtener_por_id(cls, db, id_sexo):
        """
        Obtiene un género por su ID desde la base de datos.
        """
        try:
            consulta = "SELECT * FROM sexo WHERE id_sexo = ?"
            parametros = (id_sexo,)
            resultado = db.ejecutar_consulta(consulta, parametros)
            if resultado:
                fila = resultado.fetchone()
                if fila:
                    return cls(fila[0], fila[1])
        except Exception as e:
            print(f"Error al obtener el género por ID: {str(e)}")
        return None
