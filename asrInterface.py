from PyQt5 import QtCore, QtGui, QtWidgets

class VoiceSettingsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Voice Settings')
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: white")
        layout = QtWidgets.QVBoxLayout(self)

        # Voice
        voice_layout = QtWidgets.QHBoxLayout()
        voice_label = QtWidgets.QLabel("Voice")
        self.voice_edit = QtWidgets.QLineEdit()
        voice_layout.addWidget(voice_label)
        voice_layout.addWidget(self.voice_edit)
        layout.addLayout(voice_layout)

        # Prompt
        prompt_layout = QtWidgets.QHBoxLayout()
        prompt_label = QtWidgets.QLabel("Prompt")
        self.prompt_edit = QtWidgets.QLineEdit()
        prompt_layout.addWidget(prompt_label)
        prompt_layout.addWidget(self.prompt_edit)
        layout.addLayout(prompt_layout)

        # Temperature
        temperature_layout = QtWidgets.QHBoxLayout()
        temperature_label = QtWidgets.QLabel("Temperature")
        self.temperature_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.temperature_slider.setRange(0, 10)
        temperature_layout.addWidget(temperature_label)
        temperature_layout.addWidget(self.temperature_slider)
        layout.addLayout(temperature_layout)

        # Top_p
        top_p_layout = QtWidgets.QHBoxLayout()
        top_p_label = QtWidgets.QLabel("Top_p")
        self.top_p_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.top_p_slider.setRange(0, 10)
        top_p_layout.addWidget(top_p_label)
        top_p_layout.addWidget(self.top_p_slider)
        layout.addLayout(top_p_layout)

        # Top_k
        top_k_layout = QtWidgets.QHBoxLayout()
        top_k_label = QtWidgets.QLabel("Top_k")
        self.top_k_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.top_k_slider.setRange(1, 20)
        top_k_layout.addWidget(top_k_label)
        top_k_layout.addWidget(self.top_k_slider)
        layout.addLayout(top_k_layout)

        # Skip_refine
        skip_refine_layout = QtWidgets.QHBoxLayout()
        skip_refine_label = QtWidgets.QLabel("Skip_refine")
        self.skip_refine_checkbox = QtWidgets.QCheckBox()
        skip_refine_layout.addWidget(skip_refine_label)
        skip_refine_layout.addWidget(self.skip_refine_checkbox)
        layout.addLayout(skip_refine_layout)

        # Custom_voice
        custom_voice_layout = QtWidgets.QHBoxLayout()
        custom_voice_label = QtWidgets.QLabel("Custom_voice")
        self.custom_voice_checkbox = QtWidgets.QCheckBox()
        custom_voice_layout.addWidget(custom_voice_label)
        custom_voice_layout.addWidget(self.custom_voice_checkbox)
        layout.addLayout(custom_voice_layout)

        # 确认按钮
        buttons_layout = QtWidgets.QHBoxLayout()
        self.ok_button = QtWidgets.QPushButton("确认")
        self.cancel_button = QtWidgets.QPushButton("取消")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)
        layout.addLayout(buttons_layout)

        # 从文件加载设置
        self.loadSettingsFromFile()

    def loadSettingsFromFile(self):
        try:
            with open('voice_settings.txt', 'r', encoding='utf-8') as file:
                settings = {}
                for line in file:
                    key, value = line.strip().split('=')
                    settings[key] = value

                self.voice_edit.setText(settings.get("voice", "1111"))
                self.prompt_edit.setText(settings.get("prompt", "[break_1],[oral_2]"))
                self.temperature_slider.setValue(int(float(settings.get("temperature", "0.5")) * 10))
                self.top_p_slider.setValue(int(float(settings.get("top_p", "0.7")) * 10))
                self.top_k_slider.setValue(int(settings.get("top_k", "20")))
                self.skip_refine_checkbox.setChecked(bool(int(settings.get("skip_refine", "0"))))
                self.custom_voice_checkbox.setChecked(bool(int(settings.get("custom_voice", "0"))))
        except FileNotFoundError:
            pass  # 如果文件不存在，则保持默认值

    def getSettings(self):
        return {
            "voice": self.voice_edit.text(),
            "prompt": self.prompt_edit.text(),
            "temperature": self.temperature_slider.value() / 10,  # 转换为0.5的中间值
            "top_p": self.top_p_slider.value() / 10,  # 转换为0.7的中间值
            "top_k": self.top_k_slider.value(),
            "skip_refine": int(self.skip_refine_checkbox.isChecked()),
            "custom_voice": int(self.custom_voice_checkbox.isChecked())
        }

class InstructionsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Instructions')
        self.setGeometry(100, 100, 800, 300)
        self.setStyleSheet("background-color: white")
        layout = QtWidgets.QVBoxLayout(self)

        instructions_text = QtWidgets.QLabel("""
    这是一个语音识别助手
    如何使用：
    唤醒词是“嘿小邓”，唤醒后，当听到告诉我你的问题后即可向他说话，如果想要结束对话，对他说“结束对话即可”
                                             
    支持调整语音音色：（点击右上角设置按钮）
    text: 必须， 要合成语音的文字
    voice: 可选，默认 2222, 决定音色的数字， 2222 | 1111 | 5555 | 7869 | 6653 | 4099 | 5099，可选其一，或者任意传入将随机使用音色
    prompt: 可选，默认 空， 设定 笑声、停顿，例如 [oral_2][laugh_0][break_6]
    temperature: 可选， 默认 0.3
    top_p: 可选， 默认 0.7
    top_k: 可选， 默认 20
    skip_refine: 可选， 默认0， 1=跳过 refine text，0=不跳过
    custom_voice: 可选， 默认0，自定义获取音色值时的种子值，需要大于0的整数，如果设置了则以此为准，将忽略 `voice`
                                             
    支持折叠功能:
    点击showless可以折叠页面
    之后点击showmore可以还原页面
        """)
        instructions_text.setWordWrap(True)
        layout.addWidget(instructions_text)

        close_button = QtWidgets.QPushButton("关闭")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setFixedSize(300, 600) 
        MainWindow.setWindowTitle('GIF Switcher')

        self.background_label = QtWidgets.QLabel(MainWindow)
        self.background_label.setGeometry(0, 0, 300, 600)
        self.background_pixmap = QtGui.QPixmap('icon/StarrySky.jpg')
        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.lower()
        
        # 创建标签用于显示初始GIF
        self.label_initial = QtWidgets.QLabel(MainWindow)
        self.label_initial.setGeometry(50, 0, 200, 200)
        self.initial_gif = QtGui.QMovie('icon/play.gif')
        self.initial_gif.setScaledSize(QtCore.QSize(200, 200))
        self.label_initial.setMovie(self.initial_gif)
        self.initial_gif.start()

        # 创建标签用于显示第二个GIF
        self.label_second = QtWidgets.QLabel(MainWindow)
        self.label_second.setGeometry(-50, -50, 399, 300)
        self.second_gif = QtGui.QMovie('icon/voice.gif')
        self.second_gif.setScaledSize(QtCore.QSize(399, 300))
        self.label_second.setMovie(self.second_gif)
        self.label_second.setVisible(False)

        # 创建透明按钮并覆盖在GIF上方
        self.button = QtWidgets.QPushButton(MainWindow)
        self.button.setStyleSheet("background-color: transparent; border: none;")
        self.button.setGeometry(50, 0, 200, 200)
        self.button.pressed.connect(self.onButtonPressed)
        self.button.released.connect(self.onButtonReleased)

        # 设置按钮
        self.settings_button = QtWidgets.QPushButton(MainWindow)
        self.settings_button.setStyleSheet("background-color: transparent; border: none;")
        self.settings_button.setGeometry(260, 0, 40, 40)
        self.settings_button.setIcon(QtGui.QIcon('icon/settings.png'))
        self.settings_button.setIconSize(QtCore.QSize(40, 40))
        self.settings_button.clicked.connect(self.openSettingsDialog)

        # 说明按钮
        self.instructions_button = QtWidgets.QPushButton(MainWindow)
        self.instructions_button.setStyleSheet("background-color: transparent; border: none;")
        self.instructions_button.setGeometry(0, 0, 70, 35)
        self.instructions_button.setIcon(QtGui.QIcon('icon/instructions.png'))
        self.instructions_button.setIconSize(QtCore.QSize(70, 35))
        self.instructions_button.clicked.connect(self.openInstructionsDialog)

        # Main layout
        self.main_layout_widget = QtWidgets.QWidget(MainWindow)
        self.main_layout_widget.setGeometry(0, 240, 300, 360)
        self.main_layout = QtWidgets.QVBoxLayout(self.main_layout_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

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
        self.scroll_area.setStyleSheet("background-color: transparent; border: none;")
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
            user_item_layout = QtWidgets.QHBoxLayout(user_item_widget)
            user_item_layout.addWidget(user_label, 0, QtCore.Qt.AlignRight)
            user_item_layout.setContentsMargins(0, 0, 0, 0)
            self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, user_item_widget)

            self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

    def addBotMessage(self):
        with open('Resource/text/response.txt', 'r', encoding='utf-8') as file:
            message = file.read().strip()
        if message:
            bot_label = RoundedMessageLabel(message, "light blue", "black")
            bot_label.setMaximumWidth(250)
            bot_label.adjustSize()
            bot_item_widget = QtWidgets.QWidget()
            bot_item_layout = QtWidgets.QHBoxLayout(bot_item_widget)
            bot_item_layout.addWidget(bot_label, 0, QtCore.Qt.AlignLeft)
            bot_item_layout.setContentsMargins(0, 0, 0, 0)
            self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, bot_item_widget)

            self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

    def onButtonPressed(self):
        self.label_initial.setVisible(False)
        self.label_second.setVisible(True)
        self.second_gif.start()

    def onButtonReleased(self):
        self.label_initial.setVisible(True)
        self.label_second.setVisible(False)
        self.initial_gif.start()

    def showLess(self):
        self.scroll_area.setVisible(False)
        self.main_layout.removeWidget(self.scroll_area)
        self.main_layout_widget.setGeometry(0, 240, 300, 30)
        self.MainWindow.setFixedSize(300, 280) 
        self.show_less_button.setVisible(False)
        self.show_more_button.setVisible(True)

    def showMore(self):
        self.scroll_area.setVisible(True)
        self.main_layout.insertWidget(self.main_layout.count() - 1, self.scroll_area)
        self.main_layout_widget.setGeometry(0, 240, 300, 360)
        self.MainWindow.setFixedSize(300, 600) 
        self.show_less_button.setVisible(True)
        self.show_more_button.setVisible(False)

    def openSettingsDialog(self):
        dialog = VoiceSettingsDialog(self.MainWindow)
        if dialog.exec_():
            settings = dialog.getSettings()
            self.saveSettingsToFile(settings)

    def openInstructionsDialog(self):
        instructions_dialog = InstructionsDialog(self.MainWindow)
        instructions_dialog.exec_()

    def saveSettingsToFile(self, settings):
        with open('settings.txt', 'w', encoding='utf-8') as file:
            for key, value in settings.items():
                file.write(f"{key}={value}\n")

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

        rect = self.rect()
        painter.setBrush(QtGui.QColor(self.bg_color))
        painter.setPen(QtGui.QColor(self.bg_color))
        painter.drawRoundedRect(rect, 22, 22)

        painter.setPen(QtGui.QColor(self.text_color))
        text_rect = rect.adjusted(10, 10, -10, -10)
        painter.drawText(text_rect, QtCore.Qt.TextWordWrap, self.text())

    def sizeHint(self):
        fm = QtGui.QFontMetrics(self.font())
        text_rect = fm.boundingRect(0, 0, 250, 0, QtCore.Qt.TextWordWrap, self.text())
        text_rect.adjust(0, 0, 30, 20)
        return text_rect.size()
