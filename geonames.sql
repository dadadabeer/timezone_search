CREATE TABLE country (
   countrycode char(2) NOT NULL,
   countryname varchar(200) NOT NULL,
   PRIMARY KEY (countrycode)
);

CREATE TABLE geonames (
   geonameid int(10) NOT NULL default '0',
   `name` varchar(200) NOT NULL default '',
   countrycode char(2) NOT NULL,
   `population` bigint(11) default '0',
   timezone varchar(40),
   PRIMARY KEY (`geonameid`)
   FOREIGN KEY (countrycode) REFERENCES country(countrycode)
);