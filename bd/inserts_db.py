import sqlite3

# Conectar a la base de datos (asegúrate de que el archivo "jumbox.db" exista)
conn = sqlite3.connect("jumbox.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Ejecutar las inserciones para la tabla unidad_medida
unidad_medida_data = [
    ('Kilogramo', 'Unidad de peso en kilogramos'),
    ('Litro', 'Unidad de volumen en litros'),
    ('Metro', 'Unidad de longitud en metros'),
    ('Unidad', 'Unidad individual'),
    ('Docena', 'Paquete de 12 unidades')
]

for unidad in unidad_medida_data:
    cursor.execute("INSERT INTO unidad_medida (nombre, descripcion) VALUES (?, ?)", unidad)

# Ejecutar las inserciones para la tabla categoria_producto
categoria_producto_data = [
    ('Frutas', 'Productos frescos y naturales'),
    ('Verduras', 'Vegetales y hortalizas'),
    ('Carnes', 'Cortes de carne de res, cerdo y pollo'),
    ('Lácteos', 'Productos lácteos como leche y queso'),
    ('Panadería', 'Productos de panadería como pan y pasteles'),
    ('Bebidas', 'Bebidas como refrescos y jugos'),
    ('Cereales', 'Cereales y productos de desayuno'),
    ('Higiene', 'Productos de higiene personal'),
    ('Limpieza', 'Productos de limpieza del hogar'),
    ('Electrónicos', 'Electrónicos y dispositivos'),
    ('Ropa', 'Ropa y accesorios'),
    ('Hogar', 'Artículos para el hogar'),
    ('Juguetes', 'Juguetes y juegos'),
    ('Automotriz', 'Productos para automóviles'),
    ('Mascotas', 'Alimentos y productos para mascotas')
]

for categoria in categoria_producto_data:
    cursor.execute("INSERT INTO categoria_producto (nombre, descripcion) VALUES (?, ?)", categoria)


# Ejecutar las inserciones para la tabla sexo
sexo_data = [
    ('Masculino'),
    ('Femenino')
]

for sexo in sexo_data:
    cursor.execute("INSERT INTO sexo (nombre) VALUES (?)", (sexo,))

# Ejecutar las inserciones para la tabla provincia
provincia_data = [
    ('Buenos Aires'),
    ('Córdoba'),
    ('Santa Fe'),
    ('Mendoza'),
    ('Tucumán'),
    ('Entre Ríos'),
    ('Salta'),
    ('Chaco'),
    ('Corrientes'),
    ('Misiones'),
    ('San Juan'),
    ('Jujuy'),
    ('Río Negro'),
    ('Neuquén'),
    ('Formosa')

]

for provincia in provincia_data:
    cursor.execute("INSERT INTO provincia (nombre) VALUES (?)", (provincia,))

# Ejecutar las inserciones para la tabla ciudad
ciudad_data = [
    ('Buenos Aires', 1),  # La provincia de Buenos Aires tiene el id 1 (debes ajustarlo según tu base de datos)
    ('Córdoba', 2),       # La provincia de Córdoba tiene el id 2
    ('Rosario', 3),       # La provincia de Santa Fe tiene el id 3
    ('Mendoza', 4),       # La provincia de Mendoza tiene el id 4
    ('San Miguel de Tucumán', 5),
    ('Paraná', 6),
    ('Salta', 7),
    ('Resistencia', 8),
    ('Corrientes', 9),
    ('Posadas', 10),
    ('San Juan', 11),
    ('San Salvador de Jujuy', 12),
    ('Viedma', 13),
    ('Neuquén', 14),
    ('Formosa', 15),
    ('La Plata', 1),  # Ejemplo de ciudad en la provincia de Buenos Aires
    ('Mar del Plata', 1),  # Ejemplo de ciudad en la provincia de Buenos Aires

]

for ciudad in ciudad_data:
    cursor.execute("INSERT INTO ciudad (nombre, provincia_id) VALUES (?, ?)", ciudad)

# Ejecutar las inserciones para la tabla domicilio
domicilio_data = [
    ('Calle 123, Ciudad 1', 1),  # Ciudad 1 tiene el id 1 (debes ajustarlo según tu base de datos)
    ('Avenida Principal 456, Ciudad 2', 2),  # Ciudad 2 tiene el id 2
    ('Calle Central 789, Ciudad 3', 3),  # Ciudad 3 tiene el id 3
    ('Calle Norte 101, Ciudad 4', 4),  # Ciudad 4 tiene el id 4
    ('Calle Sur 222, Ciudad 5', 5),
    ('Avenida Este 333, Ciudad 6', 6),
    ('Calle Oeste 444, Ciudad 7', 7),
    ('Avenida Libertad 555, Ciudad 8', 8),
    ('Calle Independencia 666, Ciudad 9', 9),
    ('Avenida 25 de Mayo 777, Ciudad 10', 10),
    ('Calle San Martín 888, Ciudad 11', 11),
    ('Avenida Belgrano 999, Ciudad 12', 12),
    ('Calle Rivadavia 1010, Ciudad 13', 13),
    ('Avenida Sarmiento 1111, Ciudad 14', 14),
    ('Calle Alberdi 1212, Ciudad 15', 15),
    ('Avenida Juan XXIII 1313, Ciudad 16', 16),
    ('Calle San Lorenzo 1414, Ciudad 17', 17),
    ('Avenida 9 de Julio 1515, Ciudad 18', 18),
    ('Calle Paseo Colón 1616, Ciudad 19', 19),
    ('Avenida Corrientes 1717, Ciudad 20', 20),
]

for domicilio in domicilio_data:
    cursor.execute("INSERT INTO domicilio (direccion, ciudad_id) VALUES (?, ?)", domicilio)

# Ejecutar las inserciones para la tabla sucursal con FK en domicilio
sucursal_data = [
    ( 1, 'jumbox1@jumbox.com', '+1234567890'),
    ( 2, 'jumbox2@jumbox.com', '+9876543210'),
    ( 3, 'jumbox3@jumbox.com', '+1112223333'),
    ( 4, 'jumbox4@jumbox.com', '+4445556666'),
    ( 5, 'jumbox5@jumbox.com', '+7778889999'),
    ( 6, 'jumbox6@jumbox.com', '+2223334444'),
    ( 7, 'jumbox7@jumbox.com', '+5556667777'),
    ( 8, 'jumbox8@jumbox.com', '+9990001111'),
]

for sucursal in sucursal_data:
    cursor.execute("INSERT INTO sucursal (domicilio_id, email, telefono) VALUES (?, ?, ?)", sucursal)

# Ejemplo de inserciones para la tabla empleado_sucursal con sucursal_id y domicilio_id únicos
empleado_sucursal_data = [
    ('Juan', 'González', 1, '1985-03-15', '2023-01-10', 1, 1),  # Empleado 1 en Sucursal 1 y Domicilio 1
    ('María', 'Martínez', 2, '1987-05-20', '2023-01-15', 2, 2),  # Empleado 2 en Sucursal 2 y Domicilio 2
    ('Carlos', 'López', 1, '1984-07-25', '2023-01-20', 3, 3),  # Empleado 3 en Sucursal 3 y Domicilio 3
    ('Ana', 'Fernández', 2, '1989-09-30', '2023-01-25', 4, 4),  # Empleado 4 en Sucursal 4 y Domicilio 4
    ('Diego', 'Rodríguez', 1, '1983-11-05', '2023-01-30', 5, 5),  # Empleado 5 en Sucursal 5 y Domicilio 5
    ('Laura', 'Gómez', 2, '1986-01-10', '2023-02-05', 6, 6),  # Empleado 6 en Sucursal 6 y Domicilio 6
    ('Pablo', 'Díaz', 1, '1982-03-15', '2023-02-10', 7, 7),  # Empleado 7 en Sucursal 7 y Domicilio 7
    ('Silvia', 'Pérez', 2, '1988-05-20', '2023-02-15', 8, 8),  # Empleado 8 en Sucursal 8 y Domicilio 8
    ('Jorge', 'Fernández', 1, '1981-07-25', '2023-02-20', 9, 9),  # Empleado 9 en Sucursal 9 y Domicilio 9
    ('Cecilia', 'Martínez', 2, '1990-09-30', '2023-02-25', 10, 10),  # Empleado 10 en Sucursal 10 y Domicilio 10
    ('Luis', 'González', 1, '1980-11-05', '2023-03-01', 11, 11),  # Empleado 11 en Sucursal 11 y Domicilio 11
    ('Valeria', 'López', 2, '1991-01-10', '2023-03-05', 12, 12),  # Empleado 12 en Sucursal 12 y Domicilio 12
    ('Martín', 'Sánchez', 1, '1979-03-15', '2023-03-10', 13, 13),  # Empleado 13 en Sucursal 13 y Domicilio 13
    ('Natalia', 'García', 2, '1992-05-20', '2023-03-15', 14, 14),  # Empleado 14 en Sucursal 14 y Domicilio 14
    ('Gustavo', 'Fernández', 1, '1978-07-25', '2023-03-20', 15, 15),  # Empleado 15 en Sucursal 15 y Domicilio 15
    ('Rosa', 'Díaz', 2, '1993-09-30', '2023-03-25', 16, 16),  # Empleado 16 en Sucursal 16 y Domicilio 16
]

for empleado in empleado_sucursal_data:
    cursor.execute("INSERT INTO empleado_sucursal (nombre, apellido, sexo_id, fecha_nac, fecha_incorporacion, domicilio_id, sucursal_id) VALUES (?, ?, ?, ?, ?, ?, ?)", empleado)


# Inserts para la tabla stock_producto
# Inserts para la tabla stock_producto con producto_id (donde aplicable)
stock_producto_data = [
    (80, 8, 4, 1),    # Producto 1 en unidad de medida 4
    (120, 12, 5, 2),  # Producto 2 en unidad de medida 5
    (70, 7, 1, 3),    # Producto 3 en unidad de medida 1
    (90, 9, 2, 6),  # 
    (60, 6, 3, 4),  # 
    (150, 15, 4, 7), # 
    (110, 11, 5, 8), #
    (100, 10, 1, 9), # 
    (130, 13, 2, 10), # 
    (85, 8, 3, 11),   # 
    (95, 9, 4, 12),   # 
    (75, 7, 5, 13),   # 
]
for stock in stock_producto_data:
    cursor.execute("INSERT INTO stock_producto (stock, stock_minimo, unidad_medida_id, producto_id) VALUES (?, ?, ?, ?)", stock)


# Inserts adicionales para la tabla sucursal_stock
sucursal_stock_data = [
    (6, 6),   # Sucursal 1 con stock_producto 6
    (7, 7),   # Sucursal 1 con stock_producto 7
    (8, 8),   # Sucursal 1 con stock_producto 8
    (9, 9),   # Sucursal 2 con stock_producto 9
    (10, 10), # Sucursal 2 con stock_producto 10
    (11, 11), # Sucursal 2 con stock_producto 11
    (12, 12), # Sucursal 3 con stock_producto 12
    (13, 13), # Sucursal 3 con stock_producto 13
    (14, 14), # Sucursal 3 con stock_producto 14
    (15, 15), # Sucursal 4 con stock_producto 15
]

for sucursal_stock in sucursal_stock_data:
    cursor.execute("INSERT INTO sucursal_stock (sucursal_id, stock_id) VALUES (?, ?)", sucursal_stock)


# Guardar los cambios y cerrar la conexión a la base de datos
conn.commit()
conn.close()

print("Inserciones realizadas con éxito.")
