import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("Hey! I'm a Rickroll bot. Use the /rickroll command to get a link to a Rickroll video.")

def rickroll(update, context):
    update.message.reply_text("Never gonna give you up, never gonna let you down: https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def help(update, context):
    update.message.reply_text("Use the /start command to start the bot, and the /rickroll command to get a link to a Rickroll video.")

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def send_message(chat_id, text):
    # Replace YOUR_TOKEN_HERE with your actual bot token
    token = "5690956314:AAGX58r-RgvSaiGeXNmBIcnVPJrpYGJ6hWI"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, json=data)

def main():
    # Replace YOUR_TOKEN_HERE and YOUR_WEBHOOK_URL with your actual bot token and webhook URL
    updater = Updater("5690956314:AAGX58r-RgvSaiGeXNmBIcnVPJrpYGJ6hWI", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rickroll", rickroll))
    dp.add_handler(CommandHandler("help", help))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
