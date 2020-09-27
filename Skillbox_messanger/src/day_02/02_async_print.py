"""
Пример программы для работы с асинхронностью

Данные
- пользователь вводит число X

Сделать
- асинхронную функцию, которая запустится X раз
- функция должна считать от 0 до числа X
- между выводом чисел должны быть паузы по 0,5 сек

Синхронные функции - функции, которые выполняются последовательно, одна за другой
Асинхронные функции - функции, которые могут выполняться одновременно. Для этого
требуется больше оперативной памяти и мощный процессор
"""
import asyncio

"""
Для каждого временного числа в диапазоне Х нужно вывести number
range(x) - формирует список из чисел от 0 до X (не включает само значение Х)
"""
async def print_counter(x:int):                     #  async - ключевое слово, которое указывает на асинхронную операцию
    for number in range(x):
        print(number)
        await asyncio.sleep(.5)                     # Sleep - поспать, т.е. подожать 0.5 сек

async def start(x:int):
    corountines = []                                # Corountines - асинхронная операция, которая имеет время жизни

    for _ in range(x):                              # Нижниее подчеркивание - переменная, которая никому не нужна и
                                                    # питон ее не сохраняет

        corountines.append(                         # append - добавляет значения в конец списка
           asyncio.create_task(print_counter(x))    # create_task - "создай задачу". Результат print_counter будет
                                                    # сохранен в специальную задачу и эта задача будет сложена в
                                                    # очередь corountines, после чего эти corountines должны быть
                                                    # запущены
        )

    await asyncio.wait(corountines)                 # Подожди пока все corountines закончатся. Это ожидание и есть
                                                    # запуск на выполнение. Await - дождаться результата и только потом
                                                    # его return

user_count = int(input("Количество функций >>>"))

asyncio.run(start(user_count))
"""
asyncio запускает в асинхронном режиме функцию start c количеством, которое укажет пользователь.
Сама функция start создаст по кол-ву несколько других функций, которые будут считать от 0 да Х.
Если функция работает долго то делаем ее асинхронной.
"""
