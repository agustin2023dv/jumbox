class Ciudad:
    """
    Clase que representa una ciudad en una base de datos.

    Atributos:
        - id_ciudad (int): Identificador único de la ciudad.
        - nombre_ciudad (str): Nombre de la ciudad.
        - provincia (Provincia): Provincia a la que pertenece la ciudad. En la base de datos, provincia seria FK en la tabla ciudad.

    Métodos:
        - __init__(id_ciudad, nombre_ciudad, provincia): Inicializa un objeto Ciudad.
        - __str__(): Devuelve una representación en cadena de los atributos de la ciudad.
        - get_id_ciudad(): Obtiene el ID de la ciudad.
        - get_nombre_ciudad(): Obtiene el nombre de la ciudad.
        - get_provincia(): Obtiene la provincia a la que pertenece la ciudad.
        - set_id_ciudad(id_ciudad): Establece el ID de la ciudad.
        - set_nombre_ciudad(nombre_ciudad): Establece el nombre de la ciudad.
        - set_provincia(provincia): Establece la provincia a la que pertenece la ciudad.
    """
    
    def __init__(self, id_ciudad, nombre_ciudad, provincia):
        """
        Inicializa un objeto Ciudad con los atributos proporcionados.
        """
        self.__id_ciudad = id_ciudad
        self.__nombre_ciudad = nombre_ciudad
        self.__provincia = provincia

    def __str__(self):
        """
        Devuelve una representación en cadena de la ciudad.
        """
        return f"ID Ciudad: {self.__id_ciudad}\n" \
               f"Nombre Ciudad: {self.__nombre_ciudad}\n" \
               f"Provincia: {self.__provincia.get_nombre_provincia()}"

    # Getters
    def get_id_ciudad(self):
        """
        Obtiene el ID de la ciudad.
        """
        return self.__id_ciudad

    def get_nombre_ciudad(self):
        """
        Obtiene el nombre de la ciudad.
        """
        return self.__nombre_ciudad

    def get_provincia(self):
        """
        Obtiene la provincia a la que pertenece la ciudad.
        """
        return self.__provincia

    # Setters
    def set_id_ciudad(self, id_ciudad):
        """
        Establece el ID de la ciudad.
        """
        self.__id_ciudad = id_ciudad

    def set_nombre_ciudad(self, nombre_ciudad):
        """
        Establece el nombre de la ciudad.
        """
        self.__nombre_ciudad = nombre_ciudad

    def set_provincia(self, provincia):
        """
        Establece la provincia a la que pertenece la ciudad.
        """
        self.__provincia = provincia
