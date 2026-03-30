-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: haircut_memberships
-- ------------------------------------------------------
-- Server version	8.0.43

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
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `AppointmentID` int NOT NULL AUTO_INCREMENT,
  `CustomerID` int DEFAULT NULL,
  `HTypeID` int DEFAULT NULL,
  `StaffID` int DEFAULT NULL,
  `appointmentDate` date DEFAULT NULL,
  `appointmentTime` time DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`AppointmentID`),
  KEY `CustomerID` (`CustomerID`),
  KEY `HTypeID` (`HTypeID`),
  KEY `StaffID` (`StaffID`),
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`),
  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`HTypeID`) REFERENCES `haircut_types` (`HTypeID`),
  CONSTRAINT `appointments_ibfk_3` FOREIGN KEY (`StaffID`) REFERENCES `staff` (`StaffID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `beard_trims`
--

DROP TABLE IF EXISTS `beard_trims`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beard_trims` (
  `BeardTrimID` int NOT NULL AUTO_INCREMENT,
  `beardtrim` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `beardtrimcost` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`BeardTrimID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beard_trims`
--

LOCK TABLES `beard_trims` WRITE;
/*!40000 ALTER TABLE `beard_trims` DISABLE KEYS */;
/*!40000 ALTER TABLE `beard_trims` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `CustomerID` int NOT NULL AUTO_INCREMENT,
  `cfirst_name` varchar(50) DEFAULT NULL,
  `clast_name` varchar(50) DEFAULT NULL,
  `membership_status` tinyint(1) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `haircut_types`
--

DROP TABLE IF EXISTS `haircut_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `haircut_types` (
  `HTypeID` int NOT NULL AUTO_INCREMENT,
  `htype` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `htypeCost` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`HTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `haircut_types`
--

LOCK TABLES `haircut_types` WRITE;
/*!40000 ALTER TABLE `haircut_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `haircut_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hairwash_types`
--

DROP TABLE IF EXISTS `hairwash_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hairwash_types` (
  `HWTypesID` int NOT NULL AUTO_INCREMENT,
  `hwtype` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `hwcost` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`HWTypesID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hairwash_types`
--

LOCK TABLES `hairwash_types` WRITE;
/*!40000 ALTER TABLE `hairwash_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `hairwash_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membership_types`
--

DROP TABLE IF EXISTS `membership_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membership_types` (
  `MTypeID` int NOT NULL AUTO_INCREMENT,
  `mtype` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `mtypeCost` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`MTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membership_types`
--

LOCK TABLES `membership_types` WRITE;
/*!40000 ALTER TABLE `membership_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `membership_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_details`
--

DROP TABLE IF EXISTS `order_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_details` (
  `OrderDetailsID` int NOT NULL AUTO_INCREMENT,
  `OrderID` int DEFAULT NULL,
  `RefundID` int DEFAULT NULL,
  `CostBeforeTax` decimal(6,2) DEFAULT NULL,
  `Tax` decimal(6,2) DEFAULT NULL,
  `CostAfterTax` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`OrderDetailsID`),
  KEY `OrderID` (`OrderID`),
  KEY `RefundID` (`RefundID`),
  CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`),
  CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`RefundID`) REFERENCES `refunds` (`RefundID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_details`
--

LOCK TABLES `order_details` WRITE;
/*!40000 ALTER TABLE `order_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `OrderID` int NOT NULL AUTO_INCREMENT,
  `CustomerID` int DEFAULT NULL,
  `HTypeID` int DEFAULT NULL,
  `MTypeID` int DEFAULT NULL,
  `ProductID` int DEFAULT NULL,
  `AppointmentID` int DEFAULT NULL,
  `orderCost` decimal(6,2) DEFAULT NULL,
  `HWTypesID` int DEFAULT NULL,
  `BeardTrimID` int DEFAULT NULL,
  `PaymentMethod` varchar(50) DEFAULT NULL,
  `cardNumber` int DEFAULT NULL,
  `expiration_date` date DEFAULT NULL,
  PRIMARY KEY (`OrderID`),
  KEY `CustomerID` (`CustomerID`),
  KEY `HTypeID` (`HTypeID`),
  KEY `MTypeID` (`MTypeID`),
  KEY `ProductID` (`ProductID`),
  KEY `AppointmentID` (`AppointmentID`),
  KEY `HWTypesID` (`HWTypesID`),
  KEY `BeardTrimID` (`BeardTrimID`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`HTypeID`) REFERENCES `haircut_types` (`HTypeID`),
  CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`MTypeID`) REFERENCES `membership_types` (`MTypeID`),
  CONSTRAINT `orders_ibfk_4` FOREIGN KEY (`ProductID`) REFERENCES `products` (`ProductID`),
  CONSTRAINT `orders_ibfk_5` FOREIGN KEY (`AppointmentID`) REFERENCES `appointments` (`AppointmentID`),
  CONSTRAINT `orders_ibfk_6` FOREIGN KEY (`HWTypesID`) REFERENCES `hairwash_types` (`HWTypesID`),
  CONSTRAINT `orders_ibfk_7` FOREIGN KEY (`BeardTrimID`) REFERENCES `beard_trims` (`BeardTrimID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `ProductID` int NOT NULL AUTO_INCREMENT,
  `product` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `productCost` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`ProductID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `refunds`
--

DROP TABLE IF EXISTS `refunds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `refunds` (
  `RefundID` int NOT NULL AUTO_INCREMENT,
  `refundReason` varchar(100) DEFAULT NULL,
  `refundAmount` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`RefundID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `refunds`
--

LOCK TABLES `refunds` WRITE;
/*!40000 ALTER TABLE `refunds` DISABLE KEYS */;
/*!40000 ALTER TABLE `refunds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `StaffID` int NOT NULL AUTO_INCREMENT,
  `sfirst_name` varchar(50) DEFAULT NULL,
  `slast_name` varchar(50) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`StaffID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-30 12:31:42
