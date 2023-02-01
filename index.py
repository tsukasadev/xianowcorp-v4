import tkinter as tk
import openai
import requests
import time

openai.api_key = "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"

history = ""

def generate_response(prompt):
    global history
    # Ajoutez cette ligne pour ajouter la dernière entrée de l'utilisateur à l'historique de conversation
    history = history + " " + prompt

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=history,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def send_message():
    user_input = user_entry.get()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "User: " + user_input + "\n")
    chat_history.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)
    user_entry.config(state=tk.DISABLED)
    send_button.config(state=tk.DISABLED)
    loading_label.pack()
    root.update()
    bot_response = generate_response(user_input)
    time.sleep(2)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "Bot: " + bot_response + "\n")
    chat_history.config(state=tk.DISABLED)
    user_entry.config(state=tk.NORMAL)
    send_button.config(state=tk.NORMAL)
    loading_label.pack_forget()

root = tk.Tk()
root.title("OpenAI Chatbot")

frame = tk.Frame(root)

scrollbar = tk.Scrollbar(frame)

chat_history = tk.Text(frame, height=8, yscrollcommand=scrollbar.set, state=tk.DISABLED)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame.pack()

user_entry = tk.Entry(root, width=50)
user_entry.pack()

send_button = tk.Button(root, text="Envoyer", command=send_message)
send_button.pack()

loading_label = tk.Label(root, text="Chargement...", font=("TkDefaultFont", 8), fg="gray")

root.mainloop()