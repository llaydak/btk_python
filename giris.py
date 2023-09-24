import sys
from PyQt5.QtWidgets import *
from giris_ui import Ui_girisw
from home import AnaEkran
import veritabani_06 as baglanti


class GirisPenceresi(QWidget, Ui_girisw):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.girisbutonu.clicked.connect(self.fGirisKontrol)
        #şifreyi ***** şeklinde gizli göstermek için
        #self.passt.EchoMode

    def fGirisKontrol(self):
        self.text.setText("Giriş butonu tıklandı.")
        # bolum2
        eposta = self.mailt.text()
        sifre = self.passt.text()
        k_id=baglanti.k_giris(eposta,sifre)
        if k_id==0:
            elf.text.setText("Hatalı giriş yapıldı.")
        else:
            self.text.setText("Giriş onaylandı.")
            self.close()
            self.ype=AnaEkran(k_id)
            self.ype.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = GirisPenceresi()
    pencere.show()
    sys.exit(app.exec_())
