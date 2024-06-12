import threading
import win32api
import webbrowser
from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
import sys

import speech_recognition as sr


class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.myThread = None

    def showEvent(self, e):
        print("窗口显示")
        try:
            self.myThread = MyThread()
            self.myThread.start()
        except:
            print("thread start failed")

    def closeEvent(self, e):
        self.myThread.stop()
        print("closed")


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
        self._running = True

    def stop(self):
        self._running = False
        print(self._running)

    def runasrbot(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        asrbot=asrbot()
        asrbot.run()
        
            


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()
    sys.exit(app.exec())
