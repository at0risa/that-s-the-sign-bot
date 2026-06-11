from telegram import Update
from telegram.ext import ContextTypes, CallbackContext

from services import get_random_message, load_messages

messages = load_messages()

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ That's The Sign\n\n"
        "Я надсилатиму тобі маленькі підтримуючі повідомлення.\n\n"
        "Напиши /message, щоб отримати знак."
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = get_random_message(messages)
    await update.message.reply_text(message)

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ That's The Sign\n\n"
        "Команди:\n"
        "/start — почати\n"
        "/message — отримати підтримуюче повідомлення\n"
        "/help — показати список команд"
    )
