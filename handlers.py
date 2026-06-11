from telegram import Update
from telegram.ext import ContextTypes, CallbackContext

from services import get_random_message, load_messages

user_languages = {}
async def uk_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_languages[user_id] = "uk"
    await update.message.reply_text("Мову змінено на українську 🇺🇦")

async def en_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_languages[user_id] = "en"
    await update.message.reply_text("Language changed to English 🇬🇧")
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ That's The Sign\n\n"
        "Я надсилатиму тобі маленькі підтримуючі повідомлення.\n\n"
        "Напиши /message, щоб отримати знак."
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    language = user_languages.get(user_id, "uk")
    message = get_random_message(language)
    await update.message.reply_text(message)

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ That's The Sign\n\n"
        "Команди:\n"
        "/start — почати\n"
        "/message — отримати підтримуюче повідомлення\n"
        "/help — показати список команд"
    )
