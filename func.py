import random

import telegram
from logger import logger
from telegram.error import BadRequest
from telegram.ext import updater

from cons import *
from cons import dct
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove
from time import sleep
from sql_cons import *
from sql_cons_promo import *

import sqlite3


def start(update, context):
    user_id = update.message.chat_id
    f_name = update.message.from_user.first_name

    context.bot.send_message(chat_id=user_id, text='{}, 👋🙃'.format(f_name))
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    stage_update = cur.execute(stage.format(user_id)).fetchall()
    cur.execute(stagee.format('{}', user_id).format(1))
    connect.commit()
    promoc.clear()
    promoca.clear()
    vvv.clear()
    try:
        TG_ID = TG_ID[0][0]

    except Exception:
        pass
    if user_id != TG_ID:
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()

        knopka_lang = [
            InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru')
        ]
        knopka_lang1 = [
            InlineKeyboardButton(text='''O'zbek tili🇺🇿''', callback_data='uz')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang, knopka_lang1]))

    if TG_ID == user_id:
        if 2071126215 == user_id:
            context.bot.send_message(text='👋👋👋', chat_id=user_id, )

        else:
            lang_ = cur.execute(lang_select.format(user_id)).fetchall()
            connect.commit()
            lang_ = lang_[0][0]
            k_but = [KeyboardButton(text=dct[lang_][0])]
            context.bot.send_message(text='👋👋👋', chat_id=user_id,
                                     reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True))
            cur.execute(stagee.format('{}', user_id).format(2))
            connect.commit()
    if TG_ID == 2071126215:
        knop = [InlineKeyboardButton(text='''Sovg'a qo'shish➕🎁🛒''', callback_data='admin')]
        Kmo = [InlineKeyboardButton(text='''Hamma sovg'ani o'chirish🚫🚫🚫''', callback_data='aksiya_tamom')]
        Km = [InlineKeyboardButton(text='''Sov'galar''', callback_data='sov')]
        context.bot.send_message(chat_id=user_id, text='Admin panel',
                                 reply_markup=InlineKeyboardMarkup([knop, Kmo, Km]))


