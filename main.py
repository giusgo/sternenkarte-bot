from config import get_token
from bot_utils.bot import bot



if __name__ == '__main__':

    # Get Telegram bot TOKEN
    token = get_token()

    # Initial message
    print('Setting up bot...\n')

    bot.setup(token)

    # Final message
    print('\nConnection to the bot ended by the user.')