from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        """
              As you wish. You can type /start, if you wish to talk to me later.
              I'm gonna sleep right now.
              """, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
