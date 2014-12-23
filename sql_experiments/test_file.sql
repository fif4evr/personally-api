-- I'm just using this file to run my queries that aren't currently working
.mode column
.headers on
.echo off

-- List the most extreme Extrovert (you can assume somebody is an extrovert)  
.print " "
.print "List the most extreme Extrovert (you can assume somebody is an extrovert)"
SELECT employee.name as "Employee Name", MAX(employee.ie_score) as "Maximum Extrovert Score"
FROM employee
INNER JOIN personality_type
ON employee.personality_type = personality_type.signature
WHERE personality_type.ie = "E";