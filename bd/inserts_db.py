import sqlite3

# Conectar a la base de datos (asegúrate de que el archivo "jumbox.db" exista)

# Conectar a la base de datos
conn = sqlite3.connect("C:/Users/agust/OneDrive/Escritorio/JUMBOX/jumbox.db")


# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Inserts adicionales para la tabla sexo
sexo_data = [
    ('Otro'), # Sexo no especificado
    ('Prefiero no decirlo') # Opción para no revelar el sexo
]

for sexo in sexo_data:
    cursor.execute("INSERT INTO sexo (nombre) VALUES (?)", (sexo,))

# Inserts adicionales para la tabla provincia
provincia_data = [
    ('La Pampa'),
    ('San Luis'),
    ('Catamarca'),
    ('La Rioja'),
    ('Tierra del Fuego'),
    ('Santa Cruz'),
    ('Santiago del Estero'),
    ('Chubut'),
    ('San Juan'),
    ('Misiones'),
]

for provincia in provincia_data:
    cursor.execute("INSERT INTO provincia (nombre) VALUES (?)", (provincia,))

# Inserts adicionales para la tabla ciudad
ciudad_data = [
    ('Santa Rosa', 1), # La provincia de La Pampa tiene el id 16
    ('Villa Mercedes', 2), # La provincia de San Luis tiene el id 17
    ('San Fernando del Valle de Catamarca', 3),
    ('La Rioja', 4),
    ('Ushuaia', 5), # La provincia de Tierra del Fuego tiene el id 18
    ('Río Gallegos', 6), # La provincia de Santa Cruz tiene el id 19
    ('Santiago del Estero', 7),
    ('Comodoro Rivadavia', 8), # La provincia de Chubut tiene el id 20
    ('San Juan', 9),
    ('Posadas', 10), # La provincia de Misiones tiene el id 21
]

for ciudad in ciudad_data:
    cursor.execute("INSERT INTO ciudad (nombre, provincia_id) VALUES (?, ?)", ciudad)

# Inserts adicionales para la tabla domicilio
domicilio_data = [
    ('Calle 456, Ciudad 16', 16),  # Ciudad 16 tiene el id 16 (debes ajustarlo según tu base de datos)
    ('Avenida Central 789, Ciudad 17', 17),  # Ciudad 17 tiene el id 17
    ('Calle del Valle 101, Ciudad 18', 18),  # Ciudad 18 tiene el id 18
    ('Calle 123, Ciudad 19', 19),  # Ciudad 19 tiene el id 19
    ('Avenida Principal 456, Ciudad 20', 20),  # Ciudad 20 tiene el id 20
]

for domicilio in domicilio_data:
    cursor.execute("INSERT INTO domicilio (direccion, ciudad_id) VALUES (?, ?)", domicilio)

# Inserts adicionales para la tabla categoria_producto
categoria_producto_data = [
    ('Pescados', 'Productos del mar'),
    ('Electrodomésticos', 'Electrodomésticos para el hogar'),
    ('Jardinería', 'Productos para jardín'),
    ('Farmacia', 'Productos farmacéuticos'),
    ('Ropa Deportiva', 'Ropa y accesorios deportivos'),
    ('Librería', 'Productos de papelería y libros'),
    ('Muebles', 'Muebles para el hogar'),
    ('Tecnología', 'Productos electrónicos y tecnológicos'),
    ('Instrumentos Musicales', 'Instrumentos musicales y accesorios'),
    ('Decoración', 'Productos de decoración'),
]

for categoria in categoria_producto_data:
    cursor.execute("INSERT INTO categoria_producto (nombre, descripcion) VALUES (?, ?)", categoria)

# Inserts adicionales para la tabla unidad_medida
unidad_medida_data = [
    ('Botella', 'Unidad de medida en botellas'),
    ('Paquete', 'Unidad de medida en paquetes'),
    ('Metro Cuadrado', 'Unidad de medida en metros cuadrados'),
    ('Lata', 'Unidad de medida en latas'),
    ('Pieza', 'Unidad de medida en piezas'),
    ('Bolsa', 'Unidad de medida en bolsas'),
    ('Kilómetro', 'Unidad de medida en kilómetros'),
    ('Metros Cúbicos', 'Unidad de medida en metros cúbicos'),
    ('Centímetros', 'Unidad de medida en centímetros'),
    ('Mililitros', 'Unidad de medida en mililitros'),
]

