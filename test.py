from asrbot import asrbot
import threading
from chatbot import WenxinYiyanChatBot , get_file_modification_time
import time
from Audio_player import init_audios,get_voice_set
from request import request_voice,synthesize_speech

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
        last_modification_time = get_file_modification_time(INPUT_FILE)
        print("启动文心一言")
        while True:
            time.sleep(5)  # 每5秒检测一次
            current_modification_time = get_file_modification_time(INPUT_FILE)
            if current_modification_time != last_modification_time:
                print(f"{INPUT_FILE} 文件已修改，正在处理新的问题...")
                chatbot.read_questions_and_write_responses(INPUT_FILE, OUTPUT_FILE)
                last_modification_time = current_modification_time

#request_voice("在呢",voiceset,"zaine.wav")
#synthesize_speech("在呢", "2222", "[break_2],[oral_2]", 0.5, 0.7, 20, 0, 0, "zaine.wav")
init_audios(get_voice_set())
#asrbot_instance=asrbot()
#while True:
    #asrbot.run()

