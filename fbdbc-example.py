import firebirdsql

connection = firebirdsql.connect(
    	host='Hostname/IP', 
    	database='C:/Path/To/DATABASE.FBD',
    	user='Username',
    	password='Password',
	    charset='ISO8859_1' #specify a character set for the connection
    	)

cur = connection.cursor()

cur.execute("select * from supercooltable where stuff='whatever';")

print cur.fetchall()