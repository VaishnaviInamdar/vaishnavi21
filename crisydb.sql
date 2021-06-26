-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.5.19


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema recipe_recomendation
--

CREATE DATABASE IF NOT EXISTS recipe_recomendation;
USE recipe_recomendation;

--
-- Definition of table `tbl_recipe_details`
--

DROP TABLE IF EXISTS `tbl_recipe_details`;
CREATE TABLE `tbl_recipe_details` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `recipe_type` varchar(45) NOT NULL,
  `recipe_title` varchar(445) NOT NULL,
  `recipe_indgredients` varchar(445) NOT NULL,
  `recipe_procedure` varchar(45) NOT NULL,
  `recipe_video` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_recipe_details`
--

/*!40000 ALTER TABLE `tbl_recipe_details` DISABLE KEYS */;
INSERT INTO `tbl_recipe_details` (`id`,`recipe_type`,`recipe_title`,`recipe_indgredients`,`recipe_procedure`,`recipe_video`) VALUES 
 (1,'Breakfast','test','test','tragikn','HQqVSUvVi9Q'),
 (2,'Breakfast','test','test','tragikn','HQqVSUvVi9Q'),
 (3,'Breakfast','test','test','tragikn','HQqVSUvVi9Q'),
 (4,'Breakfast','test','test','tragikn','HQqVSUvVi9Q'),
 (5,'Dinner','pramod','teatts','bsjjsj','HQqVSUvVi9Q');
/*!40000 ALTER TABLE `tbl_recipe_details` ENABLE KEYS */;


--
-- Definition of table `tbl_user`
--

DROP TABLE IF EXISTS `tbl_user`;
CREATE TABLE `tbl_user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_user`
--

/*!40000 ALTER TABLE `tbl_user` DISABLE KEYS */;
INSERT INTO `tbl_user` (`id`,`email`,`password`,`name`,`mobile`,`address`) VALUES 
 (1,'ubaledinesh4u@gmail.com','12345','Dinesh Ubale','7350456969','Pune'),
 (2,'p@gmail.com','2345','pramod','9890430022','pune');
/*!40000 ALTER TABLE `tbl_user` ENABLE KEYS */;


--
-- Definition of table `tbl_weekly_planner`
--

DROP TABLE IF EXISTS `tbl_weekly_planner`;
CREATE TABLE `tbl_weekly_planner` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) NOT NULL,
  `date_` varchar(45) NOT NULL,
  `recipe_type` varchar(45) NOT NULL,
  `recipe_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_weekly_planner`
--

/*!40000 ALTER TABLE `tbl_weekly_planner` DISABLE KEYS */;
INSERT INTO `tbl_weekly_planner` (`id`,`user_id`,`date_`,`recipe_type`,`recipe_id`) VALUES 
 (1,'ubaledinesh4u@gmail.com','Wed, 9 Jun 2021','Breakfast','test'),
 (2,'ubaledinesh4u@gmail.com','Wed, 9 Jun 2021','Lunch','testing lunch recipe');
/*!40000 ALTER TABLE `tbl_weekly_planner` ENABLE KEYS */;


--
-- Definition of table `user_feedback`
--

DROP TABLE IF EXISTS `user_feedback`;
CREATE TABLE `user_feedback` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `rating` varchar(45) NOT NULL,
  `feedback` varchar(45) NOT NULL,
  `date` varchar(45) NOT NULL,
  `r_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_feedback`
--

/*!40000 ALTER TABLE `user_feedback` DISABLE KEYS */;
INSERT INTO `user_feedback` (`id`,`email`,`rating`,`feedback`,`date`,`r_id`) VALUES 
 (1,'ubaledinesh4u@gmail.com','5.0','test','20/06/2021 23:41:35','5'),
 (2,'p@gmail.com','4.8','hello','20/06/2021 23:41:35','5');
/*!40000 ALTER TABLE `user_feedback` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
