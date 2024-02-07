import openai 
api_key = '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'

openai.api_key = api_key

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can change the engine as needed
        prompt=prompt,
        max_tokens=150  # Adjust the max tokens as per your requirement
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("Welcome to ChatGPT! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatGPT: Goodbye!")
            break

        # You can customize the prompt as per your conversation style
        prompt = f"You: {user_input}\nChatGPT:"
        response = chat_with_gpt(prompt)
        print(f"ChatGPT: {response}")