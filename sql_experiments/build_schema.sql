PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS personality_type;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS company;



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
    mb_i integer,
    mb_e integer,
    mb_s integer,
    mb_n integer,
    mb_t integer,
    mb_f integer,
    mb_j integer,
    mb_p integer,
    mb_type text,
    hire_date integer,
    gender text,
    company integer,
    department integer,
    FOREIGN KEY (company) REFERENCES company(id),
    FOREIGN KEY (department) REFERENCES department(id),
    FOREIGN KEY (mb_type) REFERENCES personality_type(signature)
);

CREATE TABLE personality_type(
    signature text primary key,
    description text
);

CREATE TABLE letter(
    letter text primary key,
    description text,
    full_name text
);

INSERT INTO department (name) VALUES ("HR");
INSERT INTO department (name) VALUES ("Engineering");
INSERT INTO department (name) VALUES ("Marketing");
INSERT INTO company (name) VALUES ("Google");
INSERT INTO company (name) VALUES ("Microsoft");
INSERT INTO company (name) VALUES ("Windsor Circle");
INSERT INTO employee (name,bio,company,department) VALUES ("Ben","Ben is a person",1,3);
INSERT INTO employee (name,bio,company,department) VALUES ("Tim","Tim is learning Python",2,3);
INSERT INTO employee (name,bio,company,department) VALUES ("Bob","I made Bob up",3,1);
INSERT INTO employee (name,bio,company,department) VALUES ("Joe","Joe dreams of being real some day",2,1);
INSERT INTO employee (name,bio,company,department) VALUES ("Liz","Liz is not learning Python",2,2);
INSERT INTO employee (name,bio,company,department) VALUES ("Claire","Claire is confused as to why she's in this database",1,1);
INSERT INTO personality_type (signature) VALUES ("ISTJ");
INSERT INTO personality_type (signature) VALUES ("ISFJ");
INSERT INTO personality_type (signature) VALUES ("INFJ");
INSERT INTO personality_type (signature) VALUES ("INTJ");
INSERT INTO personality_type (signature) VALUES ("ISTP");
INSERT INTO personality_type (signature) VALUES ("ISFP");
INSERT INTO personality_type (signature) VALUES ("INFP");
INSERT INTO personality_type (signature) VALUES ("INTP");
INSERT INTO personality_type (signature) VALUES ("ESTP");
INSERT INTO personality_type (signature) VALUES ("ESFP");
INSERT INTO personality_type (signature) VALUES ("ENFP");
INSERT INTO personality_type (signature) VALUES ("ENTP");
INSERT INTO personality_type (signature) VALUES ("ESTJ");
INSERT INTO personality_type (signature) VALUES ("ESFJ");
INSERT INTO personality_type (signature) VALUES ("ENFJ");
INSERT INTO personality_type (signature) VALUES ("ENTJ");
INSERT INTO letter (letter) VALUES ("E");
INSERT INTO letter (letter) VALUES ("I");
INSERT INTO letter (letter) VALUES ("S");
INSERT INTO letter (letter) VALUES ("N");
INSERT INTO letter (letter) VALUES ("T");
INSERT INTO letter (letter) VALUES ("F");
INSERT INTO letter (letter) VALUES ("J");
INSERT INTO letter (letter) VALUES ("P");
