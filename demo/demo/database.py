import sqlite3

conection = sqlite3.connect('myquotes.db')
currsor = conection.cursor()
# currsor.execute(""" create table mydata(
# title text,
# author text,
# tag text
# )
#
# """)

currsor.execute(""" insert into mydata values ('hello ','myname is pk','this is my database')""")
conection.commit()
conection.close()