import os


"""
    TOKEN generado por @BotFather en Telegram

    Este TOKEN corresponde a @cesar_julio_bot creador por:
    Giuseppe Gomez, Edgar Torres y Juan Padilla
"""
def get_token():

    # Chequear si NO hay un TOKEN como variable de ambiente
    if os.environ.get('TELEGRAM_TOKEN') is None:

        TOKEN = input('Ingrese el token de Telegram: ')
        os.environ['TELEGRAM_TOKEN'] = TOKEN

    return TOKEN