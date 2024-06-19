import logging
from telegram import Update
from telegram.ext import *
from dotenv import dotenv_values
import asyncio 
from typing import Final 
from helpers import * 

# varaibles
queue = asyncio.Queue()

env = dotenv_values('.env')
token = env.get('TELEGRAM')

BOT_USERNAME: Final = '@feasttBot'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting bot...')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I am feastBot, send me your ingredients and let me whip up some recipes for you')

async def recipe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text 
    chat_id = update.message.chat_id 

    text = text.split()[1:]
    text = ''.join(text)

    recipe_data = generate_recipe(text[0]) 

    recipe_template = f"""
                          Meal:  {recipe_data['meals'][0]['meal']}

                        ========== RECIPE =============
                        {recipe_data['meals'][0]['recipe']}
                        """ 

    await context.bot.send_message(chat_id=chat_id, text=recipe_template)

    #await update.message.reply_text('Hello there! send me a list of your ingredients and allow me to whip up an amazing recipe for you')

async def daily_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I am feastBot, let me get you a full days feast')

async def weekly_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I am feastBot, what are yout thoughts on a full weekly meal plan erh')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I am feastBot, what help do you need?')

def handle_responses(text: str) -> str:
    text = text.lower()
    if 'hello' in text or 'hi' in text:
        return """
                Hello i am feastBot, use /recipe to and send me your ingredients and i'll be back with an amazing meal shortly 
                """

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type 
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip() 
            response: str = handle_responses(new_text)

        else:
            return 
    
    else:
        response: str = handle_responses(text) 

    print('Bot: ', response)
    await update.message.reply_text(response) 

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f'Update {update} caused error {context.error}') 


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('recipe', recipe_command))
    app.add_handler(CommandHandler('daily', daily_command))
    app.add_handler(CommandHandler('weekly', weekly_command))
    app.add_handler(CommandHandler('help', help_command))



    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval = 1.0)
    