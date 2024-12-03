from telegram.ext import ContextTypes
from telegram import Update


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        If you have some trouble - here's the list of commands that can help:
        /random_joke - I'll show random joke to you.
        /single_joke - Same as /random_joke, but more simple.
        /start - I'll activate (how original)
        /help - I'll show all commands, that I can offer.
        /cancel - I'll stop a conversation.
        /gen_rand_num - I'll generate random number from 1 to 1 million.
        """)
