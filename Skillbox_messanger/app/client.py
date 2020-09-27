#
# Клиентское приложение с интерфейсом
#

"""
[1]    Т.к. на этот раз наш протокол должен взаимодействовать с окном или чатом, нам понадобится установить между
ними связь. Самый простой способ - это сделать в момент создания протокола в конструкторе. Для этого укажем, что
принимаем некий chat_window: 'MainWindow'. Далее мы назначем его в некую локальную переменную под названием self.window.
Теперь при создании протокола мы сразу запишем ссылку на окно и всегда сможем обращаться к полям, кнопкам и прочим
элементам интерфейса.

[2]    Необходимо создать протокол. Для этого необходимо class MainWindow заполнить функциями создания этого самого
подключения. Они будут почемены как: "[2]"
"""
import asyncio
from asyncio import transports
from PySide2.QtWidgets import QMainWindow, QApplication
from asyncqt import QEventLoop
from Skillbox_messanger.app.interface import Ui_MainWindow

class ClientProtocol(asyncio.Protocol):  # Логика, отвечающая за подключение и передачу сообщения
    # Инициализатором подключения в этот раз будет не отдельный
    # класс типа Clients, а само приложение (Само окно)
    transport: transports.Transport
    chat_window: 'MainWindow'

    # Конструктор
    def __init__(self, chat_window: 'MainWindow'):  # [1]
        self.window = chat_window

    # Обработчик. Вызывается когда сервер присылает нам чье-то сообщение
    def data_received(self, data: bytes):
        decoded = data.decode()  # Декодируем сообщение
        self.window.append_text(decoded)  # Добавили в общее сообщение

    # Метод, используемый для отправки данных. Он будет принимать сообщения из окна и отправлять его
    # в закодированном виде на сервер, по-этому в качестве аргумента добавляем message: str
    def send_data(self, message: str):
        encoded = message.encode()  # Кодируем сообщение
        self.transport.write(encoded)  # Отрпавляем сообщение на сервер

    # Обработка успешного соединения с сервером
    def connection_made(self, transport: transports.Transport):
        self.window.append_text("Подключено")
        self.transport = transport

    # Обработчик отключения от сервера
    def connection_lost(self, exception):
        self.window.append_text("Отключено")


class MainWindow(QMainWindow, Ui_MainWindow):
    protocol: ClientProtocol

    def __init__(self):
        # Конструктор основного родительского класса
        super().__init__()  # Специальная команда, которая позволяет обращаться не к self объекту, а именно
        # к родительскому классу. super() - своеобразная ссылка, которая говорит, что
        # этот код надо вызвать не у текущего класса, а у того, от которого мы наследовались
        # Вызываем специальный метод, который был создан самим дизайнером для установки интерфейса
        self.setupUi(self)  # Передаем self для того, что бы он знал
        # какое окно настроить
        self.message_button.clicked.connect(self.button_handler)  # Привязка функции обработчика к кнопке

    # Привязка специальных функций к кнопке. button_handler - обработчик кнопки.

    def button_handler(self):
        """
            Мы забираем сообщение из тексового поля, отправляем на сервер и только, когда он нам что-то вернет
        мы будем добавлять его в общее поле. Для этого необходимо создать функцию def append_text, она будет
        принимать некое содержимое, которое придет от другого клиента
        """

        message_text = self.message_input.text()  # Сохранем текст в переменную [2]
        self.message_input.clear()  # Симулируем отправку сообщения путем отчистки поля message_input
        self.protocol.send_data(message_text)  # Передадим текст в протокол для отправки [2]

    def append_text(self, content: str):  # Этот метод будет вызываться из протокола [2]
        self.message_box.appendPlainText(content)  # Добавляем простой текст

    # Функция, создающая новые протоколы
    def bild_protocol(self):
        self.protocol = ClientProtocol(self)  # Создаем протокол и записываем его в форму, а так же самому
        # протоколу передаем себя. Передаем самого себя т.к. в конструкторе класса ClientProtocol мы принимаем
        # chat_window для взяимодействия с интерфейсом т.е. установив связь
        return self.protocol  # Из функции вернули готовый объект

    # Асинхронная функция для запуска клиента для работы с сервером. Здесь необходимо обратьиться к событийному циклу
    async def start(self):
        self.show()
        event_loop = asyncio.get_running_loop()  # Получили активный цикл событий (Коробочка с ф-ми для выполнения)
        coroutine = event_loop.create_connection(  # Те самые функции в коробочке. Создай соединение
            self.bild_protocol,  # Обращаемся к протоколу без скобок вызова
            '127.0.0.1',
            8888
        )

        """
            Т.к сервер может не отвечать, то надо сделать вызов безопасным, звучит он следующим образом:
            "Попробуй подключится к серверу и если в течении секунты подключение не установиться, то иди дальше"
        """
        await asyncio.wait_for(coroutine, 1000)  # Безопасный вызов, 1000 == 1 сек


# Вызываем показ окна
app = QApplication()  # app - приложение - цикл, который знает, что запустить и работает если к нему обратиться
loop = QEventLoop(app)  # Специальная оболочка, которая создат связь между асинхронным интерфейсом и
# асинхронным сервером или клиентом. QEventLoop генерирует событийные модели, по-этому
# мы создаем его для конкретного приложения (app)
asyncio.set_event_loop(loop)  # asyncio должен установить event loop из пециального модуля loop
window = MainWindow()  # Создали окно
#window.show()
loop.create_task(window.start())
loop.run_forever()  # Бесконечный цикл
