import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repost(message):
    if not message.text.startswith('(') :
        bot.send_message("@shorteez", message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)