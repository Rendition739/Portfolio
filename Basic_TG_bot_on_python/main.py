import telegram.error
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from Utils.start.core import start
from Utils.help.core import help
from Utils.joker.core import random_joke
from Utils.joker.core_two import single_joke
from Utils.random_number_generator.core import gen_rand_num
from Utils.cancel.core import cancel
from Utils.error_message.core import error_message
from dotenv import load_dotenv
import os

load_dotenv()
API = os.getenv("tg_api_key")

if __name__ == "__main__":
    application = ApplicationBuilder().token(API).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    help_handler = CommandHandler("help", help)
    application.add_handler(help_handler)

    mirror_me_handler = CommandHandler("error_message", error_message)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, error_message))

    joke_handler = CommandHandler("random_joke", random_joke)
    application.add_handler(joke_handler)

    single_joke_handler = CommandHandler("single_joke", single_joke)
    application.add_handler(single_joke_handler)

    gen_rand_num_handler = CommandHandler("gen_rand_num", gen_rand_num)
    application.add_handler(gen_rand_num_handler)

    cancel_handler = CommandHandler("cancel", cancel)
    application.add_handler(cancel_handler)

    application.run_polling()

if telegram.error.Conflict:
    raise Warning("Sorry but only one bot instance can run at a time.")
elif telegram.error.TimedOut:
    raise ConnectionError("I've tried my best but I wasn't able to connect.\n"
                          "So please try again.")
