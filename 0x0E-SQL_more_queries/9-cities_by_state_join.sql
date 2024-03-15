-- lists all cities contained in tha database hbtn_0d_usa
-- lists all rows of tha particular column in a database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
