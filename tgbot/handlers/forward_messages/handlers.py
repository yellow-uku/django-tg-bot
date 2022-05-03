# import telegram
from telegram import Update
from telegram.ext import CallbackContext
from tgbot.models import User, Contact, Message

def reply_to_forward_message(update: Update, context) -> None:
	update.message.reply_text(text=f'Recieve forwarded message! Here is user data:\n{update.message.forward_from}')
