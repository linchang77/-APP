import threading
import logging
from PyQt5 import QtWidgets
from asrbot import asrbot
import threading
from chatbot import WenxinYiyanChatBot , get_file_modification_time
import time
from asrInterface import Ui_MainWindow
import sys
import speech_recognition as sr
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

chatsettings="你是一个语音聊天助手,下面你将会开始和我聊天,你的回答要简短一点,不超过30个字。"

class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chatThread = None
        self.asrThread  = None

    def showEvent(self, e):
        print("窗口显示")
        try:
            self.chatThread=chatThread()
            self.chatThread.start()
            self.asrThread=asrThread()
            self.asrThread.start()
        except:
            print("thread start failed")

    def closeEvent(self, e):
        self.chatThread.stop()
        self.asrThread.stop()
        print("closed")

# 聊天机器人线程
class chatThread(threading.Thread):
    def __init__(self):
        super(chatThread, self).__init__()
        self._running = True

    def stop(self):
        self._running = False
        print(self._running)

    def run(self):
        API_KEY = "s6z1XgjYynPyVJBlR5YZlPux"
        SECRET_KEY = "1hKtL5jwSJdzFg98STHMyIuNFhHjGjE0"
        INPUT_FILE = 'Resource/text/question.txt'
        OUTPUT_FILE = 'Resource/text/response.txt'
        
        chatbot = WenxinYiyanChatBot(API_KEY, SECRET_KEY)
        #给聊天机器人预先加一些设定
        chatbot.get_response(chatsettings)
        last_modification_time = get_file_modification_time(INPUT_FILE)
        
        print("启动文心一言")
        while self._running:
            time.sleep(2)  # 每5秒检测一次
            current_modification_time = get_file_modification_time(INPUT_FILE)
            if current_modification_time != last_modification_time:
                print(f"{INPUT_FILE} 文件已修改，正在处理新的问题...")
                chatbot.read_questions_and_write_responses(INPUT_FILE, OUTPUT_FILE)
                last_modification_time = current_modification_time

#语音识别线程
class asrThread(threading.Thread):
    def __init__(self):
        super(asrThread, self).__init__()
        self._running = True

    def stop(self):
        self._running = False
        print(self._running)

    def run(self):
        print("启动语音识别线程")
        asrbot_instance=asrbot()
        logger.info('running...')
        while self._running:
            asrbot_instance.run()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()
    sys.exit(app.exec())
