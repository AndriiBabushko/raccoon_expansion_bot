from telegram import *
from telegram.ext import *
from requests import *

with open('raccoons_expansion_bot/token.txt', 'r', encoding='utf-8') as token_file:
    token = token_file.read()

ukrainian: str = 'UKR'
russian: str = 'RU'


def bot_start(update: Update, context: CallbackContext):
    buttons: list = [[KeyboardButton(ukrainian), KeyboardButton(russian)], [KeyboardButton('Help')]]
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to Raccoons Expansion! Pls, choose one language:', reply_markup=ReplyKeyboardMarkup(buttons))


def message_handler(update: Update, context: CallbackContext):
    if ukrainian in update.message.text:
        buttons: list = [[KeyboardButton('Відправити картинку єнотика'), KeyboardButton('Допомога'), KeyboardButton('Повернутися назад')]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Успішно! Ви вибрали правильну сторону.', reply_markup=ReplyKeyboardMarkup(buttons))

    if russian in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Кацапів не підтримуємо! Ідіть за кораблем.')

    if 'Help' in update.message.text or 'Допомога' in update.message.text or '/help' in update.message.text:
        bot_help(update, context)

    if 'Повернутися назад' in update.message.text:
        bot_start(update, context)

    if 'Відправити картинку єнотика' in update.message.text:
        from random import randint
        image_number: int = randint(1, 50)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'raccoons_expansion_bot/img/{image_number}.jpg', 'rb'), caption=f'{image_number} photo of the raccoon')


def bot_help(update: Update, context):
    update.message.reply_text("""
    Бот підтримує наступні команди:
    
    /start -> Початок роботи з ботом
    /help -> Це повідомлення
    """)


updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', bot_start))
dispatcher.add_handler(CommandHandler('help', bot_help))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

updater.start_polling()
updater.idle()
