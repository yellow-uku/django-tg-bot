# import telegram
from telegram import Update
from telegram.ext import CallbackContext
from tgbot.models import User, Contact, Message
from typing import Dict

def reply_to_forward_message(update: Update, context) -> None:
	data = Contact.get_contact_data(update)['user']
	update.message.reply_text(text=f'Recieve forwarded message!\n{data}\nHere is user data:\n{update.message.forward_from}')


def forward_message_handler(update: Update, context) -> None:
	data = Contact.get_contact_data(update)
	contact_data = data['contact']
	user_data = data['user']
	update.message.reply_text(text=f'Recieve forwarded message! Here is user data:\n{contact_data}')
	id = data['contact']['id']
#	tg_user = Contact.get_contact_data(update)['user']['username']
	username = Contact.get_contact_data(update)['contact']['username']
	first_name = Contact.get_contact_data(update)['contact']['first_name']
	last_name = Contact.get_contact_data(update)['contact']['last_name']
	print('CONTACT OBJECTS:\n', Contact.objects.all())
	Contact.objects.create(contact_id=id, contact_username=username, contact_first_name=first_name, contact_last_name=last_name)
