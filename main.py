import telebot
import os
import time

bot = telebot.TeleBot("5387232805:AAEoln5wfrjoJKBzE3KJM51a8EhjxHufauM")

ruta = os.getcwd() + "/salida/"

@bot.message_handler(comands=["start" , "help"])
def enviar(message)
    bot.reply_to(message, "Bienvenido al bot de Descarga de videos de Youtube de Rey Michel, mi creador es un fantastico creador de bots y me siento orgulloso de ser su creacion.
    /nPara descargar un video aplica el comando /descargar")
@bot.message_handler(comands=[descargar])
def enviar(message)
    bot.reply_to(message, "Ingrese la direccion del video que desea descargar: ")
    a = message.text
    print(a)
    if a == "/descargar":
        @bot.message_handler(func=lambda message:True)
        def descargar(message):
            bot.reply_to(message, "Su video se esta descargando espere un moemnto.......")
            direccion = message.text
            mess = message.chat.id
            print(direccion, mess)
            video = pafy.new(direccion)
            best = cideo.getbest(preftype="mp4")
            best.download(ruta)
            p = ruta + video.title + "mp4"
            video = open(p, "rb")
            return bot.send_document(mess, video)
            
            
            
            
bot.infinity_polling()
