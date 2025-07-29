from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
import os

# --- Replace this with your Bot Token ---
BOT_TOKEN = '8499142251:AAHh5pnQpHmnT-mtiU_eEHuvQ0e7v9nAdEg'

# --- Mapping Chapters to Folders ---
CHAPTER_IMAGES = {
    'science_chapter1': 'images/chapter1',
    'science_chapter2': 'images/chapter2'
}

# --- Start Command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Science Chapter 1", callback_data='science_chapter1')],
        [InlineKeyboardButton("Science Chapter 2", callback_data='science_chapter2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose a chapter:", reply_markup=reply_markup)

# --- When a Chapter is Tapped ---
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chapter = query.data
    image_folder = CHAPTER_IMAGES.get(chapter)

    if image_folder and os.path.exists(image_folder):
        image_files = sorted(os.listdir(image_folder))
        for file_name in image_files:
            file_path = os.path.join(image_folder, file_name)
            if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                with open(file_path, 'rb') as photo:
                    await query.message.reply_photo(photo=photo)
    else:
        await query.message.reply_text("No images found for this chapter.")

# --- Main Function ---
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
