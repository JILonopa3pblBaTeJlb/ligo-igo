import os
import logging
import re
import random
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Your Telegram bot token
BOT_TOKEN = "insert_token"

def lexical_reduplication(word):
    vowels = "аеёиоуыэюя"
    vowel_mapping = {"а": "я", "е": "е", "ё": "ё", "и": "и", "о": "ё", "у": "ю", "ы": "ы", "э": "е", "ю": "ю", "я": "я"}

    first_vowel_index = None
    for i, char in enumerate(word):
        if char.lower() in vowels:
            first_vowel_index = i
            break

    if first_vowel_index is None:
        return word

    first_vowel = word[first_vowel_index].lower()
    mapped_vowel = vowel_mapping.get(first_vowel, first_vowel)

    new_word = "ху" + ("" if first_vowel_index == 1 else "й") + mapped_vowel + word[first_vowel_index:]

    # Remove doubled letters
    new_word = "".join(new_word[i] for i in range(len(new_word)) if i == 0 or new_word[i] != new_word[i - 1])

    # Handle specific combinations
    new_word = new_word.replace("ёо", "ё").replace("йю", "ю").replace("яа", "я").replace("юу", "ю").replace("йе", "е")

    if word[0].isupper():
        new_word = new_word.capitalize()

    return new_word

def contains_cyrillic(text):
    return bool(re.search(r'[а-яА-ЯёЁ]', text))

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

def error_handler(update: Update, context: CallbackContext):
    logging.error(msg=f"Update {update} caused error: {context.error}")

def reduplicate(update: Update, context: CallbackContext):
    try:
        message_text = update.message.text.strip()
        if not contains_cyrillic(message_text):
            return

        last_word = message_text.split(" ")[-1]
        last_word_clean = remove_punctuation(last_word.lower())

        logging.info(f"Last word: {last_word}")  # Log the last word

        random_responses = ['не понил', 'ачо всмысли', 'сам понел чо сказал счас', 'поясни']

        if last_word_clean == "да":
            reduplicated_word = "Пизда" if last_word.istitle() else "пизда"
        elif last_word_clean == "нет":
            reduplicated_word = "Пидора ответ" if last_word.istitle() else "пидора ответ"
        elif last_word_clean == "300" or last_word_clean == "триста":
            reduplicated_word = "Отсоси у тракториста" if last_word.istitle() else "отсоси у тракториста"
        elif len(last_word) >= 3 and len(last_word) <= 20 and not last_word.lower().startswith("ху") and contains_cyrillic(last_word):
            reduplicated_word = lexical_reduplication(last_word)
        else:
            reduplicated_word = random.choice(random_responses)

        update.message.reply_text(reduplicated_word)
    except Exception as e:
        logging.error(f"Error while reduplicating: {e}")

def main():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )

    updater = Updater(BOT_TOKEN, use_context=True)

    # Register error_handler
    updater.dispatcher.add_error_handler(error_handler)

    # Update filter to include group and private chats
    updater.dispatcher.add_handler(MessageHandler(Filters.text & (Filters.chat_type.groups | Filters.chat_type.private), reduplicate))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
