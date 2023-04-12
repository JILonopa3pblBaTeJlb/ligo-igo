import time
import logging
import telegram
from telegram import Update, ParseMode, InputMediaPhoto, InputMediaVideo, InputMediaAnimation, InputMediaAudio, InputMediaDocument
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = "YOUR_BOT_TOKEN"
SOURCE_CHANNEL_ID = source_chanel_id
TARGET_CHANNEL_ID = target_channel_id

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

media_group_cache = {}

def forward_without_author(update: Update, context: CallbackContext):
    if update.channel_post and update.channel_post.chat.id == SOURCE_CHANNEL_ID:
        message = update.channel_post

        if message.media_group_id:
            if message.media_group_id not in media_group_cache:
                media_group_cache[message.media_group_id] = []

            if message.photo:
                media_group_cache[message.media_group_id].append(InputMediaPhoto(
                    media=message.photo[-1].file_id,
                    caption=message.caption,
                    parse_mode=ParseMode.HTML,
                    caption_entities=message.caption_entities
                ))
            elif message.video:
                media_group_cache[message.media_group_id].append(InputMediaVideo(
                    media=message.video.file_id,
                    caption=message.caption,
                    parse_mode=ParseMode.HTML,
                    caption_entities=message.caption_entities
                ))
            return

        if message.photo:
            context.bot.send_photo(chat_id=TARGET_CHANNEL_ID, photo=message.photo[-1].file_id, caption=message.caption, parse_mode=ParseMode.HTML, caption_entities=message.caption_entities)
        elif message.video:
            context.bot.send_video(chat_id=TARGET_CHANNEL_ID, video=message.video.file_id, caption=message.caption, parse_mode=ParseMode.HTML, caption_entities=message.caption_entities)
        elif message.animation:
            context.bot.send_animation(chat_id=TARGET_CHANNEL_ID, animation=message.animation.file_id, caption=message.caption, parse_mode=ParseMode.HTML, caption_entities=message.caption_entities)
        elif message.audio:
            context.bot.send_audio(chat_id=TARGET_CHANNEL_ID, audio=message.audio.file_id, caption=message.caption, parse_mode=ParseMode.HTML, caption_entities=message.caption_entities, title=message.audio.title, performer=message.audio.performer)
        elif message.document:
            context.bot.send_document(chat_id=TARGET_CHANNEL_ID, document=message.document.file_id, caption=message.caption, parse_mode=ParseMode.HTML, caption_entities=message.caption_entities)
        elif message.text:
            copy_kwargs = {'chat_id': TARGET_CHANNEL_ID, 'from_chat_id': SOURCE_CHANNEL_ID, 'message_id': message.message_id, 'disable_notification': True}
            context.bot.copy_message(**copy_kwargs)
        else:
            context.bot.forward_message(chat_id=TARGET_CHANNEL_ID, from_chat_id=message.chat_id, message_id=message.message_id)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.update.channel_posts, forward_without_author))

    last_update_id = None

    while True:
        try:
            updates = updater.bot.get_updates(offset=last_update_id, limit=100, allowed_updates=["channel_post"], timeout=10)
            for update in updates:
                dp.process_update(update)

            if updates:
                last_update_id = updates[-1].update_id + 1

                for message in updates:
                    if message.channel_post and message.channel_post.chat.id == SOURCE_CHANNEL_ID:
                        if message.channel_post.media_group_id and message.update_id != last_update_id - 1:
                            if message.channel_post.media_group_id in media_group_cache:
                                media_group = media_group_cache[message.channel_post.media_group_id]
                                updater.bot.send_media_group(chat_id=TARGET_CHANNEL_ID, media=media_group)
                                del media_group_cache[message.channel_post.media_group_id]

            time.sleep(10)
        except telegram.error.TimedOut:
            logger.warning("Timed out, retrying...")
            continue

    updater.idle()

if __name__ == '__main__':
    main()
