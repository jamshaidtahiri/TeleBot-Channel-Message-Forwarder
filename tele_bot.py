import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# -1001895252355
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6099247492:AAF9Y66ioueIrwgbcfUUEcaDpvuTNAPv8hI'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi! I'm your echo bot. Send me any message, and I'll echo it back.")

# def echo(update: Update, context: CallbackContext) -> None:
#     # print(f"Received message from {update.message}: {update.message.text}")
#     update.message.reply_text(update.message.text)

def read_channel(update: Update, context: CallbackContext) -> None:
    if update.channel_post:
        # update.channel_post.reply_text(update.channel_post.text)
        # New channel post
        print(f"Received message from {update.channel_post.chat.title}: {update.channel_post.text}")
        context.bot.send_message(chat_id="-1001956756810", text=update.channel_post.text)
    elif update.edited_channel_post:
        # Edited channel post
        print(f"Edited message from {update.edited_channel_post.chat.title}: {update.edited_channel_post.text}")

# def read_channel(update: Update, context: CallbackContext) -> None:
#     # print(update.channel_post)
#     print(update.channel_post.text)

    # if update.message. == 'channel':
        # You can access the channel message content using update.message.text
        # print(f"Received message from ")
            #   {update.message.chat.title}: {update.message.text}")

def main():
    # Create the Updater and pass your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the command and message handlers
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Add a handler to read messages from the channel
    dp.add_handler(MessageHandler(Filters.text & Filters.chat_type.channel & Filters.chat(-1001895252355), read_channel))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
