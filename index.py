#!/usr/bin/python3

import cgi
import cgitb

cgitb.enable()

from telegram.ext import Updater

TG_CHAT_ID = -463207868
TG_BOT_TOKEN = '736664895:AAHu6fiJso4ZtfAJCsUBQ6FOUW9IewN0SNY'
PARAMS = [
    {
        'name': 'name',
        'mandatory': True,
        'i18n': 'Имя'
    },
    {
        'name': 'tel',
        'mandatory': True,
        'i18n': 'Телефон'
    },
    {
        'name': 'comment',
        'mandatory': False,
        'i18n': 'Комментарий'
    }
]


def build_message(form):
    text = 'Новый заказ:\n'

    for param in PARAMS:
        if param['name'] in form:
            text += param['i18n'] + ": " + form[param['name']] + '\n'
        elif param['mandatory']:
            text += 'Не указан обязательный параметр ' + param['i18n'] + '\n'
    return text


def send_notification(msg):
    updater = Updater(TG_BOT_TOKEN, use_context=True)
    updater.bot.send_message(TG_CHAT_ID, msg)
    return


form = cgi.FieldStorage()
msg = build_message(form)
send_notification(msg)

print("Content-Type: text/html\n\n")
print("""
<p>Надо бы сверстать страницу с текстом "ок, вы подписались" и ещё одну "не вышло подписаться, потому что вы мудак"</p>
""")
