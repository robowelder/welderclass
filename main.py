
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
import cv2
import numpy as np
from ultralytics import YOLO
from IPython.display import Image

# trained model 
model = YOLO('best.pt')
#model = YOLO('yolov8n.pt')

#bot

def start(updater, context):
    updater.message.reply_text("Привет ! \n Отправь картинку \ud83d\udd2e")

def help_(updater, context):
    updater.message.reply_text("парарарпрп \ud83d\udd2e")

def message(updater, context):
    updater.message.reply_text('Dont write anything  \n Just send a picture \ud83d\udc41 \ud83d\udc41')

def image(updater, context):
    photo = updater.message.photo[-1].get_file()
    photo.download("img.jpg")
    model.predict(source= "img.jpg" ,save_txt=True ,save=True,exist_ok=True)
# sending prediction to user
bot = Updater(token='6775806362:AAF6kkrbwpJPb0Xz3ypmSWytuLSgfA10qsA')
def send_image(updater, context):
    photo = updater.message.photo[-1].get_file()
    photo.download("img.jpg")
    model.predict(source= "img.jpg" ,save_txt=True ,save=True,exist_ok=True)
    chat_id = updater.message.chat_id

# Replace image_path with the path to your image
    photo = open('/content/runs/detect/predict/img.jpg', 'rb')
    bot.send_photo(chat_id=chat_id, photo=photo)

updater = Updater('6775806362:AAF6kkrbwpJPb0Xz3ypmSWytuLSgfA10qsA')
dispatcher = updater.dispatcher

# Handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help_))
dispatcher.add_handler(MessageHandler(Filters.text, message))
dispatcher.add_handler(MessageHandler(Filters.photo, send_image))
dispatcher.add_handler(CommandHandler('send_image', send_image))

updater.start_polling()
updater.idle()

import sys
values = sys.modules.keys()
with open("file.txt", "w") as output:
    output.write(str(values))
