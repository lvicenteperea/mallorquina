-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mallorquina
-- ------------------------------------------------------
-- Server version	9.0.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `mll_campos`
--

DROP TABLE IF EXISTS `mll_campos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mll_campos` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ID_Tabla` int NOT NULL COMMENT 'Relación con la tabla MLL_tablas',
  `Nombre` varchar(100) NOT NULL,
  `Nombre_Destino` varchar(100) DEFAULT NULL,
  `Tipo` varchar(50) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `ID_Tabla` (`ID_Tabla`),
  CONSTRAINT `mll_campos_ibfk_1` FOREIGN KEY (`ID_Tabla`) REFERENCES `mll_tablas` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mll_campos`
--

LOCK TABLES `mll_campos` WRITE;
/*!40000 ALTER TABLE `mll_campos` DISABLE KEYS */;
INSERT INTO `mll_campos` VALUES (1,1,'[Id Puesto]','Id_Puesto','int'),(2,1,'Descripcion','Descripcion','varchar(100)'),(3,2,'stIdEnt','stIdEnt','nvarchar(20)'),(4,2,'Nombre','Nombre','nvarchar(100)'),(5,2,'[Id Modo SQL]','Id_Modo_SQL','int');
/*!40000 ALTER TABLE `mll_campos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mll_cfg`
--

DROP TABLE IF EXISTS `mll_cfg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mll_cfg` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Lista_emails` varchar(500) NOT NULL,
  `Credenciales` json NOT NULL,
  `En_Ejecucion` tinyint(1) DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mll_cfg`
--

LOCK TABLES `mll_cfg` WRITE;
/*!40000 ALTER TABLE `mll_cfg` DISABLE KEYS */;
-- INSERT INTO `mll_cfg` VALUES (1,'lvicente@hangarxxi
-- .com','{\"de\": \"contacto@somosimaginales.com\", \"host\": \"smtp.sen
-- dgrid.net\", \"puerto\": \"587\", \"usuario\": \"apikey\", \"pass
-- word\": \"", \"reply_to\": \"co
-- ntacto@somosimaginales.com\"}',0);
/*!40000 ALTER TABLE `mll_cfg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mll_cfg_bbdd`
--

DROP TABLE IF EXISTS `mll_cfg_bbdd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mll_cfg_bbdd` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) NOT NULL,
  `Conexion` json NOT NULL COMMENT 'Contiene datos como host, usuario, contraseña, etc.',
  `Ultima_Fecha_Carga` datetime DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mll_cfg_bbdd`
--

LOCK TABLES `mll_cfg_bbdd` WRITE;
/*!40000 ALTER TABLE `mll_cfg_bbdd` DISABLE KEYS */;
INSERT INTO `mll_cfg_bbdd` VALUES (1,'Velázquez','{\"host\": \"\", \"port\": \"\", \"user\": \"\", \"database\": \"\", \"password\": \"\"}','2024-11-16 15:29:37'),(2,'Quevedo','{\"host\": \"\", \"port\": \"\", \"user\": \"\", \"database\": \"\", \"password\": \"\"}','2024-11-20 15:29:37');
/*!40000 ALTER TABLE `mll_cfg_bbdd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mll_tablas`
--

DROP TABLE IF EXISTS `mll_tablas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mll_tablas` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Tabla_Origen` varchar(100) NOT NULL,
  `Tabla_Destino` varchar(100) DEFAULT NULL,
  `Borrar_Tabla` tinyint(1) DEFAULT '0' COMMENT 'Si se borra la tabla de BD_Mallorquina',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mll_tablas`
--

LOCK TABLES `mll_tablas` WRITE;
/*!40000 ALTER TABLE `mll_tablas` DISABLE KEYS */;
INSERT INTO `mll_tablas` VALUES (1,'[Puestos Facturacion]','tpv_Puestos_Facturacion',0),(2,'Entidades','tpv_Entidades',0);
/*!40000 ALTER TABLE `mll_tablas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mll_tablas_bbdd`
--

DROP TABLE IF EXISTS `mll_tablas_bbdd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mll_tablas_bbdd` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ID_BBDD` int NOT NULL COMMENT 'Relación con la tabla MLL_cfg_bbdd',
  `ID_Tabla` int NOT NULL COMMENT 'Relación con la tabla MLL_tablas',
  `Fecha_Ultima_Actualizacion` datetime DEFAULT NULL,
  `Cada_Cuanto_Ejecutar` int DEFAULT '1' COMMENT 'Intervalo en días para ejecutar',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `ID_BBDD` (`ID_BBDD`),
  KEY `ID_Tabla` (`ID_Tabla`),
  CONSTRAINT `mll_tablas_bbdd_ibfk_1` FOREIGN KEY (`ID_BBDD`) REFERENCES `mll_cfg_bbdd` (`ID`),
  CONSTRAINT `mll_tablas_bbdd_ibfk_2` FOREIGN KEY (`ID_Tabla`) REFERENCES `mll_tablas` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mll_tablas_bbdd`
--

LOCK TABLES `mll_tablas_bbdd` WRITE;
/*!40000 ALTER TABLE `mll_tablas_bbdd` DISABLE KEYS */;
INSERT INTO `mll_tablas_bbdd` VALUES (1,1,1,'2024-11-19 19:18:33',1),(2,1,2,'2024-11-19 19:18:33',1),(3,2,1,'2024-11-16 15:29:37',1),(4,2,2,'2024-11-16 15:29:37',1);
/*!40000 ALTER TABLE `mll_tablas_bbdd` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-26 13:17:13
