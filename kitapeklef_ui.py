# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kitapeklef.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KitapEkleForm(object):
    def setupUi(self, KitapEkleForm):
        KitapEkleForm.setObjectName("KitapEkleForm")
        KitapEkleForm.resize(826, 661)
        self.formLayoutWidget = QtWidgets.QWidget(KitapEkleForm)
        self.formLayoutWidget.setGeometry(QtCore.QRect(250, 120, 231, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.kitapAdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kitapAdLabel.setObjectName("kitapAdLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.kitapAdLabel)
        self.kitapAdiText = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kitapAdiText.setObjectName("kitapAdiText")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kitapAdiText)
        self.kitapYazarLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kitapYazarLabel.setObjectName("kitapYazarLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.kitapYazarLabel)
        self.kitapYazarText = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kitapYazarText.setObjectName("kitapYazarText")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kitapYazarText)
        self.okumaDurumuLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.okumaDurumuLabel.setObjectName("okumaDurumuLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.okumaDurumuLabel)
        self.okumaDurumuText = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.okumaDurumuText.setObjectName("okumaDurumuText")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.okumaDurumuText)
        self.begeniLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.begeniLabel.setObjectName("begeniLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.begeniLabel)
        self.begeniText = QtWidgets.QComboBox(self.formLayoutWidget)
        self.begeniText.setObjectName("begeniText")
        self.begeniText.addItem("")
        self.begeniText.addItem("")
        self.begeniText.addItem("")
        self.begeniText.addItem("")
        self.begeniText.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.begeniText)
        self.kayitlabel = QtWidgets.QLabel(KitapEkleForm)
        self.kayitlabel.setGeometry(QtCore.QRect(250, 330, 151, 16))
        self.kayitlabel.setObjectName("kayitlabel")
        self.kayitbuton = QtWidgets.QPushButton(KitapEkleForm)
        self.kayitbuton.setGeometry(QtCore.QRect(252, 380, 231, 28))
        self.kayitbuton.setObjectName("kayitbuton")

        self.retranslateUi(KitapEkleForm)
        QtCore.QMetaObject.connectSlotsByName(KitapEkleForm)

    def retranslateUi(self, KitapEkleForm):
        _translate = QtCore.QCoreApplication.translate
        KitapEkleForm.setWindowTitle(_translate("KitapEkleForm", "Form"))
        self.kitapAdLabel.setText(_translate("KitapEkleForm", "Kitap Adı"))
        self.kitapYazarLabel.setText(_translate("KitapEkleForm", "Kitap Yazarı"))
        self.okumaDurumuLabel.setText(_translate("KitapEkleForm", "Okuma Durumu"))
        self.begeniLabel.setText(_translate("KitapEkleForm", "Beğeni Durumu"))
        self.begeniText.setItemText(0, _translate("KitapEkleForm", "*"))
        self.begeniText.setItemText(1, _translate("KitapEkleForm", "**"))
        self.begeniText.setItemText(2, _translate("KitapEkleForm", "***"))
        self.begeniText.setItemText(3, _translate("KitapEkleForm", "****"))
        self.begeniText.setItemText(4, _translate("KitapEkleForm", "*****"))
        self.kayitlabel.setText(_translate("KitapEkleForm", "Kayıt Durumu"))
        self.kayitbuton.setText(_translate("KitapEkleForm", "Kitap Kaydet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KitapEkleForm = QtWidgets.QWidget()
    ui = Ui_KitapEkleForm()
    ui.setupUi(KitapEkleForm)
    KitapEkleForm.show()
    sys.exit(app.exec_())
