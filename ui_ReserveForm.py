# Form implementation generated from reading ui file './FirstQtProject/reserveForm.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ReserveForm(object):
    def setupUi(self, ReserveForm):
        ReserveForm.setObjectName("ReserveForm")
        ReserveForm.resize(580, 242)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ReserveForm.sizePolicy().hasHeightForWidth())
        ReserveForm.setSizePolicy(sizePolicy)
        self.groupBox = QtWidgets.QGroupBox(ReserveForm)
        self.groupBox.setGeometry(QtCore.QRect(9, 10, 281, 221))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tbXueHao = QtWidgets.QTextEdit(self.groupBox)
        self.tbXueHao.setGeometry(QtCore.QRect(70, 10, 211, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbXueHao.sizePolicy().hasHeightForWidth())
        self.tbXueHao.setSizePolicy(sizePolicy)
        self.tbXueHao.setPlaceholderText("")
        self.tbXueHao.setObjectName("tbXueHao")
        self.tbPassword = QtWidgets.QTextEdit(self.groupBox)
        self.tbPassword.setGeometry(QtCore.QRect(70, 40, 121, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbPassword.sizePolicy().hasHeightForWidth())
        self.tbPassword.setSizePolicy(sizePolicy)
        self.tbPassword.setObjectName("tbPassword")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 15, 58, 16))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 45, 58, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 75, 58, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 105, 58, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 135, 58, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 165, 58, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 195, 58, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.deReserveDate = QtWidgets.QDateEdit(self.groupBox)
        self.deReserveDate.setGeometry(QtCore.QRect(70, 70, 211, 24))
        self.deReserveDate.setDate(QtCore.QDate(2022, 1, 1))
        self.deReserveDate.setObjectName("deReserveDate")
        self.teReserveTime = QtWidgets.QTimeEdit(self.groupBox)
        self.teReserveTime.setGeometry(QtCore.QRect(70, 100, 211, 24))
        self.teReserveTime.setTime(QtCore.QTime(7, 0, 0))
        self.teReserveTime.setObjectName("teReserveTime")
        self.cbbHall = QtWidgets.QComboBox(self.groupBox)
        self.cbbHall.setGeometry(QtCore.QRect(70, 130, 211, 24))
        self.cbbHall.setObjectName("cbbHall")
        self.cbbPlayTime = QtWidgets.QComboBox(self.groupBox)
        self.cbbPlayTime.setGeometry(QtCore.QRect(70, 160, 211, 24))
        self.cbbPlayTime.setObjectName("cbbPlayTime")
        self.cbbFieldNum = QtWidgets.QComboBox(self.groupBox)
        self.cbbFieldNum.setGeometry(QtCore.QRect(70, 190, 211, 24))
        self.cbbFieldNum.setObjectName("cbbFieldNum")
        self.btnLogin = QtWidgets.QPushButton(self.groupBox)
        self.btnLogin.setGeometry(QtCore.QRect(200, 40, 80, 28))
        self.btnLogin.setObjectName("btnLogin")
        self.groupBox_2 = QtWidgets.QGroupBox(ReserveForm)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 10, 280, 221))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tbEmail = QtWidgets.QTextEdit(self.groupBox_2)
        self.tbEmail.setGeometry(QtCore.QRect(40, 143, 231, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbEmail.sizePolicy().hasHeightForWidth())
        self.tbEmail.setSizePolicy(sizePolicy)
        self.tbEmail.setObjectName("tbEmail")
        self.runInfo = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.runInfo.setGeometry(QtCore.QRect(10, 10, 261, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runInfo.sizePolicy().hasHeightForWidth())
        self.runInfo.setSizePolicy(sizePolicy)
        self.runInfo.setObjectName("runInfo")
        self.btnConfirm = QtWidgets.QPushButton(self.groupBox_2)
        self.btnConfirm.setGeometry(QtCore.QRect(10, 173, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.btnConfirm.setFont(font)
        self.btnConfirm.setAutoFillBackground(False)
        self.btnConfirm.setFlat(False)
        self.btnConfirm.setObjectName("btnConfirm")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 150, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(ReserveForm)
        QtCore.QMetaObject.connectSlotsByName(ReserveForm)

    def retranslateUi(self, ReserveForm):
        _translate = QtCore.QCoreApplication.translate
        ReserveForm.setWindowTitle(_translate("ReserveForm", "AutoReserver"))
        self.label.setText(_translate("ReserveForm", "学号"))
        self.label_2.setText(_translate("ReserveForm", "密码"))
        self.label_3.setText(_translate("ReserveForm", "开抢日期"))
        self.label_4.setText(_translate("ReserveForm", "开抢时间"))
        self.label_5.setText(_translate("ReserveForm", "场馆"))
        self.label_6.setText(_translate("ReserveForm", "打球时间"))
        self.label_7.setText(_translate("ReserveForm", "场地号码"))
        self.deReserveDate.setDisplayFormat(_translate("ReserveForm", "yyyy-MM-dd"))
        self.btnLogin.setText(_translate("ReserveForm", "登录"))
        self.btnConfirm.setText(_translate("ReserveForm", "创建预约"))
        self.label_8.setText(_translate("ReserveForm", "邮件"))