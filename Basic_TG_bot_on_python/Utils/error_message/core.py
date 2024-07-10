from telegram import Update
from telegram.ext import ContextTypes


async def error_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Maybe you don't know what to type and you're somewhat confused.\n"
                                    f"To avoid that, type '/help.' \n"
                                    f"But not that message: {update.message.text}.")

    await update.message.reply_text("There's a very little I know, comparing to your human minds.\n"
                                    "So please, be more careful what you're typing.")