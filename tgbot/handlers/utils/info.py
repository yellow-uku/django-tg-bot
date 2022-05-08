from functools import wraps
from typing import Dict, Callable, Tuple

import telegram
from telegram import Update


def send_typing_action(func: Callable):
    """Sends typing action while processing func command."""
    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=telegram.ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)

    return command_func


def extract_user_data_from_update(update: Update) -> Dict:
    """ python-telegram-bot's Update instance --> User info """
    if update.message is not None:
        user = update.message.from_user.to_dict()
    elif update.inline_query is not None:
        user = update.inline_query.from_user.to_dict()
    elif update.chosen_inline_result is not None:
        user = update.chosen_inline_result.from_user.to_dict()
    elif update.callback_query is not None and update.callback_query.from_user is not None:
        user = update.callback_query.from_user.to_dict()
    elif update.callback_query is not None and update.callback_query.message is not None:
        user = update.callback_query.message.chat.to_dict()
    else:
        raise Exception(f"Can't extract user data from update: {update}")

    return dict(
        user_id=user["id"],
        is_blocked_bot=False,
        **{
            k: user[k]
            for k in ["username", "first_name", "last_name", "language_code"]
            if k in user and user[k] is not None
        },
    )

def extract_contact_data_from_update(update: Update) -> Dict:
    """ python-telegram-bot's Update instance --> Contact info """
#   print('MESSAGE:\n', update.message)
    if update.message.forward_from is not None:
        contact = update.message.forward_from
        user = update.message.from_user.to_dict()
        #user.save()
    else:
        raise Exception(f"Can't extract contact data from update: {update}")
    data = dict()
    data['contact'] = contact
    data['user'] = user
    return data
"""
    return dict(
        user_id=user["id"],
        is_blocked_bot=False,
        **{
            k: user[k]
            for k in ["username", "first_name", "last_name", "language_code"]
            if k in user and user[k] is not None
        },
    )
    elif update.inline_query is not None:
        user = update.inline_query.forward_from.to_dict()
    elif update.chosen_inline_result is not None:
        user = update.chosen_inline_result.forward_from.to_dict()
    elif update.callback_query is not None and update.callback_query.forward_from is not None:
        user = update.callback_query.forward_from.to_dict()
    elif update.callback_query is not None and update.callback_query.message is not None:
        user = update.callback_query.message.chat.to_dict()
    """