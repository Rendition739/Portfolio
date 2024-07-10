from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
single_joke_func = os.getenv("single_joke_api")

payload = ""
headers = {"User-Agent": "insomnia/8.6.1"}

response = requests.request("GET", single_joke_func, data=payload, headers=headers)
json_data = json.loads(response.text)

request = json_data


async def single_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    set_joke = ("\nRandom joke: ", request["joke"])
    await (context.bot.send_message
           (chat_id=update.effective_chat.id,
            text=("".join(set_joke))))


"""
That's a commented code, which works with API response but only within file.
"""

# def single_joke():
#   request = json_data
#   set_joke = ("\nRandom joke: ", request["joke"])
#   print("".join(set_joke))
#
#
# if __name__ == "__main__":
#     single_joke()
