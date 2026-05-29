import tkinter as tk
from tkinter import messagebox
import requests


def get_fact():
    # API с интересными фактами (не требует ключа)
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        response = requests.get(url)
        data = response.json()
        fact = data['text']
        label_result.config(text=fact, wraplength=350)
    except:
        label_result.config(text="Ошибка! Проверьте интернет")


def get_year_fact():
    year = entry_year.get()
    if not year:
        messagebox.showwarning("Ошибка", "Введите год")
        return

    # API с историческими событиями по годам
    url = f"http://numbersapi.com/{year}/year"

    try:
        response = requests.get(url)
        fact = response.text
        label_result.config(text=fact, wraplength=350)
    except:
        label_result.config(text="Ошибка!")


# Создаём окно
window = tk.Tk()
window.title("Исторические факты")
window.geometry("450x300")

tk.Label(window, text="Случайный факт:").pack(pady=5)
tk.Button(window, text="Получить факт", command=get_fact).pack(pady=5)

tk.Label(window, text="--- или ---").pack(pady=10)

tk.Label(window, text="Год (например, 1066):").pack(pady=5)
entry_year = tk.Entry(window, width=20)
entry_year.pack(pady=5)
tk.Button(window, text="Факт о годе", command=get_year_fact).pack(pady=5)

label_result = tk.Label(window, text="", font=("Arial", 10), justify="left")
label_result.pack(pady=15)

window.mainloop()