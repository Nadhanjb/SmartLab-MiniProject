/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - smartlab
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`smartlab` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `smartlab`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add course_table',7,'add_course_table'),
(26,'Can change course_table',7,'change_course_table'),
(27,'Can delete course_table',7,'delete_course_table'),
(28,'Can view course_table',7,'view_course_table'),
(29,'Can add dept_table',8,'add_dept_table'),
(30,'Can change dept_table',8,'change_dept_table'),
(31,'Can delete dept_table',8,'delete_dept_table'),
(32,'Can view dept_table',8,'view_dept_table'),
(33,'Can add labsubject_table',9,'add_labsubject_table'),
(34,'Can change labsubject_table',9,'change_labsubject_table'),
(35,'Can delete labsubject_table',9,'delete_labsubject_table'),
(36,'Can view labsubject_table',9,'view_labsubject_table'),
(37,'Can add login_table',10,'add_login_table'),
(38,'Can change login_table',10,'change_login_table'),
(39,'Can delete login_table',10,'delete_login_table'),
(40,'Can view login_table',10,'view_login_table'),
(41,'Can add staff_table',11,'add_staff_table'),
(42,'Can change staff_table',11,'change_staff_table'),
(43,'Can delete staff_table',11,'delete_staff_table'),
(44,'Can view staff_table',11,'view_staff_table'),
(45,'Can add student_table',12,'add_student_table'),
(46,'Can change student_table',12,'change_student_table'),
(47,'Can delete student_table',12,'delete_student_table'),
(48,'Can view student_table',12,'view_student_table'),
(49,'Can add system_table',13,'add_system_table'),
(50,'Can change system_table',13,'change_system_table'),
(51,'Can delete system_table',13,'delete_system_table'),
(52,'Can view system_table',13,'view_system_table'),
(53,'Can add system_stud_allo_table',14,'add_system_stud_allo_table'),
(54,'Can change system_stud_allo_table',14,'change_system_stud_allo_table'),
(55,'Can delete system_stud_allo_table',14,'delete_system_stud_allo_table'),
(56,'Can view system_stud_allo_table',14,'view_system_stud_allo_table'),
(57,'Can add sub_staff_allo_table',15,'add_sub_staff_allo_table'),
(58,'Can change sub_staff_allo_table',15,'change_sub_staff_allo_table'),
(59,'Can delete sub_staff_allo_table',15,'delete_sub_staff_allo_table'),
(60,'Can view sub_staff_allo_table',15,'view_sub_staff_allo_table'),
(61,'Can add student_feedback',16,'add_student_feedback'),
(62,'Can change student_feedback',16,'change_student_feedback'),
(63,'Can delete student_feedback',16,'delete_student_feedback'),
(64,'Can view student_feedback',16,'view_student_feedback'),
(65,'Can add staff_lab_allocatio',17,'add_staff_lab_allocatio'),
(66,'Can change staff_lab_allocatio',17,'change_staff_lab_allocatio'),
(67,'Can delete staff_lab_allocatio',17,'delete_staff_lab_allocatio'),
(68,'Can view staff_lab_allocatio',17,'view_staff_lab_allocatio'),
(69,'Can add notification_table',18,'add_notification_table'),
(70,'Can change notification_table',18,'change_notification_table'),
(71,'Can delete notification_table',18,'delete_notification_table'),
(72,'Can view notification_table',18,'view_notification_table'),
(73,'Can add lab_assistant_table',19,'add_lab_assistant_table'),
(74,'Can change lab_assistant_table',19,'change_lab_assistant_table'),
(75,'Can delete lab_assistant_table',19,'delete_lab_assistant_table'),
(76,'Can view lab_assistant_table',19,'view_lab_assistant_table'),
(77,'Can add exam_table',20,'add_exam_table'),
(78,'Can change exam_table',20,'change_exam_table'),
(79,'Can delete exam_table',20,'delete_exam_table'),
(80,'Can view exam_table',20,'view_exam_table'),
(81,'Can add doubt_table',21,'add_doubt_table'),
(82,'Can change doubt_table',21,'change_doubt_table'),
(83,'Can delete doubt_table',21,'delete_doubt_table'),
(84,'Can view doubt_table',21,'view_doubt_table'),
(85,'Can add complaint_table',22,'add_complaint_table'),
(86,'Can change complaint_table',22,'change_complaint_table'),
(87,'Can delete complaint_table',22,'delete_complaint_table'),
(88,'Can view complaint_table',22,'view_complaint_table'),
(89,'Can add process',23,'add_process'),
(90,'Can change process',23,'change_process'),
(91,'Can delete process',23,'delete_process'),
(92,'Can view process',23,'view_process'),
(93,'Can add screenshot',24,'add_screenshot'),
(94,'Can change screenshot',24,'change_screenshot'),
(95,'Can delete screenshot',24,'delete_screenshot'),
(96,'Can view screenshot',24,'view_screenshot'),
(97,'Can add command',25,'add_command'),
(98,'Can change command',25,'change_command'),
(99,'Can delete command',25,'delete_command'),
(100,'Can view command',25,'view_command');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$X46Eg3FqMHB8dZZjcB9rG6$HH6g+FMPzymKY3+B0aQWSkqtqSygwabtGvh4ojphX0g=','2023-12-01 11:55:11.111729',1,'admin','','','admin@gmail.com',1,1,'2023-11-19 10:52:37.578902');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(25,'smartlab_app','command'),
(22,'smartlab_app','complaint_table'),
(7,'smartlab_app','course_table'),
(8,'smartlab_app','dept_table'),
(21,'smartlab_app','doubt_table'),
(20,'smartlab_app','exam_table'),
(19,'smartlab_app','lab_assistant_table'),
(9,'smartlab_app','labsubject_table'),
(10,'smartlab_app','login_table'),
(18,'smartlab_app','notification_table'),
(23,'smartlab_app','process'),
(24,'smartlab_app','screenshot'),
(17,'smartlab_app','staff_lab_allocatio'),
(11,'smartlab_app','staff_table'),
(16,'smartlab_app','student_feedback'),
(12,'smartlab_app','student_table'),
(15,'smartlab_app','sub_staff_allo_table'),
(14,'smartlab_app','system_stud_allo_table'),
(13,'smartlab_app','system_table');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-10-24 05:03:40.387767'),
(2,'auth','0001_initial','2023-10-24 05:03:40.942513'),
(3,'admin','0001_initial','2023-10-24 05:03:41.115995'),
(4,'admin','0002_logentry_remove_auto_add','2023-10-24 05:03:41.131708'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-10-24 05:03:41.164413'),
(6,'contenttypes','0002_remove_content_type_name','2023-10-24 05:03:41.274488'),
(7,'auth','0002_alter_permission_name_max_length','2023-10-24 05:03:41.338273'),
(8,'auth','0003_alter_user_email_max_length','2023-10-24 05:03:41.386076'),
(9,'auth','0004_alter_user_username_opts','2023-10-24 05:03:41.416821'),
(10,'auth','0005_alter_user_last_login_null','2023-10-24 05:03:41.479596'),
(11,'auth','0006_require_contenttypes_0002','2023-10-24 05:03:41.496162'),
(12,'auth','0007_alter_validators_add_error_messages','2023-10-24 05:03:41.512738'),
(13,'auth','0008_alter_user_username_max_length','2023-10-24 05:03:41.590178'),
(14,'auth','0009_alter_user_last_name_max_length','2023-10-24 05:03:41.654021'),
(15,'auth','0010_alter_group_name_max_length','2023-10-24 05:03:41.668625'),
(16,'auth','0011_update_proxy_permissions','2023-10-24 05:03:41.684256'),
(17,'auth','0012_alter_user_first_name_max_length','2023-10-24 05:03:41.779813'),
(18,'sessions','0001_initial','2023-10-24 05:03:41.826467'),
(19,'smartlab_app','0001_initial','2023-10-24 05:03:43.328783'),
(20,'smartlab_app','0002_alter_student_table_course','2023-10-24 09:22:39.846049'),
(21,'smartlab_app','0003_student_table_semester','2023-11-02 09:13:43.161098'),
(22,'smartlab_app','0004_auto_20231106_1448','2023-11-06 09:18:59.320982'),
(23,'smartlab_app','0005_alter_staff_table_qualification','2023-11-06 09:34:12.018512'),
(24,'smartlab_app','0006_alter_staff_table_qualification','2023-11-06 10:53:36.727114'),
(25,'smartlab_app','0007_auto_20231118_0954','2023-11-18 04:24:15.102613'),
(26,'smartlab_app','0008_auto_20231118_1005','2023-11-18 04:36:20.296357'),
(27,'smartlab_app','0009_auto_20231118_1032','2023-11-18 05:03:53.617090'),
(28,'smartlab_app','0010_course_table_sem','2023-11-22 07:14:47.690325'),
(29,'smartlab_app','0011_command_process_screenshot','2023-11-26 18:51:51.654127'),
(30,'smartlab_app','0012_auto_20231127_0051','2023-11-26 19:21:24.205223'),
(31,'smartlab_app','0013_auto_20231201_1701','2023-12-01 11:31:21.566052');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('1x99tp6l1yi8v8vv19x7ft8o0wn011lj','.eJxVjsFuhCAQht-Fs3FBFLW39tL00HOTXswAs4oF3Agmu2n67oXVtNnb_80388M3sUaTJ1aQcAsR3ZCpLohajqB1Dm3ym5zvlvEEOVTJ4iXuwybfbGvAHWlB8Aru_yDC-byTyLRp9PHPgrXLDukhCxJCMMPxrwG2OA1bwPU-IYw8zCSoL_RZ6Bn8uJRq8XE1sswr5WFD-b5otC_H7kPBBGHKtZT22HAumKZS1RSha-q-VYhaKNH0LRWAijcgBW27SmsuFVCKDDqFVQWp1IPD1PQsJ5PIuDHByaE2cHLg2fB6tbfPj7dyvozk5xe3nXcu:1r4zcG:XvTYMkDUGLgkvvJN-XFwHYrC0a9OLv1T01cRGeBAywA','2023-12-04 08:26:48.595495'),
('6o3y2m20k4guce1ekuo8m61wl7qpiu75','eyJzdGFmZl9pZCI6MTMsImlkIjoxNiwiYWxsb19pZCI6MTZ9:1r0ItK:sF4HqBvdfe-FK8D8ccYnhT9OqVfVW3aLKhcGs4MbzrE','2023-11-21 10:01:02.075401'),
('bkfhoveuv81sv1k3weii12r3cfgkbzyn','.eJyrVkrMycmPz0xRsjLUUUpJLSiBsZPzS4uKUyG8WgAAoQzI:1qvFFm:xm_kPtVXCOusnYOL_U6lANuh2vPs1LLlZ1_ZYUAEMn0','2023-11-07 11:07:18.823623'),
('e3lyifpez6xez3cb7mm7b4qjbesgm3vl','.eJxVj89OxCAQh1_FcG5YoKV_vLnZqybGB2gGmBQqpZsFDsb47kLdGD2QDPP9-Ib5JDPkZOcc8TY7Qx4JJ83fngL9jqECs0JYdqr3kG5O0Rqhdxrp827Qn-_ZfwIL0VYtYxPKtu25YUp3DGGU3TRoRNPrXk4D6wF1K0H1bBiFMa3SwBhyGDUKAUXq6_94Q2IovqePaOGhHAuhQrctpXva0Dg4bRD4fIHXvApJ1-tSuMFrOhbksiHg_X5cBGtItZ1dyCX0lvLlJ9SVMUdRAjFlgyH9ggAbljcvzoInX99OT2VY:1r5lWJ:3ABgBGdY0eTLBC9F93DkqFBIH2BtIOI8zk1et7Ay_qU','2023-12-06 11:35:51.021274'),
('n418rnc7p8l62xa0fvoax935e4rtiqwt','.eJyrVspJTEosLs6Mz0xRsjLSUUrOLy0qTgXzDIHc4pLEtDQIzxTEK01JzSuB8A1rAXkHFA0:1r0Fdi:6Lgi-ioTdOfdUy1NGBPS-pYXym7aqery77Gn63kXIcc','2023-11-21 06:32:42.294868'),
('n63dufggl8mt8ivuvsqw07yslksir7wp','.eJxVjrkOwjAQRP_FdWTWcewklFQ09HTR2l4SQw6EE4lD_Ds2SgHNHjOzT_tiDS5z1yyBbo13bMsEy341g_ZCYzLcGcd24nYa55s3PEX46gZ-mBz1uzX7B-gwdAkLUJOSUgsHxhZAWKmiLi2R01arugSNZKVCo6GscueksQhAAitLeY4R2qf_pM7YiANF5N6bJPuhjctmIOdxc6IBexLNUpvnHY78fG1jJLCtilXEcxH7I8wJVcQxfIf3B829UvM:1r90IK:AiGcSwxBBKq1YmPP5TfHNjzNqjjBJFd-_26GbrdXiYU','2023-12-15 09:58:48.609110'),
('q6l61zv1zbag4xg3ljt4pfd3wbhnv3tc','.eJyrVsrJTFGyMrLQUUpJAbEMdZSS86GMYrAUkC5NyooHixkDOSWJaWkQnomOUk5iUmJxcWY8TGVJaUpqXglccWpFYi6ck5iTkw_hWNQCAGTAJFE:1r2E4s:baOMb2_pvHi8ayfQ0THSzx6igLlbTfI2-MFFYkA1TmA','2023-11-26 17:16:54.787753'),
('ujh1um7n7277vr0heu3yx6bw55a4nq7s','.eJyrVkpJLSiJz0xRsrLUUUrOLy0qTgXzLHSUiksS09LAHENTHaWcxKTE4uJMCB8kWZqSmgfRaWiko5SYk5MPVVsLAK_gG4I:1r0H9b:QrAR2Ju0mTMUKuIqqHYAjZ4VXmoDqhFTHKG-BAu7NZs','2023-11-21 08:09:43.169536'),
('wqsfpnnlti0haoa48y62q5u6nttib671','.eJw9jFEKgCAQBe-y3_uRJEVdJtbcwLCMVqGI7l4p9DfDPN4Flrc4OAt9gzCGtAtnaxEk0jRl6RDI-5BZ1W9JZi5SIXgyJOKKI_BBS2H1XSTLa_wfT4lcqkbII30_16QpfA:1qzYiQ:nQLIztEFYwFOnPHIsTbA-KbUYfftMtRdiqeuFwR-fic','2023-11-19 08:42:42.984092'),
('y3w2zw8xsnr0rfkq7vkkrkeblordnqnq','.eJxVjjsOwjAQBe_iGllrO_6Ekj5niNa7KxyIEilOKsTdwVIKaN-MRu-lRjz2Mh5VtnFidVVGXX63jPSUpQF-4HJfNa3Lvk1ZN0WftOphZZlvp_sXKFhLywL04p0LhiFTB4LJd30kEQ4UfB8hoJDzmAPEZJldJgQQg4nEWvxG5_bPvD-fWjop:1r4zfc:7AgIKnmzKPxN6mucnMQVOYebESLr0grU8y0nVTPLLa4','2023-12-04 08:30:16.224244'),
('yk30u9j4af64lmhe62wkkdrp7mg40oec','.eJxVjrkOwjAMht8lM0qdpk2PkYmFna1yEtOm9ECklTjEu5OgDrDY_g998os1uC5ds3q6Nc6ymgm2-_U0mgtNMbA9Tu3MzTwtN6d5rPAt9fw4Wxr2W_cP0KHvIhagolxKJSxokwFhmWdVYYisMiqvClBIRuaoFRRlaq3UBgFIYGkoTTFAh_ifVDs24UgBeXA62m5sg0hGsg6TM404kGjWSj_vcOL9tQ0Vz-osTMFqVYT98EtERct_j_cHzmhS-w:1r7TX0:-nR9VfRjOq-vZR5PeY7SYw-TYwZFqUqCBoU5F_cJ7zs','2023-12-11 04:47:38.942010'),
('z2a44cgtrr0h5eu3ah78tee35dtx85zk','.eJxVjrtuwzAMRf9FcyBTli0_xkxdsmczKIqxldhyEdlA0qL_Xgnw0C4k7wMH_BYD7ts07JGfg3eiF0qc_noW6cEhB-6OYVwlrWF7eitzRR5plJfV8Xw-uv8AE8YpYwE6rrU2yoGlChjbuuoaYnaGTN01YJBJ12gNNG3pnLaEAKywJS5LTNA5_6fNSQRcOCE_vM22X8YkioWdx-LGC86shr2zXy-4yvvnmCpR9FWaSvSmSTtmUDbecTvOQIkhfn4BaX5Uug:1r92Cm:aAHZiKD4LP0J4P2qy48ugqA9XbYq0j2Etrfao5C_y7M','2023-12-15 12:01:12.350840');

/*Table structure for table `smartlab_app_command` */

DROP TABLE IF EXISTS `smartlab_app_command`;

CREATE TABLE `smartlab_app_command` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `process` varchar(100) NOT NULL,
  `SYSTEM_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_command_SYSTEM_id_76861cc0_fk_smartlab_` (`SYSTEM_id`),
  CONSTRAINT `smartlab_app_command_SYSTEM_id_76861cc0_fk_smartlab_` FOREIGN KEY (`SYSTEM_id`) REFERENCES `smartlab_app_system_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_command` */

/*Table structure for table `smartlab_app_complaint_table` */

DROP TABLE IF EXISTS `smartlab_app_complaint_table`;

CREATE TABLE `smartlab_app_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` longtext NOT NULL,
  `date` date NOT NULL,
  `reply` longtext NOT NULL,
  `STAFF_id` bigint NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_complai_STAFF_id_ac347e9c_fk_smartlab_` (`STAFF_id`),
  KEY `smartlab_app_complai_STUDENT_id_4a5808c6_fk_smartlab_` (`STUDENT_id`),
  CONSTRAINT `smartlab_app_complai_STAFF_id_ac347e9c_fk_smartlab_` FOREIGN KEY (`STAFF_id`) REFERENCES `smartlab_app_staff_table` (`id`),
  CONSTRAINT `smartlab_app_complai_STUDENT_id_4a5808c6_fk_smartlab_` FOREIGN KEY (`STUDENT_id`) REFERENCES `smartlab_app_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_complaint_table` */

insert  into `smartlab_app_complaint_table`(`id`,`complaint`,`date`,`reply`,`STAFF_id`,`STUDENT_id`) values 
(2,'dfghb','2023-11-18','pending',16,10),
(3,'bad girl','2023-11-18','pending',14,10),
(4,'rdfghj','2023-11-19','gdfhj',15,11),
(5,'cfvgbhnjkjn','2023-11-19','pending',14,12);

/*Table structure for table `smartlab_app_course_table` */

DROP TABLE IF EXISTS `smartlab_app_course_table`;

CREATE TABLE `smartlab_app_course_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `course` varchar(35) NOT NULL,
  `details` longtext NOT NULL,
  `DEPARTMENT_id` bigint NOT NULL,
  `sem` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_course__DEPARTMENT_id_9922344f_fk_smartlab_` (`DEPARTMENT_id`),
  CONSTRAINT `smartlab_app_course__DEPARTMENT_id_9922344f_fk_smartlab_` FOREIGN KEY (`DEPARTMENT_id`) REFERENCES `smartlab_app_dept_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_course_table` */

insert  into `smartlab_app_course_table`(`id`,`course`,`details`,`DEPARTMENT_id`,`sem`) values 
(10,'MCA','MCA stands for \"Master of Computer Applications,\" and it is a postgraduate academic program in computer science and information technology. MCA programs are typically offered by universities and colleges, and they are designed to provide students with advanced knowledge and skills in computer science, software development, and related areas',15,3),
(11,'CSE',' Computer Science and Engineering (CSE)\r\nfocuses on computer hardware, software, programming, algorithms, and computer systems.',15,7),
(12,'Bsc physics','A Bachelor of Science (BSc) in Physics is an undergraduate degree program that focuses on the study of the fundamental principles of physics. Physics is the scientific discipline that explores the behavior of the physical universe, from the smallest subatomic particles to the largest galaxies',16,5),
(13,'Msc Physics','A Master of Science (MSc) in Physics is a graduate-level program that allows students to deepen their knowledge and expertise in the field of physics. This degree typically involves advanced coursework, research, and specialization in specific areas of physics.',16,2);

/*Table structure for table `smartlab_app_dept_table` */

DROP TABLE IF EXISTS `smartlab_app_dept_table`;

CREATE TABLE `smartlab_app_dept_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(50) NOT NULL,
  `details` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_dept_table` */

insert  into `smartlab_app_dept_table`(`id`,`dept_name`,`details`) values 
(15,'Department of Computer Science','Concentrates on computer programming, software development, rel'),
(16,'Department of Physics','Concentrates o.');

/*Table structure for table `smartlab_app_doubt_table` */

DROP TABLE IF EXISTS `smartlab_app_doubt_table`;

CREATE TABLE `smartlab_app_doubt_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doubt` longtext NOT NULL,
  `date` date NOT NULL,
  `reply` longtext NOT NULL,
  `image` varchar(100) NOT NULL,
  `STAFF_id` bigint NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_doubt_t_STAFF_id_22bd420f_fk_smartlab_` (`STAFF_id`),
  KEY `smartlab_app_doubt_t_STUDENT_id_79c8b042_fk_smartlab_` (`STUDENT_id`),
  CONSTRAINT `smartlab_app_doubt_t_STAFF_id_22bd420f_fk_smartlab_` FOREIGN KEY (`STAFF_id`) REFERENCES `smartlab_app_staff_table` (`id`),
  CONSTRAINT `smartlab_app_doubt_t_STUDENT_id_79c8b042_fk_smartlab_` FOREIGN KEY (`STUDENT_id`) REFERENCES `smartlab_app_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_doubt_table` */

insert  into `smartlab_app_doubt_table`(`id`,`doubt`,`date`,`reply`,`image`,`STAFF_id`,`STUDENT_id`) values 
(1,'pppp\r\n','2023-11-01','ok','hhh',14,10),
(2,'sdfdgfgfhfhghh gcbfhg','2023-11-18','pending','fabian-irsara-67l-QujB14w-unsplash.jpg',13,10),
(3,'gthj','2023-11-18','pending','man1.avif',13,10),
(5,'ghjjn','2023-11-19','gtfghj','man1_WcNSCuj.avif',15,11),
(6,'fcvgbhnjjhgvcfvb','2023-11-19','dcfvgbhb vcfgvhb','photo-1463171379579-3fdfb86d6285.jpg',14,12),
(7,'vgbhnj','2023-11-19','pending','fabian-irsara-67l-QujB14w-unsplash_0tZMe3d.jpg',14,12);

/*Table structure for table `smartlab_app_exam_table` */

DROP TABLE IF EXISTS `smartlab_app_exam_table`;

CREATE TABLE `smartlab_app_exam_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `exam_name` longtext NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `details` varchar(1000) NOT NULL,
  `STAFF_id` bigint NOT NULL,
  `SUBJECT_id` bigint NOT NULL,
  `duration` varchar(50) NOT NULL,
  `syllabus` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_exam_ta_STAFF_id_e94a71c5_fk_smartlab_` (`STAFF_id`),
  KEY `smartlab_app_exam_ta_SUBJECT_id_ff3d6b08_fk_smartlab_` (`SUBJECT_id`),
  CONSTRAINT `smartlab_app_exam_ta_STAFF_id_e94a71c5_fk_smartlab_` FOREIGN KEY (`STAFF_id`) REFERENCES `smartlab_app_staff_table` (`id`),
  CONSTRAINT `smartlab_app_exam_ta_SUBJECT_id_ff3d6b08_fk_smartlab_` FOREIGN KEY (`SUBJECT_id`) REFERENCES `smartlab_app_labsubject_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_exam_table` */

insert  into `smartlab_app_exam_table`(`id`,`exam_name`,`date`,`time`,`details`,`STAFF_id`,`SUBJECT_id`,`duration`,`syllabus`) values 
(13,'First Internal Examination','2023-11-22','19:30:00.000000','hnjmk',14,14,'2hr','Introduction to Computing: Introduction, Art of Programming through\r\nAlgorithms and Flowcharts (Chapter 1)\r\nOverview of C: History and importance of C, Basic structure of C program,\r\nexecuting a C program. (Chapter 2)\r\nConstants, Variable and Data Types: Introduction, Character Set, C\r\nTokens, Keywords and Identifiers, Constants, Variables, Data Types,\r\nDeclaration of Variables, Assigning Values to Variables, Defining Symbolic\r\nConstants. (Chapter 3)\r\nManaging Input and Output Operations: Reading a Character, Writing a\r\nCharacter, Formatted Input, Formatted Output. (Chapter 5)\r\n'),
(15,'second internal','2023-11-28','18:05:00.000000','gfvgghjn',15,15,'3hr','xrdcfghb nj'),
(16,'mid term','2023-11-29','23:43:00.000000','vgbhjn',15,18,'2 hr','vg bhn'),
(17,'bhnj','2023-12-07','01:43:00.000000','vgbhn',15,13,'nm','hjnm'),
(18,'fghjcfgghju','2023-11-29','22:08:00.000000','fghbjnmknb nm,',16,17,'cfgvhj','cfgvgbhnjvbn'),
(19,'gtyh','2023-11-29','15:38:00.000000','vghn',14,16,'hjm','gyhj');

/*Table structure for table `smartlab_app_lab_assistant_table` */

DROP TABLE IF EXISTS `smartlab_app_lab_assistant_table`;

CREATE TABLE `smartlab_app_lab_assistant_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `gender` varchar(35) NOT NULL,
  `dob` date NOT NULL,
  `place` varchar(50) NOT NULL,
  `pin` bigint NOT NULL,
  `post` varchar(30) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_lab_ass_LOGIN_id_83e1f6af_fk_smartlab_` (`LOGIN_id`),
  CONSTRAINT `smartlab_app_lab_ass_LOGIN_id_83e1f6af_fk_smartlab_` FOREIGN KEY (`LOGIN_id`) REFERENCES `smartlab_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_lab_assistant_table` */

insert  into `smartlab_app_lab_assistant_table`(`id`,`name`,`gender`,`dob`,`place`,`pin`,`post`,`phone`,`email`,`qualification`,`photo`,`LOGIN_id`) values 
(1,'Binu','Male','2013-12-17','Kallayi',463545,'Kallayi',7098743646,'binu@gmail,com','MCA','man1_QTUJIks.jpg',6),
(3,'kalindhi','Female','1996-12-24','malappuram',678954,'malappuram',9876543216,'kalindhi@gmail.com','ssls,plus two,','istockphoto-1413249877-2048x2048.jpg',38);

/*Table structure for table `smartlab_app_labsubject_table` */

DROP TABLE IF EXISTS `smartlab_app_labsubject_table`;

CREATE TABLE `smartlab_app_labsubject_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subject` varchar(35) NOT NULL,
  `syllabus` longtext NOT NULL,
  `COURSE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_labsubj_COURSE_id_3012a804_fk_smartlab_` (`COURSE_id`),
  CONSTRAINT `smartlab_app_labsubj_COURSE_id_3012a804_fk_smartlab_` FOREIGN KEY (`COURSE_id`) REFERENCES `smartlab_app_course_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_labsubject_table` */

insert  into `smartlab_app_labsubject_table`(`id`,`subject`,`syllabus`,`COURSE_id`) values 
(13,'Python','Python is a popular and versatile programming language used for a wide range of applications, from web development and data analysis to artificial intelligence and scientific computing. If you\'re interested in learning Python, you can explore various subjects and topics related to Python programming.',10),
(14,'C programming','In a C programming lab, you will typically cover a range of practical exercises and assignments that allow you to apply the concepts and skills learned in your C programming course. The lab exercises help reinforce your understanding of C programming and improve your coding abilities.',10),
(15,'SQL ','SQL, which stands for Structured Query Language, is a domain-specific programming language used for managing and querying relational databases. It is the standard language for interacting with databases and is used for a wide range of data-related tasks. ',11),
(16,'java','Java may be used in certain physics courses or projects, especially those related to computer simulations or data analysis. Java is known for its portability and object-oriented features.',12),
(17,'R','R is a language and environment for statistical computing and graphics. It is frequently used for statistical analysis and data visualization in physics research',13),
(18,'C++','sdfgh',11);

/*Table structure for table `smartlab_app_login_table` */

DROP TABLE IF EXISTS `smartlab_app_login_table`;

CREATE TABLE `smartlab_app_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_login_table` */

insert  into `smartlab_app_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','Admin@123','admin'),
(6,'Binulb','Binu@123','labassistant'),
(28,'Athirastf','Athira@123','staff'),
(29,'Abhistf','Abhi@123','staff'),
(31,'Nihalstf','Nihal@123','staff'),
(32,'Anustd','Anu@123','student'),
(33,'Ayshastd','Aysha@123','student'),
(34,'Abhaystd','Abhay@123','student'),
(36,'Hibastf','Hiba@123','staff'),
(37,'rdcfvgbhn','Adcfvgbh1234@','staff'),
(38,'kalindhi','Kalindhi@123','labassistant'),
(39,'Amala','Amala@123','student');

/*Table structure for table `smartlab_app_notification_table` */

DROP TABLE IF EXISTS `smartlab_app_notification_table`;

CREATE TABLE `smartlab_app_notification_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `screenshot` varchar(100) NOT NULL,
  `camera_image` varchar(100) NOT NULL,
  `timedate` datetime(6) NOT NULL,
  `status` varchar(50) NOT NULL,
  `SYSTEM_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_notific_SYSTEM_id_35eb8242_fk_smartlab_` (`SYSTEM_id`),
  CONSTRAINT `smartlab_app_notific_SYSTEM_id_35eb8242_fk_smartlab_` FOREIGN KEY (`SYSTEM_id`) REFERENCES `smartlab_app_system_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_notification_table` */

insert  into `smartlab_app_notification_table`(`id`,`screenshot`,`camera_image`,`timedate`,`status`,`SYSTEM_id`) values 
(1,'female1_hHTj9nP.jpg','female1_hHTj9nP.jpg','2023-11-08 16:09:31.000000','viewed',7),
(2,'20231201-170311.jpg','s20231201-170311.jpg','2023-12-01 17:03:00.000000','viewed',4),
(3,'20231201-170334.jpg','s20231201-170334.jpg','2023-12-01 17:03:00.000000','viewed',4),
(4,'20231201-170542.jpg','s20231201-170542.jpg','2023-12-01 17:06:00.000000','viewed',4),
(5,'20231201-171106.jpg','s20231201-171106.jpg','2023-12-01 17:11:00.000000','viewed',4),
(6,'20231201-171511.jpg','s20231201-171511.jpg','2023-12-01 17:15:00.000000','viewed',4),
(7,'20231201-171637.jpg','s20231201-171637.jpg','2023-12-01 17:16:00.000000','viewed',4),
(8,'20231201-171706.jpg','s20231201-171706.jpg','2023-12-01 17:17:00.000000','viewed',4);

/*Table structure for table `smartlab_app_process` */

DROP TABLE IF EXISTS `smartlab_app_process`;

CREATE TABLE `smartlab_app_process` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `process` varchar(100) NOT NULL,
  `SYSTEM_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_process_SYSTEM_id_f8a3dced_fk_smartlab_` (`SYSTEM_id`),
  CONSTRAINT `smartlab_app_process_SYSTEM_id_f8a3dced_fk_smartlab_` FOREIGN KEY (`SYSTEM_id`) REFERENCES `smartlab_app_system_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1147 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_process` */

insert  into `smartlab_app_process`(`id`,`process`,`SYSTEM_id`) values 
(269,'MoUsoCoreWorker.exe',4),
(314,'MusNotifyIcon.exe',4),
(342,'winpty-agent.exe',4),
(349,'runnerw.exe',4),
(363,'Code.exe',4),
(482,'PubPlatform.exe',4),
(484,'studio64.exe',4),
(485,'fsnotifier.exe',4),
(489,'SQLyogCommunity.exe',4),
(490,'Video.UI.exe',4),
(511,'FileCoAuth.exe',4),
(515,'adb.exe',4),
(516,'cmd.exe',4),
(524,'WINWORD.EXE',4),
(526,'ApplicationFrameHost.exe',4),
(530,'java.exe',4),
(534,'notepad.exe',4),
(562,'smartscreen.exe',4),
(563,'LocationNotificationWindows.exe',4),
(736,'igfxCUIServiceN.exe',5),
(747,'WUDFHost.exe',5),
(755,'AsusOptimization.exe',5),
(758,'AsusScreenXpertHostService.exe',5),
(759,'AsusAppService.exe',5),
(761,'AsusNumPadService.exe',5),
(762,'AsusSoftwareManager.exe',5),
(764,'AsusLinkRemote.exe',5),
(765,'AsusLinkNear.exe',5),
(766,'AsusSystemDiagnosis.exe',5),
(767,'AsusSwitch.exe',5),
(768,'AsusSystemAnalysis.exe',5),
(772,'OfficeClickToRun.exe',5),
(773,'DtsApo4Service.exe',5),
(774,'ELANFPService.exe',5),
(775,'EMP_UDSA.exe',5),
(776,'GlideXService.exe',5),
(777,'GlideXServiceExt.exe',5),
(779,'IntelAudioService.exe',5),
(780,'OneApp.IGCC.WinService.exe',5),
(782,'esif_uf.exe',5),
(783,'RstMwService.exe',5),
(786,'RtkBtManServ.exe',5),
(790,'turbo_vpn-service.exe',5),
(793,'WMIRegistrationService.exe',5),
(795,'jhi_service.exe',5),
(797,'mysqld.exe',5),
(803,'AggregatorHost.exe',5),
(807,'unsecapp.exe',5),
(815,'SearchIndexer.exe',5),
(831,'servicehost.exe',5),
(832,'csrss.exe',5),
(833,'winlogon.exe',5),
(834,'fontdrvhost.exe',5),
(835,'dwm.exe',5),
(836,'AsusOptimizationStartupTask.exe',5),
(837,'uihost.exe',5),
(838,'sihost.exe',5),
(840,'AsusScreenXpertUI.exe',5),
(841,'igfxEMN.exe',5),
(842,'mc-fw-host.exe',5),
(846,'PCHelpSoftDriverUpdater.exe',5),
(847,'explorer.exe',5),
(849,'SearchHost.exe',5),
(850,'StartMenuExperienceHost.exe',5),
(851,'Widgets.exe',5),
(857,'ctfmon.exe',5),
(858,'SecurityHealthSystray.exe',5),
(859,'OneDrive.exe',5),
(860,'FileCoAuth.exe',5),
(861,'TeraBox.exe',5),
(862,'TextInputHost.exe',5),
(864,'TeraBoxRender.exe',5),
(865,'TeraBoxWebService.exe',5),
(868,'TeraBoxHost.exe',5),
(875,'Spotify.exe',5),
(877,'pycharm64.exe',5),
(878,'TurboVPN.exe',5),
(879,'RtkAudUService64.exe',5),
(880,'AsusOSD.exe',5),
(881,'WhatsApp.exe',5),
(883,'dvt-jb_licsrv.amd64.exe',5),
(886,'WindowsTerminal.exe',5),
(888,'fsnotifier64.exe',5),
(891,'ApplicationFrameHost.exe',5),
(892,'SystemSettings.exe',5),
(894,'UserOOBEBroker.exe',5),
(895,'HxOutlook.exe',5),
(897,'HxTsr.exe',5),
(898,'HxAccounts.exe',5),
(899,'AsusSoftwareManagerAgent.exe',5),
(900,'ShellExperienceHost.exe',5),
(902,'WidgetService.exe',5),
(909,'LockApp.exe',5),
(911,'SystemSettingsBroker.exe',5),
(912,'PushNotificationsLongRunningTask.exe',5),
(913,'SQLyogCommunity.exe',5),
(914,'dllhost.exe',5),
(915,'SDXHelper.exe',5),
(916,'GoogleCrashHandler.exe',5),
(917,'GoogleCrashHandler64.exe',5),
(928,'browserhost.exe',5),
(929,'mc-extn-browserhost.exe',5),
(930,'chrome.exe',5),
(931,'audiodg.exe',5),
(937,'winpty-agent.exe',5),
(943,'mc-web-view.exe',5),
(949,'msedgewebview2.exe',5),
(958,'msedge.exe',5),
(961,'RuntimeBroker.exe',5),
(966,'smartscreen.exe',5),
(969,'cmd.exe',5),
(971,'OpenConsole.exe',5),
(972,'svchost.exe',5),
(973,'taskhostw.exe',5),
(974,'WmiPrvSE.exe',5),
(975,'backgroundTaskHost.exe',5),
(976,'python.exe',5),
(977,'conhost.exe',5),
(979,'csrss.exe',4),
(981,'winlogon.exe',4),
(983,'WUDFHost.exe',4),
(984,'fontdrvhost.exe',4),
(987,'dwm.exe',4),
(1010,'igfxCUIServiceN.exe',4),
(1030,'armsvc.exe',4),
(1035,'esif_uf.exe',4),
(1036,'OneApp.IGCC.WinService.exe',4),
(1037,'jhi_service.exe',4),
(1038,'mongod.exe',4),
(1040,'WsNativePushService.exe',4),
(1043,'Locator.exe',4),
(1044,'RstMwService.exe',4),
(1045,'WmiApSrv.exe',4),
(1046,'MsMpEng.exe',4),
(1047,'WMIRegistrationService.exe',4),
(1051,'TeamViewer_Service.exe',4),
(1052,'RtkBtManServ.exe',4),
(1054,'mysqld.exe',4),
(1058,'SearchIndexer.exe',4),
(1059,'NisSrv.exe',4),
(1060,'sihost.exe',4),
(1064,'igfxEMN.exe',4),
(1067,'TeamViewer.exe',4),
(1069,'ctfmon.exe',4),
(1071,'explorer.exe',4),
(1072,'tv_w32.exe',4),
(1073,'tv_x64.exe',4),
(1075,'StartMenuExperienceHost.exe',4),
(1077,'GoogleCrashHandler.exe',4),
(1081,'GoogleCrashHandler64.exe',4),
(1082,'TextInputHost.exe',4),
(1084,'SecurityHealthSystray.exe',4),
(1085,'OneDrive.exe',4),
(1086,'AnyDesk.exe',4),
(1087,'jusched.exe',4),
(1088,'WSHelper.exe',4),
(1096,'WsToastNotification.exe',4),
(1098,'dvt-jb_licsrv.amd64.exe',4),
(1100,'dllhost.exe',4),
(1101,'pycharm64.exe',4),
(1102,'fsnotifier64.exe',4),
(1105,'SgrmBroker.exe',4),
(1109,'ShellExperienceHost.exe',4),
(1116,'CompPkgSrv.exe',4),
(1118,'msedge.exe',4),
(1119,'UserOOBEBroker.exe',4),
(1121,'PhoneExperienceHost.exe',4),
(1122,'LockApp.exe',4),
(1123,'RuntimeBroker.exe',4),
(1124,'SearchApp.exe',4),
(1130,'taskhostw.exe',4),
(1139,'chrome.exe',4),
(1140,'SearchProtocolHost.exe',4),
(1141,'WmiPrvSE.exe',4),
(1142,'SearchFilterHost.exe',4),
(1144,'svchost.exe',4),
(1145,'python.exe',4),
(1146,'conhost.exe',4);

/*Table structure for table `smartlab_app_screenshot` */

DROP TABLE IF EXISTS `smartlab_app_screenshot`;

CREATE TABLE `smartlab_app_screenshot` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `scrnsht` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `SYSTEM_id` bigint NOT NULL,
  `campic` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_screens_SYSTEM_id_6b0d489d_fk_smartlab_` (`SYSTEM_id`),
  CONSTRAINT `smartlab_app_screens_SYSTEM_id_6b0d489d_fk_smartlab_` FOREIGN KEY (`SYSTEM_id`) REFERENCES `smartlab_app_system_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_screenshot` */

insert  into `smartlab_app_screenshot`(`id`,`scrnsht`,`date`,`status`,`SYSTEM_id`,`campic`) values 
(1,'20231127-005401.jpg','2023-11-27 00:54:10.165471','pending',4,'s20231127-005401.jpg'),
(2,'20231127-010921.jpg','2023-11-27 01:09:29.275032','pending',4,'s20231127-010921.jpg'),
(3,'20231127-011114.jpg','2023-11-27 01:11','pending',4,'s20231127-011114.jpg'),
(4,'20231127-011306.jpg','2023-11-27 01:13','pending',4,'s20231127-011306.jpg'),
(5,'20231127-094944.jpg','2023-11-27 09:49','pending',4,'s20231127-094944.jpg'),
(6,'20231127-095759.jpg','2023-11-27 09:58','pending',4,'s20231127-095759.jpg'),
(7,'20231127-095850.jpg','2023-11-27 09:59','pending',4,'s20231127-095850.jpg'),
(8,'20231127-100032.jpg','2023-11-27 10:00','pending',4,'s20231127-100032.jpg'),
(9,'20231127-100610.jpg','2023-11-27 10:06','pending',4,'s20231127-100610.jpg'),
(10,'20231127-100811.jpg','2023-11-27 10:08','pending',4,'s20231127-100811.jpg'),
(11,'20231127-101122.jpg','2023-11-27 10:11','pending',4,'s20231127-101122.jpg'),
(12,'20231127-101404.jpg','2023-11-27 10:14','pending',4,'s20231127-101404.jpg'),
(13,'20231127-101456.jpg','2023-11-27 10:15','pending',4,'s20231127-101456.jpg'),
(14,'20231127-101636.jpg','2023-11-27 10:16','pending',4,'s20231127-101636.jpg'),
(15,'20231127-101744.jpg','2023-11-27 10:17','pending',4,'s20231127-101744.jpg'),
(16,'20231201-155055.jpg','2023-12-01 15:51','pending',4,'s20231201-155055.jpg'),
(17,'20231201-155153.jpg','2023-12-01 15:52','pending',4,'s20231201-155153.jpg'),
(18,'20231201-155333.jpg','2023-12-01 15:53','pending',4,'s20231201-155333.jpg'),
(19,'20231201-155500.jpg','2023-12-01 15:55','pending',4,'s20231201-155500.jpg'),
(20,'20231201-155552.jpg','2023-12-01 15:56','pending',4,'s20231201-155552.jpg'),
(21,'20231201-155658.jpg','2023-12-01 15:57','pending',4,'s20231201-155658.jpg');

/*Table structure for table `smartlab_app_staff_lab_allocatio` */

DROP TABLE IF EXISTS `smartlab_app_staff_lab_allocatio`;

CREATE TABLE `smartlab_app_staff_lab_allocatio` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `day` varchar(50) NOT NULL,
  `period` varchar(30) NOT NULL,
  `SUBJECT_STAFF_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_staff_l_SUBJECT_STAFF_id_5f068d0d_fk_smartlab_` (`SUBJECT_STAFF_id`),
  CONSTRAINT `smartlab_app_staff_l_SUBJECT_STAFF_id_5f068d0d_fk_smartlab_` FOREIGN KEY (`SUBJECT_STAFF_id`) REFERENCES `smartlab_app_sub_staff_allo_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_staff_lab_allocatio` */

insert  into `smartlab_app_staff_lab_allocatio`(`id`,`day`,`period`,`SUBJECT_STAFF_id`) values 
(22,'Monday','1st period',16),
(23,'Monday','2nd Period',16),
(24,'Monday','3rd Period',16),
(25,'Monday','4th Period',16),
(26,'Wednesday','5th Period',17),
(27,'Wednesday','6th Period',17),
(28,'Thursday','1st period',17),
(29,'Thursday','2nd Period',17),
(30,'Friday','3rd Period',18),
(31,'Friday','4th Period',18),
(32,'Tuesday','1st period',18),
(33,'Tuesday','2nd Period',18),
(34,'Friday','2nd Period',18),
(35,'Thursday','4th Period',20),
(36,'Thursday','5th Period',20),
(37,'Thursday','6th Period',20);

/*Table structure for table `smartlab_app_staff_table` */

DROP TABLE IF EXISTS `smartlab_app_staff_table`;

CREATE TABLE `smartlab_app_staff_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `gender` varchar(35) NOT NULL,
  `dob` date NOT NULL,
  `place` varchar(50) NOT NULL,
  `pin` bigint NOT NULL,
  `post` varchar(30) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `qualification` longtext NOT NULL,
  `programming_lang` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `COURSE_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_staff_t_COURSE_id_f8b434d4_fk_smartlab_` (`COURSE_id`),
  KEY `smartlab_app_staff_t_LOGIN_id_29e3ca66_fk_smartlab_` (`LOGIN_id`),
  CONSTRAINT `smartlab_app_staff_t_COURSE_id_f8b434d4_fk_smartlab_` FOREIGN KEY (`COURSE_id`) REFERENCES `smartlab_app_course_table` (`id`),
  CONSTRAINT `smartlab_app_staff_t_LOGIN_id_29e3ca66_fk_smartlab_` FOREIGN KEY (`LOGIN_id`) REFERENCES `smartlab_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_staff_table` */

insert  into `smartlab_app_staff_table`(`id`,`name`,`gender`,`dob`,`place`,`pin`,`post`,`phone`,`email`,`qualification`,`programming_lang`,`photo`,`COURSE_id`,`LOGIN_id`) values 
(13,'Athira','female','1995-10-31','Kudukkil',875643,' Balussery',8976542345,'athira@gmail.com','Bsc.Computer Science,Msc.Computer Science','Python,Mysql,C programming','female1_wyXi3Gr.jpg',10,28),
(14,'Abhi','male','1994-06-30','Kunnamangalam',673572,'   Kunnamangalam',7895432190,'abhay@gmail.com','Phd,MSC,MCA','Mysql,C programming','man1_GxlyZWI.jpg',10,29),
(15,'Nihal','male','1991-07-17','Poonoor',673572,'            Ponoor',9867453210,'nihal@gmail.com','Bachelor\'s degree,Master\'s degree,High school diploma,Professional certifications ','Python,Mysql','man1_DaQuj25.jpg',13,31),
(16,'Hiba','female','1996-06-18','Kathiyode',564321,'Omassery',8945321789,'hiba06@gmail.com','Btech CSE,Mtech CSE','Java,Flutter,Android','female1_u9bzx0X.jpg',11,36),
(17,'dfghert','female','2013-12-03','cdfvgbh',123456,'dfvgbhn',9876543210,'nidhalkc369@gmail.com','rd5rfgvjmk,wdrvh,swdftgbh','Python,Flutter','female1_wyXi3Gr_fWVFFoC.jpg',12,37);

/*Table structure for table `smartlab_app_student_feedback` */

DROP TABLE IF EXISTS `smartlab_app_student_feedback`;

CREATE TABLE `smartlab_app_student_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` longtext NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `STAFF_id` bigint NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_student_STAFF_id_6a55d784_fk_smartlab_` (`STAFF_id`),
  KEY `smartlab_app_student_STUDENT_id_a07a23c2_fk_smartlab_` (`STUDENT_id`),
  CONSTRAINT `smartlab_app_student_STAFF_id_6a55d784_fk_smartlab_` FOREIGN KEY (`STAFF_id`) REFERENCES `smartlab_app_staff_table` (`id`),
  CONSTRAINT `smartlab_app_student_STUDENT_id_a07a23c2_fk_smartlab_` FOREIGN KEY (`STUDENT_id`) REFERENCES `smartlab_app_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_student_feedback` */

insert  into `smartlab_app_student_feedback`(`id`,`feedback`,`datetime`,`STAFF_id`,`STUDENT_id`) values 
(6,'bad class','2023-11-10 14:23:18.000000',13,10),
(7,'good class','2023-11-10 14:23:52.000000',14,10),
(8,'mxfngdgdg','2023-11-18 13:47:22.220351',14,10),
(9,'gfhj','2023-11-19 10:42:18.760185',15,11);

/*Table structure for table `smartlab_app_student_table` */

DROP TABLE IF EXISTS `smartlab_app_student_table`;

CREATE TABLE `smartlab_app_student_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `gender` varchar(35) NOT NULL,
  `dob` date NOT NULL,
  `place` varchar(50) NOT NULL,
  `pin` bigint NOT NULL,
  `post` varchar(30) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `COURSE_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `semester` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_student_LOGIN_id_017d0922_fk_smartlab_` (`LOGIN_id`),
  KEY `smartlab_app_student_COURSE_id_f4633424_fk_smartlab_` (`COURSE_id`),
  CONSTRAINT `smartlab_app_student_COURSE_id_f4633424_fk_smartlab_` FOREIGN KEY (`COURSE_id`) REFERENCES `smartlab_app_course_table` (`id`),
  CONSTRAINT `smartlab_app_student_LOGIN_id_017d0922_fk_smartlab_` FOREIGN KEY (`LOGIN_id`) REFERENCES `smartlab_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_student_table` */

insert  into `smartlab_app_student_table`(`id`,`fname`,`lname`,`gender`,`dob`,`place`,`pin`,`post`,`phone`,`email`,`qualification`,`photo`,`COURSE_id`,`LOGIN_id`,`semester`) values 
(10,'anu','ram','Female','2002-02-04','Koodathai',123456,'Thamarassery',7895432190,'anu@gmail.com','Plus two','female1_cQ9PVFa.jpg',11,32,'3'),
(11,'Aysha','shahana','Female','2003-12-01','Odupara',987658,'Narikkuni',9563283206,'shahana@gmail.com','Bsc Physics','female1_fwLXCEB.jpg',13,33,'1'),
(12,'Abhay','Raveendran','Male','2003-12-02','Balussery',987654,'Balussery',7895432190,'abhay@gmail.com','Bsc Physics','man1_Sah9v98.jpg',10,34,'2'),
(14,'Amala','Raj','Female','2003-12-30','Kudukkil',123456,'dfgth',9876543210,'nidhalkc369@gmail.com','gbhn,sdcfvgbhn','istockphoto-1413249877-2048x2048_HMrmBU8.jpg',11,39,'3');

/*Table structure for table `smartlab_app_sub_staff_allo_table` */

DROP TABLE IF EXISTS `smartlab_app_sub_staff_allo_table`;

CREATE TABLE `smartlab_app_sub_staff_allo_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `STAFF_id` bigint NOT NULL,
  `SUBJECT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_sub_sta_STAFF_id_59deb0f0_fk_smartlab_` (`STAFF_id`),
  KEY `smartlab_app_sub_sta_SUBJECT_id_cc674057_fk_smartlab_` (`SUBJECT_id`),
  CONSTRAINT `smartlab_app_sub_sta_STAFF_id_59deb0f0_fk_smartlab_` FOREIGN KEY (`STAFF_id`) REFERENCES `smartlab_app_staff_table` (`id`),
  CONSTRAINT `smartlab_app_sub_sta_SUBJECT_id_cc674057_fk_smartlab_` FOREIGN KEY (`SUBJECT_id`) REFERENCES `smartlab_app_labsubject_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_sub_staff_allo_table` */

insert  into `smartlab_app_sub_staff_allo_table`(`id`,`STAFF_id`,`SUBJECT_id`) values 
(16,14,13),
(17,13,15),
(18,16,17),
(19,14,15),
(20,15,16),
(21,13,14);

/*Table structure for table `smartlab_app_system_stud_allo_table` */

DROP TABLE IF EXISTS `smartlab_app_system_stud_allo_table`;

CREATE TABLE `smartlab_app_system_stud_allo_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `STUDENT_id` bigint NOT NULL,
  `SYSTEM_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `smartlab_app_system__STUDENT_id_a448f92f_fk_smartlab_` (`STUDENT_id`),
  KEY `smartlab_app_system__SYSTEM_id_6bc7e119_fk_smartlab_` (`SYSTEM_id`),
  CONSTRAINT `smartlab_app_system__STUDENT_id_a448f92f_fk_smartlab_` FOREIGN KEY (`STUDENT_id`) REFERENCES `smartlab_app_student_table` (`id`),
  CONSTRAINT `smartlab_app_system__SYSTEM_id_6bc7e119_fk_smartlab_` FOREIGN KEY (`SYSTEM_id`) REFERENCES `smartlab_app_system_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_system_stud_allo_table` */

insert  into `smartlab_app_system_stud_allo_table`(`id`,`STUDENT_id`,`SYSTEM_id`) values 
(17,10,4),
(18,12,4),
(19,10,5);

/*Table structure for table `smartlab_app_system_table` */

DROP TABLE IF EXISTS `smartlab_app_system_table`;

CREATE TABLE `smartlab_app_system_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `system_id` int NOT NULL,
  `HDD` longtext NOT NULL,
  `date` date NOT NULL,
  `RAM` longtext NOT NULL DEFAULT (_utf8mb3'2023-11-18 05:03:53.460773+00:00'),
  `SSD` longtext NOT NULL DEFAULT (_utf8mb3'1'),
  `processor` longtext NOT NULL DEFAULT (_utf8mb3'1'),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `smartlab_app_system_table` */

insert  into `smartlab_app_system_table`(`id`,`system_id`,`HDD`,`date`,`RAM`,`SSD`,`processor`) values 
(4,67,'CFVGBH','2023-11-18','RFGBH','FRGH','ERDFG'),
(5,31,'DFGHJ','2023-11-18','RTFGY','DFGH','FDG'),
(6,78,'SWDFG','2023-11-18','DFGHB','DXXFG','CFVG'),
(7,5,'SEDCFG','2023-11-18','XDFVGBH','FGH','FV'),
(9,94,'CFDCGV','2023-11-18','FCGVBH','FDFG','CFVGHBJN');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
