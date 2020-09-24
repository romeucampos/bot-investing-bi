import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.environ['TELEGRAM_TOKEN']
PORT = int(os.environ.get("PORT", "8443"))
HEROKU_APP_NAME = os.environ.get("bot-telegram-turing")

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# /help
def send_welcome(update, context):
    update.message.reply_text("Comandos: /quant; /nlp; /cv; /rl; /ds")

# Descrição das Areas de foco

# /quant
def send_quant_describe(update, context):
    update.message.reply_text('Essa área de foco tem como principal objetivo estudar as aplicações de programação no mercado financeiro, através de determinadas plataformas. Buscamos, juntos, aprender tanto sobre mercado financeiro quanto sobre aplicações e métodos quantitativos utilizados nesse mercado.')

# /nlp
def send_nlp_describe(update, context):
    update.message.reply_text('Processamento de Linguagem Natural é uma área da inteligência artificial cujo objetivo é a interpretação e manipulação de linguagens humanas. NLP tem muitas tarefas, algumas se relacionam ao processamento mais imediato dos componentes linguísticos, como a análise sintática, morfossintática (POS Tagging), lematização etc.')

# /cv
def send_cv_describe(update, context):
    update.message.reply_text('Em Computer Vision (ou Visão Computacional) trabalhamos principalmente com o processamento de imagens.')

# /rl
def send_rl_describe(update, context):
    update.message.reply_text('O Aprendizado por Reforço é uma das áreas mais únicas do Aprendizado de Máquina, fundamentada em ensinar a um agente como agir em um ambiente a partir de suas experiências.')

# /ds
def send_ds_describe(update, context):
    update.message.reply_text('Data Science (ou Ciência de Dados) é sobre obter insights ou conhecimento através do estudo e análise de dados')

# /start
def send_welcome(update, context):
    update.message.reply_text("Salve, Salve Grupo Turing!")

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():

    updater = Updater(
        TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", send_welcome))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("quant", send_quant_describe))
    dp.add_handler(CommandHandler("nlp", send_nlp_describe))
    dp.add_handler(CommandHandler("ds", send_ds_describe))
    dp.add_handler(CommandHandler("cv", send_cv_describe))
    dp.add_handler(CommandHandler("rl", send_rl_describe))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
    updater.idle()

if __name__ == '__main__':
    main()