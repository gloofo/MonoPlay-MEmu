from turtle import update
from telegram import Update,Bot
from telegram.ext import Updater,MessageHandler,Filters
from telegram.utils.request import Request
import os,json


pwd = ("6469822803:AAHc--K-47bW6SfF1xunb-fXGVgKCZbbNSQ")

def mesaage_handler(update,context):
    user_message=update.message.text
    os.system('cls')
    print(user_message) 


def main():
    req=Request(connect_timeout=0.5)
    t_bot=Bot(request=req,token=pwd)
    updater=Updater(bot=t_bot,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.all,callback=mesaage_handler))
    updater.start_polling()

    