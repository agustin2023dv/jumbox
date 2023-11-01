class Domicilio:
    """
    Clase que representa un domicilio en una base de datos.

    Atributos:
        - id_domicilio (int): Identificador único del domicilio.
        - domicilio (str): Dirección del domicilio.
        - ciudad (Ciudad): Ciudad a la que pertenece el domicilio. En la base de datos, ciudad sería una FK en la tabla domicilio.

    Métodos:
        - __init__(self, id_domicilio, domicilio, ciudad): Inicializa un objeto Domicilio.
        - __str__(self): Devuelve una representación en cadena de los atributos del domicilio.
        - guardar(self, db): Guarda el domicilio en la base de datos.
        - actualizar(self, db): Actualiza el domicilio en la base de datos.
        - eliminar(self, db): Elimina el domicilio de la base de datos.
        - obtener_por_id(cls, db, id_domicilio): Obtiene un domicilio por su ID desde la base de datos.

    Uso:
        Esta clase se utiliza para representar y gestionar domicilios en una base de datos.
    """

    def __init__(self, id_domicilio, domicilio, ciudad):
        """
        Inicializa un objeto Domicilio con los atributos proporcionados.
        """
        self.id_domicilio = id_domicilio
        self.domicilio = domicilio
        self.ciudad = ciudad

    def __str__(self):
        """
        Devuelve una representación en cadena del domicilio.
        """
        ciudad_nombre = self.ciudad.get_nombre_ciudad()
        provincia_nombre = self.ciudad.get_provincia().get_nombre_provincia()
        return f"ID Domicilio: {self.id_domicilio}\n" \
               f"Domicilio: {self.domicilio}\n" \
               f"Ciudad: {ciudad_nombre}, Provincia: {provincia_nombre}"

    def guardar(self, db):
        """
        Guarda el domicilio en la base de datos.
        """
        try:
            consulta = "INSERT INTO domicilio (direccion, ciudad_id) VALUES (?, ?)"
            parametros = (self.domicilio, self.ciudad.get_id_ciudad())
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al guardar el domicilio: {str(e)}")

    def actualizar(self, db):
        """
        Actualiza el domicilio en la base de datos.
        """
        try:
            consulta = "UPDATE domicilio SET direccion=?, ciudad_id=? WHERE id_domicilio=?"
            parametros = (self.domicilio, self.ciudad.get_id_ciudad(), self.id_domicilio)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar el domicilio: {str(e)}")

    def eliminar(self, db):
        """
        Elimina el domicilio de la base de datos.
        """
        try:
            consulta = "DELETE FROM domicilio WHERE id_domicilio = ?"
            parametros = (self.id_domicilio,)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al eliminar el domicilio: {str(e)}")

    @classmethod
    def obtener_por_id(cls, db, id_domicilio):
        """
        Obtiene un domicilio por su ID desde la base de datos.
        """
        try:
            consulta = "SELECT * FROM domicilio WHERE id_domicilio = ?"
            parametros = (id_domicilio,)
            resultado = db.ejecutar_consulta(consulta, parametros)
            if resultado:
                fila = resultado.fetchone()
                if fila:
                    ciudad = Ciudad.obtener_por_id(db, fila[2])
                    return cls(fila[0], fila[1], ciudad)
        except Exception as e:
            print(f"Error al obtener el domicilio por ID: {str(e)}")
        return None
