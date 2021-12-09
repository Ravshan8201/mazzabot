from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from func import *
from cons import *
upd = Updater(token=TOKE, workers=4)
dis = upd.dispatcher
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CallbackQueryHandler(pattern='admin', callback=admin))
dis.add_handler(CallbackQueryHandler(pattern='aksiya_tamom', callback=aksiya_tamom))
dis.add_handler(CallbackQueryHandler(pattern='sov', callback=sov))
dis.add_handler(CallbackQueryHandler(pattern='ru', callback=ru))
dis.add_handler(CallbackQueryHandler(pattern='uz', callback=uz))
dis.add_handler(MessageHandler(Filters.text, next_func))
dis.add_handler(MessageHandler(Filters.contact, get_contac))
dis.add_handler(MessageHandler(Filters.photo, adm))
dis.add_handler(MessageHandler(Filters.video, adm_v))
upd.start_polling(drop_pending_updates=True)
