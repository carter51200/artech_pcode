import speech_recognition as sr
from gpt import ask_gpt
import keyboard
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def toggle_speech_to_text():
    recognizer = sr.Recognizer()
    is_listening = False
    print("스페이스바를 눌러 듣기를 시작/중지하세요.")

    with sr.Microphone() as source:
        print("대기 중... (스페이스바로 음성 입력 토글)")
        audio = None
        while True:
            if keyboard.is_pressed("space"):
                if not is_listening:
                    is_listening = True
                    print("듣기 시작!")
                    try:
                        audio = recognizer.listen(source, timeout=None, phrase_time_limit=10)
                        print("녹음 완료!")
                    except Exception as e:
                        print(f"오류 발생: {e}")
                else:
                    print("듣기 종료. 음성을 처리 중...")
                    is_listening = False
                    try:
                        text = recognizer.recognize_google(audio, language="ko-KR")
                        return text
                    except sr.UnknownValueError:
                        return "음성을 이해하지 못했습니다. 다시 시도해주세요."
                    except Exception as e:
                        return f"오류 발생: {e}"

if __name__ == "__main__":
    print("스페이스바를 눌러 질문을 말하세요. '종료'라고 말하면 종료됩니다.")
    while True:
        user_question = toggle_speech_to_text()
        if "종료" in user_question:
            print("대화를 종료합니다.")
            speak("대화를 종료합니다.")
            break
        gpt_response = ask_gpt(user_question)
        print(f"GPT 응답: {gpt_response}")
        speak(gpt_response)
