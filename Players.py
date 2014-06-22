#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import sqlite3
class Players:
	
	def __init__(self):
		mydatabase="Players.db"
		if os.path.isfile("Players.db") : 
			# "file exists"
			self.connection=sqlite3.connect(mydatabase)
			self.cursor=self.connection.cursor()
			
		
		else :
			# "file doesnt exist"
			self.connection=sqlite3.connect(mydatabase)
			self.cursor=self.connection.cursor()
			self.cursor.execute('CREATE TABLE Players (Id INTEGER PRIMARY KEY,Name TEXT UNIQUE, BD NUMERIC,Job TEXT,Tel TEXT,Address Text,Email TEXT ,Game TEXT,JoinDate TEXT,LastRenew TEXT ,LastRenewValue NUMERIC,ValidTill TEXT)')
			#cursor.close()
			#quit()
			
		
		
	def addPlayer(self,Name,BD,Job,Tel,Address,Email,Game,JoinDate):
		query=u"SELECT * FROM Players WHERE Name = '{}'".format(Name)
		
		self.cursor.execute(query)
		allentries=self.cursor.fetchall()

		if len(allentries)==0:
			count=self.cursor.execute('INSERT INTO Players VALUES(null, ?, ?, ?, ?, ?, ?, ?, ?,"2000-1-1","0","2000-1-1")', (Name,BD,Job,Tel,Address,Email,Game,JoinDate))
			self.connection.commit()
			return "Success"
			
			
		else:
			return "Duplicate Entry"
		
		
		
			
	def deletePlayer(self,Name):
		
		query=u"SELECT * FROM Players WHERE Name = '{}'".format(Name)
		#(query)
		self.cursor.execute(query)
		allentries=self.cursor.fetchall()
		for x in allentries:
			Id=x[0]
			query=u"Delete FROM Players WHERE Id = '{}'".format(Id)
			self.cursor.execute(query)
			self.connection.commit()
			return "Success Deletion"
			
			
	
	def updatePlayer(self,OldName,Name,BD,Tel,Address,Email,Game,JoinDate):
		query=u"SELECT * FROM Players WHERE Name = '{}'".format(OldName)
		#(query)
		self.cursor.execute(query)
		allentries=self.cursor.fetchall()
		for x in allentries:
			Id=x[0]
			
		if len(allentries)==0:
			return "Empty"
			
		else:
			query=u"UPDATE Players SET  Name = '{}' , BD='{}' , Tel='{}' ,Address='{}' , Email='{}' ,Game='{}' ,JoinDate='{}' WHERE Id='{}'".format(Name,BD,Tel,Address,Email,Game,JoinDate,Id)
			#(query)
			
			self.cursor.execute(query)
			self.connection.commit()
			return "Success Update"
			
			
	def renewToPlayer(self,Name,LastRenew,LastRenewValue,ValidTill):
		query=u"SELECT * FROM Players WHERE Name = '{}'".format(Name)
		#(query)
		self.cursor.execute(query)
		allentries=self.cursor.fetchall()
		for x in allentries:
			Id=x[0]

		if len(allentries)==0:
			return "Empty"
			
		else:
			query=u"UPDATE Players SET LastRenew ='{}' ,LastRenewValue ='{}' ,ValidTill='{}' WHERE Id='{}'".format(LastRenew,LastRenewValue,ValidTill,Id)
			#(query)
			
			self.cursor.execute(query)
			self.connection.commit()
			return "Success Renew"
			
			
		
		

	
		
		
		

if __name__ == '__main__':
	m=Players()
	# m.addPlayer("Moustafa ","1992-2-1","Programmer","01140609033"," 6 oct ewrwe r" ,"Mousta @ moustafa ","Aikido","11-7-1992")
	# m.addPlayer(u"بي ","1994-2-4","Programmer","01140609033"," 6 oct ewrwe r" ,"Mousta @ moustafa ","Aikido","11-7-1992")
	# m.addPlayer(u"بasds ","1994-2-4","Programmer","01140609033"," 6 oct ewrwe r" ,"Mousta @ moustafa ","KungFu","11-7-1992")
	
	m.cursor.execute('SELECT * FROM Players')
	allentries=m.cursor.fetchall()
	
		

