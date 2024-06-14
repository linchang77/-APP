from PyQt5 import QtCore, QtGui, QtWidgets

class VoiceSettingsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Voice Settings')
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: white")
        layout = QtWidgets.QVBoxLayout(self)

        # 音色选择
        tone_layout = QtWidgets.QHBoxLayout()
        tone_label = QtWidgets.QLabel("选择音色")
        self.tone_combo = QtWidgets.QComboBox()
        self.tone_combo.addItems(["男(11)", "女(22)", "其他"])
        tone_layout.addWidget(tone_label)
        tone_layout.addWidget(self.tone_combo)
        layout.addLayout(tone_layout)

        # 音色值
        tone_value_layout = QtWidgets.QHBoxLayout()
        tone_value_label = QtWidgets.QLabel("音色值")
        self.tone_value_edit = QtWidgets.QLineEdit()
        tone_value_layout.addWidget(tone_value_label)
        tone_value_layout.addWidget(self.tone_value_edit)
        layout.addLayout(tone_value_layout)

        # 自定义音色种子值
        custom_tone_layout = QtWidgets.QHBoxLayout()
        custom_tone_label = QtWidgets.QLabel("自定义音色种子值，大")
        self.custom_tone_edit = QtWidgets.QLineEdit()
        custom_tone_layout.addWidget(custom_tone_label)
        custom_tone_layout.addWidget(self.custom_tone_edit)
        layout.addLayout(custom_tone_layout)

        # 文本种子
        text_seed_layout = QtWidgets.QHBoxLayout()
        text_seed_label = QtWidgets.QLabel("text seed")
        self.text_seed_edit = QtWidgets.QLineEdit("42")
        text_seed_layout.addWidget(text_seed_label)
        text_seed_layout.addWidget(self.text_seed_edit)
        layout.addLayout(text_seed_layout)

        # Prompt
        prompt_layout = QtWidgets.QHBoxLayout()
        prompt_label = QtWidgets.QLabel("Prompt")
        self.prompt_edit = QtWidgets.QLineEdit()
        prompt_layout.addWidget(prompt_label)
        prompt_layout.addWidget(self.prompt_edit)
        layout.addLayout(prompt_layout)

        # 语速
        speed_layout = QtWidgets.QHBoxLayout()
        speed_label = QtWidgets.QLabel("语速")
        self.speed_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.speed_slider.setRange(1, 10)
        self.speed_slider.setValue(5)
        speed_layout.addWidget(speed_label)
        speed_layout.addWidget(self.speed_slider)
        layout.addLayout(speed_layout)

        # temperature
        temperature_layout = QtWidgets.QHBoxLayout()
        temperature_label = QtWidgets.QLabel("temperature")
        self.temperature_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.temperature_slider.setRange(1, 10)
        self.temperature_slider.setValue(3)
        temperature_layout.addWidget(temperature_label)
        temperature_layout.addWidget(self.temperature_slider)
        layout.addLayout(temperature_layout)

        # top_p
        top_p_layout = QtWidgets.QHBoxLayout()
        top_p_label = QtWidgets.QLabel("top_p")
        self.top_p_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.top_p_slider.setRange(1, 10)
        self.top_p_slider.setValue(7)
        top_p_layout.addWidget(top_p_label)
        top_p_layout.addWidget(self.top_p_slider)
        layout.addLayout(top_p_layout)

        # top_k
        top_k_layout = QtWidgets.QHBoxLayout()
        top_k_label = QtWidgets.QLabel("top_k")
        self.top_k_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.top_k_slider.setRange(1, 20)
        self.top_k_slider.setValue(20)
        top_k_layout.addWidget(top_k_label)
        top_k_layout.addWidget(self.top_k_slider)
        layout.addLayout(top_k_layout)

        # 确认按钮
        buttons_layout = QtWidgets.QHBoxLayout()
        self.ok_button = QtWidgets.QPushButton("确认")
        self.cancel_button = QtWidgets.QPushButton("取消")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)
        layout.addLayout(buttons_layout)

    def getSettings(self):
        return {
            "Tone": self.tone_combo.currentText(),
            "Tone Value": self.tone_value_edit.text(),
            "Custom Tone": self.custom_tone_edit.text(),
            "Text Seed": self.text_seed_edit.text(),
            "Prompt": self.prompt_edit.text(),
            "Speed": self.speed_slider.value(),
            "Temperature": self.temperature_slider.value(),
            "Top P": self.top_p_slider.value(),
            "Top K": self.top_k_slider.value(),
        }

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setGeometry(300, 300, 300, 600)
        MainWindow.setWindowTitle('GIF Switcher')
        MainWindow.setStyleSheet("background-color:rgb(0,0,0)")

        # 创建标签用于显示初始GIF
        self.label_initial = QtWidgets.QLabel(MainWindow)
        self.label_initial.setGeometry(50, 0, 200, 200)  # 绝对定位
        self.initial_gif = QtGui.QMovie('icon/play.gif')
        self.initial_gif.setScaledSize(QtCore.QSize(200, 200))
        self.label_initial.setMovie(self.initial_gif)
        self.initial_gif.start()

        self.text_label = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.text_label.setGeometry(0, 210, 300, 30)
        self.text_label.setWordWrap(True)
        self.text_label.setStyleSheet("color:rgb(200,0,117);")
        self.text_label.setFont(font)
        self.text_label.setObjectName("text")
        self.text_label.setText("    Press the microphone to")

        self.text_Start = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.text_Start.setGeometry(230, 210, 300, 30)
        self.text_Start.setWordWrap(True)
        self.text_Start.setStyleSheet("color:rgb(200,200,0);")
        self.text_Start.setFont(font)
        self.text_Start.setObjectName("Start")
        self.text_Start.setText(" Start")

        # 创建标签用于显示第二个GIF
        self.label_second = QtWidgets.QLabel(MainWindow)
        self.label_second.setGeometry(-50, -50, 399, 300)  # 绝对定位
        self.second_gif = QtGui.QMovie('icon/voice.gif')
        self.second_gif.setScaledSize(QtCore.QSize(399, 300))
        self.label_second.setMovie(self.second_gif)
        self.label_second.setVisible(False)  # 初始隐藏第二个GIF

        # 创建透明按钮并覆盖在GIF上方
        self.button = QtWidgets.QPushButton(MainWindow)
        self.button.setStyleSheet("background-color: transparent; border: none;")
        self.button.setGeometry(50, 0, 200, 200)  # 绝对定位
        self.button.pressed.connect(self.onButtonPressed)
        self.button.released.connect(self.onButtonReleased)

        # 设置按钮
        self.settings_button = QtWidgets.QPushButton(MainWindow)
        self.settings_button.setStyleSheet("background-color: transparent; border: none;")
        self.settings_button.setGeometry(250, 0, 40, 40)  # 绝对定位
        self.settings_button.setIcon(QtGui.QIcon('icon/settings.png'))  # 请确保路径正确
        self.settings_button.setIconSize(QtCore.QSize(40, 40))
        self.settings_button.clicked.connect(self.openSettingsDialog)

        # Main layout
        self.main_layout_widget = QtWidgets.QWidget(MainWindow)
        self.main_layout_widget.setGeometry(0, 240, 300, 360)  # 绝对定位
        self.main_layout = QtWidgets.QVBoxLayout(self.main_layout_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)  # 去掉边距

        # 创建“Show Less”和“Show More”按钮
        self.show_less_button = QtWidgets.QPushButton('Show Less', self.main_layout_widget)
        self.show_less_button.clicked.connect(self.showLess)
        self.show_less_button.setStyleSheet("""
            QPushButton {
                background-color: blue;  
                color: white;              
            }
        """)
        self.main_layout.addWidget(self.show_less_button)
        self.show_more_button = QtWidgets.QPushButton('Show More', self.main_layout_widget)
        self.show_more_button.clicked.connect(self.showMore)
        self.show_more_button.setVisible(False)
        self.show_more_button.setStyleSheet("""
            QPushButton {
                background-color: blue;  
                color: white;              
            }
        """)
        self.main_layout.addWidget(self.show_more_button)

        # Scroll area
        self.scroll_area = QtWidgets.QScrollArea(self.main_layout_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)
        self.main_layout.addWidget(self.scroll_area)

        self.scroll_layout.addStretch(1)

        # 文件监视器
        self.file_watcher = QtCore.QFileSystemWatcher()
        self.file_watcher.addPath('Resource/text/question.txt')
        self.file_watcher.addPath('Resource/text/response.txt')
        self.file_watcher.fileChanged.connect(self.onFileChanged)

    def onFileChanged(self, path):
        if path == 'Resource/text/question.txt':
            self.addUserMessage()
        elif path == 'Resource/text/response.txt':
            self.addBotMessage()

    def addUserMessage(self):
        with open('Resource/text/question.txt', 'r', encoding='utf-8') as file:
            message = file.read().strip()
        if message:
            user_label = RoundedMessageLabel(message, "light green", "black")
            user_label.setMaximumWidth(250)
            user_label.adjustSize()

            user_item_widget = QtWidgets.QWidget()
            user_layout = QtWidgets.QHBoxLayout(user_item_widget)
            user_layout.addStretch()
            user_layout.addWidget(user_label)
            user_layout.setContentsMargins(0, 0, 0, 0)
            self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, user_item_widget)

            self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

    def addBotMessage(self):
        with open('Resource/text/response.txt', 'r', encoding='utf-8') as file:
            message = file.read().strip()
        if message:
            bot_label = RoundedMessageLabel(message, "white", "black")
            bot_label.setMaximumWidth(250)
            bot_label.adjustSize()

            bot_item_widget = QtWidgets.QWidget()
            bot_layout = QtWidgets.QHBoxLayout(bot_item_widget)
            bot_layout.addWidget(bot_label)
            bot_layout.addStretch()
            bot_layout.setContentsMargins(0, 0, 0, 0)
            self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, bot_item_widget)

            self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

    def onButtonPressed(self):
        # 在按钮按下时显示第二个GIF并隐藏第一个GIF
        self.label_initial.setVisible(False)
        self.label_second.setVisible(True)
        self.second_gif.start()

    def onButtonReleased(self):
        # 在按钮松开时显示初始GIF并隐藏第二个GIF
        self.label_initial.setVisible(True)
        self.label_second.setVisible(False)
        self.initial_gif.start()

    def showLess(self):
        # 隐藏scroll_area和input_layout，但不移除它们
        self.scroll_area.setVisible(False)
        self.main_layout.removeWidget(self.scroll_area)
        self.main_layout_widget.setGeometry(0, 240, 300, 30)  # 绝对定位
        self.MainWindow.setGeometry(300, 300, 300, 280)
        self.show_less_button.setVisible(False)
        self.show_more_button.setVisible(True)

    def showMore(self):
        # 显示scroll_area和input_layout
        self.scroll_area.setVisible(True)
        self.main_layout.insertWidget(self.main_layout.count() - 1, self.scroll_area)
        self.main_layout_widget.setGeometry(0, 240, 300, 360)  # 绝对定位
        self.MainWindow.setGeometry(300, 300, 300, 600)
        self.show_less_button.setVisible(True)
        self.show_more_button.setVisible(False)

    def openSettingsDialog(self):
        dialog = VoiceSettingsDialog(self.MainWindow)
        if dialog.exec_():
            settings = dialog.getSettings()
            self.saveSettingsToFile(settings)  # 在关闭对话框后自动导出音色调节获得的文本

    def saveSettingsToFile(self, settings):
        with open('voice_settings.txt', 'w', encoding='utf-8') as file:
            for key, value in settings.items():
                file.write(f"{key}: {value}\n")

class RoundedMessageLabel(QtWidgets.QLabel):
    def __init__(self, text, bg_color, text_color):
        super().__init__(text)
        self.bg_color = bg_color
        self.text_color = text_color
        self.setWordWrap(True)
        self.setStyleSheet(f"color: {self.text_color}; padding: 10px;")
        self.setContentsMargins(15, 10, 0, 10)
        self.adjustSize()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        # Draw the background
        rect = self.rect()
        painter.setBrush(QtGui.QColor(self.bg_color))
        painter.setPen(QtGui.QColor(self.bg_color))
        painter.drawRoundedRect(rect, 22, 22)

        # Draw the text
        painter.setPen(QtGui.QColor(self.text_color))
        text_rect = rect.adjusted(10, 10, -10, -10)
        painter.drawText(text_rect, QtCore.Qt.TextWordWrap, self.text())

    def sizeHint(self):
        fm = QtGui.QFontMetrics(self.font())
        text_rect = fm.boundingRect(0, 0, 250, 0, QtCore.Qt.TextWordWrap, self.text())
        text_rect.adjust(0, 0, 30, 20)  # Add padding for margins
        return text_rect.size()
