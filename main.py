from config import get_token
from telegram.ext import *


if __name__ == '__main__':
    # Get Telegram bot TOKEN
    get_token()

    # Mensaje de inicio
    print('Iniciando bot...')