from gpt import speech_to_text, ask_gpt

# 음성 파일 경로
FILENAME = "voice.wav"

if __name__ == "__main__":
    # 음성 파일에서 텍스트 추출
    user_question = speech_to_text(FILENAME)
    if "오류" in user_question:
        print(user_question)
    else:
        print(f"음성에서 변환된 질문: {user_question}")
        
        # ChatGPT에게 질문하고 응답 출력
        gpt_response = ask_gpt(user_question)
        print(f"GPT 응답: {gpt_response}")
