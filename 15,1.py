from tkinter import *
import requests

def get_weather():
    city = cityField.get()

    # мой ключ
    key = '294874f25f17a43c0327063b501df7bc'

    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}

    try:
        result = requests.get(url, params=params)
        weather = result.json()

        # Проверка
        if weather.get('cod') != 200:
            info['text'] = 'Город не найден!'
        else:
            temp = weather['main']['temp']
            feels_like = weather['main']['feels_like']
            humidity = weather['main']['humidity']
            wind = weather['wind']['speed']
            description = weather['weather'][0]['description']

            info['text'] = f'''{weather["name"]}, {weather["sys"]["country"]}
Температура: {temp}°C (ощущается как {feels_like}°C)
Влажность: {humidity}%
Ветер: {wind} м/с
{description.capitalize()}'''

    except:
        info['text'] = 'Ошибка! Проверьте интернет'


root = Tk()
root['bg'] = '#fafafa'
root.title('Погодное приложение')
root.geometry('600x300')
root.resizable(False, False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack(pady=5)

btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.35)

info = Label(frame_bottom, text='Введите город и нажмите кнопку', bg='#ffb700', font=('Arial', 9), justify='left')
info.pack(pady=10)

root.mainloop()