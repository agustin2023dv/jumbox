import sqlite3

# Conectar a la base de datos 
conn = sqlite3.connect("jumbox.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla 'provincia'
cursor.execute("""
CREATE TABLE IF NOT EXISTS provincia (
    id_provincia INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);
""")

# Crear la tabla 'ciudad' con relación a 'provincia'
cursor.execute("""
CREATE TABLE IF NOT EXISTS ciudad (
    id_ciudad INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    provincia_id INTEGER NOT NULL,
    FOREIGN KEY (provincia_id) REFERENCES provincia (id_provincia)
);
""")

# Crear la tabla 'domicilio' con relación a 'ciudad'
cursor.execute("""
CREATE TABLE IF NOT EXISTS domicilio (
    id_domicilio INTEGER PRIMARY KEY AUTOINCREMENT,
    direccion TEXT NOT NULL,
    ciudad_id INTEGER NOT NULL,
    FOREIGN KEY (ciudad_id) REFERENCES ciudad (id_ciudad)
);
""")

# Crear la tabla 'categoria_producto'
cursor.execute("""
CREATE TABLE IF NOT EXISTS categoria_producto (
    id_categoria_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT
);
""")

# Crear la tabla 'unidad_medida'
cursor.execute("""
CREATE TABLE IF NOT EXISTS unidad_medida (
    id_unidad_medida INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_producto (
    id_stock_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    stock INTEGER NOT NULL,
    stock_minimo INTEGER NOT NULL,
    unidad_medida_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    FOREIGN KEY (unidad_medida_id) REFERENCES unidad_medida (id_unidad_medida),
    FOREIGN KEY (producto_id) REFERENCES producto (id_producto)
);
""")

# Crear la tabla 'producto' con relación a 'categoria_producto' y 'stock_producto'
cursor.execute("""
CREATE TABLE IF NOT EXISTS producto (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL,
    categoria_id INTEGER NOT NULL,

    FOREIGN KEY (categoria_id) REFERENCES categoria_producto (id_categoria_producto)
);
""")


# Crear la tabla 'sucursal' con relación a 'domicilio'
cursor.execute("""
CREATE TABLE IF NOT EXISTS sucursal (
    id_sucursal INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    telefono TEXT,
    domicilio_id INTEGER NOT NULL,
    FOREIGN KEY (domicilio_id) REFERENCES domicilio (id_domicilio)
);
""")




# Crear la tabla 'sucursal_stock' para la relación muchos a muchos entre 'sucursal' y 'stock_producto'
cursor.execute("""
CREATE TABLE IF NOT EXISTS sucursal_stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sucursal_id INTEGER NOT NULL,
    stock_id INTEGER NOT NULL,
    FOREIGN KEY (sucursal_id) REFERENCES sucursal (id_sucursal),
    FOREIGN KEY (stock_id) REFERENCES stock_producto (id_stock_producto)
);
""")

# Crear la tabla 'sexo'
cursor.execute("""
CREATE TABLE IF NOT EXISTS sexo (
    id_sexo INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);
""")

# Crear la tabla 'empleado_sucursal' con relación a 'sexo', 'domicilio' y 'sucursal'
cursor.execute("""
CREATE TABLE IF NOT EXISTS empleado_sucursal (
    id_empleado_sucursal INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    sexo_id INTEGER NOT NULL,
    fecha_nac DATE,
    fecha_incorporacion DATE,
    domicilio_id INTEGER NOT NULL,
    sucursal_id INTEGER NOT NULL,
    FOREIGN KEY (sexo_id) REFERENCES sexo (id_sexo),
    FOREIGN KEY (domicilio_id) REFERENCES domicilio (id_domicilio),
    FOREIGN KEY (sucursal_id) REFERENCES sucursal (id_sucursal)
);
""")

# Crear la tabla 'cliente' con relación a 'sexo', 'domicilio' y 'sucursal'
cursor.execute("""
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    sexo_id INTEGER NOT NULL,
    fecha_nac DATE,
    telefono TEXT,
    email TEXT,
    domicilio_id INTEGER NOT NULL,
    FOREIGN KEY (sexo_id) REFERENCES sexo (id_sexo),
    FOREIGN KEY (domicilio_id) REFERENCES domicilio (id_domicilio)
);
""")

# Crear la tabla 'factura'
cursor.execute("""
CREATE TABLE IF NOT EXISTS factura (
    id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha DATE,
    cliente_id INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES cliente (id_cliente)
);
""")

# Crear la tabla 'detalle_factura' con relación a 'factura' y 'producto'
cursor.execute("""
CREATE TABLE IF NOT EXISTS detalle_factura (
    id_detalle_factura INTEGER PRIMARY KEY AUTOINCREMENT,
    factura_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    FOREIGN KEY (factura_id) REFERENCES factura (id_factura),
    FOREIGN KEY (producto_id) REFERENCES producto (id_producto)
);
""")

# Guardar los cambios y cerrar la conexión a la base de datos
conn.commit()
conn.close()

print("Base de datos creada exitosamente.")