def next_func(update, context):
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    f_name = update.message.from_user.first_name
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()
    message = update.message.text
    message = str(message)
    stage_ = stage_[0][0]
    lang_ = lang_[0][0]
    if message.lower() == 'davom etish>>>' and stage_ == 2 or message.lower() == 'далее>>>' and stage_ == 2 or stage_ == 50 or message == \
            dct[lang_][0] and stage_ == 2:
        _but = [KeyboardButton(text='далее>>>')]
        context.bot.send_message(text=dct[lang_][16], chat_id=user_id,
                                 reply_markup=ReplyKeyboardRemove([_but], resize_keyboard=True,
                                                                  one_time_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(3))
        connect.commit()
    x = 0
    promo = cur.execute('''
    SELECT Promo
    FROM Promo_list
    WHERE Promo !=0
    ''').fetchall()
    for e in promo:
        e = e[0]

        Promocod = e == message

        if Promocod and stage_ == 3:
            q = e
            user_list.append(q)
            cur.execute(upd_pro.format('{}', user_id).format(q))
            connect.commit()
            x += 1
            cur.execute(stagee.format('{}', user_id).format(3))
            connect.commit()
            break

    if x == 1 and stage_ == 3:
        try:
            n = cur.execute(name_ru_id.format(message)).fetchall()
            n = n[0][0]
            b = cur.execute(name_uz_id.format(message)).fetchall()
            b = b[0][0]
            vvv.append(b)
            connect.commit()

            if lang_ == 1 and stage_ == 3:
                context.bot.send_message(chat_id=user_id, text=dct[lang_][15].format(n))
                cur.execute(stagee.format('{}', user_id).format(4))
            else:
                context.bot.send_message(chat_id=user_id, text=dct[lang_][15].format(b))
            cur.execute(stagee.format('{}', user_id).format(4))
            connect.commit()
            delete.append(message)
        except:
            sayt = [InlineKeyboardButton(text='📨Telegram', url='https://t.me/mazzami_sizlarga_mazza'),
                    InlineKeyboardButton(text='📸Instagram',
                                         url='https://instagram.com/mazzami_sizlarga_mazzami?utm_medium=copy_link'),
                    InlineKeyboardButton(text='📺YouTube',
                                         url='https://youtube.com/channel/UClwA3tMaxWmTfDjcniyVh6Q'),
                    ]
            syt = [InlineKeyboardButton(text=' 🌐Website', url='http://mazzami-sizlarga.uz/')]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][10],
                                     reply_markup=InlineKeyboardMarkup([sayt, syt]))
            context.bot.send_message(chat_id=user_id, text=dct[lang_][2])

    if x != 1 and stage_ == 3:
        if message == 'davom etish>>>' or message == 'далее>>>':
            pass
        else:
            sayt = [InlineKeyboardButton(text='📨Telegram', url='https://t.me/mazzami_sizlarga_mazza'),
                    InlineKeyboardButton(text='📸Instagram',
                                         url='https://instagram.com/mazzami_sizlarga_mazzami?utm_medium=copy_link'),
                    InlineKeyboardButton(text='📺YouTube',
                                         url='https://youtube.com/channel/UClwA3tMaxWmTfDjcniyVh6Q'),
                    ]
            syt = [InlineKeyboardButton(text=' 🌐Website', url='http://mazzami-sizlarga.uz/')]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][10],
                                     reply_markup=InlineKeyboardMarkup([sayt, syt]))
            context.bot.send_message(chat_id=user_id, text=dct[lang_][2])
        cur.execute(stagee.format('{}', user_id).format(3))
        connect.commit()
    promocod_ = cur.execute(select_pro.format(user_id)).fetchall()
    promocod_ = promocod_[0][0]

    stage_ = cur.execute(stage.format(user_id)).fetchall()
    connect.commit()
    stage_ = stage_[0][0]
    # IIIISSSSSMMMMM
    if stage_ == 4:
        context.bot.send_message(chat_id=user_id, text=dct[lang_][14])
        cur.execute(stagee.format('{}', user_id).format(5))
        connect.commit()
    # IIIIISSSSSSMMMM
    if message != promocod_ and stage_ == 5:
        cur.execute(upd_name.format('{}', user_id).format(message))
        connect.commit()
        cur.execute(stagee.format('{}', user_id).format(6))
        connect.commit()

    # KOOOONNNTTTTTAAAACCCCTTTT
    name = cur.execute(select_name.format(user_id)).fetchall()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    connect.commit()
    stage_ = stage_[0][0]
    name = name[0][0]
    if stage_ == 6:
        b = [KeyboardButton(text=dct[lang_][4], request_contact=True)]

        context.bot.send_message(chat_id=user_id, text=dct[lang_][5].format(name),
                                 reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True, one_time_keyboard=True))
        sleep(1)
        cur.execute(stagee.format('{}', user_id).format(7))
        connect.commit()
    ###YYYYYYAAAASHAsh
    if stage_ == 8:
        message = str(message)
        cur.execute(upd_dom.format(message, user_id))
        connect.commit()
        name_ = cur.execute(select_name.format(user_id)).fetchall()
        num_ = cur.execute(select_num.format(user_id)).fetchall()
        dom = cur.execute(select_dom.format(user_id)).fetchall()
        promodod = cur.execute(select_pro.format(user_id)).fetchall()
        connect.commit()
        promodod = promodod[0][0]
        connect.commit()
        podarka = cur.execute(name_uz_id.format(promodod)).fetchall()
        connect.commit()
        name_ = name_[0][0]
        num_ = num_[0][0]
        dom = dom[0][0]

        print(promodod)
        podarka = podarka[0][0]
        connect.commit()
        context.bot.send_message(text=dct[lang_][17], chat_id=user_id)
        context.bot.send_message(text=dct[lang_][12], chat_id=user_id)

        context.bot.send_message(chat_id=2071126215,
                                 text='Ismi: {}\nTelefon nomeri: {}\nManzil: {}\nPromokod: {}\n Podarka: {}'.format(
                                     name_, num_, dom, promodod, podarka))
        cur.execute(upd_dom.format('{}', user_id).format(message))
        connect.commit()
        cur.execute('''DELETE FROM Promo_list WHERE Promo =='{}' '''.format(delete[0]))
        print(delete[0])
        connect.commit()
        delete.clear()
        cur.execute(stagee.format('{}', user_id).format(9))
        connect.commit()
    if stage_ == 8:
        context.bot.send_message(text=':)', chat_id=user_id)

    ###AAAAAAAADDDDDMMMMIIIINNNNN___MMEENNNYYYUUU

    if stage_ == 100 and message != '/admin':
        context.bot.send_message(chat_id=user_id, text='Sovagni 🇺🇿Uzbek🇺🇿 tilidagi nomini yozing:')
        cur.execute(stagee.format('{}', user_id).format(101))
        connect.commit()
        cur.execute(first_insetd.format(message))
        connect.commit()
        promokod = cur.execute(promo_id.format(message)).fetchall()
        connect.commit()
        promokod = promokod[0][0]
        promoc.append(promokod)
        print(promoc[0])
    if stage_ == 101 and message != promoc[0]:
        cur.execute(name_uz_upd.format(message, promoc[0]))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text='Sovgani 🇷🇺Ruz🇷🇺 tilidagi nomini yozing:')
        cur.execute(stagee.format('{}', user_id).format(102))
        connect.commit()
        promokod1 = cur.execute(name_uz_id.format(promoc[0])).fetchall()
        connect.commit()
        promokod1 = promokod1[0][0]
        promoca.append(promokod1)
        print(promoca[0])
    if stage_ == 102 and message != promoca[0]:
        cur.execute(name_ru_upd.format(message, promoc[0]))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text='TAYYOR✅✅✅')
        knop = [InlineKeyboardButton(text='''Sovg'a qo'shish➕🎁🛒''', callback_data='admin')]
        Kmo = [InlineKeyboardButton(text='''Hamma sovg'ani o'chirish🚫🚫🚫''', callback_data='aksiya_tamom')]
        Km = [InlineKeyboardButton(text='''Sov'galar''', callback_data='sov')]
        context.bot.send_message(chat_id=user_id, text='Admin panel',
                                 reply_markup=InlineKeyboardMarkup([knop, Kmo, Km]))
        cur.execute(stagee.format('{}', user_id).format(2))
        connect.commit()
        promoc.clear()
        promoca.clear()


