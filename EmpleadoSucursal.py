class EmpleadoSucursal:


    """
    Clase que representa a un empleado de una sucursal de supermercado.

    Atributos:
        - id_empleado (int): Identificador único del empleado.
        - sexo (bool): Género del empleado (True para masculino, False para femenino).
        - nombre (str): Nombre del empleado.
        - apellido (str): Apellido del empleado.
        - fecha_nacimiento (str): Fecha de nacimiento del empleado (en formato YYYY-MM-DD).
        - email (str): Dirección de correo electrónico del empleado.
        - telefono (str): Número de teléfono del empleado.

    Métodos:
        - get_id_empleado(): Obtiene el ID del empleado.
        - get_sexo(): Obtiene el género del empleado.
        - get_nombre(): Obtiene el nombre del empleado.
        - get_apellido(): Obtiene el apellido del empleado.
        - get_fecha_nacimiento(): Obtiene la fecha de nacimiento del empleado.
        - get_email(): Obtiene la dirección de correo electrónico del empleado.
        - get_telefono(): Obtiene el número de teléfono del empleado.
        - set_id_empleado(id_empleado): Establece el ID del empleado.
        - set_sexo(sexo): Establece el género del empleado.
        - set_nombre(nombre): Establece el nombre del empleado.
        - set_apellido(apellido): Establece el apellido del empleado.
        - set_fecha_nacimiento(fecha_nacimiento): Establece la fecha de nacimiento del empleado.
        - set_email(email): Establece la dirección de correo electrónico del empleado.
        - set_telefono(telefono): Establece el número de teléfono del empleado.
        - __str__(): Devuelve una representación de tipo string de los atributos del objeto empleado.
    """


    def __init__(self, id_empleado, sexo, nombre, apellido, fecha_nacimiento, email, telefono):
        """
        Inicializa un objeto EmpleadoSucursal con los atributos proporcionados.
        """
        self.__id_empleado = id_empleado
        self.__sexo = sexo
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__email = email
        self.__telefono = telefono

    # Getters
    def get_id_empleado(self):
        return self.__id_empleado

    def get_sexo(self):
        return self.__sexo

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    # Setters
    def set_id_empleado(self, id_empleado):
        self.__id_empleado = id_empleado

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_email(self, email):
        self.__email = email

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):

        """
        Devuelve una representación en cadena del empleado.
        """

        return f"ID Empleado: {self.__id_empleado}\n" \
               f"Sexo: {self.__sexo}\n" \
               f"Nombre: {self.__nombre}\n" \
               f"Apellido: {self.__apellido}\n" \
               f"Fecha de Nacimiento: {self.__fecha_nacimiento}\n" \
               f"Email: {self.__email}\n" \
               f"Teléfono: {self.__telefono}"