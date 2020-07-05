学习笔记
========

#MySql
Python 3.7以上版本用 PyMysql更稳定
pip install pymysql
linux下区分大小写，windows下无法区分大小写
linux下配置文件 /etc/mysql/my.cnf文件中
[mysqld]的后面加
lower_case_table_names=1 
0:区分大小写; 1:不区分

create database scrapyDB

CREATE TABLE `movies`
(
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `title` varchar(200) NOT NULL,
      `category` char(20) NOT NULL,
      `date` char(20) NOT NULL,
	  primary key (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4

##Middleware
下载中间件改代理ip
setting中增加download_middlewares


	  

	  
