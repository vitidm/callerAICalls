import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler

# Define the function for forwarding the message
def forward_message(update, context):
    chat_id = None
    message_text = None
    
    if update.message:
        chat_id = update.message.chat_id
        message_text = update.message.text
    elif update.channel_post:
        chat_id = update.channel_post.chat_id
        message_text = update.channel_post.text
    
    if chat_id == -1001945564480:
        message_text = message_text.split("-")[0].strip()
        message_text = "<i>" + message_text + "</i>"
        message_text = "<b>🤖 Call Alert!\n--------------------\n\n</b>" + message_text
        
        keyboard = [[InlineKeyboardButton("Check Call", url='https://t.me/CAIcalls'),
                     InlineKeyboardButton("Website", url='https://www.callerai.tech/')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=-1001965203036, text=message_text, parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
# Define the function for handling the button response
def button_click(update, context):
    query = update.callback_query
    data = query.data

    # You can add the logic to handle the button response here

# Create the updater and dispatcher to handle messages
updater = Updater(token='5814713525:AAHx_J2RG_FCg9C-au4qmsGYrb12cUXTYcA', use_context=True)
dispatcher = updater.dispatcher

# Create the message handler and add it to the dispatcher
message_handler = MessageHandler(Filters.all, forward_message)
dispatcher.add_handler(message_handler)

# Create the handler for handling button response and add it to the dispatcher
button_handler = CallbackQueryHandler(button_click)
dispatcher.add_handler(button_handler)

# Start the bot
updater.start_polling()
