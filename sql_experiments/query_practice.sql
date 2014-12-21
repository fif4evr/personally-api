.mode column
.headers on
.echo on

-- Select all Microsoft Employees

.print "Select all Microsoft employees"

SELECT employee.* 
FROM employee 
INNER JOIN company 
ON employee.company = company.id 
WHERE company.name="Microsoft";

