from dotenv import load_dotenv
from telegram.ext import ContextTypes
from telegram import Update
import requests
import json
import os

load_dotenv()
joke_func = os.getenv("joke_api")

payload = ""
headers = {"User-Agent": "insomnia/8.6.1"}

response = requests.request("GET", joke_func, data=payload, headers=headers)
json_data = json.loads(response.text)


async def random_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    output = ("Category: ", json_data["category"],
              "\nJoke: ", json_data["setup"],
              "\nDelivery: ", json_data["delivery"])
    await (context.bot.send_message
           (chat_id=update.effective_chat.id,
            text=("".join(output))))

"""
That's a commented code, which works with API response but only within file. 
"""

# def random_joke():
#   request = json_data
#   set_joke = ("\nCategory: ", request["category"], "\n",
#               "Joke: ", request["setup"], "\n",
#               "Delivery: ", request["delivery"])
#   print("".join(set_joke))
#
#
# if __name__ == "__main__":
#     random_joke()


