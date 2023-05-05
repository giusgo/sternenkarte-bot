'''
This file contains all the functions the bot can do

These functions are just command handlers (or wrappers) to the functions described
in constellations/ and recurrence_relations/
'''

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    The bot listens to all non-command messages it receives

    The bot is only trained to respond to 'How are you?'. If the message it receives is
    not a command, it will ask the user to give one.
    '''

    msg_from_user = update.message.text

    print(f'New message received: {msg_from_user}')

    if msg_from_user.lower() == 'hello' or msg_from_user.lower() == 'hi':
        response = 'Hi!'
    elif msg_from_user.lower() == 'how are you?':
        response = 'Excellent!'
    else:
        response = 'I didn\'t understand you quite well. Try a command like /help.'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    Introductory message
    '''

    response ='''
    Hi! I am SternenKarte, a bot that can be used to query information about stars and constellations.
Also, I have the capacity to solve recurrence relations! Isn't that awesome?

To get started, type the /help command.
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)