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
    '''
    Basic commands
    '''
    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    app.add_handler(help_handler)

    '''
    Stars and constellations commands
    '''
    # Add this

    '''
    Recurrence relations commands
    '''
    recurrence_handler = ConversationHandler(
        entry_points=[CommandHandler('rsolve', rsolve)],
        states={
            RECURRENCE: [MessageHandler(
                filters.TEXT & ~filters.COMMAND, get_initial_values)],
            INITIAL_VALUES: [MessageHandler(
                filters.TEXT & ~filters.COMMAND, show_rsolved)]
        },
        fallbacks=[CommandHandler('cancel', cancel_rsolve)],
    )
    app.add_handler(recurrence_handler)

    '''
    General fallback
    '''
    echo_handler = MessageHandler(filters.TEXT | filters.COMMAND, echo)
    app.add_handler(echo_handler)

    '''
    Run the bot
    '''
    print('[] Bot up and running.')
    # Run app
    app.run_polling()

    return