for unidad in unidad_medida_data:
    cursor.execute("INSERT INTO unidad_medida (nombre, descripcion) VALUES (?, ?)", unidad)

# Inserciones adicionales para la tabla producto
producto_data = [
    ('Salmón Fresco', 'Salmón fresco de alta calidad', 12.99, 1),  # Categoría: Pescados
    ('Lavadora de Carga Frontal', 'Lavadora de última generación', 599.99, 2),  # Categoría: Electrodomésticos
    ('Podadora de Césped', 'Podadora para mantener tu césped en perfecto estado', 149.99, 3),  # Categoría: Jardinería
    ('Aspirina', 'Tabletas de aspirina para el alivio del dolor', 5.99, 4),  # Categoría: Farmacia
    ('Zapatillas de Running', 'Zapatillas deportivas para correr', 89.99, 5),  # Categoría: Ropa Deportiva
    ('Libro "1984" de George Orwell', 'Clásico de la literatura distópica', 14.99, 6),  # Categoría: Librería
    ('Sofá de Cuero', 'Sofá de cuero genuino para la sala de estar', 699.99, 7),  # Categoría: Muebles
    ('Smartphone Samsung Galaxy S22', 'Teléfono inteligente de última generación', 999.99, 8),  # Categoría: Tecnología
    ('Guitarra Acústica', 'Guitarra acústica de concierto', 299.99, 9),  # Categoría: Instrumentos Musicales
    ('Cuadro de Arte Abstracto', 'Cuadro decorativo para tu hogar', 49.99, 10),  # Categoría: Decoración
    ('Camiseta de Fútbol', 'Camiseta oficial de tu equipo favorito', 29.99, 5),  # Categoría: Ropa Deportiva
    ('Calculadora Científica', 'Calculadora científica para estudiantes', 19.99, 6),  # Categoría: Librería
    ('Mesa de Comedor', 'Mesa de comedor de madera maciza', 349.99, 7),  # Categoría: Muebles
    ('Tablet iPad Pro', 'Tablet de alta gama con pantalla retina', 799.99, 8),  # Categoría: Tecnología
    ('Teclado Eléctrico', 'Teclado musical electrónico', 199.99, 9),  # Categoría: Instrumentos Musicales
    ('Lámpara de Pie', 'Lámpara de pie con diseño moderno', 69.99, 10),  # Categoría: Decoración
    ('Cámara Réflex Nikon D850', 'Cámara réflex digital de alta resolución', 1499.99, 13),  # Categoría: Fotografía
    ('Maleta de Viaje', 'Maleta resistente para tus aventuras', 79.99, 14),  # Categoría: Viajes
    ('Sartén Antiadherente', 'Sartén antiadherente de calidad premium', 39.99, 15),  # Categoría: Instrumentos Culinarios
    ('Traje de Negocios', 'Traje elegante para hombres', 199.99, 19),  # Categoría: Ropa de Oficina
]


for producto in producto_data:
    cursor.execute("INSERT INTO producto (nombre, descripcion, precio, categoria_id) VALUES (?, ?, ?, ?)", producto)

# Inserts adicionales para la tabla empleado_sucursal
empleado_sucursal_data = [
    ('Elena', 'Sánchez', 2, '1987-02-20', '2023-03-01', 20, 20),
    ('Andrés', 'Pérez', 1, '1985-04-15', '2023-03-05', 21, 21),
    ('Sofía', 'Torres', 2, '1988-06-25', '2023-03-10', 22, 22),
    ('Ricardo', 'Gómez', 1, '1986-08-30', '2023-03-15', 23, 23),
    ('Carmen', 'López', 2, '1984-10-05', '2023-03-20', 24, 24),
    ('Javier', 'Martínez', 1, '1989-12-10', '2023-03-25', 25, 25),
    ('Isabella', 'Rodríguez', 2, '1983-02-15', '2023-04-01', 26, 26),
    ('Emilio', 'Fernández', 1, '1990-04-20', '2023-04-05', 27, 27),
    ('Lucía', 'García', 2, '1982-06-25', '2023-04-10', 28, 28),
    ('Adrián', 'Díaz', 1, '1981-08-30', '2023-04-15', 29, 29),
]

