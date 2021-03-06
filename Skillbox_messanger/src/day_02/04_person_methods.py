"""
Пример программы для работы с ООП

Сделать
- добавить метод для вывода сообщений с префиксом имени
- добавить метод для вывода информации об объекте
- добавить конструктор класса для формирования полей
"""

"""
В этом примере этот класс мы дополним специальными методами, которые нужны для того,
что бы вызывать операции относительно объекта. 
"""
class Person:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# Создадим два метода, которые будут работать по принципу нашей собственной функции
    def info(self):
        print(f"{self.first_name} {self.last_name}, age: {self.age}")

    # say - произнести
    def say(self, content):
        print(f"<{self.first_name}>: {content}")



"""
    Есть системные (готовые) уже за ранее написанные функции, которые в питоне так же вызываются 
через def внутри класса и через два нижних подчеркивания.
__init__(self) - Иниацилизация объекта - конструктор к которому мы обращаемся при 
создании нового объекта класса Person 
self - сам или обратиться самому к себе. Когда мы пишем self то объект понимает, что мы хотим 
к нему что-то вызвать, присвоить, добавить и т.д.

    Теперь если мы не будем передавать в Person три обязательных параметра, то питон будет выдавать 
ошибку. В итоге наш пользователь теперь создается очень компактно, функционально и при этом мны не 
делаем каких то лишних действий
"""
user1 = Person("Aleksandr", "Izotov", 22)
user2 = Person("John", "Don", 30)

user1.info()
user1.say("Hello")