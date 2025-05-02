import tkinter as tk
from datetime import datetime
import random
texts = [
    "When the sun dipped below the hills, the village\n square began to glow with warm lantern light.\n Children chased fireflies while elders exchanged stories.",

    "A curious fox trotted along the forest path, its ears twitching at every sound.Somewhere nearby, \na brook whispered secrets to the moss-covered stones.",

    "Technology has transformed the way we \ncommunicate, but nothing replaces the warmth ofa handwritten\n letter on a rainy afternoon.",

    "Before launching the balloon, the scientist\n double-checked each instrument. The sky was clear,\n the data awaited, and discovery hovered just above the clouds."
]

# === Global Variables ===
first_keystroke_time = None
completion_time = None
duration = None

# === Reset Function ===
def reset():
    global first_keystroke_time, completion_time, duration
    first_keystroke_time = None
    completion_time = None
    duration = False
    text.delete("1.0", tk.END)
    label_result.config(text="Start typing again. End with '/' to finish.")

# === First Key Detection ===
def on_keypress(event):
    global first_keystroke_time, completion_time, duration
    if first_keystroke_time is None:
        first_keystroke_time = datetime.now()
    if event.char == '/':
        completion_time = datetime.now()
        duration = int((completion_time - first_keystroke_time).total_seconds())

# === Submit Function ===
def submit():
    user_input = text.get("1.0", tk.END).strip()
    count = len(user_input.replace(" ", ""))

    try:
        cpm = (count // duration) * 60
        wpm = cpm // 5
        label_result.config(
            text=f"Typing duration: {duration} seconds"
                 f"\nNumber of characters: {count}"
                 f"\nYour Typing speed is {cpm} characters per minute and {wpm} words per minute"
        )
        root.after(3000, reset)  # Delay reset by 3 seconds
    except TypeError:
        label_result.config(text="You forgot to type '/' at the end of your submission. Please try again")

# === UI Setup ===
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("520x420")
root.configure(bg="#f7f7f7")

# === Fonts and Styles ===
font_title = ("Helvetica", 12, "bold")
font_text = ("Consolas", 11)
font_result = ("Arial", 10)

# === Header Label ===
header = tk.Label(root, text="Typing Speed Tester\nType the words below (Type '/' to submit):", font=("Helvetica", 16, "bold"),
                  bg="#f7f7f7", fg="#2c3e50")
header.pack(pady=10)

# === Instruction Label ===

selected_text = texts[random.randint(0, 3)]  # Select the random text first

label = tk.Label(root, text=f"{selected_text}",
                 font=font_title, bg="#f7f7f7", fg="#333")
label.pack(pady=8)

# === Text Input ===
text = tk.Text(root, height=6, width=50, font=font_text, bd=2, relief="groove")
text.pack(pady=5)
text.bind("<Key>", on_keypress)

# === Submit Button ===
submit_button = tk.Button(root, text="Submit", command=submit,
                          bg="#4CAF50", fg="white", activebackground="#45a049", padx=20, pady=5)
submit_button.pack(pady=15)

# === Result Label ===
label_result = tk.Label(root, text="", wraplength=480, justify="left",
                        font=font_result, bg="#f7f7f7", fg="#444")
label_result.pack(pady=10)

# === Mainloop ===
root.mainloop()
