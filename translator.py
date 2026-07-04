from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}

# Translate
def translate_text():
    try:
        text = input_box.get("1.0", END).strip()

        if text == "":
            messagebox.showwarning("Warning", "Enter some text")
            return

        lang_name = language_var.get()
        lang_code = languages[lang_name]

        translated = GoogleTranslator(
            source="auto",
            target=lang_code
        ).translate(text)

        output_box.delete("1.0", END)
        output_box.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Copy
def copy_text():
    text = output_box.get("1.0", END)

    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

    messagebox.showinfo("Copied", "Text copied successfully")

# Speak
def speak_text():
    try:
        text = output_box.get("1.0", END).strip()

        if text == "":
            messagebox.showwarning("Warning", "No translated text")
            return

        lang_name = language_var.get()
        lang_code = languages[lang_name]

        tts = gTTS(text=text, lang=lang_code)

        filename = "voice.mp3"
        tts.save(filename)

        playsound(filename)

        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        messagebox.showerror("Speech Error", str(e))

# Clear
def clear_text():
    input_box.delete("1.0", END)
    output_box.delete("1.0", END)

# Main Window
root = Tk()
root.title("AI Language Translator")
root.geometry("850x600")
root.configure(bg="#E3F2FD")

# Heading
heading = Label(
    root,
    text="🌍 AI Language Translator",
    font=("Arial", 22, "bold"),
    bg="#1976D2",
    fg="white",
    pady=10
)
heading.pack(fill=X)

# Input Label
Label(
    root,
    text="Enter Text",
    font=("Arial", 14, "bold"),
    bg="#E3F2FD"
).pack(pady=10)

# Input Box
input_box = Text(
    root,
    height=7,
    width=80,
    font=("Arial", 12)
)
input_box.pack()

# Language Label
Label(
    root,
    text="Select Language",
    font=("Arial", 14, "bold"),
    bg="#E3F2FD"
).pack(pady=10)

language_var = StringVar()

language_dropdown = ttk.Combobox(
    root,
    textvariable=language_var,
    values=list(languages.keys()),
    width=30,
    state="readonly"
)

language_dropdown.pack()
language_dropdown.set("Telugu")

# Buttons
button_frame = Frame(root, bg="#E3F2FD")
button_frame.pack(pady=20)

Button(
    button_frame,
    text="Translate",
    command=translate_text,
    bg="#4CAF50",
    fg="white",
    width=12
).grid(row=0, column=0, padx=5)

Button(
    button_frame,
    text="Copy",
    command=copy_text,
    bg="#FF9800",
    fg="white",
    width=12
).grid(row=0, column=1, padx=5)

Button(
    button_frame,
    text="Speak",
    command=speak_text,
    bg="#9C27B0",
    fg="white",
    width=12
).grid(row=0, column=2, padx=5)

Button(
    button_frame,
    text="Clear",
    command=clear_text,
    bg="#F44336",
    fg="white",
    width=12
).grid(row=0, column=3, padx=5)

# Output Label
Label(
    root,
    text="Translated Output",
    font=("Arial", 14, "bold"),
    bg="#E3F2FD"
).pack(pady=10)

# Output Box
output_box = Text(
    root,
    height=7,
    width=80,
    font=("Arial", 12),
    bg="#FFF9C4"
)
output_box.pack()

root.mainloop()