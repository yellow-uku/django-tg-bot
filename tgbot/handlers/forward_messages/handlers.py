# import telegram
from telegram import Update
from telegram.ext import CallbackContext
from tgbot.models import User, Contact, Message
from typing import Dict

"""
def reply_to_forward_message(update: Update, context) -> None:
	data = Contact.get_contact_data(update)['user']
	update.message.reply_text(text=f'Recieve forwarded message!\n{data}\nHere is user data:\n{update.message.forward_from}')
"""

def	create_and_check_existence(update: Update, id, username):
	if Contact.objects.filter(contact_id=id) or Contact.objects.filter(contact_username=username):
		return 0
	else:
		return 1

def forward_message_handler(update: Update, context: CallbackContext) -> None:
	data = Contact.get_contact_data(update)
	contact_data = data['contact']
	user_data = data['user']
	update.message.reply_text(text=f'Recieve forwarded message! Here is user data:\n{contact_data}')
	id = Contact.get_contact_data(update)['contact']['id']
	tg = User.get_user(update, context)
#	tg = data['user']['user_id']
	print('TG USER:\n', tg, '\n', 'TYPE OF TG USER:\n', type(tg))
	username = Contact.get_contact_data(update)['contact']['username']
	first_name = Contact.get_contact_data(update)['contact']['first_name']
	last_name = Contact.get_contact_data(update)['contact']['last_name']

	if create_and_check_existence(update, id, username):
		update.message.reply_text(text=f'New contact!')
		Contact.objects.create(contact_id=id, contact_username=username, contact_first_name=first_name, contact_last_name=last_name)
	else:
		update.message.reply_text(text=f'Contact already exists in database')
