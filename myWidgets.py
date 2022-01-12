from PyQt6 import QtWidgets,QtCore
from ui_ReserveForm import Ui_ReserveForm
import datetime
import json
from jsonpath_ng.ext import parse
from encryptUserInfo import myEncrypt,readPubKey
import base64
from ftplib import FTP       
import os.path   
import new_yuyue_client

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
    @QtCore.pyqtSlot()
    def on_tbXueHao_textChanged(self):
        self.__dataSet['xuehao'] = self.ui.tbXueHao.toPlainText()
    
    @QtCore.pyqtSlot()
    def on_tbEmail_textChanged(self):
        self.__dataSet['email'] = self.ui.tbEmail.toPlainText()

    @QtCore.pyqtSlot()
    def on_tbPassword_textChanged(self):
        self.__dataSet['password'] = self.ui.tbPassword.toPlainText()

    @QtCore.pyqtSlot()
    def on_deReserveDate_userDateChanged(self,qDate):
        self.__dataSet['reserveDate'] = qDate.toPyDate().strftime('%Y-%m-%d')

    @QtCore.pyqtSlot()
    def on_teReserveTime_userTimeChanged(self,qTime):
        self.__dataSet['reserveTime'] = qTime.toPyTime().strftime('%H:%M')

    @QtCore.pyqtSlot()
    def on_btnLogin_clicked(self):
        if (self.__dataSet['xuehao']) and (self.__dataSet['password']):
            raw_json =  new_yuyue_client.login(self.__dataSet['xuehao'],self.__dataSet['password'])
            if(raw_json):
                self.__infoJson = raw_json
            # with open('预约关键.json',mode='r',encoding='utf-8') as f:
            #     self.__infoJson = json.loads(f.read())
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

    @QtCore.pyqtSlot()
    def on_btnConfirm_clicked(self):
        # 弹出确认框
        dialogStrInfo = '真的要创建预约任务吗？'
        defaultBtn = QtWidgets.QMessageBox.StandardButton.Yes
        result = QtWidgets.QMessageBox.question(self,'',dialogStrInfo,QtWidgets.QMessageBox.StandardButton.No|defaultBtn)

        if(result==QtWidgets.QMessageBox.StandardButton.Yes):
            # 加密用户信息并保存到本地
            pub_key = readPubKey('./yun_public.pub')
            encryptedUserInfo = myEncrypt(str(self.__dataSet),public_key=pub_key)
            with open('userInfo.txt','wb') as f:
                cipher_text_encoded = [base64.b64encode(i)+'\n'.encode() for i in encryptedUserInfo]
                f.writelines(cipher_text_encoded)

            # 将加密文件上传到 ftp 服务器
            host = '39.105.232.211'       
            port = 21              
            timenout = 30                
            u = 'ZnRwdXNlcg=='           
            p = 'MTIzNDU2'          
            localfile = './userInfo.txt'   #本机要上传的文件与路径
            # remotepath = '/var/run/vsftpd/AutoReserver'  
            f = FTP()
            f.connect(host,port,timenout)  
            f.login(base64.b64decode(u).decode(),base64.b64decode(p).decode())     
            print(f.pwd())
            file = open(localfile,'rb')    
            f.storbinary('STOR %s' % os.path.basename(localfile),file)  #上传文件到ftp服务器
            file.close()   #关闭本地文件
            f.quit()       #退出
        else:
            pass
        

#
# TODO: 
#   1.点击确定按钮后要弹出确认框 Done
#   2.确认后把用户输入信息加密并保存到本地 Done
#   
#   3.连接服务器，上传加密后的用户信息 Done
#   4.完善运行信息框，显示软件运行情况
#        
