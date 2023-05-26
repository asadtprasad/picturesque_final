/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50508
Source Host           : localhost:3306
Source Database       : picturesque

Target Server Type    : MYSQL
Target Server Version : 50508
File Encoding         : 65001

Date: 2023-05-25 16:12:49
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2022-05-14 15:23:22');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2022-05-14 15:23:31');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2022-05-14 15:23:33');
INSERT INTO `django_migrations` VALUES ('4', 'contenttypes', '0002_remove_content_type_name', '2022-05-14 15:23:33');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0002_alter_permission_name_max_length', '2022-05-14 15:23:33');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0003_alter_user_email_max_length', '2022-05-14 15:23:34');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0004_alter_user_username_opts', '2022-05-14 15:23:34');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0005_alter_user_last_login_null', '2022-05-14 15:23:34');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0006_require_contenttypes_0002', '2022-05-14 15:23:34');
INSERT INTO `django_migrations` VALUES ('10', 'sessions', '0001_initial', '2022-05-14 15:23:37');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('0crmb6uw19qgtropmmga044xyzh5tqc7', 'eyJ1aWQiOjAsInV0eXBlIjoiYWRtaW4ifQ:1pxsWe:aubirY9aaS6GqiHEX9U2pmZ6EsGWjOr3cGxW1_wyGnc', '2023-05-27 16:55:20');
INSERT INTO `django_session` VALUES ('2wypasr6cwk4b5s4ch8nzos88ovh755v', 'N2E1Zjg1MDc0YTgzNGJmMTA0ODFmOTNmYWE2ODY5NGQyYjVhMGEzODp7InV0eXBlIjoiY3VzdG9tZXIiLCJ1aWQiOjF9', '2022-05-28 18:27:13');
INSERT INTO `django_session` VALUES ('4vy1ma68r71ni8xic6cu1ihxdtfgei2d', 'MjE0YTk0YjdlMGU4Y2M0MzUyMGFkODE5Y2EyYmU3Zjk1NDlmMmY2MTp7InV0eXBlIjoiYXJ0aXN0IiwidWlkIjo0fQ==', '2022-11-28 03:52:22');
INSERT INTO `django_session` VALUES ('58gufras3hjwjbwyoi4r6zfj8yzy5mxg', 'NmQzYTM1NWRlMzg3ZTU0NzMwZWE1OWY2NjExZmY2NThmNmJjZTk2Yzp7InV0eXBlIjoiY3VzdG9tZXIiLCJ1aWQiOjJ9', '2022-10-19 14:33:48');
INSERT INTO `django_session` VALUES ('5krpjhgp4581zq9lwkwmbwq6dma34i27', 'e30:1pwJJN:58bPSxQC62A9xgiBspueqU8lVuB0GaUChljjMMPCSUw', '2023-05-23 09:07:09');
INSERT INTO `django_session` VALUES ('78jyyjfgc2adjat6a8fn5138fob35939', 'OGJiMmFlMDlkN2RhN2Y0Zjk0NTNmMmExYjQ3OWE1NTk1OTAzYWZiZDp7InV0eXBlIjoidXNlciIsInVpZCI6MX0=', '2022-11-28 12:39:49');
INSERT INTO `django_session` VALUES ('bpttytwjs6tssby33rbzjxy83h09869o', 'OGJiMmFlMDlkN2RhN2Y0Zjk0NTNmMmExYjQ3OWE1NTk1OTAzYWZiZDp7InV0eXBlIjoidXNlciIsInVpZCI6MX0=', '2022-11-28 09:56:13');
INSERT INTO `django_session` VALUES ('ddz1s2cfdap2jn505xj7u9w2peqmcehm', 'MjE0YTk0YjdlMGU4Y2M0MzUyMGFkODE5Y2EyYmU3Zjk1NDlmMmY2MTp7InV0eXBlIjoiYXJ0aXN0IiwidWlkIjo0fQ==', '2022-11-10 00:05:18');
INSERT INTO `django_session` VALUES ('fjtevek51rmvkw1yklhyr8lg5dno7un3', 'eyJ1aWQiOjAsInV0eXBlIjoiYWRtaW4ifQ:1q12dg:XYDvvwsKALkXmyzpqZI6fmtmnHbnbLpOAMtcb6vfm_I', '2023-06-05 10:19:40');
INSERT INTO `django_session` VALUES ('gz2i6210sa3upbcgl349ofhsxlq129qi', 'NmQzYTM1NWRlMzg3ZTU0NzMwZWE1OWY2NjExZmY2NThmNmJjZTk2Yzp7InV0eXBlIjoiY3VzdG9tZXIiLCJ1aWQiOjJ9', '2022-05-29 06:37:01');
INSERT INTO `django_session` VALUES ('k3297yyzvnowpeuq2k6azhpoq7kwyvdn', 'eyJ1aWQiOjQsInV0eXBlIjoiYXJ0aXN0In0:1pxs0P:mGJCHcirnA9YVcnNDtaB3UfwQjWGnanVl1Smik1Q98I', '2023-05-27 16:22:01');
INSERT INTO `django_session` VALUES ('l0zsz8unlcn4lf4odvkmdngubx5lgxhf', 'N2E1Zjg1MDc0YTgzNGJmMTA0ODFmOTNmYWE2ODY5NGQyYjVhMGEzODp7InV0eXBlIjoiY3VzdG9tZXIiLCJ1aWQiOjF9', '2022-05-29 10:13:53');
INSERT INTO `django_session` VALUES ('ofrg8lljsar0aawmvy7rtlk1kk5cmqtf', 'N2E1MGM5MjEwNjc0OGNhODllOTJhMGMwYjFiOGI1MzVlZWE0NjcwYzp7fQ==', '2023-04-24 17:13:17');
INSERT INTO `django_session` VALUES ('pqvned13mpu5evduyiv92eupkf7mywzr', 'e30:1pxtnP:nvTPQYqsSeFgM_tbiCYl_briGaj3yJq0Nlbh7et_kI0', '2023-05-27 18:16:43');
INSERT INTO `django_session` VALUES ('q96d8rv2o5g8zwie8dglcqob5uvr30rq', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1pqmZX:l8fcoOzzALY1AE56KdUGK4xZ8QpblYTFP-dcPMfe2MM', '2023-05-08 03:08:59');
INSERT INTO `django_session` VALUES ('rpjdl3dw85lmi4s31wjhz9c2c852aztb', 'eyJ1aWQiOjEsInV0eXBlIjoidXNlciJ9:1q28NL:50Jp4H6H8imQsVoTGLabjiZGVed8Oh2UzH6GsAQTnVg', '2023-06-08 10:39:19');
INSERT INTO `django_session` VALUES ('tmt7oz47xk74ovkf7txanwxfp22ooi23', 'NmQzYTM1NWRlMzg3ZTU0NzMwZWE1OWY2NjExZmY2NThmNmJjZTk2Yzp7InV0eXBlIjoiY3VzdG9tZXIiLCJ1aWQiOjJ9', '2022-05-29 07:19:43');
INSERT INTO `django_session` VALUES ('wu3zesgbi520ybqb2i2pl29wfyd9heow', 'OGJiMmFlMDlkN2RhN2Y0Zjk0NTNmMmExYjQ3OWE1NTk1OTAzYWZiZDp7InV0eXBlIjoidXNlciIsInVpZCI6MX0=', '2022-10-21 09:23:30');
INSERT INTO `django_session` VALUES ('ygdreqhxud8xhxmu3f9y4jmfi1gcu1rc', 'N2E1Zjg1MDc0YTgzNGJmMTA0ODFmOTNmYWE2ODY5NGQyYjVhMGEzODp7InV0eXBlIjoiY3VzdG9tZXIiLCJ1aWQiOjF9', '2022-05-29 10:40:25');
INSERT INTO `django_session` VALUES ('yisxe95oy3w3dmeuvybst68eais7owg6', 'N2E1MGM5MjEwNjc0OGNhODllOTJhMGMwYjFiOGI1MzVlZWE0NjcwYzp7fQ==', '2022-11-08 06:49:40');

-- ----------------------------
-- Table structure for `tbl_auction`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_auction`;
CREATE TABLE `tbl_auction` (
  `aucid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `wrkid` int(11) NOT NULL,
  `baseamt` int(11) NOT NULL,
  `status` varchar(15) NOT NULL,
  `adate` date DEFAULT NULL,
  `remarks` varchar(100) NOT NULL,
  `pstatus` varchar(20) DEFAULT NULL,
  `bidto` int(11) DEFAULT NULL,
  PRIMARY KEY (`aucid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tbl_auction
-- ----------------------------
INSERT INTO `tbl_auction` VALUES ('1', '4', '2', '16000', 'accepted', '2023-05-25', 'NIl', 'Nil', null);

-- ----------------------------
-- Table structure for `tbl_biding`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_biding`;
CREATE TABLE `tbl_biding` (
  `bidid` int(11) NOT NULL AUTO_INCREMENT,
  `aucid` int(11) NOT NULL,
  `bidamt` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `bidate` date NOT NULL,
  `bidtime` time NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`bidid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tbl_biding
-- ----------------------------
INSERT INTO `tbl_biding` VALUES ('1', '1', '16001', '1', '2023-05-25', '16:08:39', 'bided');
INSERT INTO `tbl_biding` VALUES ('2', '1', '16500', '2', '2023-05-25', '16:09:10', 'bided');

-- ----------------------------
-- Table structure for `tbl_booking`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_booking`;
CREATE TABLE `tbl_booking` (
  `bkid` int(11) NOT NULL AUTO_INCREMENT,
  `artid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `bkdate` date NOT NULL,
  `descp` varchar(200) NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`bkid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tbl_booking
-- ----------------------------
INSERT INTO `tbl_booking` VALUES ('1', '4', '1', '2023-05-31', 'Rajagiri College', 'rejected');

-- ----------------------------
-- Table structure for `tbl_cusreg`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_cusreg`;
CREATE TABLE `tbl_cusreg` (
  `rid` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phno` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `location` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `utype` varchar(15) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of tbl_cusreg
-- ----------------------------
INSERT INTO `tbl_cusreg` VALUES ('1', 'sneha', 'kochi', '9876543211', 'sneha@gmail.com', 'kochi', 'F', 'user');
INSERT INTO `tbl_cusreg` VALUES ('2', 'shalon', 'kochi', '8976543212', 'sha@gmail.com', 'kochi', 'M', 'user');
INSERT INTO `tbl_cusreg` VALUES ('4', 'Rohtih Pai', 'Thammanm', '8111812762', 'pai@gmail.com', 'Thammanam', 'M', 'artist');
INSERT INTO `tbl_cusreg` VALUES ('5', 'qureshi', 'kochi', '7485632514', 'qur@gmail.com', 'kochi', 'M', 'artist');

-- ----------------------------
-- Table structure for `tbl_lcount`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_lcount`;
CREATE TABLE `tbl_lcount` (
  `lkid` int(11) NOT NULL AUTO_INCREMENT,
  `phid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`lkid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of tbl_lcount
-- ----------------------------
INSERT INTO `tbl_lcount` VALUES ('1', '1', '1');
INSERT INTO `tbl_lcount` VALUES ('2', '2', '1');
INSERT INTO `tbl_lcount` VALUES ('3', '3', '1');
INSERT INTO `tbl_lcount` VALUES ('4', '4', '1');

-- ----------------------------
-- Table structure for `tbl_login`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_login`;
CREATE TABLE `tbl_login` (
  `uid` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `upass` varchar(20) NOT NULL,
  `utype` varchar(20) NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`uname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of tbl_login
-- ----------------------------
INSERT INTO `tbl_login` VALUES ('0', 'admin', 'admin', 'admin', '');
INSERT INTO `tbl_login` VALUES ('4', 'pai@gmail.com', 'pai', 'artist', 'accepted');
INSERT INTO `tbl_login` VALUES ('5', 'qur@gmail.com', 'qureshi', 'artist', 'accepted');
INSERT INTO `tbl_login` VALUES ('2', 'sha@gmail.com', 'shasha', 'user', 'accepted');
INSERT INTO `tbl_login` VALUES ('1', 'sneha@gmail.com', 'sneha', 'user', 'accepted');

-- ----------------------------
-- Table structure for `tbl_order`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_order`;
CREATE TABLE `tbl_order` (
  `oid` int(11) NOT NULL AUTO_INCREMENT,
  `odate` date NOT NULL,
  `uid` int(11) NOT NULL,
  `wrkid` int(11) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`oid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of tbl_order
-- ----------------------------
INSERT INTO `tbl_order` VALUES ('1', '2023-05-09', '1', '2', 'Dispatched');

-- ----------------------------
-- Table structure for `tbl_photo`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_photo`;
CREATE TABLE `tbl_photo` (
  `phid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `img` varchar(100) NOT NULL,
  `likes` int(11) NOT NULL DEFAULT '0',
  `state` varchar(10) NOT NULL,
  `tags` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`phid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of tbl_photo
-- ----------------------------
INSERT INTO `tbl_photo` VALUES ('1', '4', 'uploads/cc_cdGFJut.jpg', '1', 'public', 'qq');
INSERT INTO `tbl_photo` VALUES ('2', '4', 'uploads/nn.webp', '10', 'public', 'nature');
INSERT INTO `tbl_photo` VALUES ('3', '4', 'uploads/fm.jpg', '1', 'public', 'asssdd');
INSERT INTO `tbl_photo` VALUES ('4', '5', 'uploads/t.jpg', '1', 'public', 'we,jki');

-- ----------------------------
-- Table structure for `tbl_sale`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_sale`;
CREATE TABLE `tbl_sale` (
  `slid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `wrkid` int(11) NOT NULL,
  `amt` int(11) NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`slid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of tbl_sale
-- ----------------------------
INSERT INTO `tbl_sale` VALUES ('1', '4', '2', '5000', 'ordered');
INSERT INTO `tbl_sale` VALUES ('2', '4', '1', '3500', 'pending');

-- ----------------------------
-- Table structure for `tbl_travel`
-- ----------------------------
DROP TABLE IF EXISTS `tbl_travel`;
CREATE TABLE `tbl_travel` (
  `trid` int(11) NOT NULL AUTO_INCREMENT,
  `loc` varchar(100) NOT NULL,
  `tdate` date NOT NULL,
  `dtls` varchar(6000) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`trid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of tbl_travel
-- ----------------------------
INSERT INTO `tbl_travel` VALUES ('1', 'Kochi', '2022-02-02', 'good expoerience', '2');
