'''
This file contains all the functions the bot can do

These functions are just command handlers (or wrappers) to the functions described
in constellations/ and recurrence_relations/
'''

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    Introductory message
    '''

    response = '''
    Hi
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)