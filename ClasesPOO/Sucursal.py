class Sucursal:
    """
    Clase que representa una sucursal en una base de datos.

    Atributos:
        - id_sucursal (int): Identificador único de la sucursal.
        - direccion (str): Dirección de la sucursal.
        - email (str): Dirección de correo electrónico de la sucursal.
        - telefono (str): Número de teléfono de la sucursal.

    Métodos:
        - __init__(self, id_sucursal, direccion, email, telefono): Inicializa un objeto Sucursal.
        - __str__(self): Devuelve una representación en cadena de los atributos de la sucursal.
        - guardar(self, db): Guarda la sucursal en la base de datos.
        - actualizar(self, db): Actualiza la sucursal en la base de datos.
        - eliminar(self, db): Elimina la sucursal de la base de datos.
        - obtener_por_id(cls, db, id_sucursal): Obtiene una sucursal por su ID desde la base de datos.

    Uso:
        Esta clase se utiliza para representar y gestionar sucursales en una base de datos.
    """

    def __init__(self, id_sucursal, direccion, email, telefono):
        """
        Inicializa un objeto Sucursal con los atributos proporcionados.
        """
        self.id_sucursal = id_sucursal
        self.direccion = direccion
        self.email = email
        self.telefono = telefono

    def __str__(self):
        """
        Devuelve una representación en cadena de la sucursal.
        """
        return f"ID Sucursal: {self.id_sucursal}\n" \
               f"Dirección: {self.direccion}\n" \
               f"Email: {self.email}\n" \
               f"Teléfono: {self.telefono}"

    def guardar(self, db):
        """
        Guarda la sucursal en la base de datos.
        """
        try:
            consulta = "INSERT INTO sucursal (direccion, email, telefono) VALUES (?, ?, ?)"
            parametros = (self.direccion, self.email, self.telefono)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al guardar la sucursal: {str(e)}")

    def actualizar(self, db):
        """
        Actualiza la sucursal en la base de datos.
        """
        try:
            consulta = "UPDATE sucursal SET direccion=?, email=?, telefono=? WHERE id_sucursal=?"
            parametros = (self.direccion, self.email, self.telefono, self.id_sucursal)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar la sucursal: {str(e)}")

    def eliminar(self, db):
        """
        Elimina la sucursal de la base de datos.
        """
        try:
            consulta = "DELETE FROM sucursal WHERE id_sucursal = ?"
            parametros = (self.id_sucursal,)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al eliminar la sucursal: {str(e)}")

    @classmethod
    def obtener_por_id(cls, db, id_sucursal):
        """
        Obtiene una sucursal por su ID desde la base de datos.
        """
        try:
            consulta = "SELECT * FROM sucursal WHERE id_sucursal = ?"
            parametros = (id_sucursal,)
            resultado = db.ejecutar_consulta(consulta, parametros)
            if resultado:
                fila = resultado.fetchone()
                if fila:
                    return cls(fila[0], fila[1], fila[2], fila[3])
        except Exception as e:
            print(f"Error al obtener la sucursal por ID: {str(e)}")
        return None
