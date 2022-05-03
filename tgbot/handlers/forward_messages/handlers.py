# import telegram
from telegram import Update
from telegram.ext import CallbackContext

# from tgbot.handlers.location.static_text import share_location, thanks_for_location
# from tgbot.handlers.location.keyboards import send_location_keyboard
# from tgbot.models import User

def reply_to_forward_message(update: Update, context) -> None:
	update.message.reply_text(text=f'Recieve forwarded message! Here is user data:{update.message.forward_from}')
