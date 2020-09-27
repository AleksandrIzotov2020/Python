"""
Пример программы для работы с ООП

Сделать
- класс User от класса Person
- добавить поле для пароля
- добавить метод проверки пароля
"""

"""
    Наследование - это одна из систем ООП, которая позволяет нам не только создавать свои собственные
 типы данных, но и расширять уже существующие 
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


class User(Person):     # Таким образом мы указываем от какого класса мы хотим забраь все функциональные возможности
    password: str

    def check_password(self, user_password):
        return self.password == user_password


user1 = User("Aleksandr", "Izotov", 22)
user2 = User("John", "Don", 30)

user1.info()
user1.say("Hello")
user1.password = "swimming1998"
print(user1.check_password("456456"))
print(user1.check_password("swimming1998"))