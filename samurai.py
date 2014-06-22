# -*- coding: utf-8 -*-

import csv



def main():
	
	if os.path.isfile("Players.db") : print "file exists"
	else : print "file doesnt exist"
	
	mydatabase="Players.db"
	connection=sqlite3.connect(mydatabase)
	cursor=connection.cursor()
	#cursor.execute('DROP TABLE mytable')
	#cursor.execute('CREATE TABLE mytable (Id INTEGER PRIMARY KEY,Name TEXT, BD NUMERIC ,Game TEXT,JoinDate TEXT,LASTRENEW TEXT ,LASTRENEWVALUE TEXT)')
	import time
	today=time.strftime("%A, %B %d, %Y")
	cursor.execute('INSERT INTO mytable VALUES(null, ?, ?)', ("hello", u"مصطفي محمود فتحي"))
	connection.commit()
	
	
	cursor.execute('SELECT * FROM mytable')
	allentries=cursor.fetchall()
	
	f=open("m.txt","wb")
	for x in allentries:
		print "Item number: " + str(x[0]) + "  Date: " + x[1] + "  Entry: " + x[2]
		strr=x[2].encode('utf8')
		f.write(strr+"\n")
		
		
	cursor.close()
	quit()
	return 0

if __name__ == '__main__':
	main()

