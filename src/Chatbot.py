# Library
from tkinter import *
import openai
import json

# Root, title
root = Tk()
root.title("Chatbot")


# Loading API key to file json
with open("secrets.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_key"]

openai.api_key = api_key

# START RESPONSE---------------------------------------------------------------------

def chatbot_response(user_input):
    # Use ChatGPT to get a response
    messages = [{"role": "system", "content": "You are a virtual assistant named Joi and you speak Italian."}, {"role": "user", "content": user_input}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_reply = response.choices[0].message["content"].strip()
    return assistant_reply

# END RESPONSE---------------------------------------------------------------------

# Create the chatbot's text area
text_area = Text(root, bg="light yellow", width=50, height=20)
text_area.pack()

# Create the user's input field
input_field = Text(root, width=50, height=4, font=('Helvetica', 9))
input_field.pack()

def send_message():
    # Get the user's input
    user_input = input_field.get("1.0", "end-1c").strip()

    if user_input:
        # Generate a response from the ChatGPT assistant
        assistant_response = chatbot_response(user_input)

        # Clear the input field
        input_field.delete("1.0", END)

        # Display the user and assistant responses in the chatbot's text area
        text_area.insert(END, f"You: {user_input}\n")
        text_area.insert(END, f"Joi: {assistant_response}\n")

        # Scroll to the bottom of the text area
        text_area.see(END)

# Create the send button
send_button = Button(root, text="Send", bg="light blue", command=send_message)
send_button.pack()

root.mainloop()
