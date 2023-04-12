import openai
import time

# Set up OpenAI API key
openai.api_key = "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"

# Define a function to generate a response from GPT-3
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message


# Start a conversation
print("Hello! I'm ChatGPT. How can I help you today?")
while True:
    user_input = input("> ")
    prompt = f"You: {user_input}\nChatGPT:"
    response = generate_response(prompt)
    print(response)
    time.sleep(1)  # Wait for a second before generating the next response
