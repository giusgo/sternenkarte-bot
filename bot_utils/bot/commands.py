'''
This file contains all the functions the bot can do

These functions are just command handlers (or wrappers) to the functions described
in constellations/ and recurrence_relations/
'''

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler
)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    The bot listens to all non-command messages it receives

    The bot is only trained to respond to 'How are you?' and greetings. If the message it receives is
    not a command, it will ask the user to give one.
    '''

    msg_from_user = update.message.text

    print(f'New message received: {msg_from_user}')

    if msg_from_user.lower() == 'hello' or msg_from_user.lower() == 'hi':
        response = 'Hi!'
    elif msg_from_user.lower() == 'how are you?':
        response = 'Excellent!'
    else:
        response = 'I didn\'t understand you quite well. Try a command in /help.'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    Introductory message
    '''

    response = '''
    Hi! I am SternenKarte, a bot that can be used to query information about stars and constellations.
Also, I have the capacity to solve recurrence relations! Isn't that awesome?

To get started, type the /help command.
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    Help menu
    '''

# Work on this
    response = '''
    In order to get use my capacities, you should know them first:

⚠️ W.I.P (stars and constellations)

And last, but not least:

🔁 Solve recurrence relation (especially, inhomogeneous)
    /rsolve
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


'''
From here below, these are commands to solve recurrence relations
These are conversations to receive multiple inputs from the user
'''

RECURRENCE, INITIAL_VALUES = range(2)


async def rsolve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = '''
    Enter the relation:
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    return RECURRENCE


async def get_initial_values(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = '''
    Enter the initial values:
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    return INITIAL_VALUES


async def show_rsolved(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = '''
    The solution is XD
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    return ConversationHandler.END


async def cancel_rsolve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = '''
    Oh no! You cancelled!
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    return ConversationHandler.END
