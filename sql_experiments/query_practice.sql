.mode column
.headers on
.echo on

-- Select all employees who work for Windsor Circle, (display only employee fields)

.print "Select all Windsor Circle employees"

SELECT employee.* 
FROM employee 
INNER JOIN company 
ON employee.company = company.id 
WHERE company.name="Windsor Circle";

-- Select all employees who don't work for WC
.print "Select all employees who don't work for WC"
SELECT employee.*
FROM employee
INNER JOIN company
ON employee.company = company.id
WHERE company.name<>"Windsor Circle";

-- Select all Employees who work for WC and are introverts
.print "Select all Employees who work for WC and are introverts"
SELECT employee.*
FROM employee
INNER JOIN company
ON employee.company = company.id
INNER JOIN personality_type
ON employee.personality_type = personality_type.signature
WHERE company.name = "Windsor Circle" 
AND personality_type.ie = "I";

-- Select all Engineers who work for WC and are NOT introverts.  Show only their name and personality type.
.print "Select all Engineers who work for WC and are NOT introverts. Show only their name and personality type."
SELECT employee.name, employee.personality_type
FROM employee
INNER JOIN company
ON employee.company = company.id
INNER JOIN personality_type
ON employee.personality_type = personality_type.signature
INNER JOIN department
ON employee.department = department.id
WHERE company.name = "Windsor Circle" 
AND personality_type.ie <> "I"
AND department.name = "Engineering";

-- Select the first 2 employees who work for WC sorted alphabetically by name 
.print "Select the first 2 employees who work for WC sorted alphabetically by name"
SELECT employee.*
FROM employee
INNER JOIN company
ON employee.company = company.id
WHERE company.name = "Windsor Circle"
ORDER BY name ASC
LIMIT 2;

-- list personality types with letters
.print "List Personality Types with Letters"
SELECT personality_type.signature
FROM personality_type
INNER JOIN letter
ON personality_type.ie = letter.letter;
