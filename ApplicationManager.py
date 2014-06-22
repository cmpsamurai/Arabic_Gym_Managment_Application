#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from Players import Players
from InterfaceHandler import InterfaceHandler
from PyQt4 import *
import datetime

class ApplicationManager:
	
	def __init__(self):
		self.players=Players()
		self.ui_handler = InterfaceHandler()
		self.ui_handler.connectUI(self)
		self.player_view_in_game()
		self.player_view_expired()
		
		
	def run(self):
		self.ui_handler.show()
	
	@staticmethod
	def convertDateString(string):
		y, m, i = map(int, string.split('-'))
		return QtCore.QDate(y, m, i)
		
	@staticmethod
	def convert(qtDate):
		return "{}-{}-{}".format(qtDate.year(), qtDate.month(), qtDate.day() )
			
	def init_interface(self):
		self.ui_handler.ui.txt_edit_name.setText("")
		self.ui_handler.ui.txt_edit_job.setText("")
		self.ui_handler.ui.txt_edit_tel.setText("")
		self.ui_handler.ui.txt_edit_email.setText("")
		
		self.ui_handler.ui.label_add_msg.setText("")
		self.ui_handler.ui.txt_add_name.setText("")
		self.ui_handler.ui.txt_add_job.setText("")
		self.ui_handler.ui.txt_add_tel.setText("")
		self.ui_handler.ui.txt_add_email.setText("")
		self.ui_handler.ui.txt_add_address.setText("")
		self.ui_handler.ui.label_add_msg.setText("")
		self.ui_handler.ui.label_renew_msg.setText("")
		self.ui_handler.ui.txt_renew_renewvalue.setText("")
		self.ui_handler.ui.label_edit_msg.setText("")
		self.ui_handler.ui.txt_edit_address.setPlainText("")
		self.ui_handler.ui.gb_edit.setDisabled(True)
		self.player_view_in_game()
		self.player_view_expired()
		
		
		
	def player_search(self):
		Name=unicode(self.ui_handler.ui.txt_search_name.text())
		query=u"SELECT * FROM Players WHERE Name LIKE '{}%'".format(Name)
		# (query)
		self.players.cursor.execute(query)
		allentries=self.players.cursor.fetchall()
		self.ui_handler.ui.list_search.clear()
		
		for x in allentries: 
			#(x[1])
			self.ui_handler.ui.list_search.addItem(unicode(x[1]))
			
		
		
	def player_delete_selected(self):
		Name=self.ui_handler.ui.list_search.currentItem().text()
		self.players.deletePlayer(Name)
		self.player_view_in_game()
		self.player_view_expired()
		self.ui_handler.ui.txt_edit_name.setText("")
		self.ui_handler.ui.txt_edit_job.setText("")
		self.ui_handler.ui.txt_edit_tel.setText("")
		self.ui_handler.ui.txt_edit_email.setText("")
		self.ui_handler.ui.txt_edit_address.setPlainText("")
		self.ui_handler.ui.label_edit_msg.setText(u"تم المسح بنجاح")
		self.ui_handler.ui.gb_edit.setDisabled(True)
		
	def player_edit_selected(self):
		if self.ui_handler.ui.list_search.currentItem() !=None:
			self.ui_handler.ui.gb_edit.setDisabled(False)
		
	def player_edit_saveedit(self):
		
		OldName=self.ui_handler.ui.list_search.currentItem().text()
			
		Name = unicode(self.ui_handler.ui.txt_edit_name.text())
		# Name
		query=u"SELECT * FROM Players WHERE Name = '{}'".format(Name)
		self.players.cursor.execute(query)
		allentries=self.players.cursor.fetchall()

		if len(allentries)!=0 and OldName !=Name:
			self.ui_handler.ui.label_edit_msg.setText(u"من فضلك ادخل اسم مش مكرر")
			return
			
			
		BD =ApplicationManager.convert(self.ui_handler.ui.date_edit_bd.date())
		# BD
		
		Joindate = ApplicationManager.convert(self.ui_handler.ui.date_edit_joindate.date())		
		Job = unicode(self.ui_handler.ui.txt_edit_job.text())
		Tel = unicode(self.ui_handler.ui.txt_edit_tel.text())
		Email = unicode(self.ui_handler.ui.txt_edit_email.text())
		Game = unicode(self.ui_handler.ui.combo_edit_game.currentText())
		Address =unicode(self.ui_handler.ui.txt_edit_address.toPlainText())
		if Name == "" :
			self.ui_handler.ui.label_edit_msg.setText(u"من فضلك ادخل اسم")
		
		else:
			if Job== "": Job = "-"
			if Tel== "": Tel = "-"
			if Email=="" :Email="-"
			self.players.updatePlayer(OldName,Name,BD,Tel,Address,Email,Game,Joindate)
			
			#empty the fileds
			self.ui_handler.ui.txt_edit_name.setText("")
			self.ui_handler.ui.txt_edit_job.setText("")
			self.ui_handler.ui.txt_edit_tel.setText("")
			self.ui_handler.ui.txt_edit_email.setText("")
			self.ui_handler.ui.txt_edit_address.setPlainText("")
			self.ui_handler.ui.label_edit_msg.setText(u"تم العديل بنجاح")
			self.player_view_in_game()
			self.player_view_expired()
			self.ui_handler.ui.gb_edit.setDisabled(True)
	
	def player_edit_canceledit(self):
		self.ui_handler.ui.gb_edit.setDisabled(True)
		
	def player_view_in_game(self):
		Game=unicode(self.ui_handler.ui.combo_search_viewbygame.currentText())
		#(Game)
		query="SELECT * FROM Players WHERE Game = '{}'".format(Game)
		# (query)
		self.players.cursor.execute(query)
		allentries=self.players.cursor.fetchall()
		self.ui_handler.ui.list_search.clear()
		
		for x in allentries: 
			#(x[1])
			self.ui_handler.ui.list_search.addItem(unicode(x[1]))
	
	
	def update_renew_info(self):
		if self.ui_handler.ui.list_renew.currentItem() != None:
			Name=self.ui_handler.ui.list_renew.currentItem().text()
			query=u"SELECT * FROM Players WHERE Name = '{}'".format(Name)
			#(query)
			self.players.cursor.execute(query)
			allentries=self.players.cursor.fetchall()
			for x in allentries:
				self.ui_handler.ui.txt_renew_renewvalue.setText(unicode(x[10]))
				self.ui_handler.ui.date_renew_renewdate.setDate(ApplicationManager.convertDateString(x[9]))
				self.ui_handler.ui.date_renew_validTill.setDate(ApplicationManager.convertDateString(x[11]))
				
	def update_edit_info(self):
		if self.ui_handler.ui.list_search.currentItem() !=None:
			Name=self.ui_handler.ui.list_search.currentItem().text()
			query=u"SELECT * FROM Players WHERE Name = '{}'".format(Name)
			#(query)
			self.players.cursor.execute(query)
			allentries=self.players.cursor.fetchall()
			for x in allentries:
                                self.ui_handler.ui.label_edit_msg.setText("")
				self.ui_handler.ui.txt_edit_name.setText(unicode(x[1]))
				self.ui_handler.ui.date_edit_bd.setDate(ApplicationManager.convertDateString(x[2]))
				self.ui_handler.ui.date_edit_joindate.setDate(ApplicationManager.convertDateString(x[8]))			
				self.ui_handler.ui.txt_edit_job.setText(unicode(x[3]))
				self.ui_handler.ui.txt_edit_tel.setText(unicode(x[4]))
				self.ui_handler.ui.txt_edit_address.setPlainText(unicode(x[5]))
				self.ui_handler.ui.txt_edit_email.setText(unicode(x[6]))
				if x[7]=="Aikido" :self.ui_handler.ui.combo_edit_game.setCurrentIndex(0)
				if x[7]=="KungFu" :self.ui_handler.ui.combo_edit_game.setCurrentIndex(1)
				if x[7]=="Free Style" :self.ui_handler.ui.combo_edit_game.setCurrentIndex(2)
				if x[7]=="Golden" :self.ui_handler.ui.combo_edit_game.setCurrentIndex(3)
	
	
	def player_view_expired(self):
		Game=unicode(self.ui_handler.ui.combo_expired.currentText())
		now = datetime.datetime.now()
		today="{}-{}-{}".format(now.year,now.month ,now.day)
		# today
		query="SELECT * FROM Players WHERE  Game='{}' AND ValidTill <= '{}' ".format(Game,today)
		# (query)
		self.players.cursor.execute(query)
		allentries=self.players.cursor.fetchall()
		self.ui_handler.ui.list_expired.clear()
		
		for x in allentries: 
			#(x[1])
			record =u"{}      :      {}".format(unicode(x[1]),unicode(x[11]))
			self.ui_handler.ui.list_expired.addItem(record)
		
	
	def player_add(self):
		
		Name = unicode(self.ui_handler.ui.txt_add_name.text())
		BD = ApplicationManager.convert(self.ui_handler.ui.date_add_bd.date())
		Joindate = ApplicationManager.convert(self.ui_handler.ui.date_add_joindate.date())
		Job = unicode(self.ui_handler.ui.txt_add_job.text())
		Tel = unicode(self.ui_handler.ui.txt_add_tel.text())
		Email = unicode(self.ui_handler.ui.txt_add_email.text())
		Game = unicode(self.ui_handler.ui.combo_add_game.currentText())
		Address = unicode(self.ui_handler.ui.txt_add_address.text())
		if Name == "" :
			self.ui_handler.ui.label_add_msg.setText(u"من فضلك ادخل اسم")
		
		else:
			if Job== "": Job = "-"
			if Tel== "": Tel = "-"
			if Email=="" :Email= "-"
			if self.players.addPlayer(Name,BD,Job,Tel,Address,Email,Game,Joindate)== "Duplicate Entry":
				self.ui_handler.ui.label_add_msg.setText(u"يوجد هذا الاسم من قبل")
			else:
				#empty the fileds
				self.ui_handler.ui.txt_add_name.setText("")
				self.ui_handler.ui.txt_add_job.setText("")
				self.ui_handler.ui.txt_add_tel.setText("")
				self.ui_handler.ui.txt_add_email.setText("")
				self.ui_handler.ui.txt_add_address.setText("")
				self.ui_handler.ui.label_add_msg.setText(u"تمت الاضافة بنجاح")
				self.player_view_in_game()
				self.player_view_expired()

	def player_renew_search(self):
		Name=unicode(self.ui_handler.ui.txt_renew_name.text())
		query=u"SELECT * FROM Players WHERE Name LIKE '{}%'".format(Name)
		# (query)
		self.players.cursor.execute(query)
		allentries=self.players.cursor.fetchall()
		self.ui_handler.ui.list_renew.clear()
		
		for x in allentries: 
			#(x[1])
			self.ui_handler.ui.list_renew.addItem(unicode(x[1]))
			
		
	def player_renew(self):
		if self.ui_handler.ui.list_renew.currentItem() != None:
			Name=self.ui_handler.ui.list_renew.currentItem().text()
			RenewDate = ApplicationManager.convert(self.ui_handler.ui.date_renew_renewdate.date())	
			ValidTill = ApplicationManager.convert(self.ui_handler.ui.date_renew_validTill.date())	
			RenewValue =self.ui_handler.ui.txt_renew_renewvalue.text()
			
			if RenewValue=="":
				self.ui_handler.ui.label_renew_msg.setText(u"من فضلك ادخل قيمة مناسبة للتجديد")
			else :
				self.players.renewToPlayer(Name,RenewDate,RenewValue,ValidTill)
				msg=u"تم التجديد ل {} بنجاح".format(Name)
				self.player_view_expired()
				self.ui_handler.ui.label_renew_msg.setText(msg)
		else:
			self.ui_handler.ui.label_renew_msg.setText(u"من فضلك اختار لاعب لتجديد اشتراكه")
		
		
	





if __name__ == '__main__':
	main()

