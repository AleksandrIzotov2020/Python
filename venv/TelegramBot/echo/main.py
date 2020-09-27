# Файл с основной логикой // Main logic file

# Импорт зависимостей из библиотек // Import dependencies from libraries

from subprocess import Popen
from subprocess import PIPE
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from echo.config import TG_TOKEN


#TG_TOKEN = "1123519624:AAHXnpy5ho5xZ-HB7P56CWU97amPGReELqc"


# Обработчики событий от телеграма // Event handlers from telegram
def do_start(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'Аноним'
    # Отправка сообщения // sending message
    bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Привет, {name}!\nОтправь мне что-нибудь.",

    )

def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Это учебный бот.",
    )

def do_time(bot: Bot, update: Update):
    process = Popen("date", stdout=PIPE)
    text, error = process.communicate()
    if error:
        text = "Ошибка. Невозможно узнать время."
    else:
        text = text.decode("utf-8")

    bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Текущее время: {text}",
    )

# Функция обрабатывающая все входящие текстовые сообщения // Function that processes all incoming text messages
def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = "{}\nВаш ID: {}".format(update.message.text, chat_id)
    bot.send_message(
        chat_id=chat_id,
        text=f"Вы отправили мне: {text}",
    )


# Основная функция // Main function
def main():
    print("__________START__________\n\n")
    # Создаем bot, экземпляр класса Bot, и передаем в него token
    bot = Bot(
        token=TG_TOKEN,
        base_url="http://telegg.ru/orig/bot",
    )
    updater = Updater(
        bot=bot,
    )
    # Обработчики // Handlers
    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
    time_handler = CommandHandler("time", do_time)
    message_handler = MessageHandler(Filters.text, do_echo)

    # Регистрация обработчиков // Registration handler
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

# Код для запуска бота
if __name__ == '__main__':
    main()


