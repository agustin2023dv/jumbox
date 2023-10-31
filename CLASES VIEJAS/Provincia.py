class Provincia:
    """
    Clase que representa una provincia en una base de datos.

    Atributos:
        - id_provincia (int): Identificador único de la provincia.
        - nombre_provincia (str): Nombre de la provincia.

    Métodos:
        - __init__(id_provincia, nombre_provincia): Inicializa un objeto Provincia.
        - __str__(): Devuelve una representación en cadena de los atributos de la provincia.
        - get_id_provincia(): Obtiene el ID de la provincia.
        - get_nombre_provincia(): Obtiene el nombre de la provincia.
        - set_id_provincia(id_provincia): Establece el ID de la provincia.
        - set_nombre_provincia(nombre_provincia): Establece el nombre de la provincia.
    """
    
    def __init__(self, id_provincia, nombre_provincia):
        """
        Inicializa un objeto Provincia con los atributos proporcionados.
        """
        self.__id_provincia = id_provincia
        self.__nombre_provincia = nombre_provincia

    def __str__(self):
        """
        Devuelve una representación de tipo string de la provincia.
        """
        return f"ID Provincia: {self.__id_provincia}\n" \
               f"Nombre Provincia: {self.__nombre_provincia}"

    # Getters
    def get_id_provincia(self):
        """
        Obtiene el ID de la provincia.
        """
        return self.__id_provincia

    def get_nombre_provincia(self):
        """
        Obtiene el nombre de la provincia.
        """
        return self.__nombre_provincia

    # Setters
    def set_id_provincia(self, id_provincia):
        """
        Establece el ID de la provincia.
        """
        self.__id_provincia = id_provincia

    def set_nombre_provincia(self, nombre_provincia):
        """
        Establece el nombre de la provincia.
        """
        self.__nombre_provincia = nombre_provincia
