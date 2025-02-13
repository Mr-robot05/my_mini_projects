import random
from tkinter import *


# Функция для начала игры
def start_game():
    # Убираем из видимости элементы начального экрана
    name_game.pack_forget()
    play_button.place_forget()
    exit_button.place_forget()
    # Вызываем функцию выбора диапазона
    choose_range()


# Функция для выбора диапазона
def choose_range():
    # Создаем текстовую метку с информацией о выборе диапазона
    range_label = Label(root,
                        text="Выберите диапазон (0, N):",
                        font=("Arial", 30),
                        bg="black",
                        fg="white")
    range_label.pack(pady=10)

    # Создаем поле для ввода диапазона
    range_entry = Entry(root)
    range_entry.pack(pady=40)

    # Функция для обработки значения диапазона
    def proceed_range():
        # Получаем значение диапазона и переводим его в число
        try:
            max_range = int(range_entry.get())
        except ValueError:
            return

        # Убираем элементы этапа выбора диапазона
        range_label.pack_forget()
        range_entry.pack_forget()
        range_button.pack_forget()
        # Запускаем основной игровой процесс
        gameplay(max_range)

    # Создаем кнопку для продолжения после выбора диапазона
    range_button = Button(root, text="Продолжить", font=("Arial", 30), command=proceed_range)
    range_button.pack()


# Функция основного игрового процесса
def gameplay(max_range: int):
    # Генерируем секретное число
    secret_number = random.randint(0, max_range)
    # Вычисляем количество попыток
    attempts_remaining = int(max_range / 2)

    # Создаем метку с оставшимися попытками
    attempts_label = Label(root, text=f"Осталось попыток: {attempts_remaining}", font=("Arial", 14), bg="black",
                           fg="white")
    attempts_label.pack(pady=10)

    # Создаем метку для ввода числа
    guess_label = Label(root, text="Введите ваше число:", font=("Arial", 40), bg="black", fg="white")
    guess_label.pack(pady=10)

    # Создаем поле для ввода числа
    guess_entry = Entry(root)
    guess_entry.pack(pady=30)

    # Создаем метку для вывода результата
    result_label = Label(root, font=("Arial", 14), bg="black", fg="white")
    result_label.pack(pady=20)

    # Функция для проверки числа
    def check_guess():
        nonlocal attempts_remaining

        # Получаем значение введенного числа
        try:
            guess = int(guess_entry.get())
        except ValueError:
            return

        # Проверяем угаданное число
        if guess == secret_number:
            # Если число угадано, выводим сообщение и завершаем игру
            result_label.config(text="Поздравляем! Вы угадали число!")
            attempts_label.pack_forget()
            guess_label.pack_forget()
            guess_entry.pack_forget()
            guess_button.pack_forget()
            root.update_idletasks()
            root.after(5000, restart_game)
        else:
            # Если число не угадано, уменьшаем количество попыток и выводим подсказку
            attempts_remaining -= 1
            attempts_label["text"] = f"Осталось попыток: {attempts_remaining}"

            if attempts_remaining == 0:
                # Если попытки закончились, выводим сообщение о проигрыше и завершаем игру
                result_label.config(text=f"Вы проиграли. Загаданное число: {secret_number}")
                guess_label.pack_forget()
                guess_entry.pack_forget()
                guess_button.pack_forget()
                root.update_idletasks()
                root.after(5000, restart_game)
            else:
                # Выводим подсказку о том, загаданное число больше или меньше введенного
                hint = 'меньше' if secret_number > guess else 'больше'
                result_label.config(text=f'Ваше число {hint} загадонного числа ')

    # Создаем кнопку для проверки числа
    guess_button = Button(root, text="Проверить", font=("Arial", 14), command=check_guess)
    guess_button.pack(pady=10)


# Функция для выхода из игры
def exit_game():
    root.quit()
    root.destroy()


# Функция для перезапуска игры
def restart_game():
    # Удаляем все элементы с экрана
    for widget in root.winfo_children():
        widget.pack_forget()
    # Показываем начальный экран
    name_game.pack()
    play_button.place(x=180, y=200)
    exit_button.place(x=110, y=400)


# Создаем главное окно
root = Tk()
root.title("Игра Угадай число")
root.geometry("600x600+350+200")
root.resizable(width=False, height=False)
root.iconbitmap("number-blocks.ico")
root.config(bg="black")

# Создаем метку с названием игры
name_game = Label(root,
                  text="Игра\n*** Угадай-ка ***",
                  background="blue",
                  borderwidth=40,
                  font=("Arial", 25),
                  foreground="white",
                  relief="ridge"
                  )
name_game.pack()

# Создаем кнопку для начала игры
play_button = Button(root,
                     command=start_game,
                     text="ИГРАТЬ",
                     borderwidth=40,
                     font=("Arial", 25)
                     )
play_button.place(x=180, y=200)

# Создаем кнопку для выхода из игры
exit_button = Button(root,
                     command=exit_game,
                     text="ВЫЙТИ ИЗ ИГРЫ",
                     borderwidth=40,
                     font=("Arial", 25),
                     relief="ridge"
                     )
exit_button.place(x=110, y=400)

# ps
# Запускаем главный цикл обработки событий для окна
root.mainloop()
