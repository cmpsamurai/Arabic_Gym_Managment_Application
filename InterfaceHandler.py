#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Main.py
#       
#  Copyright 2012 Mahmoud Aladdin <aladdin.cmp2014@gmail.com>, Moustafa Mahmoud
#		
#	 This is the Interface Handler for ZeniabEzzatOrphanage Management system.
#

from PyQt4 import QtCore, QtGui
from PyQt4 import *
 

from Interface_Gui import Ui_Form



class InterfaceHandler(QtGui.QMainWindow):
	
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent)
		self.ui =Ui_Form()
		self.ui.setupUi(self)
		
		
		
	def connectUI(self, obj):
		""" Connects components in UI with their corresponding event handlers in Application Manager """
		
		
		self.ui.bt_search.clicked.connect(obj.player_search)
		self.ui.bt_edit_edit_selected.clicked.connect(obj.player_edit_selected)
		self.ui.bt_edit_edit_selected.clicked.connect(obj.player_edit_selected)
		self.ui.bt_edit_saveedit.clicked.connect(obj.player_edit_saveedit)
		self.ui.bt_edit_canceledit.clicked.connect(obj.player_edit_canceledit)
		self.ui.bt_edit_delete.clicked.connect(obj.player_delete_selected)
		self.ui.bt_add.clicked.connect(obj.player_add)
		self.ui.bt_renew.clicked.connect(obj.player_renew)
		self.ui.bt_renew_search.clicked.connect(obj.player_renew_search)
		
		
		QtCore.QObject.connect(self.ui.combo_expired, QtCore.SIGNAL("currentIndexChanged(QString)"), obj.player_view_expired)
		
		QtCore.QObject.connect(self.ui.tabWidget, QtCore.SIGNAL("currentChanged(int)"), obj.init_interface)
		QtCore.QObject.connect(self.ui.tabWidget_2, QtCore.SIGNAL("currentChanged(int)"), obj.init_interface)
		
		QtCore.QObject.connect(self.ui.combo_search_viewbygame, QtCore.SIGNAL("currentIndexChanged(QString)"), obj.player_view_in_game)
		QtCore.QObject.connect(self.ui.combo_expired, QtCore.SIGNAL("currentIndexChanged(QString)"), obj.player_view_expired)
		QtCore.QObject.connect(self.ui.list_search, QtCore.SIGNAL("currentRowChanged(int)"), obj.update_edit_info)
		QtCore.QObject.connect(self.ui.list_renew, QtCore.SIGNAL("currentRowChanged(int)"), obj.update_renew_info)
		
		
	def __del__(self):
		pass

