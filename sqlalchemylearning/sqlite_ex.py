import sqlite3
con = sqlite3.connect("test.db")

c = con.cursor()
c.execute("""
		  CREATE TABLE person
		  (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
		  """)

c.execute("""
		  CREATE TABLE address
		  (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
		  post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
		  FOREIGN KEY(person_id) REFERENCES person(id))
		  """)

c.execute(""" INSERT INTO person VALUES(1, 'John Smith')""")

c.execute(""" INSERT INTO address VALUES(1, 'USA SanFransisco', '1', '456345', 1)""")

con.commit()
con.close()

