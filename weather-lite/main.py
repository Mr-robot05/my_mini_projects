import tkinter as tk
import requests

# API клюс с сайта . Надо зарегаться чтобы получить ключ.
api_key = 'fb95ac7cf586e32f429cac1e668bc950'


def foo():
    "Функция которая будет отрабатывать , когда появится ошибка Keyerror"
    button.config(text='УЗНАТЬ ПОГОДУ')


def to_do():
    'Функция делает get запрос на сайт с погодой'
    city = entry.get()
    entry.delete(0, last='end')
    try:
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather/?q={city}&appid={api_key}&units=metric&lang=ru')
        result = res.json()
        button.config(text=f"{result['name']}     {round(result['main']['temp'], 1)}", font=('Times new roman', 40))
    except KeyError:
        button.config(text='Нет такого города\n Введите название города еще раз', )
        root.after(2000, foo)


# Создание окна, задаем размер, название, неизменяемость окна, задний фон
root = tk.Tk()
root.title('Weather-lite')
root.geometry('500x400')
root.resizable(False, False)
root.configure(bg='lightblue')

# Добавим логотоп в Label
weather_logo = tk.PhotoImage(file='./111.png')

# Надпись "Введите город"
label = tk.Label(root, image=weather_logo, font=("Arial", 20), text="Введите город", compound="top", )
label.pack(pady=10)

# Создаем поле для ввода
entry = tk.Entry(width=20, justify='center', font=('Arial', 30), background='lightgrey')
entry.pack(pady=10)

# Создаем кнопку "Узнать погоду"
button = tk.Button(text='УЗНАТЬ ПОГОДУ', font=('Arial', 20), command=to_do)
button.pack(pady=2)

# для цикличности окно, без нее графическое окно просто закроется
root.mainloop()
