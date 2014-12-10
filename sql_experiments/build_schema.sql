PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS company_department;
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

CREATE TABLE company_department(
    company_id integer,
    department_id integer UNIQUE,
    FOREIGN KEY (company_id) REFERENCES company(id),
    FOREIGN KEY (department_id) REFERENCES department(id)
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
    mb_p integer
);

INSERT INTO department (name) VALUES ("HR");
INSERT INTO company (name) VALUES ("google");
INSERT INTO company_department VALUES (1,1);