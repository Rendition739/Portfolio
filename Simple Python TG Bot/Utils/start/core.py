from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
    Hello. My name is Test_bot. I am telegram bot, written on "Python" programming language.
    And let me type that dear user, programming languages and regular languages are completely different things. 
    Regular languages are for people, while programming languages are for us.
    They're used for apps, systems, bots - like me.
    I've introduced myself, so let's begin, shall we?
    If you want to know, what I can offer - type '/help' 
        """)
