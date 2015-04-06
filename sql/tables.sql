CREATE TABLE Address (
  id_address int(11) NOT NULL DEFAULT '0',
  id_name int(11) DEFAULT NULL,
  address varchar(750) DEFAULT NULL,
  city varchar(100) DEFAULT NULL,
  country varchar(250) DEFAULT NULL,
  add_remarks varchar(200) DEFAULT NULL,
  PRIMARY KEY (id_address)
);

CREATE TABLE Aka (
  id_aka int(11) NOT NULL DEFAULT '0',
  id_name int(11) DEFAULT NULL,
  aka_type varchar(10) DEFAULT NULL,
  aka_name varchar(350) DEFAULT NULL,
  aka_remarks varchar(200) DEFAULT NULL,
  PRIMARY KEY (id_aka)
);

CREATE TABLE Name (
  id_name int(11) NOT NULL DEFAULT '0',
  name varchar(350) DEFAULT NULL,
  type varchar(12) DEFAULT NULL,
  program varchar(50) DEFAULT NULL,
  title varchar(200) DEFAULT NULL,
  remarks varchar(1000) DEFAULT NULL,
  PRIMARY KEY (id_name)
);