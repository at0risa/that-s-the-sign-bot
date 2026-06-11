import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import start_handler, message_handler, help_handler
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start_handler))
app.add_handler(CommandHandler("message", message_handler))
app.add_handler(CommandHandler("help", help_handler))
print("Bot is running...")
app.run_polling()



