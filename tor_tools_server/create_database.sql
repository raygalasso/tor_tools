create database tor_tools character set utf8 collate utf8_bin;
create user 'tor_tools'@'localhost' identified by '9b47a1d75b4e43e3b5560fc79f289136';
grant all privileges on tor_tools.* to 'tor_tools'@'localhost';
flush privileges;
quit;