def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(text='нажмите на кнопку далее...', chat_id=user_id,
                             reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True))


def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='davom etish>>>')]
    context.bot.send_message(chat_id=user_id, text='davom etamish tugmasini bosing...',
                             reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True))


def get_contac(update, context):
    user_id = update.message.chat_id

    num = update.message.contact.phone_number
    name = update.message.from_user.first_name
    num = str(num)
    conn = sqlite3.connect('user_list.sqlite')
    cur = conn.cursor()

    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    conn.commit()
    stage_ = stage_[0][0]
    lang_ = lang_[0][0]
    if stage_ == 7:
        cur.execute(update_phone_num.format(num, user_id))
        cur.execute(stagee.format('{}', user_id).format(8))
        conn.commit()

        _but = [KeyboardButton(text=dct[lang_][13])]
        context.bot.send_message(text=dct[lang_][13], chat_id=user_id,
                                 reply_markup=ReplyKeyboardRemove([_but], resize_keyboard=True,
                                                                  one_time_keyboard=True))
    else:
        pass


def adm(update, context):
    user_id = update.message.chat_id
    for e in admindct[1]:
        if user_id == e:
            text = update.message.caption
            photo_id = update.message.photo[-1].file_id
            file = context.bot.getFile(photo_id)
            file.download('Picture.jpeg')
            if text == None:
                pass
            else:
                try:
                    connect = sqlite3.connect('user_list.sqlite')
                    cur = connect.cursor()
                    id = cur.execute('''
                 SELECT TG_ID
                 FROM Users
                 WHERE TG_ID !=0
                 ''').fetchall()
                    for e in id:
                        e = e[0]
                        context.bot.send_photo(photo=open('Picture.jpeg', 'rb'), chat_id=e, caption=text)
                        sleep(1.5)
                except Exception:
                    continue


def adm_v(update, context):
    user_id = update.message.chat_id
    for e in admindct[1]:
        if user_id == e:
            text = update.message.caption
            photo_id = update.message.video.file_id
            file = context.bot.getFile(photo_id)
            file.download('Video_base/Picture.mp4')
            if text == None:
                pass
            else:
                try:
                    connect = sqlite3.connect('user_list.sqlite')
                    cur = connect.cursor()
                    id = cur.execute('''
                SELECT TG_ID
                FROM Users
                WHERE TG_ID !=0
                ''').fetchall()
                    for e in id:
                        e = e[0]
                        context.bot.send_video(video=open('Video_base/Picture.mp4', 'rb'), chat_id=e, caption=text)
                        sleep(1.5)
                        if TypeError:
                            pass
                except Exception:
                    continue


def admin(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()

    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()

    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()

    stage_ = stage_[0][0]
    for e in admindct[1]:
        if user_id == e:
            context.bot.send_message(chat_id=user_id, text='🎫🎫🎫Promokodni kiritind:')
            cur.execute(stagee.format('{}', user_id).format(100))
            connect.commit()


def aksiya_tamom(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()

    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()

    stage_ = stage_[0][0]
    for e in admindct[1]:
        if user_id == e:
            context.bot.send_message(chat_id=user_id, text="Barcha promokodlar ochirilidi")
            cur.execute('''DELETE FROM Promo_list
         ''')
            connect.commit()


def sov(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()

    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()

    stage_ = stage_[0][0]
    for e in admindct[1]:
        if user_id == e:
            id = cur.execute('''
         SELECT Promo
         FROM Promo_list
         WHERE Promo !=0
         ''').fetchall()
            for e in id:
                e = e[0]
                name_uz = cur.execute('''
             SELECT Name_uz
             FROM Promo_list
             Where Promo = '{}'
             '''.format(e)).fetchall()
                context.bot.send_message(chat_id=user_id, text="Promo-kod: {}\nSovg'a {} ".format(e, name_uz[0][0]))
            x = 0
            for e in id:
                x+=1
            context.bot.send_message(chat_id=user_id, text="Sovg*alar soni:  {}".format(x))



def error_callback(bot, update, error):
    try:
        raise error
    except BadRequest:
        # handle malformed requests - read more below!
        print('Same message')



def error(bot, update, error):
    if not (error.message == "Message is not modified"):
        logger.warning('Update "%s" caused error "%s"' % (update, error))

    updater.dispatcher.logger.addFilter(
        (lambda s: not s.msg.endswith('A TelegramError was raised while processing the Update')))
