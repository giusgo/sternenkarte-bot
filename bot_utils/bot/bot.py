from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from .commands import *



def setup(token):
    '''
    Initial setup for the bot
    '''

    print('[] Authenticating token...')
    # Specific bot app
    app = ApplicationBuilder().token(token).build()
    print('[] Valid token')

    print('[] Adding commands to the bot...')
    # Adding commands
    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    print('[] Bot up and running.')
    # Run app
    app.run_polling()

    return

