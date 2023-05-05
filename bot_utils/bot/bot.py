from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, ConversationHandler
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
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    app.add_handler(echo_handler)

    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    app.add_handler(help_handler)


    print('[] Bot up and running.')
    # Run app
    app.run_polling()

    return

