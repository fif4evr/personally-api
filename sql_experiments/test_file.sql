-- I'm just using this file to run my queries that aren't currently working
.mode column
.headers on
.echo on

.print "List Personality Types with Letters"
SELECT personality_type.*, letter.full_name
FROM personality_type
INNER JOIN letter
ON personality_type.ie = letter.letter; 