-- Crear tabla MLL_cfg
CREATE TABLE `mll_cfg` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Lista_emails` varchar(500) NOT NULL,
  `Credenciales` json NOT NULL,
  `En_Ejecucion` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Crear tabla MLL_cfg_bbdd
CREATE TABLE MLL_CFG_BBDD (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Conexion JSON NOT NULL comment "Contiene datos como host, usuario, contraseña, etc.",
    Ultima_Fecha_Carga DATETIME DEFAULT NULL
);

-- Crear tabla MLL_tablas
CREATE TABLE MLL_TABLAS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre_Tabla VARCHAR(100) NOT NULL,
    Borrar_Tabla BOOLEAN DEFAULT FALSE comment "Si se borra la tabla de BD_Mallorquina"
);

-- Crear tabla MLL_campos
CREATE TABLE MLL_CAMPOS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_Tabla INT NOT NULL comment "Relación con la tabla MLL_tablas",
    Campo_Nombre VARCHAR(100) NOT NULL,
    Campo_Tipo VARCHAR(50) NOT NULL,
    FOREIGN KEY (ID_Tabla) REFERENCES MLL_tablas(ID)
);

-- Crear tabla MLL_tablas_bbdd
CREATE TABLE MLL_TABLAS_BBDD (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_BBDD INT NOT NULL comment "Relación con la tabla MLL_cfg_bbdd",
    ID_Tabla INT NOT NULL comment "Relación con la tabla MLL_tablas",
    Fecha_Ultima_Actualizacion DATETIME DEFAULT NULL,
    Cada_Cuanto_Ejecutar INT DEFAULT 1 comment "Intervalo en días para ejecutar",
    FOREIGN KEY (ID_BBDD) REFERENCES MLL_cfg_bbdd(ID),
    FOREIGN KEY (ID_Tabla) REFERENCES MLL_tablas(ID)
);
