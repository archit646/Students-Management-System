-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `Roll_no` int NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Contact` bigint DEFAULT NULL,
  `Dob` date DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Roll_no`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Amit Sharma','amit1@example.com','Male',9876543210,'2000-01-15','Delhi'),(2,'Neha Verma','neha2@example.com','Female',9876543211,'2001-02-20','Mumbai'),(3,'Rahul Gupta','rahul3@example.com','Male',9876543212,'1999-12-10','Kolkata'),(4,'Pooja Singh','pooja4@example.com','Female',9876543213,'2002-05-25','Chennai'),(5,'Vikram Yadav','vikram5@example.com','Male',9876543214,'2000-07-18','Pune'),(6,'Sneha Pandey','sneha6@example.com','Female',9876543215,'2001-08-30','Bangalore'),(7,'Suresh Kumar','suresh7@example.com','Male',9876543216,'1998-09-12','Hyderabad'),(8,'Meena Joshi','meena8@example.com','Female',9876543217,'1999-10-05','Jaipur'),(9,'Rohit Mehta','rohit9@example.com','Male',9876543218,'2002-03-28','Lucknow'),(10,'Anjali Saxena','anjali10@example.com','Female',9876543219,'2001-06-15','Indore'),(11,'Arjun Kapoor','arjun11@example.com','Male',9876543220,'2000-11-23','Nagpur'),(12,'Simran Kaur','simran12@example.com','Female',9876543221,'1999-04-11','Chandigarh'),(13,'Harsh Tiwari','harsh13@example.com','Male',9876543222,'2001-07-07','Patna'),(14,'Divya Mishra','divya14@example.com','Female',9876543223,'2002-09-21','Bhopal'),(15,'Manish Sharma','manish15@example.com','Male',9876543224,'2000-02-14','Guwahati'),(16,'Ritu Jain','ritu16@example.com','Female',9876543225,'2001-03-29','Dehradun'),(17,'Tarun Malhotra','tarun17@example.com','Male',9876543226,'1999-06-10','Agra'),(18,'Kavita Rani','kavita18@example.com','Female',9876543227,'2002-01-18','Varanasi'),(19,'Aditya Prasad','aditya19@example.com','Male',9876543228,'2001-08-05','Surat'),(20,'Nidhi Sinha','nidhi20@example.com','Female',9876543229,'2000-12-30','Ranchi'),(21,'Rakesh Kumar','rakesh21@example.com','Male',9876543230,'1998-10-15','Jodhpur'),(22,'Preeti Saxena','preeti22@example.com','Female',9876543231,'2001-05-08','Shimla'),(23,'Gaurav Nanda','gaurav23@example.com','Male',9876543232,'2002-07-19','Mysore'),(24,'Swati Das','swati24@example.com','Female',9876543233,'1999-11-25','Kanpur'),(25,'Deepak Chawla','deepak25@example.com','Male',9876543234,'2000-03-12','Udaipur'),(26,'Anusha Reddy','anusha26@example.com','Female',9876543235,'2001-06-21','Vijayawada'),(27,'Siddharth Jha','siddharth27@example.com','Male',9876543236,'1999-09-05','Raipur'),(28,'Juhi Thakur','juhi28@example.com','Female',9876543237,'2002-02-08','Coimbatore'),(29,'Ashish Patil','ashish29@example.com','Male',9876543238,'2000-04-25','Bhubaneswar'),(30,'Pallavi Singh','pallavi30@example.com','Female',9876543239,'2001-11-11','Madurai'),(31,'Mohit Rana','mohit31@example.com','Male',9876543240,'2000-07-08','Nashik'),(32,'Sonali Ghosh','sonali32@example.com','Female',9876543241,'2001-10-20','Amritsar'),(33,'Vikas Saini','vikas33@example.com','Male',9876543242,'1999-12-18','Gwalior'),(34,'Alka Yadav','alka34@example.com','Female',9876543243,'2002-05-14','Meerut'),(35,'Nitin Joshi','nitin35@example.com','Male',9876543244,'2000-02-28','Haridwar'),(36,'Bhavna Kapoor','bhavna36@example.com','Female',9876543245,'2001-08-22','Jalandhar'),(37,'Rajesh Sharma','rajesh37@example.com','Male',9876543246,'1999-06-09','Panaji'),(38,'Kirti Agarwal','kirti38@example.com','Female',9876543247,'2002-03-15','Kochi'),(39,'Hemant Verma','hemant39@example.com','Male',9876543248,'2001-04-17','Kurnool'),(40,'Megha Sharma','megha40@example.com','Female',9876543249,'2000-09-29','Solapur'),(41,'Ankur Saxena','ankur41@example.com','Male',9876543250,'1998-11-10','Kakinada'),(42,'Priyanka Das','priyanka42@example.com','Female',9876543251,'2001-07-27','Siliguri'),(43,'Dinesh Kumar','dinesh43@example.com','Male',9876543252,'1999-10-06','Gandhinagar'),(44,'Shweta Tiwari','shweta44@example.com','Female',9876543253,'2002-12-24','Kozhikode'),(45,'Ravi Patel','ravi45@example.com','Male',9876543254,'2000-05-13','Thrissur'),(46,'Pankaj Yadav','pankaj46@example.com','Male',9876543255,'2001-02-09','Ajmer'),(47,'Jyoti Sinha','jyoti47@example.com','Female',9876543256,'1999-06-17','Cuttack'),(48,'Satish Mehra','satish48@example.com','Male',9876543257,'2002-08-23','Ujjain'),(49,'Kiran Sharma','kiran49@example.com','Female',9876543258,'2001-09-30','Bilaspur'),(50,'Mahesh Bhatt','mahesh50@example.com','Male',9876543259,'2000-03-05','Tirupati');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-06 18:04:30
