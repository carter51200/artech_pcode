import speech_recognition as sr
from gpt import ask_gpt

def live_speech_to_text():
    """
    실시간 음성 입력을 텍스트로 변환하는 함수
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("실시간 음성 입력을 시작합니다. 마이크에 질문을 말하세요.")
        try:
            recognizer.adjust_for_ambient_noise(source)  # 주변 소음 조정
            print("듣는 중...")
            audio = recognizer.listen(source, timeout=10)  # 최대 10초 동안 대기
            print("음성을 텍스트로 변환 중...")
            text = recognizer.recognize_google(audio, language="ko-KR")  # 한국어 인식
            return text
        except sr.UnknownValueError:
            return "음성을 이해하지 못했습니다. 다시 말해 주세요."
        except sr.RequestError as e:
            return f"Google Speech Recognition 서비스에 접근할 수 없습니다: {e}"
        except Exception as e:
            return f"오류 발생: {e}"

if __name__ == "__main__":
    user_question = live_speech_to_text()
    if "오류" in user_question:
        print(user_question)
    else:
        print(f"음성에서 변환된 질문: {user_question}")
        
        gpt_response = ask_gpt(user_question)
        print(f"GPT 응답: {gpt_response}")
