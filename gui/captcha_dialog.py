# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/captcha_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaptchaRequest(object):
    def setupUi(self, CaptchaRequest):
        CaptchaRequest.setObjectName("CaptchaRequest")
        CaptchaRequest.setWindowModality(QtCore.Qt.WindowModal)
        CaptchaRequest.resize(178, 155)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CaptchaRequest.sizePolicy().hasHeightForWidth())
        CaptchaRequest.setSizePolicy(sizePolicy)
        CaptchaRequest.setModal(True)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(CaptchaRequest)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(CaptchaRequest)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.imageLabel = QtWidgets.QLabel(CaptchaRequest)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout_4.addWidget(self.imageLabel)
        self.captchaKey = QtWidgets.QLineEdit(CaptchaRequest)
        self.captchaKey.setObjectName("captchaKey")
        self.verticalLayout_4.addWidget(self.captchaKey)
        self.catpchaButton = QtWidgets.QPushButton(CaptchaRequest)
        self.catpchaButton.setObjectName("catpchaButton")
        self.verticalLayout_4.addWidget(self.catpchaButton)

        self.retranslateUi(CaptchaRequest)
        self.catpchaButton.pressed.connect(CaptchaRequest.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(CaptchaRequest)

    def retranslateUi(self, CaptchaRequest):
        _translate = QtCore.QCoreApplication.translate
        CaptchaRequest.setWindowTitle(_translate("CaptchaRequest", "Запрос капчи"))
        self.label.setText(_translate("CaptchaRequest", "Введите код из капчи"))
        self.imageLabel.setText(_translate("CaptchaRequest", "изображение"))
        self.catpchaButton.setText(_translate("CaptchaRequest", "Отправить"))
