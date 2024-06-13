import requests

PATH=PATH='Resource/wav/'
def synthesize_speech(text, voice="11", prompt="[break_1]", temperature=0.3, top_p=0.7, top_k=20, skip_refine=0, custom_voice=0):
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
            with open(PATH+"output.wav", "wb") as file:
                file.write(audio_response.content)
            print("Audio content written to file 'output.wav'")

        else:
            print(f"Error: {response_data['msg']}")
    except Exception as e:
        print(f"An error occurred: {e}")
