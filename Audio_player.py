import pyaudio
import wave

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