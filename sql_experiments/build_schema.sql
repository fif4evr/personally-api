PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS personality_type;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS letter;



CREATE TABLE company(
	id integer primary key,
	name text not null
);

CREATE TABLE department(
	id integer primary key,
	name text not null
);

CREATE TABLE employee(
    id integer primary key,
    name text not null,
    bio text,
    ie_score integer,
    sn_score integer,
    tf_score integer,
    jp_score integer,
    personality_type text,
    hire_date DATE,
    gender text,
    company integer,
    department integer,
    FOREIGN KEY (company) REFERENCES company(id),
    FOREIGN KEY (department) REFERENCES department(id),
    FOREIGN KEY (personality_type) REFERENCES personality_type(signature)
);

CREATE TABLE personality_type(
    signature text primary key,
    ie text,
    sn text,
    tf text,
    jp text,
    description text,
    FOREIGN KEY (ie) REFERENCES letter(letter),
    FOREIGN KEY (sn) REFERENCES letter(letter),
    FOREIGN KEY (tf) REFERENCES letter(letter),
    FOREIGN KEY (jp) REFERENCES letter(letter)
);

CREATE TABLE letter(
    letter text primary key,
    description text,
    full_name text
);

INSERT INTO department (name) VALUES ("Sales");
INSERT INTO department (name) VALUES ("Engineering");
INSERT INTO department (name) VALUES ("Marketing");
INSERT INTO company (name) VALUES ("Google");
INSERT INTO company (name) VALUES ("Microsoft");
INSERT INTO company (name) VALUES ("Windsor Circle");
INSERT INTO letter (letter,description,full_name) VALUES ("E","Weird people who surround themselves with others to gain energy","Extrovert");
INSERT INTO letter (letter,description,full_name) VALUES ("I","Normal people who recharge by hiding in their hobbit holes","Introvert");
INSERT INTO letter (letter,description,full_name) VALUES ("S","Very sensingtive people","Sensing");
INSERT INTO letter (letter,description,full_name) VALUES ("N","Illogical people who INTUIT their ways to ideas","Intuitive");
INSERT INTO letter (letter,description,full_name) VALUES ("T","Brain-using people","Thinking");
INSERT INTO letter (letter,description,full_name) VALUES ("F","Buy me some kleenex","Feeling");
INSERT INTO letter (letter,description,full_name) VALUES ("J","Judge not lest ye be judged","Judging");
INSERT INTO letter (letter,description,full_name) VALUES ("P","I've got a mind like a perceive","Perceiving");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ISTJ","I","S","T","J");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ISFJ","I","S","F","J");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("INFJ","I","N","F","J");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("INTJ","I","N","T","J");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ISTP","I","S","T","P");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ISFP","I","S","F","P");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("INFP","I","N","F","P");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("INTP","I","N","T","P");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ESTP","E","S","T","P");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ESFP","E","S","F","P");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ENFP","E","N","F","P");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ENTP","E","N","T","P");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ESTJ","E","S","T","J");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ESFJ","E","S","F","J");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ENFJ","E","N","F","J");
INSERT INTO personality_type (signature,ie,sn,tf,jp) VALUES ("ENTJ","E","N","T","J");
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Ben","Ben is a person",2,3,'2014-02-21','M','ENTJ','56','76','1','30');
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Tim","Tim is learning Python",2,3,'2014-06-01','M','INTJ','56','76','1','30');
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Bob","I made Bob up",3,3,'2014-11-02','M','ISFP','30','99','2','14');
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Joe","Joe dreams of being real some day",1,3,'2014-09-21','M','ENTJ','56','76','1','30');
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Liz","Liz is not learning Python",3,3,'2014-05-21','F','INFJ','33','21','37','2');
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Claire","Claire is confused as to why she's in this database",1,3,'2014-12-25','F','ISFJ','80','90','15','33');
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Mark","Mark enjoys fictional walks on the beach",2,3,'2014-03-21','M','INTP','30','9','12','70');
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Caleb","Caleb doesn't work at WC yet",2,3,'2014-12-31','M','INTJ','33','22','80','22');
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Jane","I made Jane up",3,3,'2014-05-02','F','ISFP','30','99','2','14');
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Samoa","Samoa is a dog.  She probably will not be a good employee, but is happy to be included",1,3,null,'F','ESFJ','100','50','100','50');
INSERT INTO employee (name,bio,department,company,hire_date,gender,personality_type,ie_score,sn_score,tf_score,jp_score)
VALUES ("Michael","There are many Michaels in the world.  This is one of them",3,2,'2009-01-01','M','ESFP','33','21','37','2');