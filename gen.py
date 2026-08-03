from google import genai

# Add your Gemini API Key here
client = genai.Client(api_key="for privacy not reveaL")

# Create a chat session
chat = client.chats.create(
    model="models/gemini-2.0-flash"
)

# Give initial context about yourself
chat.send_message("""
My name is Vaibhav Sugandhi.
I am a final year Computer Science student at VIT Bhopal.
I am learning Generative AI.
I have solved 250+ LeetCode problems.
I like cricket and music.
""")

print("Gemini Chat Started! Type 'exit' to quit.\n")

while True:
    try:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chat Ended!")
            break

        response = chat.send_message(user_input)

        print("\nGemini:", response.text)
        print()

    except KeyboardInterrupt:
        print("\nChat Ended!")
        break

    except Exception as e:
        print(f"\nError: {e}\n")
