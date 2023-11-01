class SucursalStock:
    """
    Clase que representa el stock de un producto en una sucursal.

    Atributos:
        - id_sucursal_stock (int): Identificador único del stock en la sucursal.
        - sucursal (Sucursal): La sucursal a la que pertenece el stock.
        - stock_producto (StockProducto): El producto al que corresponde el stock.
        - stock (int): Cantidad de unidades en stock en la sucursal.

    Métodos:
        - __init__(id_sucursal_stock, sucursal, stock_producto, stock): Inicializa un objeto SucursalStock.
        - __str__(): Devuelve una representación en cadena del SucursalStock.
        - actualizar_stock(cantidad): Actualiza la cantidad de productos en stock en la sucursal.

    Uso:
        Esta clase se utiliza para representar y gestionar el stock de un producto en una sucursal.
    """

    def __init__(self, id_sucursal_stock, sucursal, stock_producto, stock):
        """
        Inicializa un objeto SucursalStock con los atributos proporcionados.
        """
        self.id_sucursal_stock = id_sucursal_stock
        self.sucursal = sucursal
        self.stock_producto = stock_producto
        self.stock = stock

    def __str__(self):
        """
        Devuelve una representación en cadena de SucursalStock.
        """
        return f"SucursalStock ID: {self.id_sucursal_stock}\n" \
               f"Sucursal: {self.sucursal.direccion}\n" \
               f"Producto: {self.stock_producto.producto.nombre}\n" \
               f"Stock: {self.stock}"

    def actualizar_stock(self, cantidad):
        """
        Actualiza la cantidad de productos en stock en la sucursal.

        Args:
            cantidad (int): La nueva cantidad de stock. Debe ser mayor o igual a cero.

        Returns:
            None
        """
        if cantidad >= 0:
            self.stock = cantidad
            # Actualizar la base de datos para reflejar el cambio en el stock
            # Esto requeriría ejecutar una consulta SQL para actualizar el stock en la base de datos
        else:
            print("Error: La cantidad de stock no puede ser negativa.")
