import sys

from home_ui import Ui_menu
from PyQt5.QtWidgets import *
from kitapeklef import KitapEkleEkrani
import veritabani_06 as baglanti

class AnaEkran(QMainWindow,Ui_menu):
    def __init__(self,k_id):
        super().__init__()
        self.k_id=k_id
        self.karsilama()

    def karsilama(self):
        self.setupUi(self)
        self.actioneklemek.triggered.connect(self.kitap_ekle)
        self.actionsil.triggered.connect(self.kitap_silme)
        self.actionguncelle.triggered.connect(self.kitap_guncelle)
        self.actionlistele.triggered.connect(self.kitap_listele)
        self.tableWidget


    def kitap_ekle(self):
        print("kitap ekle tıklandı")
        self.setCentralWidget(KitapEkleEkrani(self.k_id))

    def kitap_listele(self):
       print("kitap liste tıklandı")
       kitaplar=baglanti.listele(self.k_id)
       satir_sayisi=len(kitaplar)
       self.tableWidget.setRowCount(satir_sayisi)
       k=0
       for a in kitaplar:
           self.tableWidget.setItem(k, 0, QTableWidgetItem(str(a[0])))
           self.tableWidget.setItem(k, 1, QTableWidgetItem(str(a[1])))
           self.tableWidget.setItem(k, 2, QTableWidgetItem(str(a[2])))
           self.tableWidget.setItem(k, 3, QTableWidgetItem(str(a[3])))
           k+=1

       self.karsilama()
    def kitap_silme(self):
        print("kitap silme tıklandı")
    def kitap_guncelle(self):
        print("kitap güncelleme tıklandı")



if __name__=="__main__":
    app= QApplication(sys.argv)
    pencere=AnaEkran()
    pencere.show()
    sys.exit((app.exec_()))