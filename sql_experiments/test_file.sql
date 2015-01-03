-- I'm just using this file to run my queries that aren't currently working
.mode column
.headers on
.echo off

-- select engineers from WC
.print " "
.print "Select WC engineers"
SELECT employee.name, employee.personality_type, department.name
FROM employee
INNER JOIN department
ON employee.department = department.id
WHERE department.name = "Engineering";

-- Select feeling engineers  
.print " "
.print "Select feeling engineers"
SELECT employee.name, employee.personality_type, department.name
FROM employee
INNER JOIN department
ON employee.department = department.id
INNER JOIN personality_type
ON employee.personality_type = personality_type.signature
INNER JOIN letter
ON personality_type.signature = letter.letter
WHERE department.name = "Engineering"
AND letter.full_name = "Feeling";
