-- Creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT AUTO_INCREMENT UNIQUE NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
