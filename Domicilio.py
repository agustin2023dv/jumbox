class Domicilio:
    """
    Clase que representa un domicilio en una base de datos.

    Atributos:
        - id_domicilio (int): Identificador único del domicilio.
        - domicilio (str): Dirección del domicilio.
        - ciudad (Ciudad): Ciudad a la que pertenece el domicilio. En la base de datos, ciudad seria FK en la tabla domicilio

    Métodos:
        - __init__(id_domicilio, domicilio, ciudad): Inicializa un objeto Domicilio.
        - __str__(): Devuelve una representación en cadena de los atributos del domicilio.
        - get_id_domicilio(): Obtiene el ID del domicilio.
        - get_domicilio(): Obtiene la dirección del domicilio.
        - get_ciudad(): Obtiene la ciudad a la que pertenece el domicilio.
        - set_id_domicilio(id_domicilio): Establece el ID del domicilio.
        - set_domicilio(domicilio): Establece la dirección del domicilio.
        - set_ciudad(ciudad): Establece la ciudad a la que pertenece el domicilio.
    """
    
    def __init__(self, id_domicilio, domicilio, ciudad):
        """
        Inicializa un objeto Domicilio con los atributos proporcionados.
        """
        self.__id_domicilio = id_domicilio
        self.__domicilio = domicilio
        self.__ciudad = ciudad

    def __str__(self):
        """
        Devuelve una representación en cadena del domicilio.
        """
        ciudad_nombre = self.__ciudad.get_nombre_ciudad()
        provincia_nombre = self.__ciudad.get_provincia().get_nombre_provincia()
        return f"ID Domicilio: {self.__id_domicilio}\n" \
               f"Domicilio: {self.__domicilio}\n" \
               f"Ciudad: {ciudad_nombre}, Provincia: {provincia_nombre}"

    # Getters
    def get_id_domicilio(self):
        """
        Obtiene el ID del domicilio.
        """
        return self.__id_domicilio

    def get_domicilio(self):
        """
        Obtiene la dirección del domicilio.
        """
        return self.__domicilio

    def get_ciudad(self):
        """
        Obtiene la ciudad a la que pertenece el domicilio.
        """
        return self.__ciudad

    # Setters
    def set_id_domicilio(self, id_domicilio):
        """
        Establece el ID del domicilio.
        """
        self.__id_domicilio = id_domicilio

    def set_domicilio(self, domicilio):
        """
        Establece la dirección del domicilio.
        """
        self.__domicilio = domicilio

    def set_ciudad(self, ciudad):
        """
        Establece la ciudad a la que pertenece el domicilio.
        """
        self.__ciudad = ciudad