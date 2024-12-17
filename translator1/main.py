import tkinter as tk
from tkinter import ttk
from translate import Translator


def on_button_click():
    from_lang = from_lang_combobox.get()
    to_lang = to_lang_combobox.get()
    user_input = entry.get()
    result = Translator(from_lang=from_lang, to_lang=to_lang).translate(user_input)
    label.config(text=result)


root = tk.Tk()
root.title("Пример Tkinter")
root.geometry('500x400')

to_lang_label = tk.Label(root, text="Выберите язык перевода:", font=("Helvetica", 8))
to_lang_label.pack(pady=5)

from_lang_combobox = ttk.Combobox(root, values=["ru", "en", "fr", "de", "es"], state="readonly")
from_lang_combobox.set("ru")
from_lang_combobox.pack(pady=5)

to_lang_combobox = ttk.Combobox(root, values=["en", "ru", "fr", "de", "es"], state="readonly")
to_lang_combobox.set("en")
to_lang_combobox.pack(pady=5)


label = tk.Label(root, text="ВВЕДИТЕ ТЕКСТ ДЛЯ ПЕРЕВОДА", font=("Helvetica", 15))
label.pack(pady=5)

entry = tk.Entry(root, width=30, font=10)
entry.pack(pady=5)

button = tk.Button(root, text="ПЕРЕВЕСТИ", command=on_button_click, bg="blue",
                   fg="white", width=20, height=2)
button.pack(pady=20)

root.mainloop()

# Мой первый проект на гитхаб