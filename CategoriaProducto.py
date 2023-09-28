class CategoriaProducto:


    """
    Clase que representa una categoría de productos en un supermercado.

    Atributos:
        - id_categoria (int): Identificador único de la categoría.
        - nombre (str): Nombre de la categoría.
        - descripcion (str): Descripción de la categoría.

    
    Métodos:
        - __init__(id_categoria, nombre, descripcion): Inicializa un objeto CategoriaProducto.
        - __str__(): Devuelve una representación en cadena de los atributos de la categoría.
        - get_id_categoria(): Obtiene el ID de la categoría.
        - get_nombre(): Obtiene el nombre de la categoría.
        - get_descripcion(): Obtiene la descripción de la categoría.
        - set_id_categoria(id_categoria): Establece el ID de la categoría.
        - set_nombre(nombre): Establece el nombre de la categoría.
        - set_descripcion(descripcion): Establece la descripción de la categoría.

    Uso:
        Esta clase se utiliza para representar y organizar diferentes categorías de productos del supermercado.
    """


    def __init__(self, id_categoria, nombre, descripcion):
        """
        Inicializa un objeto CategoriaProducto con los atributos proporcionados.
        """

        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):

        """
        Devuelve una representación de tipo string de la categoría.
        """

        return f"ID Categoría: {self.id_categoria}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Descripción: {self.descripcion}"
    


    # Getters
    def get_id_categoria(self):
        """
        Obtiene el ID de la categoría.
        """
        return self.id_categoria

    def get_nombre(self):
        """
        Obtiene el nombre de la categoría.
        """
        return self.nombre

    def get_descripcion(self):
        """
        Obtiene la descripción de la categoría.
        """
        return self.descripcion

    # Setters
    def set_id_categoria(self, id_categoria):
        """
        Establece el ID de la categoría.
        """
        self.id_categoria = id_categoria

    def set_nombre(self, nombre):
        """
        Establece el nombre de la categoría.
        """
        self.nombre = nombre

    def set_descripcion(self, descripcion):
        """
        Establece la descripción de la categoría.
        """
        self.descripcion = descripcion