#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       QueryResult.py
#       
#       Copyright 2012 Mahmoud Aladdin <aladdin.cmp2014@gmail.com>
#       

class QueryResult:
	def __init__(self, RowCount = 0, Data = ()):
		self.rowCount = RowCount
		self.data = Data
		self.nextRow = 0
		pass
		
	def GetAffectedRowCount(self):
		return self.rowCount
		
	def GetResultData(self):
		return self.data
		
	def GetResultRow(self, index):
		if self.data != None and index < self.rowCount:
			return self.data[index]
		
	def GetNextRow(self) :
		if (self.nextRow == self.rowCount): return None
		if self.data != None:
			self.nextRow += 1
			return self.data[self.nextRow - 1]
		
	def __len__(self) :
		return len(self.data)
		
	def __iter__(self) :
		if self.data != None:
			for row in self.data:
				yield row
			
	def __str__(self) :
		return str(self.data)

if __name__ == '__main__':
	tuple_ = ((1, 2, 3), (1,2,3), (1,2,3))
	s = QueryResult(len(tuple_), tuple_)
	print str(s)
	for row in s:
		print row
	print s.GetRowCount()
	print s.GetResultRow(10)
	print s.GetResultData()
