#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       DBLayer.py
#       
#       Copyright 2012 Mahmoud Aladdin <aladdin.cmp2014@gmail.com>
#       

import os.path
import sqlite3
import re #for data sanitization
from QueryResult import QueryResult

class DBLayer:
	def __init__(self):
		mydatabase="Players.db"
		if os.path.isfile("Players.db") : 
			print "file exists"
			self.connection=sqlite3.connect(mydatabase)
			self.cursor=self.connection.cursor()
			
		
		else :
			print "file doesnt exist"
			self.connection=sqlite3.connect(mydatabase)
			self.cursor=self.connection.cursor()
			self.cursor.execute('CREATE TABLE Players (Id INTEGER PRIMARY KEY,Name TEXT UNIQUE, BD NUMERIC ,Game TEXT,JoinDate TEXT,LastRenew TEXT ,LastRenewValue NUMERIC)')
			#cursor.close()
			#quit()

	def InsertQuery(self, tableName, attributes):
		self.query = u"INSERT INTO `{}`".format(tableName)
		cols = u""
		vals = u""
		for key in attributes.keys():
			cols += u"`{}`".format(key) + ','
			if type(attributes[key]) is int or type(attributes[key]) is long or type(attributes[key]) is float:
				vals += str(attributes[key]) + ','
			else:
				vals += u"'{}'".format((attributes[key])) + ','
		self.query += u"({})".format(cols[:-1])
		self.query += u" VALUES ({})".format(vals[:-1])
		print self.query
		self.cursor.execute('SELECT * FROM Players')
		allentries=self.cursor.fetchall()
		
	
		for x in allentries:
			print "Item number: " + str(x[0]) + "  Date: " + x[1] + "  Entry: " + x[2]
			strr=x[2].encode('utf8')

	
	def UpdateQuery(self, tablesName, attributes, cond = ''):
		self.query = u"UPDATE"
		table_part = u"" 
		set_part = u""
		for table in tablesName:
			table_part = u"`{}`,".format(table)
			set_part = u""
			for key in attributes[table].keys():
				set_part += u"`{}`.`{}`=".format(table, key)
				if type(attributes[table][key]) is int or type(attributes[table][key]) is long or type(attributes[table][key]) is float:
					set_part += str(attributes[table][key]) + u','
				else:
					set_part += u"'{}'".format(attributes[table][key]) + u','
				
		self.query += u' ' +table_part[:-1] + u' SET ' + set_part[:-1]
		if cond != "":
			self.query += u" WHERE {}".format(cond)
		print self.query

	def SelectQuery(self, tablesName, attributes, cond = ''):
		self.query = u"SELECT"
		columns_required = u""
		tables_part = u""
		for table in tablesName:
			tables_part += u"`{}`,".format(table)
			for column in attributes[table]:
				columns_required += u"`{}`.`{}`,".format(table, column)
		self.query += u' ' + columns_required[:-1] + u" FROM " + tables_part[:-1]
		if cond != '':
			self.query += u" WHERE {}".format(cond)
		print self.query

	def DeleteQuery(self, tablename, cond = ''):
		self.query = u"DELETE FROM `{}`".format(tablename)
		if cond != '':
			self.query += u" WHERE {}".format(cond)
		print self.query

	def CustomQuery(self, query):
		self.query = query

	def ExecuteQuery(self):
		print self.query
		count = self.cursor.execute(self.query)
		self.connection.commit()
		data = self.cursor.fetchall()
		print count
		return QueryResult(count, data)

	def __del__(self):
		pass
	
	@staticmethod
	def cleanText(text):
		
		if isinstance(text, str):
			return text.replace("'", "\'")
			#rx = re.compile('\W+')
			#text = rx.sub(' ', text).strip()
		return text


if __name__ == '__main__':
	pass

