import requests
import pyttsx3
import pyaudio
import json
from vosk import Model, KaldiRecognizer
from PIL import Image
from io import BytesIO

engine = pyttsx3.init()
engine.setProperty('rate', 150)

model = Model("vosk-model-small-ru-0.4")
recognizer = KaldiRecognizer(model, 16000)

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000,
                    input=True, frames_per_buffer=8000)
stream.start_stream()

# API
base_url = "https://rickandmortyapi.com/api/character/108"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_command():
    print("Слушаю...")
    data = stream.read(4000, exception_on_overflow=False)
    
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result.get("text", "")
        if text:
            print(f"Распознано: {text}")
            return text
    return ""

def get_character_data():
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            return response.json()
        else:
            speak("Ошибка при получении данных")
            return None
    except:
        speak("Ошибка соединения")
        return None

def main():
    speak("Ассистент запущен")
    while True:
        command = recognize_command()
        
        if not command:
            continue
        
        # 1 Команда "случайный"
        if "случайный" in command:
            character = get_character_data()
            if character:
                name = character.get("name", "неизвестно")
                speak(f"Случайный персонаж: {name}")
                print(f"Случайный персонаж: {name}")
        
        # 2 Команда "сохранить"
        elif "сохранить" in command:
            character = get_character_data()
            if character:
                image_url = character.get("image", "")
                if image_url:
                    try:
                        img_response = requests.get(image_url)
                        img = Image.open(BytesIO(img_response.content))
                        img.save("saved_image.png")
                        speak("Изображение сохранено")
                        print("Изображение сохранено")
                    except:
                        speak("Ошибка сохранения изображения")
        
        # 3 Команда "эпизод"
        elif "эпизод" in command:
            character = get_character_data()
            if character:
                episode_url = character.get("episode", [""])[0]
                if episode_url:
                    try:
                        ep_response = requests.get(episode_url)
                        episode_data = ep_response.json()
                        episode_name = episode_data.get("name", "неизвестно")
                        speak(f"Первый эпизод: {episode_name}")
                        print(f"Первый эпизод: {episode_name}")
                    except:
                        speak("Ошибка получения эпизода")
        
        # 4 Команда "разрешение"
        elif "разрешение" in command:
            character = get_character_data()
            if character:
                image_url = character.get("image", "")
                if image_url:
                    try:
                        img_response = requests.get(image_url)
                        img = Image.open(BytesIO(img_response.content))
                        width, height = img.size
                        speak(f"Разрешение: {width} на {height} пикселей")
                        print(f"Разрешение: {width}x{height}")
                    except:
                        speak("Ошибка получения разрешения")

        else:
            print("Команда не распознана")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nЗавершение работы")
        stream.stop_stream()
        stream.close()
        audio.terminate()
