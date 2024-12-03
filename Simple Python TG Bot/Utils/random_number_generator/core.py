from telegram.ext import ContextTypes
from telegram import Update
import random


async def gen_rand_num(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Your generated number is: {random.randrange(1000000)}")
