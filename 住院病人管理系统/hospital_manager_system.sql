/*
 Navicat Premium Data Transfer

 Source Server         : 本机数据库
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : hospital_manager_system

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 19/06/2020 15:35:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `用户编号` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `用户名` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `用户密码` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `用户类型` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`用户编号`) USING BTREE,
  UNIQUE INDEX `用户名`(`用户名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'test', '123', '管理员1');
INSERT INTO `user` VALUES ('123', 'test1', '123', '管理');
INSERT INTO `user` VALUES ('34', 'qwe', 'erwe', '管理3');

-- ----------------------------
-- Table structure for zybr
-- ----------------------------
DROP TABLE IF EXISTS `zybr`;
CREATE TABLE `zybr`  (
  `住院号` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `姓名` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `性别` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `年龄` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `民族` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `诊断` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `入院日期` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`住院号`) USING BTREE,
  UNIQUE INDEX `住院号`(`住院号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of zybr
-- ----------------------------
INSERT INTO `zybr` VALUES ('1', 'tom', '男', '23', '汉', '感冒', '2020-06-18 21:56:42');

-- ----------------------------
-- Table structure for zysf
-- ----------------------------
DROP TABLE IF EXISTS `zysf`;
CREATE TABLE `zysf`  (
  `住院号` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `收费日期` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `收费项目` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `金额` int(0) NULL DEFAULT NULL,
  `临床科室` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `医生代码` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  INDEX `住院号`(`住院号`, `医生代码`) USING BTREE,
  INDEX `医生代码`(`医生代码`) USING BTREE,
  CONSTRAINT `zysf_ibfk_1` FOREIGN KEY (`住院号`) REFERENCES `zybr` (`住院号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `zysf_ibfk_2` FOREIGN KEY (`医生代码`) REFERENCES `zyys` (`医生代码`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of zysf
-- ----------------------------
INSERT INTO `zysf` VALUES ('1', '2020年6月18日', '清开灵', 12, '外科', '1');

-- ----------------------------
-- Table structure for zyys
-- ----------------------------
DROP TABLE IF EXISTS `zyys`;
CREATE TABLE `zyys`  (
  `医生代码` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `姓名` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `性别` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `职称` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`医生代码`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of zyys
-- ----------------------------
INSERT INTO `zyys` VALUES ('1', 'jack', '男', '主治医师');

SET FOREIGN_KEY_CHECKS = 1;