for empleado in empleado_sucursal_data:
    cursor.execute("INSERT INTO empleado_sucursal (nombre, apellido, sexo_id, fecha_nac, fecha_incorporacion, domicilio_id, sucursal_id) VALUES (?, ?, ?, ?, ?, ?, ?)", empleado)

# Inserts adicionales para la tabla cliente
cliente_data = [
    ('Pedro', 'Ramírez', 1, '1986-03-10', '+1122334455', 'pedro@email.com', 30),
    ('Marcela', 'González', 2, '1989-05-15', '+5566778899', 'marcela@email.com', 31),
    ('Alejandro', 'Silva', 1, '1984-07-20', '+9900112233', 'alejandro@email.com', 32),
    ('Florencia', 'Hernández', 2, '1987-09-25', '+3322114455', 'florencia@email.com', 33),
    ('Gustavo', 'Torres', 1, '1983-11-30', '+7755332211', 'gustavo@email.com', 34),
    ('Laura', 'Ríos', 2, '1990-02-05', '+1122334466', 'laura@email.com', 35),
    ('Miguel', 'Ortega', 1, '1982-04-10', '+5566778900', 'miguel@email.com', 36),
    ('Valentina', 'Mendoza', 2, '1991-06-15', '+9900112234', 'valentina@email.com', 37),
    ('Roberto', 'Romero', 1, '1981-08-20', '+3322114456', 'roberto@email.com', 38),
    ('Luciana', 'Pérez', 2, '1992-10-25', '+7755332212', 'luciana@email.com', 39),
]

for cliente in cliente_data:
    cursor.execute("INSERT INTO cliente (nombre, apellido, sexo_id, fecha_nac, telefono, email, domicilio_id) VALUES (?, ?, ?, ?, ?, ?, ?)", cliente)

# Inserts adicionales para la tabla factura
factura_data = [
    ('2023-03-01', 30),
    ('2023-03-02', 31),
    ('2023-03-03', 32),
    ('2023-03-04', 33),
    ('2023-03-05', 34),
    ('2023-03-06', 35),
    ('2023-03-07', 36),
    ('2023-03-08', 37),
    ('2023-03-09', 38),
    ('2023-03-10', 39),
]

for factura in factura_data:
    cursor.execute("INSERT INTO factura (fecha, cliente_id) VALUES (?, ?)", factura)


# Inserts adicionales para la tabla detalle_factura
detalle_factura_data = [
    (1, 5, 3, 2.5),
    (2, 3, 4, 2.0),
    (3, 2, 2, 1.8),
    (4, 6, 1, 10.5),
    (5, 7, 2, 8.0),
    (6, 8, 5, 1.5),
    (7, 9, 3, 3.0),
    (8, 4, 2, 2.0),
    (9, 1, 4, 1.2),
    (10, 10, 2, 2.0),
]


for detalle in detalle_factura_data:
    cursor.execute("INSERT INTO detalle_factura (factura_id, producto_id, cantidad, precio_unitario) VALUES (?, ?, ?, ?)", detalle)

# Inserts adicionales para la tabla venta
venta_data = [
    ('2023-02-01', 1, 1),
    ('2023-02-02', 2, 2),
    ('2023-02-03', 3, 3),
    ('2023-02-04', 4, 4),
    ('2023-02-05', 5, 5),
    ('2023-02-06', 6, 6),
    ('2023-02-07', 7, 7),
    ('2023-02-08', 8, 8),
    ('2023-02-09', 9, 9),
    ('2023-02-10', 10, 10),
]

for venta in venta_data:
    cursor.execute("INSERT INTO venta (fecha, empleado_id, sucursal_id) VALUES (?, ?, ?)", venta)


detalle_venta_data = [
    (1, 5, 3, 2.5),  # Eliminamos el valor 11
    (2, 3, 4, 2.0),
    (3, 2, 2, 1.8),
    (4, 6, 1, 10.5),
    (5, 7, 2, 8.0),
    (6, 8, 5, 1.5),
    (7, 9, 3, 3.0),
    (8, 4, 2, 2.0),
    (9, 1, 4, 1.2),
    (10, 10, 2, 2.0),
]

for detalle in detalle_venta_data:
    cursor.execute("INSERT INTO detalle_venta (venta_id, producto_id, cantidad, precio_unitario) VALUES (?, ?, ?, ?)", detalle)



# Guardar los cambios y cerrar la conexión a la base de datos
conn.commit()
conn.close()

print("Inserciones adicionales realizadas con éxito.")