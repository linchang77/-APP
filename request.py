import requests

PATH='Resource/wav/'
def request_voice(text, voiceset, name='output.wav'):
    # 获取配置参数
    voice = voiceset.get("voice", "11")
    prompt = voiceset.get("prompt", "[break_1]")
    temperature = voiceset.get("temperature", 0.3)
    top_p = voiceset.get("top_p", 0.7)
    top_k = voiceset.get("top_k", 20)
    skip_refine = voiceset.get("skip_refine", 0)
    custom_voice = voiceset.get("custom_voice", 0)
    # 调用合成函数
    synthesize_speech(text, voice, prompt, temperature, top_p, top_k, skip_refine, custom_voice, name)

def synthesize_speech(text, voice="11", prompt="[break_1]", temperature=0.5, top_p=0.7, top_k=20, skip_refine=0, custom_voice=0,name='output.wav'):
    url = 'http://127.0.0.1:9966/tts'
    payload = {
        "text": text,
        "voice": voice,
        "prompt": prompt,
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "skip_refine": skip_refine,
        "custom_voice": custom_voice
    }

    try:
        response = requests.post(url, data=payload)
        response_data = response.json()
        
        if response_data["code"] == 0:
            audio_file = response_data["audio_files"][0]
            filename = audio_file["filename"]
            download_url = audio_file["url"]

            print(f"Audio file generated: {filename}")
            print(f"Download URL: {download_url}")

            # You can add code here to download and save the file if needed.
            # For example:
            audio_response = requests.get(download_url)
            with open(PATH+name, "wb") as file:
                file.write(audio_response.content)
            print("Audio content written to file"+name)

        else:
            print(f"Error: {response_data['msg']}")
    except Exception as e:
        print(f"An error occurred: {e}")
