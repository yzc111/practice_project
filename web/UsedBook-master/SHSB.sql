/*
MySQL Data Transfer
Source Host: 123.56.12.176
Source Database: SHSB
Target Host: 123.56.12.176
Target Database: SHSB
Date: 2020/7/3 11:46:58
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for T_Admin
-- ----------------------------
CREATE TABLE `T_Admin` (
  `Admin_id` int(11) NOT NULL AUTO_INCREMENT,
  `Admin_true_name` char(4) CHARACTER SET utf8 DEFAULT NULL,
  `Admin_login_pwd` char(10) DEFAULT NULL,
  `Admin_login_name` char(10) DEFAULT NULL,
  PRIMARY KEY (`Admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for T_BegToBuy
-- ----------------------------
CREATE TABLE `T_BegToBuy` (
  `Beg_id` int(4) NOT NULL,
  `Book_name` varchar(50) NOT NULL,
  `User_id` int(4) NOT NULL,
  `BookInfo` varchar(255) NOT NULL,
  `Remark` varchar(255) DEFAULT NULL,
  `PubDate` datetime DEFAULT NULL,
  PRIMARY KEY (`Beg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for T_Book
-- ----------------------------
CREATE TABLE `T_Book` (
  `Book_id` int(4) NOT NULL,
  `Book_name` varchar(200) CHARACTER SET utf8 NOT NULL,
  `Book_type_id` int(4) NOT NULL,
  `Author` varchar(50) CHARACTER SET utf8 NOT NULL,
  `Publisher` varchar(50) CHARACTER SET utf8 NOT NULL,
  `Price` int(8) DEFAULT NULL,
  `Cover` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `User_login_name` varchar(32) CHARACTER SET utf8 NOT NULL,
  `Depreciation` int(4) NOT NULL,
  `SalePrice` int(8) NOT NULL,
  `SaleInfo` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `Issaled` bit(1) DEFAULT NULL,
  `PubDate` datetime NOT NULL,
  PRIMARY KEY (`Book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for T_BulletinLnfo
-- ----------------------------
CREATE TABLE `T_BulletinLnfo` (
  `Bulletin_id` int(4) NOT NULL,
  `Title` varchar(255) CHARACTER SET utf8 NOT NULL,
  `Content` varchar(255) CHARACTER SET utf8 NOT NULL,
  `PubDate` datetime NOT NULL,
  PRIMARY KEY (`Bulletin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for T_Car
-- ----------------------------
CREATE TABLE `T_Car` (
  `Car_id` int(4) NOT NULL AUTO_INCREMENT,
  `User_id` int(4) NOT NULL,
  `Book_id` int(4) NOT NULL,
  `Number` int(11) DEFAULT NULL,
  `Price` decimal(10,0) DEFAULT NULL,
  `Money` decimal(10,0) NOT NULL,
  PRIMARY KEY (`Car_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for T_Category
-- ----------------------------
CREATE TABLE `T_Category` (
  `Cate_id` int(8) NOT NULL AUTO_INCREMENT,
  `Cate_name` char(10) CHARACTER SET utf8 NOT NULL,
  `cate_desc` text CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`Cate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for T_MsgInfo
-- ----------------------------
CREATE TABLE `T_MsgInfo` (
  `Msg_id` int(4) NOT NULL,
  `Title` varchar(50) CHARACTER SET utf8 NOT NULL,
  `Content` varchar(255) CHARACTER SET utf8 NOT NULL,
  `User_id` int(4) NOT NULL,
  `PubDate` datetime NOT NULL,
  `HasRead` bit(1) NOT NULL,
  PRIMARY KEY (`Msg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for T_Orders
-- ----------------------------
CREATE TABLE `T_Orders` (
  `Order_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(4) NOT NULL,
  `Car_id` int(4) NOT NULL,
  `Order_date` datetime DEFAULT NULL,
  `Order_status` int(4) DEFAULT NULL,
  `Pay_id` int(4) NOT NULL,
  PRIMARY KEY (`Order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for T_Pay
-- ----------------------------
CREATE TABLE `T_Pay` (
  `Pay_id` int(4) NOT NULL,
  `Pay_name` varchar(255) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`Pay_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for T_User
-- ----------------------------
CREATE TABLE `T_User` (
  `User_id` int(4) NOT NULL AUTO_INCREMENT,
  `User_login_name` varchar(32) CHARACTER SET utf8 DEFAULT NULL,
  `User_login_pwd` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `T_Admin` VALUES ('1', '裴婉婷', '123', 'PWT');
INSERT INTO `T_Admin` VALUES ('2', '加华丽', '123', 'JHL');
INSERT INTO `T_Admin` VALUES ('3', '张瑞', '123', 'ZR');
INSERT INTO `T_Book` VALUES ('1', '计算机网络', '3', '张三', '李四', '10', '11', '小红', '7', '3', null, null, '2020-06-09 18:08:46');
INSERT INTO `T_Book` VALUES ('2', '霸道总裁爱上我', '1', '刘某', '林某', '8', '11', '张三', '3', '3', null, null, '2020-06-02 18:10:24');
INSERT INTO `T_BulletinLnfo` VALUES ('1', '520劲爆来袭', '活动仅三天！全场8.8折', '2020-05-20 00:00:08');
INSERT INTO `T_BulletinLnfo` VALUES ('2', '六一快乐', '全场9折', '2020-06-01 00:00:46');
INSERT INTO `T_Car` VALUES ('1', '1', '1', '2', '2', '4');
INSERT INTO `T_Car` VALUES ('2', '2', '2', '2', '2', '4');
INSERT INTO `T_Category` VALUES ('1', '小说', '言情小说、玄幻小说等等');
INSERT INTO `T_Category` VALUES ('2', '杂志', '时尚杂志、军事杂志等');
INSERT INTO `T_Category` VALUES ('3', '学习资料', '课本、试卷等');
INSERT INTO `T_MsgInfo` VALUES ('1', '夸奖', '这个网站不错 提供的书也不错', '2', '2020-06-02 17:57:33', '');
INSERT INTO `T_MsgInfo` VALUES ('2', '建议', '希望有更多的书籍类型', '1', '2020-06-09 17:57:46', '');
INSERT INTO `T_Orders` VALUES ('1', '1', '1', '2020-05-21 17:59:20', null, '1');
INSERT INTO `T_Orders` VALUES ('2', '2', '3', '2020-06-03 17:59:38', null, '2');
INSERT INTO `T_Pay` VALUES ('1', '支付宝支付');
INSERT INTO `T_Pay` VALUES ('2', '花呗支付');
INSERT INTO `T_Pay` VALUES ('3', '银行卡支付');
INSERT INTO `T_User` VALUES ('1', '小小鸟', '123');
INSERT INTO `T_User` VALUES ('2', '仙女', '123');
