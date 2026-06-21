from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES


# Initialize Translator
translator = Translator()



# Function to Translate Text
def translate_text():
    try:
        text = input_text.get("1.0", END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter text!")
            return

        src_lang = language_dict[source_lang.get()]
        dest_lang = language_dict[target_lang.get()]

        translated = translator.translate(
            text,
            src=src_lang,
            dest=dest_lang
        )

        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to Copy Text
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", END))
    root.update()
    messagebox.showinfo("Success", "Text copied!")

# Function for Text-to-Speech
def speak_text():
    text = output_text.get("1.0", END).strip()

    if text:
        engine.say(text)
        engine.runAndWait()

# GUI Window
root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")
root.resizable(False, False)

Label(root, text="Language Translation Tool",
      font=("Arial", 18, "bold")).pack(pady=10)

# Input Text
Label(root, text="Enter Text").pack()

input_text = Text(root, height=6, width=70)
input_text.pack(pady=5)

# Languages
language_dict = LANGUAGES
language_names = sorted([lang.title() for lang in language_dict.values()])

frame = Frame(root)
frame.pack(pady=10)

source_lang = StringVar()
target_lang = StringVar()

source_lang.set("English")
target_lang.set("Hindi")

ttk.Combobox(
    frame,
    textvariable=source_lang,
    values=language_names,
    width=25
).grid(row=0, column=0, padx=10)

Label(frame, text="→", font=("Arial", 16)).grid(row=0, column=1)

ttk.Combobox(
    frame,
    textvariable=target_lang,
    values=language_names,
    width=25
).grid(row=0, column=2, padx=10)

# Reverse dictionary
language_dict = {
    value.title(): key
    for key, value in LANGUAGES.items()
}

# Translate Button
Button(root,
       text="Translate",
       command=translate_text,
       bg="green",
       fg="white",
       width=20).pack(pady=10)

# Output Text
Label(root, text="Translated Text").pack()

output_text = Text(root, height=6, width=70)
output_text.pack(pady=5)

# Buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

Button(button_frame,
       text="Copy",
       command=copy_text,
       width=15).grid(row=0, column=0, padx=10)

Button(button_frame,
       text="Speak",
       command=speak_text,
       width=15).grid(row=0, column=1, padx=10)

root.mainloop()