import os
import time
import requests
from telegram import InputMediaPhoto, InputMediaVideo
from telegram import Update
from telegram.ext import ExtBot, CallbackContext, MessageHandler, Filters
from telegram.error import BadRequest

API_TOKEN = 'YOUR_API_TOKEN'
SOURCE_CHANNEL_ID = SOURCE_CHANNEL_ID
TARGET_CHANNEL_ID = SOURCE_CHANNEL_ID
REQUEST_URL = f'https://api.telegram.org/bot{API_TOKEN}/getUpdates'

bot = ExtBot(API_TOKEN)

# Set the START_MESSAGE_ID to the desired message ID (36 in this case)
START_MESSAGE_ID = YOUR_MESSAGE_ID

def main():
    current_message_id = START_MESSAGE_ID

    while True:
        try:
            bot.forward_message(chat_id=TARGET_CHANNEL_ID, from_chat_id=SOURCE_CHANNEL_ID, message_id=current_message_id)
            current_message_id += 1
        except BadRequest as e:
            if str(e) == "Message to forward not found" or str(e) == "The message can't be forwarded":
                current_message_id += 1
                continue
            else:
                print(f"Error forwarding message {current_message_id}: {e}")
                break
        except Exception as e:
            print(f"Error forwarding message {current_message_id}: {e}")
            break

        # Forward messages every 15 seconds
        time.sleep(15)

if __name__ == "__main__":
    main()
