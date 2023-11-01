from . import Domicilio, Sexo

class Cliente:
    """
    Clase que representa un cliente en una base de datos.

    Atributos:
        - id_cliente (int): Identificador único del cliente.
        - nombre (str): Nombre del cliente.
        - apellido (str): Apellido del cliente.
        - sexo (Sexo): Sexo del cliente.
        - fecha_nac (date): Fecha de nacimiento del cliente.
        - telefono (str): Número de teléfono del cliente.
        - email (str): Correo electrónico del cliente.
        - domicilio (Domicilio): Domicilio del cliente.

    Métodos:
        - __init__(self, id_cliente, nombre, apellido, sexo, fecha_nac, telefono, email, domicilio): Inicializa un objeto Cliente.
        - __str__(self): Devuelve una representación en cadena del Cliente.
        - guardar(self, db): Guarda el cliente en la base de datos.
        - actualizar(self, db): Actualiza la información del cliente en la base de datos.
        - eliminar(self, db): Elimina el cliente de la base de datos.
        - obtener_por_id(cls, db, id_cliente): Obtiene un cliente por su ID desde la base de datos.

    Uso:
        Esta clase se utiliza para representar y gestionar información de clientes en una base de datos.
    """

    def __init__(self, id_cliente, nombre, apellido, sexo, fecha_nac, telefono, email, domicilio):
        """
        Inicializa un objeto Cliente con los atributos proporcionados.
        """
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.fecha_nac = fecha_nac
        self.telefono = telefono
        self.email = email
        self.domicilio = domicilio

    def __str__(self):
        """
        Devuelve una representación en cadena del Cliente.
        """
        return f"Cliente ID: {self.id_cliente}\n" \
               f"Nombre: {self.nombre} {self.apellido}\n" \
               f"Sexo: {self.sexo.nombre}\n" \
               f"Fecha de Nacimiento: {self.fecha_nac}\n" \
               f"Teléfono: {self.telefono}\n" \
               f"Email: {self.email}\n" \
               f"Domicilio: {str(self.domicilio)}"

    def guardar(self, db):
        """
        Guarda el cliente en la base de datos.
        """
        try:
            consulta = "INSERT INTO cliente (nombre, apellido, sexo_id, fecha_nac, telefono, email, domicilio_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
            parametros = (self.nombre, self.apellido, self.sexo.id_sexo, self.fecha_nac, self.telefono, self.email, self.domicilio.id_domicilio)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al guardar el cliente: {str(e)}")

    def actualizar(self, db):
        """
        Actualiza la información del cliente en la base de datos.
        """
        try:
            consulta = "UPDATE cliente SET nombre=?, apellido=?, sexo_id=?, fecha_nac=?, telefono=?, email=?, domicilio_id=? WHERE id_cliente=?"
            parametros = (self.nombre, self.apellido, self.sexo.id_sexo, self.fecha_nac, self.telefono, self.email, self.domicilio.id_domicilio, self.id_cliente)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar el cliente: {str(e)}")

    def eliminar(self, db):
        """
        Elimina el cliente de la base de datos.
        """
        try:
            consulta = "DELETE FROM cliente WHERE id_cliente = ?"
            parametros = (self.id_cliente,)
            db.ejecutar_consulta(consulta, parametros)
            db.conexion.commit()
        except Exception as e:
            print(f"Error al eliminar el cliente: {str(e)}")

    @classmethod
    def obtener_por_id(cls, db, id_cliente):
        """
        Obtiene un cliente por su ID desde la base de datos.
        """
        try:
            consulta = "SELECT * FROM cliente WHERE id_cliente = ?"
            parametros = (id_cliente,)
            resultado = db.ejecutar_consulta(consulta, parametros)
            if resultado:
                fila = resultado.fetchone()
                if fila:
                    sexo = Sexo.obtener_por_id(db, fila[3])
                    domicilio = Domicilio.obtener_por_id(db, fila[7])
                    return cls(fila[0], fila[1], fila[2], sexo, fila[4], fila[5], fila[6], domicilio)
        except Exception as e:
            print(f"Error al obtener el cliente por ID: {str(e)}")
        return None
