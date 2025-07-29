from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import os

BOT_TOKEN = os.getenv("8499142251:AAHh5pnQpHmnT-mtiU_eEHuvQ0e7v9nAdEg")

# Example chapter data
chapter_images = {
    'Chapter 1': ['images/ch1/1.jpg', 'images/ch1/2.jpg'],
    'Chapter 2': ['images/ch2/1.jpg', 'images/ch2/2.jpg'],
}

def start(update, context):
    keyboard = [[InlineKeyboardButton(text=ch, callback_data=ch)] for ch in chapter_images]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose a chapter:", reply_markup=reply_markup)

def button_handler(update, context):
    query = update.callback_query
    query.answer()
    chapter = query.data
    for img_path in chapter_images.get(chapter, []):
        context.bot.send_photo(chat_id=query.message.chat_id, photo=open(img_path, 'rb'))

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
