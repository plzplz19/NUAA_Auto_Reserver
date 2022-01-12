from PyQt6 import QtWidgets,QtCore
from ui_ReserveForm import Ui_ReserveForm
import datetime
import json
from jsonpath_ng.ext import parse
from encryptUserInfo import myEncrypt,readPubKey
import base64

class QmyReserveForm(QtWidgets.QWidget):
    
    # 保存用户输入信息
    __dataSet = {
        'xuehao':'',
        'password':'',
        'reserveDate':'',
        'reserveTime':'',
        'hall':'',
        'playTime':'',
        'fieldNum':'',
        'email':'',
    }

    # 场地信息
    __infoJson = None

    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_ReserveForm()
        self.ui.setupUi(self)

        # 设置默认开抢日期为明天
        date_str = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        qdate = QtCore.QDate.fromString(date_str, "yyyy-MM-dd")
        self.ui.deReserveDate.setDate(qdate)
        self.__dataSet['reserveDate'] = date_str

        # 默认开抢时间是 7:00
        self.__dataSet['reserveTime'] = '07:00'

    # 事件处理函数们
    def on_tbXueHao_textChanged(self):
        self.__dataSet['xuehao'] = self.ui.tbXueHao.toPlainText()
    
    def on_tbEmail_textChanged(self):
        self.__dataSet['email'] = self.ui.tbEmail.toPlainText()

    def on_tbPassword_textChanged(self):
        self.__dataSet['password'] = self.ui.tbPassword.toPlainText()

    def on_deReserveDate_userDateChanged(self,qDate):
        self.__dataSet['reserveDate'] = qDate.toPyDate().strftime('%Y-%m-%d')

    def on_teReserveTime_userTimeChanged(self,qTime):
        self.__dataSet['reserveTime'] = qTime.toPyTime().strftime('%H:%M')

    def on_btnLogin_clicked(self):
        if (self.__dataSet['xuehao']) and (self.__dataSet['password']):
            with open('预约关键.json',mode='r',encoding='utf-8') as f:
                self.__infoJson = json.loads(f.read())
            hallArr_expr = parse('$..list[*].name')
            hallArr = [i.value for i in hallArr_expr.find(self.__infoJson)]
            self.ui.cbbHall.clear()
            self.ui.cbbHall.addItems(hallArr)

    @QtCore.pyqtSlot(str)
    def on_cbbHall_currentTextChanged(self,qString):
        self.__dataSet['hall'] = str(qString)

        # 切换场馆后，也要更新可供选择的号码和时间
        # 更新可以选择的时间
        playTime_expr = parse('$..list[?(@.name=="{}")].table.*[*].yaxis'.format(self.__dataSet['hall']))
        playTimeArr = [i.value for i in playTime_expr.find(self.__infoJson)]
        tempPlayTimeArr = []
        [tempPlayTimeArr.append(i) for i in playTimeArr if not i in tempPlayTimeArr]
        playTimeArr = tempPlayTimeArr
        self.ui.cbbPlayTime.clear()
        self.ui.cbbPlayTime.addItems(playTimeArr)

        # 更新可以选择的场地号码
        fieldNum_expr = parse('$..list[?(@.name=="{}")].table.*[*].abscissa'.format(self.__dataSet['hall']))
        fieldNumArr = [i.value for i in fieldNum_expr.find(self.__infoJson)]
        tempFieldNumArr = []
        [tempFieldNumArr.append(i) for i in fieldNumArr if not i in tempFieldNumArr]
        fieldNumArr = tempFieldNumArr
        self.ui.cbbFieldNum.clear()
        self.ui.cbbFieldNum.addItems(fieldNumArr)

    @QtCore.pyqtSlot(str)
    def on_cbbPlayTime_currentTextChanged(self,qString):
        self.__dataSet['playTime'] = str(qString)

    @QtCore.pyqtSlot(str)
    def on_cbbFieldNum_currentTextChanged(self,qString):
        self.__dataSet['fieldNum'] = str(qString)
    
    def on_btnConfirm_clicked(self):
        pub_key = readPubKey('./yun_public.pub')
        encryptedUserInfo = myEncrypt(str(self.__dataSet),public_key=pub_key)

        with open('userInfo.txt','wb') as f:
            cipher_text_encoded = [base64.b64encode(i)+'\n'.encode() for i in encryptedUserInfo]
            f.writelines(cipher_text_encoded)

#
# TODO: 
#   1.点击确定按钮后要弹出确认框
#   2.确认后把用户输入信息加密并保存到本地
#   
#   3～4 在 shell 脚本完成
#   3.连接服务器，上传加密后的用户信息
#   4.创建定时任务
#   
#   5.完善运行信息框，显示软件运行情况
#        
