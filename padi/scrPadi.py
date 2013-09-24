# -*- coding: utf-8 -*-
#
# Licensed under GPL v3
# Copyright 2013, Mehmet Nuri ÖZTÜRK <mnozturk2@gmail.com>
#
# Please read the COPYING file.


from PyQt4 import QtCore, QtGui
from ui_padi import Ui_padi
import Sayfalar
import icons_rc
import sys
import os

import urllib, re, time



class MainWindow(QtGui.QMainWindow, Ui_padi):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.buttonGeri.hide()
        self.buttonSon.hide()
        
        self.labelAlt.hide()
  
        
        self.xdesktopLabel.hide()
        self.buttonGeri2.hide()
        self.animasyon.hide()
        self.yukleniyor = QtGui.QMovie(":/icons/loading.gif")
        self.animasyon.setMovie(self.yukleniyor)
        self.yukleniyor.start()

     

        
        
        QtCore.QObject.connect(self.buttonIleri, QtCore.SIGNAL("clicked()"), self.indexNext)
        QtCore.QObject.connect(self.buttonGeri, QtCore.SIGNAL("clicked()"), self.indexBack)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("activated(QString)"), self.checkIndex)
        
        QtCore.QObject.connect(self.getinfoButton, QtCore.SIGNAL("clicked()"), self.desktopInfo) 
        QtCore.QObject.connect(self.buttonGeri2, QtCore.SIGNAL("clicked()"), self.backAnasayfa)
        QtCore.QObject.connect(self.urlDevelop, QtCore.SIGNAL("clicked()"), self.openDevelop)
        QtCore.QObject.connect(self.urlPage, QtCore.SIGNAL("clicked()"), self.openPage)
        QtCore.QObject.connect(self.urlLicense, QtCore.SIGNAL("clicked()"), self.openLicense)
        QtCore.QObject.connect(self.buttonIptal, QtCore.SIGNAL("clicked()"), self.cancelPadi)
        QtCore.QObject.connect(self.downloadButton, QtCore.SIGNAL("clicked()"), self.installDesktop)


    

    
      
    def cancelPadi(self):
	  a = QtGui.QMessageBox()
	  a.setWindowTitle(u"Program çıkışı")
	  a.setIcon(a.Information)
	  a.setText(u"Programdan çıkmak istediğinize eminmisiniz?")
	  hayir = a.addButton(u"Hayır",a.DestructiveRole)
	  evet = a.addButton(u"Evet",a.AcceptRole)	  
	  b = QtGui.QIcon(":/icons/padi.png")
	  a.setWindowIcon(b)
	  a.exec_()
	  
	  if a.clickedButton() == evet:
		sys.exit()


    def openPage(self):
        import webbrowser
        webbrowser.open_new_tab("https://github.com/mehmetnuriozturk/Padi")
    def openDevelop(self):
        self.welcomeLabel.setText(u"Yazar: Mehmet Nuri Öztürk <mnozturk2@gmail.com>")
    def openLicense(self):
        self.welcomeLabel.setText(u"""
        GNU GENERAL PUBLIC LICENSE
        Version 3, 29 Jun 2007   
""")

    def backAnasayfa(self):
        self.labelAlt.hide()
        
        self.buttonGeri2.hide()

        
        self.downloadButton.show()
        self.stackedWidget.setCurrentIndex(1)
        self.buttonGeri.show()
        self.buttonIleri.show()
        self.statusLabel.setText(u"Masaüstünü seç")
        self.screenLabel.setText(u"Masaüstü yöneticisini seç")
        
        self.statusProgLabel.setPixmap(QtGui.QPixmap(":/icons/applications-other.png"))

        
    def desktopInfo(self):
        self.stackedWidget.setCurrentIndex(3)
        self.buttonGeri.hide()
        self.buttonIleri.hide()
        self.buttonGeri2.show()
        self.statusLabel.setText(self.comboBox.currentText()+u" Masaüstü Hakkında")
        self.screenLabel.setText(u"Masaüstü Hakkında")
        
        self.statusProgLabel.setPixmap(QtGui.QPixmap(":/icons/dialog-information.png"))

    

    def internetControl(self):
        #value = 0 => bağlı değil demek
        global netWorkConnectValue
        netWorkConnectValue = ["0"]
        try:
            url = urllib.urlopen("http://www.google.com.tr")      
            url.read()
            self.labelAlt.show()
            self.labelAlt.setText(u"İnterner bağlantısı sağlanamadı")
            print"\n\33[2;36mİnternet bağlantısı başarılı!\n\033[0m"
            netWorkConnectValue.pop()
            netWorkConnectValue.append("1")      
        except:
            QtGui.QMessageBox.warning(self, u"Hata!: Bağlantı Başarısız", u"İnternet bağlantınızın olmadığı algılandı. Lütfen internet bağlantılarınızı kontrol ediniz. ve uygulamayı yeniden başlatınız")  
            netWorkConnectValue.pop()
            netWorkConnectValue.append("0")
            sys.exit()
         	
            
    

 
    def installDesktop(self):
	  
	 
	  desktopValue = self.comboBox.currentIndex()
	  
	  
	  if desktopValue == 1 :
		self.labelAlt.show()
		self.animasyon.show()
		self.labelAlt.setText(u"Bilgiler alnıyor")
		self.labelAlt.setText(u"Kde Masaüstü ortamı yükleniyor")
		kdekomut = os.system("sudo apdt-get install kde-full -y")
		kdekomut2 = os.system("sudo apt-get update")
		
		if kdekomut == 0 and kdekomut2 == 0:
		  
		  a = QtGui.QMessageBox()
		  a.setWindowTitle(u"Kde Masaüstü Ortamı Kuruldu")
		  a.setText(u"Kde Masaüstü Ortamı Kuruldu! \n Lütfen bilgisayarınızı yeniden başlatınız.")
		  a.setIcon(a.Warning)
		  yeniden = a.addButton(u"Yeniden başlat",a.AcceptRole)
		  dahasonra = a.addButton(u"Daha sonra başlat",a.DestructiveRole)
		  b = QtGui.QIcon(":/icons/padi.png")
		  a.setWindowIcon(b)
		  a.exec_()		  
		  if a.clickedButton() == yeniden:
			os.system("sudo reboot")
		  
		  elif kdekomut == 256 and kdekomut2 == 256:			
			
			a = QtGui.QMessageBox()
			a.setWindowTitle(u"Hata Oluştu")
			a.setText(u"Kde Masaüstü Ortamı Hata! \n Masaüstü ortamı  kurulurken hata ile karşılaşıldı.Bu sorunun devam etmesi  durumunda geliştirici ile irtibata geçiniz.")
			a.setIcon(a.Warning)
			tamam = a.addButton(u"Tamam",a.DestructiveRole)			
			b = QtGui.QIcon(":/icons/padi.png")
			a.setWindowIcon(b)
			a.exec_()
			if a.clickedButton() == tamam:
			  sys.exit()
		  		    

			
			
			
	  if desktopValue == 2 :
		self.labelAlt.show()
		self.animasyon.show()
		self.labelAlt.setText(u"Bilgiler alnıyor")
		self.labelAlt.setText(u"Gnome Masaüstü ortamı yükleniyor")
		gnomekomut = os.system("sudo apt-get install gnome-shell -y")
		gnomekomut2 = os.system("sudo apt-get update")
		
		
		if gnomekomut == 0 and gnomekomut2 == 0:
		  a = QtGui.QMessageBox()
		  a.setWindowTitle(u"Gnome Masaüstü Ortamı Kuruldu")
		  a.setText(u"Gnome Masaüstü Ortamı Kuruldu! \n Lütfen bilgisayarınızı yeniden başlatınız.")
		  a.setIcon(a.Warning)
		  yeniden = a.addButton(u"Yeniden başlat",a.AcceptRole)
		  dahasonra = a.addButton(u"Daha sonra başlat",a.DestructiveRole)
		  b = QtGui.QIcon(":/icons/padi.png")
		  a.setWindowIcon(b)
		  a.exec_()		  
		  if a.clickedButton() == yeniden:
			os.system("sudo reboot")
		  
		  elif gnomekomut == 256 and gnomekomut2 == 256:			
			
			a = QtGui.QMessageBox()
			a.setWindowTitle(u"Hata Oluştu")
			a.setText(u"Gnome Masaüstü Ortamı Hata! \n Masaüstü ortamı  kurulurken hata ile karşılaşıldı.Bu sorunun devam etmesi  durumunda geliştirici ile irtibata geçiniz.")
			a.setIcon(a.Warning)
			tamam = a.addButton(u"Tamam",a.DestructiveRole)			
			b = QtGui.QIcon(":/icons/padi.png")
			a.setWindowIcon(b)
			a.exec_()
			if a.clickedButton() == tamam:
			  sys.exit()
		  		    
		  

		  
		  
	  if desktopValue == 3 :
		self.labelAlt.show()
		self.animasyon.show()
		self.labelAlt.setText(u"Bilgiler alnıyor")
		self.labelAlt.setText(u"Xfce Masaüstü ortamı yükleniyor")
		xfcekomut = os.system("sudo apt-get install xfce4 -y")
		xfcekomut2 = os.system("sudo apt-get update")
		
		
		if xfcekomut == 0 and xfcekomut2 == 0:
		  a = QtGui.QMessageBox()
		  a.setWindowTitle(u"Xfce Masaüstü Ortamı Kuruldu")
		  a.setText(u"Xfce Masaüstü Ortamı Kuruldu! \n Lütfen bilgisayarınızı yeniden başlatınız.")
		  a.setIcon(a.Warning)
		  yeniden = a.addButton(u"Yeniden başlat",a.AcceptRole)
		  dahasonra = a.addButton(u"Daha sonra başlat",a.DestructiveRole)
		  b = QtGui.QIcon(":/icons/padi.png")
		  a.setWindowIcon(b)
		  a.exec_()		  
		  if a.clickedButton() == yeniden:
			os.system("sudo reboot")
		  
		  elif xfcekomut == 256 and xfcekomut2 == 256:			
			
			a = QtGui.QMessageBox()
			a.setWindowTitle(u"Hata Oluştu")
			a.setText(u"Xfce Masaüstü Ortamı Hata! \n Masaüstü ortamı  kurulurken hata ile karşılaşıldı.Bu sorunun devam etmesi  durumunda geliştirici ile irtibata geçiniz.")
			a.setIcon(a.Warning)
			tamam = a.addButton(u"Tamam",a.DestructiveRole)			
			b = QtGui.QIcon(":/icons/padi.png")
			a.setWindowIcon(b)
			a.exec_()
		  		  
			if a.clickedButton() == tamam:
			  sys.exit()
		  		    
			

			
	  if desktopValue == 4 :
		self.labelAlt.show()
		self.animasyon.show()
		self.labelAlt.setText(u"Bilgiler alnıyor")
		self.labelAlt.setText(u"Lxde Masaüstü ortamı yükleniyor")
		lxdekomut = os.system("sudo apt-get install lxde -y")
		lxdekomut2 = os.system("sudo apt-get update")
		
		
		if lxdekomut == 0 and lxdekomut2 == 0:
		  a = QtGui.QMessageBox()
		  a.setWindowTitle(u"Lxde Masaüstü Ortamı Kuruldu")
		  a.setText(u"Lxde Masaüstü Ortamı Kuruldu! \n Lütfen bilgisayarınızı yeniden başlatınız.")
		  a.setIcon(a.Warning)
		  yeniden = a.addButton(u"Yeniden başlat",a.AcceptRole)
		  dahasonra = a.addButton(u"Daha sonra başlat",a.DestructiveRole)
		  b = QtGui.QIcon(":/icons/padi.png")
		  a.setWindowIcon(b)
		  a.exec_()		  
		  if a.clickedButton() == yeniden:
			os.system("sudo reboot")
		  
		  elif lxdekomut == 256 and lxdekomut2 == 256:			
			
			a = QtGui.QMessageBox()
			a.setWindowTitle(u"Hata Oluştu")
			a.setText(u"Lxde Masaüstü Ortamı Hata! \n Masaüstü ortamı  kurulurken hata ile karşılaşıldı.Bu sorunun devam etmesi durumunda geliştirici ile irtibata geçiniz.")
			a.setIcon(a.Warning)
			tamam = a.addButton(u"Tamam",a.DestructiveRole)			
			b = QtGui.QIcon(":/icons/padi.png")
			a.setWindowIcon(b)
			a.exec_()
			if a.clickedButton() == tamam:
			  sys.exit()
		  		    
		  		  
	  

			
	  if desktopValue == 5 :
		self.labelAlt.show()
		self.animasyon.show()
		self.labelAlt.setText(u"Bilgiler alnıyor")
		self.labelAlt.setText(u"Mate Masaüstü ortamı yükleniyor")
		matekomut = os.system("sudo add-apt-repository 'deb http://repo.mate-desktop.org/debian wheezy main' -y")
		matekomut2 = os.system("sudo apt-get update")
		matekomut3 = os.system("sudo apt-get install mate-archive-keyring -y")
		matekomut4 = os.system("sudo apt-get update")
		matekomut5 = os.system("sudo apt-get install mate-core -y")
		matekomut6 = os.system("sudo apt-get install mate-desktop-environment -y")
		
		
		if matekomut == 0 and matekomut6 == 0:
		  a = QtGui.QMessageBox()
		  a.setWindowTitle(u"Mate Masaüstü Ortamı Kuruldu")
		  a.setText(u"Mate Masaüstü Ortamı Kuruldu! \n Lütfen bilgisayarınızı yeniden başlatınız.")
		  a.setIcon(a.Warning)
		  yeniden = a.addButton(u"Yeniden başlat",a.AcceptRole)
		  dahasonra = a.addButton(u"Daha sonra başlat",a.DestructiveRole)
		  b = QtGui.QIcon(":/icons/padi.png")
		  a.setWindowIcon(b)
		  a.exec_()		  
		  if a.clickedButton() == yeniden:
			os.system("sudo reboot")
		  
		  elif matekomut == 256 and matekomut6 == 256:			
			
			a = QtGui.QMessageBox()
			a.setWindowTitle(u"Hata Oluştu")
			a.setText(u"Mate Masaüstü Ortamı Hata! \n Masaüstü ortamı  kurulurken hata ile karşılaşıldı.Bu sorunun devam etmesi  durumunda geliştirici ile irtibata geçiniz.")
			a.setIcon(a.Warning)
			tamam = a.addButton(u"Tamam",a.DestructiveRole)			
			b = QtGui.QIcon(":/icons/padi.png")
			a.setWindowIcon(b)
			a.exec_()
			
			if a.clickedButton() == tamam:
			  sys.exit()
		  		    
        

			
	  if desktopValue == 6:
		self.labelAlt.show()
		self.animasyon.show()
		self.labelAlt.setText(u"Bilgiler alnıyor")
		self.labelAlt.setText(u"Cinnamon Masaüstü ortamı yükleniyor")
		cinnamonkomut = os.system("sudo apt-get install cinnamon -y")
		cinnamonkomut3 = os.system("sudo apt-get install cinnamon-themes -y")
		cinnamonkomut2 = os.system("sudo apt-get update")
		
		
		if cinnamonkomut == 0 and cinnamonkomut2 == 0:
		  a = QtGui.QMessageBox()
		  a.setWindowTitle(u"Cinnamon Masaüstü Ortamı Kuruldu")
		  a.setText(u"Cinnamon Masaüstü Ortamı Kuruldu! \n Lütfen bilgisayarınızı yeniden başlatınız.")
		  a.setIcon(a.Warning)
		  yeniden = a.addButton(u"Yeniden başlat",a.AcceptRole)
		  dahasonra = a.addButton(u"Daha sonra başlat",a.DestructiveRole)
		  b = QtGui.QIcon(":/icons/padi.png")
		  a.setWindowIcon(b)
		  a.exec_()		  
		  if a.clickedButton() == yeniden:
			os.system("sudo reboot")
		  
		  elif cinnamonkomut == 256 and cinnamonkomut2 == 256:			
			
			a = QtGui.QMessageBox()
			a.setWindowTitle(u"Hata Oluştu")
			a.setText(u"Cinnamon Masaüstü Ortamı Hata! \n Masaüstü ortamı  kurulurken hata ile karşılaşıldı.Bu sorunun devam etmesi  durumunda geliştirici ile irtibata geçiniz.")
			a.setIcon(a.Warning)
			tamam = a.addButton(u"Tamam",a.AcceptRole)			
			b = QtGui.QIcon(":/icons/padi.png")
			a.setWindowIcon(b)
			a.exec_()
			
			if a.clickedButton() == tamam:
			  sys.exit()
		 
		  		  
	  if desktopValue == 7:
		self.labelAlt.show()
		self.animasyon.show()
		self.labelAlt.setText(u"Bilgiler alnıyor")
		self.labelAlt.setText(u"FluxBox Masaüstü ortamı yükleniyor")
		fluxboxkomut = os.system("sudo apt-get install fluxbox -y")		
		fluxboxkomut2 = os.system("sudo apt-get update")
		
		
		if fluxboxkomut == 0 and fluxboxkomut2 == 0:
		  a = QtGui.QMessageBox()
		  a.setWindowTitle(u"FluxBox Masaüstü Ortamı Kuruldu")
		  a.setText(u"FluxBox Masaüstü Ortamı Kuruldu! \n Lütfen bilgisayarınızı yeniden başlatınız.")
		  a.setIcon(a.Warning)
		  yeniden = a.addButton(u"Yeniden başlat",a.AcceptRole)
		  dahasonra = a.addButton(u"Daha sonra başlat",a.DestructiveRole)
		  b = QtGui.QIcon(":/icons/padi.png")
		  a.setWindowIcon(b)
		  a.exec_()		  
		  if a.clickedButton() == yeniden:
			os.system("sudo reboot")
		  
		  elif fluxboxkomut == 256 and fluxboxkomut2 == 256:			
			
			a = QtGui.QMessageBox()
			a.setWindowTitle(u"Hata Oluştu")
			a.setText(u"FluxBox Masaüstü Ortamı Hata! \n Masaüstü ortamı  kurulurken hata ile karşılaşıldı.Bu sorunun devam etmesi durumunda geliştirici ile irtibata geçiniz.")
			a.setIcon(a.Warning)
			tamam = a.addButton(u"Tamam",a.AcceptRole)			
			b = QtGui.QIcon(":/icons/padi.png")
			a.setWindowIcon(b)
			a.exec_()
			
			if a.clickedButton() == tamam:
			  sys.exit()
		  
	         
            
        
       
       
        

        
    def widgetShow(self):
        self.animasyon.hide()
        self.labelAlt.setText(u"Yeni Masaüstü Hazır! ")
        self.statusLabel.setText(u"Masaüstü Hazır!")
        self.screenLabel.setText(u"Bitti!")    
        self.statusProgLabel.setPixmap(QtGui.QPixmap(":/icons/dialog-ok-apply.png"))       


        self.buttonGeri.hide()     
		
        
				
    def checkIndex(self):
        Sayfalar.check(self)
        

    def indexNext(self):
        self.index = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.index+1)
        self.checkIndex()
        self.internetControl()
        

    def indexBack(self):
        self.downloadButton.show()
        self.index = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.index-1)
        self.checkIndex()
        self.buttonIleri.setEnabled(True)
        
    def EkranOrtala(self):
      screen = QtGui.QDesktopWidget().screenGeometry()
      size =  self.geometry()
      self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

def main():
    app = QtGui.QApplication(sys.argv) 
    ek = MainWindow()
    ek.EkranOrtala()
    ek.show() 
    return app.exec_()
 
if __name__ == "__main__":
    main()
