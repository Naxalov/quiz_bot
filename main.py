from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, PollAnswerHandler, PollHandler
import read_data

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name}!')
   
updater = Updater('5054783826:AAHDvhvejpjNAYnmeiAT5VPcgCfmzVUpnZ8')

def document(update,context):
    bot = context.bot
    document = update.message.document
    doc = context.bot.get_file(document).download()
    data = read_data.read_data_csv(doc)
    chennal_id = -1001445417275

    for quiz in data:
        question = quiz['question']
        image_link = quiz['image_link']
        options = [quiz['option01'],quiz['option02'],quiz['option03'],quiz['option04']]
        bot.sendPhoto(chennal_id,image_link,caption='#python #test #print')
        bot.send_poll(chennal_id,question,options,is_anonymous=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.document,document))

updater.start_polling()
updater.idle()