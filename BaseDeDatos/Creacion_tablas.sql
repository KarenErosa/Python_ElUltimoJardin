CREATE TABLE categorias (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT
);

-- Crear tabla de productos
CREATE TABLE productos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  categoria_id INTEGER,
  nombre TEXT UNIQUE,
  precio REAL,
  FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

-- Crear tabla de empleados
CREATE TABLE empleados (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT,
  apellido_paterno TEXT,
  apellido_materno TEXT,
  horario TEXT,
  username TEXT UNIQUE,
  contrasena TEXT
);

CREATE TABLE ventas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fecha TEXT,
  hora TEXT,
  total_venta REAL,
  empleado_id TEXT,
  FOREIGN KEY (empleado_id) REFERENCES empleados(id)
);

-- Crear tabla de productos_vendidos
CREATE TABLE productos_vendidos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  venta_id INTEGER,
  producto_id INTEGER,
  cantidad INTEGER,
  importe REAL,
  FOREIGN KEY (venta_id) REFERENCES ventas(id),
  FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Crear tabla de ventas_por_categoria
CREATE TABLE ventas_por_categoria (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  categoria TEXT,
  cantidad_vendida INTEGER,
  total_diario REAL,
  fecha TEXT
);