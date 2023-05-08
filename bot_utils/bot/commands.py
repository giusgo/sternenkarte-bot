'''
This file contains all the functions the bot can do

These functions are just command handlers (or wrappers) to the functions described
in constellations/ and recurrence_relations/
'''

from telegram import Update, Chat
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler
)
import sympy as sp
import requests
import io
from ..recurrence_relations.recurrence import *
from ..constellations.main import *
import re


def render_latex(equation):
    '''
    Render a equation in latex
    '''

    response = requests.get(
        'http://latex.codecogs.com/png.latex?\dpi{{1200}} {formula}'.format(formula=equation))

    # Get the HTTP requested image
    imagen_bytes = io.BytesIO(response.content)

    return imagen_bytes


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

❌ You can cancel any of these commands at any time with the command /cancel
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


'''
From here below, these are commands to solve recurrence relations
These are conversations to receive multiple inputs from the user
'''

RECURRENCE, INITIAL_VALUES = range(2)


async def rsolve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    Recurrence relation solver input
    '''

    response = '''
    🔢 Enter the recurrence relation you want to solve. It has to be linear, homogeneous or non-homogeneous and with constant coefficients.

Try to write the function this way:
f(n) = c_1*f(n-1) + c_2*f(n-2) + ... + g(n)    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    return RECURRENCE


async def get_initial_values(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    Initial values input
    '''
        
    response_1 = '''
    You entered the following function:
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_1)

    # Get the function from the user
    function_from_user = update.message.text.split("=")[1]
    context.chat_data['fn'] = function_from_user
    parsed_function = 'f(n) =' + sp.latex(sp.parse_expr(function_from_user))

    # Transform the parsed function to image (latex rendered)
    img = render_latex(parsed_function)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    response_2 = '''
    Now, give me the initial values like this:
f(0) = 1, f(1) = 2, ...
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_2)

    return INITIAL_VALUES


async def show_rsolved(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    Show final result
    '''

    # Retrieve the function asked previously
    function_from_user = context.chat_data['fn']
    initial_conditions = update.message.text

    # Process the function
    solution = solve_recurrence(function_from_user, initial_conditions)

    response_1 = '''
    🤓🧠 The non-recurring form of the function is:
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_1)

    img = render_latex(solution)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    response_2 = '''
    Incredible, isn't it?
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_2)

    return ConversationHandler.END


async def cancel_rsolve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    Cancel option
    '''

    response = '''
    ❌ Cancelled!
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    return ConversationHandler.END

'''
From here below, these are commands to solve constellations problems
These are conversations to receive multiple inputs from the user
'''

CONSTELLATION = range(1)

async def constellations(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    response = '''
    Welcome to constellations menu 🌌🌌💫!
    
    Please select an option of what you'd like to see👀:
    
    1. All stars ✨
    2. All stars and one constellations ✨🌌
    3. All stars and constellations 🌟
    
    Constellations list🗒️:
    
    0. Boyero
    1. Casiopea
    2. Cazo
    3. Cygnet
    4. Geminis
    5. Hydra
    6. OsaMayor
    7. OsaMenor
    
    For instance type: 
    
    All stars for fist option.
    All stars and 0 for second option. (if you want another type the correspondent number)
    All stars and constellations for third option.
    
    FOLLOWING INPUTS ARE NOT ALLOWED ❎❎
    
    All stars Boyero
    All stars 0 1 2 3 
    '''
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    
    return CONSTELLATION

async def get_input_values(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user_input = update.message.text
    
    response = '''
    Fetching data in database👀👀
    '''
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    
    #efecto de escribir 
    
    validation = r'^All stars(?:\sand\s(?:[1-7]|[0]))?$|^All stars and constellations$'
    
    if bool(re.match(validation, user_input.strip())):
        
        req_type = None 
        constelacion = 0
        img_name = ""
        
        if user_input == "All stars":
            
            req_type = "tde"
        
        elif user_input == "All stars and constellations":
            
            req_type = "tddc"
        
        else:
            
            req_type = "tdc"
            constelacion = int(user_input.split(" ")[3])
            
        request = {"req-type": req_type, "constelacion": constelacion} 
        
        img = main(request)
        
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)
    
    else: 
        
        response = '''
        An error has ocurred😥😥
        
        Please check for the input value.
        '''
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    return ConversationHandler.END

