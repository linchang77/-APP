import pyaudio
import wave
from request import request_voice
CHUNK = 2048
PATH='Resource/wav/'

def play_audio(wave_input_path):
        if PATH not in wave_input_path:
             wave_input_path=PATH+wave_input_path
        p = pyaudio.PyAudio()
        wf = wave.open(wave_input_path, 'rb')
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(CHUNK)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)
        stream.stop_stream()
        stream.close()
        p.terminate()
        
def play_waiting(): 
    play_audio('sikaoyixia.wav')

def play_wakeup():
    play_audio('zaine.wav')

def get_voice_set():
    voiceset = {}
    try:
        with open('voice_settings.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                if key in ["voice", "prompt"]:
                    # Ensure voice and prompt remain strings
                    voiceset[key] = value
                elif value.isdigit():
                    # Convert numeric values to integers
                    value = int(value)
                    voiceset[key] = value
                else:
                    # Check if the value is a float
                    try:
                        value = float(value)
                    except ValueError:
                        pass  # Keep value as a string if it is not a float
                    voiceset[key] = value
    except FileNotFoundError:
        print("The file 'voice_settings.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return voiceset
def init_audios(voiceset):
    request_voice("我在啊",voiceset,"zaine.wav")
    request_voice("好的[uv_break]再见吧。",voiceset,"goodbye.wav")
    request_voice("告诉我你有什么问题",voiceset,"request_question.wav")
    request_voice("让我思考一下",voiceset,"sikaoyixia.wav")
    request_voice("我没有听清请你重新说一遍吧",voiceset,"try_again.wav")