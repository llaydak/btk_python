# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'girisyap.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_girisw(object):
    def setupUi(self, girisw):
        girisw.setObjectName("girisw")
        girisw.resize(574, 476)
        self.mailt = QtWidgets.QLineEdit(girisw)
        self.mailt.setGeometry(QtCore.QRect(230, 90, 113, 22))
        self.mailt.setObjectName("mailt")
        self.passt = QtWidgets.QLineEdit(girisw)
        self.passt.setGeometry(QtCore.QRect(230, 140, 113, 22))
        self.passt.setObjectName("passt")
        self.mailtext = QtWidgets.QLabel(girisw)
        self.mailtext.setGeometry(QtCore.QRect(110, 90, 55, 16))
        self.mailtext.setObjectName("mailtext")
        self.passtext = QtWidgets.QLabel(girisw)
        self.passtext.setGeometry(QtCore.QRect(110, 140, 55, 16))
        self.passtext.setObjectName("passtext")
        self.text = QtWidgets.QLabel(girisw)
        self.text.setGeometry(QtCore.QRect(110, 270, 331, 16))
        self.text.setObjectName("text")
        self.girisbutonu = QtWidgets.QPushButton(girisw)
        self.girisbutonu.setGeometry(QtCore.QRect(230, 210, 93, 28))
        self.girisbutonu.setObjectName("girisbutonu")

        self.retranslateUi(girisw)
        QtCore.QMetaObject.connectSlotsByName(girisw)

    def retranslateUi(self, girisw):
        _translate = QtCore.QCoreApplication.translate
        girisw.setWindowTitle(_translate("girisw", "Form"))
        self.mailtext.setText(_translate("girisw", "E-posta:"))
        self.passtext.setText(_translate("girisw", "Şifre:"))
        self.text.setText(_translate("girisw", "Mesaj:"))
        self.girisbutonu.setText(_translate("girisw", "Giriş"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    girisw = QtWidgets.QWidget()
    ui = Ui_girisw()
    ui.setupUi(girisw)
    girisw.show()
    sys.exit(app.exec_())