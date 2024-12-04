import openai
import os

# OpenAI API Key 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(question):
    """
    ChatGPT에게 질문하고 응답을 받는 함수
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Chat with ChatGPT. Type 'exit' to quit.")
    while True:
        question = input("Question: ")
        if question.lower() == "exit":
            print("Exiting the chat.")
            break
        response = ask_gpt(question)
        print(f"GPT Response: {response}")
