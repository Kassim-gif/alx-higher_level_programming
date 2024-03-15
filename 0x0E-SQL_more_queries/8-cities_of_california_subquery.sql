-- lists all tha cities of California that can be found in tha database hbtn_0d_usa
-- lists all rows of a column in  database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
