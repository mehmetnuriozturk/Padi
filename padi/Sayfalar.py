# -*- coding: utf-8 -*-
#Mehmet Nuri ÖZTÜRK <mnozturk2@gmail.com>
import urllib, re, time
import os
import descriptionsDesktop 
from PyQt4 import QtCore, QtGui
import scrPadi

def check(self):
	self.index = self.stackedWidget.currentIndex()  
	self.labelAlt.show()
	#self.internetControl()
	if self.index == 0:
	    self.buttonIleri.show()
	    self.statusLabel.setText(u"Masaüstünüzü seçiniz")
	    self.screenLabel.setText(u"Padi'ye hoşgeldiniz!")
	    
	    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/icons/padi.png"))
	    self.buttonGeri.hide()
	    
	if self.index == 1:
	    self.buttonIleri.show()
	    self.statusLabel.setText(u"Masaüstü Yükleme")
	    self.screenLabel.setText(u"Masaüstünü Seçme")  
	    
	    
	    self.buttonGeri.show()
	    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/icons/applications-other.png"))
	    desktopValue = self.comboBox.currentIndex()
	    if desktopValue == 0:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(""))
		    self.xdesktopLabel.setText("none")
		    self.buttonIleri.setEnabled(False)
		    self.getinfoButton.setEnabled(False)
	    if desktopValue == 1:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Kde.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/kde.png"))
		    self.xdesktopLabel.setText("kde")
		    self.buttonIleri.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/kde.png" /></p>"""+descriptionsDesktop.kdeDescrip)               
	    if desktopValue == 2:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Gnome.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/gnome.png"))
		    self.xdesktopLabel.setText("gnome")
		    self.buttonIleri.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/gnome.png" /></p>"""+descriptionsDesktop.gnomeDescrip)
	    if desktopValue == 3:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Xfce.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/xfce.png"))
		    self.xdesktopLabel.setText("xfce")
		    self.buttonIleri.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/xfce.png" /></p>"""+descriptionsDesktop.xfceDescrip)
	    if desktopValue == 4:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Lxde.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/lxde.png"))
		    self.xdesktopLabel.setText("lxde")
		    self.buttonIleri.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/lxde.png" /></p>"""+descriptionsDesktop.lxdeDescrip)
	    if desktopValue == 5:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Mate.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/mate.png"))
		    self.xdesktopLabel.setText("mate")
		    self.buttonIleri.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/mate.png" /></p>"""+descriptionsDesktop.mateDescrip)
	    if desktopValue == 6:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Cinnamon.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/cinnamon.png"))
		    self.xdesktopLabel.setText("cinnamon")
		    self.buttonIleri.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/cinnamon.png" /></p>"""+descriptionsDesktop.cinnamonDescrip)
	    if desktopValue == 7:
		    self.labelScreenshots.setPixmap(QtGui.QPixmap(":/screenshots/Screenshots/Fluxbox.png"))
		    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/fluxbox.png"))
		    self.xdesktopLabel.setText("fluxbox")
		    self.buttonIleri.setEnabled(True)
		    self.getinfoButton.setEnabled(True)
		    self.infoTextBrowser.setText("""<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src=":/desktops/Desktops/fluxbox.png" /></p>"""+descriptionsDesktop.fluxboxDescrip)
	self.labelAlt.setText("'"+self.comboBox.currentText()+"' secildi")
			    
	if self.index == 2:
		
	    self.buttonGeri.show()
	    self.buttonIleri.hide()	    
	    self.statusLabel.setText(u"Bitti")
	    self.screenLabel.setText(u"Masaüstünü Yükleme")
	    
	    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/icons/Download.png"))
	    self.desktopLogoLabel.setPixmap(QtGui.QPixmap(":/logo/Logo/"+self.xdesktopLabel.text()+".png"))

		
		
		
		
		
		

	if self.index == 3:
		
		
	    self.buttonGeri.show()
	    		
	    self.buttonIleri.hide()
	    self.statusLabel.setText(u"Bitti!")
	    self.screenLabel.setText(u"Bitti")
	    
	    self.statusProgLabel.setPixmap(QtGui.QPixmap(":/icons/applications-internet.png"))
	    
	    
	    self.desktopLogoLabel.setPixmap(QtGui.QPixmap(":/icons/Logo/"+self.xdesktopLabel.text()+".png"))
