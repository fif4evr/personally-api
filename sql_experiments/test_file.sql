-- I'm just using this file to run my queries that aren't currently working
.mode column
.headers on
.echo on

-- Select all Male Employees and show their name and whether they're an introvert or extrovert, and the degree of that.
SELECT employee.name as "name", letter.full_name as "Introvert/Extrovert", employee.ie_score as "IE Degree", letter.description as "Description"
FROM employee
INNER JOIN personality_type
ON employee.personality_type = personality_type.signature
INNER JOIN letter
ON letter.letter = personality_type.ie
WHERE employee.gender = "M";