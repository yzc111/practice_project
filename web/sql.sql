/*
SQLyog Ultimate v12.08 (64 bit)
MySQL - 5.6.46 : Database - library
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`library` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `library`;

/*Table structure for table `book` */

DROP TABLE IF EXISTS `book`;

CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nam` varchar(255) DEFAULT NULL,
  `intro` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `lag` varchar(255) DEFAULT NULL,
  `typ` varchar(255) DEFAULT NULL,
  `cond` varchar(255) DEFAULT NULL,
  `ctime` varchar(255) DEFAULT NULL,
  `stock` varchar(255) DEFAULT NULL,
  `seller` varchar(255) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

/*Data for the table `book` */

insert  into `book`(`id`,`nam`,`intro`,`price`,`lag`,`typ`,`cond`,`ctime`,`stock`,`seller`,`uid`) values (20,'计算机网络','本书的特点是概念准确、论述严谨、内容新颖、图文并茂，突出基本原理和基本概念的阐述，同时力图反映计算机网络的一些最新发展。','26.5 元','中文','教材','七成新','2019.12.15','目前还有八本','山西财经大学信息学院学生',10),(21,'计算机网络','本书的特点是概念准确、论述严谨、内容新颖、图文并茂，突出基本原理和基本概念的阐述，同时力图反映计算机网络的一些最新发展。','26.5 元','中文','教材','七成新','2019.12.15','目前还有八本','山西财经大学信息学院学生',10),(22,'计算机网络','本书的特点是概念准确、论述严谨、内容新颖、图文并茂，突出基本原理和基本概念的阐述，同时力图反映计算机网络的一些最新发展。','26.5 元','中文','教材','七成新','2019.12.15','目前还有八本','山西财经大学信息学院学生',21),(23,'计算机网络','本书的特点是概念准确、论述严谨、内容新颖、图文并茂，突出基本原理和基本概念的阐述，同时力图反映计算机网络的一些最新发展。','26.5 元','中文','教材','七成新','2019.12.15','目前还有八本','山西财经大学信息学院学生',21);

/*Table structure for table `bookorder` */

DROP TABLE IF EXISTS `bookorder`;

CREATE TABLE `bookorder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `addre` varchar(255) DEFAULT NULL,
  `people` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `prodname` varchar(255) DEFAULT NULL,
  `unitprice` float DEFAULT NULL,
  `cou` int(11) DEFAULT NULL,
  `totalprice` float DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8;

/*Data for the table `bookorder` */

insert  into `bookorder`(`id`,`addre`,`people`,`phone`,`prodname`,`unitprice`,`cou`,`totalprice`,`uid`) values (69,'11','11','111','计算机网络技术',26.5,1,26.5,10),(70,'','','','计算机网络技术',26.5,1,26.5,21),(71,'','','','计算机网络技术',26.5,1,26.5,21),(72,'qwe','12346','195','计算机网络技术',26.5,1,26.5,21),(73,'','','','计算机网络技术',26.5,1,26.5,21);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `gender` int(11) DEFAULT NULL COMMENT '1:男 2:女',
  `age` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `place` varchar(255) DEFAULT NULL,
  `introduce` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

/*Data for the table `user` */

insert  into `user`(`id`,`name`,`gender`,`age`,`email`,`place`,`introduce`,`password`) values (10,'111111',1,1,'1347673839@qq.com','1','1','111111'),(21,'song123',1,21,'1958936108@qq.com','天津市','...','123456');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
