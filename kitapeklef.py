import sys
from PyQt5.QtWidgets import *
from kitapeklef_ui import Ui_KitapEkleForm
import veritabani_06 as baglanti

class KitapEkleEkrani(QWidget, Ui_KitapEkleForm):
    def __init__(self,k_id):
        super().__init__()
        self.k_id=k_id
        self.setupUi(self)
        self.kayitbuton.clicked.connect(self.kitap_ekle)
        #self.begeniText.addItem("6")
    def kitap_ekle(self):
        k_adi=self.kitapAdiText.text()
        k_yazari=self.kitapYazarText.text()
        k_durum=self.okumaDurumuText.checkState()
        k_begeni=self.begeniText.currentText()
        sonuc=baglanti.ekle(k_adi,k_yazari,k_durum,k_begeni,self.k_id)

if __name__== "__main__":
    app = QApplication(sys.argv)
    pencere= KitapEkleEkrani(1)
    pencere.show()
    sys.exit(app.exec_())