from aiogram import types
from misc import dp, bot
from .sqlit import proverka_channel,cheak_traf,reg_user,cheach_status_and_channel,cheak_person,cheak_traf2
import random


reg_user(1,1)

list_channel = cheak_traf()
name_channel_1 = list_channel[0]
name_channel_2 = list_channel[1]
name_channel_3 = list_channel[2]

def obnovlenie():
    global name_channel_1,name_channel_2,name_channel_3
    list_channel = cheak_traf()
    name_channel_1 = list_channel[0]
    name_channel_2 = list_channel[1]
    name_channel_3 = list_channel[2]


@dp.callback_query_handler(text_startswith='start_watch')  # Нажал кнопку Начать смотреть
async def start_watch(call: types.callback_query):
    ### Проверить проценты
    per = cheak_person()
    a = random.randint(1,100)
    if a < int(per[0]): # Выполняется 1 группа
        list_channel = cheak_traf()

        name_channel_1 = list_channel[0]
        name_channel_2 = list_channel[1]
        name_channel_3 = list_channel[2]

        name_channel = call.data[12:]

        # 616 - если админа нету, или массив с данными о канале
        q = cheach_status_and_channel(name_channel)

        if q != 616:
            if int(q[0]) == 3: #ЗАмена каналов если 3 уровень
                try: int(q[1])
                except: name_channel_1 = q[1]

                try: int(q[2])
                except: name_channel_2 = q[2]

                try: int(q[3])
                except: name_channel_3 = q[3]

            if int(q[0]) == 2: #ЗАмена каналов если 2 уровень
                try: int(q[2])
                except: name_channel_2 = q[2]

                try: int(q[3])
                except: name_channel_3 = q[3]

            if int(q[0]) == 1: #ЗАмена каналов если 1 уровень
                try: int(q[2])
                except: name_channel_2 = q[2]



        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🥤Я ПОДПИСАЛСЯ🥤', callback_data=f'check1{name_channel}')
        markup.add(bat_a)

        await bot.send_message(call.message.chat.id, '❌ ДОСТУП ЗАКРЫТ ❌\n\n '
                                                         '👉Для доступа к приватному каналу нужно быть подписчиком <b>Кино-каналов.</b>\n\n'
                                                         'Подпишись на <b>каналы</b> ниже 👇 и нажми кнопку <b>Я ПОДПИСАЛСЯ</b> для проверки!\n\n'
                                                         f'<b>Канал 1</b> - https://t.me/{name_channel_1}\n'
                                                         f'<b>Канал 2</b> - https://t.me/{name_channel_2}\n'
                                                         f'<b>Канал 3</b> - https://t.me/{name_channel_3}', parse_mode='html',reply_markup=markup,disable_web_page_preview=True)
    else:
        list_channel = cheak_traf2()

        name_channel_1 = list_channel[0]
        name_channel_2 = list_channel[1]
        name_channel_3 = list_channel[2]

        name_channel = call.data[12:]

        # 616 - если админа нету, или массив с данными о канале
        q = cheach_status_and_channel(name_channel)

        if q != 616:
            if int(q[0]) == 3:  # ЗАмена каналов если 3 уровень
                try:
                    int(q[1])
                except:
                    name_channel_1 = q[1]

                try:
                    int(q[2])
                except:
                    name_channel_2 = q[2]

                try:
                    int(q[3])
                except:
                    name_channel_3 = q[3]

            if int(q[0]) == 2:  # ЗАмена каналов если 2 уровень
                try:
                    int(q[2])
                except:
                    name_channel_2 = q[2]

                try:
                    int(q[3])
                except:
                    name_channel_3 = q[3]

            if int(q[0]) == 1:  # ЗАмена каналов если 1 уровень
                try:
                    int(q[2])
                except:
                    name_channel_2 = q[2]

        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🥤Я ПОДПИСАЛСЯ🥤', callback_data=f'check2{name_channel}')
        markup.add(bat_a)

        await bot.send_message(call.message.chat.id, '❌ ДОСТУП ЗАКРЫТ ❌\n\n '
                                                     '👉Для доступа к приватному каналу нужно быть подписчиком <b>Кино-каналов.</b>\n\n'
                                                     'Подпишись на <b>каналы</b> ниже 👇 и нажми кнопку <b>Я ПОДПИСАЛСЯ</b> для проверки!\n\n'
                                                     f'<b>Канал 1</b> - https://t.me/{name_channel_1}\n'
                                                     f'<b>Канал 2</b> - https://t.me/{name_channel_2}\n'
                                                     f'<b>Канал 3</b> - https://t.me/{name_channel_3}',
                               parse_mode='html', reply_markup=markup, disable_web_page_preview=True)




@dp.callback_query_handler(text_startswith='check')  # Нажал кнопку Я ПОДПИСАЛСЯ. ДЕЛАЕМ ПРОВЕРКУ
async def check(call: types.callback_query):
    await bot.send_message(call.message.chat.id, '⏳ Ожидайте. Идёт проверка подписки.')
    groop = call.data[5]
    name_channel = call.data[6:]

    list_channel = cheak_traf() # первая группа
    list_channel2 = cheak_traf2() # Вторая группа

    if int(groop) == 1: #ЗАмена для первой группы
        name_channel_1 = list_channel[0]
        name_channel_2 = list_channel[1]
        name_channel_3 = list_channel[2]

    else: #ЗАмена для второй группы
        name_channel_1 = list_channel2[0]
        name_channel_2 = list_channel2[1]
        name_channel_3 = list_channel2[2]

    q = cheach_status_and_channel(name_channel)
    if q != 616:
        if int(q[0]) == 3:  # ЗАмена каналов если 3 уровень
            try:
                int(q[1])
            except:
                name_channel_1 = q[1]

            try:
                int(q[2])
            except:
                name_channel_2 = q[2]

            try:
                int(q[3])
            except:
                name_channel_3 = q[3]

        if int(q[0]) == 2:  # ЗАмена каналов если 2 уровень
            try:
                int(q[2])
            except:
                name_channel_2 = q[2]

            try:
                int(q[3])
            except:
                name_channel_3 = q[3]

        if int(q[0]) == 1:  # ЗАмена каналов если 1 уровень
            try:
                int(q[2])
            except:
                name_channel_2 = q[2]


    proverka1 = (await bot.get_chat_member(chat_id=f'@{name_channel_1}', user_id=call.message.chat.id)).status
    proverka2 = (await bot.get_chat_member(chat_id=f'@{name_channel_2}', user_id=call.message.chat.id)).status
    proverka3 = (await bot.get_chat_member(chat_id=f'@{name_channel_3}', user_id=call.message.chat.id)).status


    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='🥤Я ПОДПИСАЛСЯ🥤', callback_data=f'check{groop}{name_channel}')
    markup.add(bat_a)

    if (proverka1 == 'member' and proverka2 == 'member' and proverka3 == 'member') or proverka1 == 'administrator' or proverka2 == 'administrator' or proverka3 == 'administrator': #Человек прошел все 3 проверки
        if name_channel == '':
            ######  Человек перещел без реферальной ссылке    #####
            markup_2 = types.InlineKeyboardMarkup()
            bat_b = types.InlineKeyboardButton(text='🥤ПОДПИСАТЬСЯ🥤',
                                               url=f'https://t.me/{name_channel_1}')  # Cсылка на приват канал # ВАЖНО!!!!!
            markup_2.add(bat_b)
            await bot.send_message(call.message.chat.id, '✅ ДОСТУП ОТКРЫТ\n\n'
                                                         'Все новинки 2021 сливаем на наш приватный канал.<b> Подпишись</b> 👇',parse_mode='html', reply_markup=markup_2)


            ###########   Человек перешел по реферальной ссылке    ##########

        else:
            status = proverka_channel(name_channel) ## Возвращает 1, если телеграмм канал проверен. 0 - Если нет

            if status == 0:
                markup_2 = types.InlineKeyboardMarkup()
                bat_b = types.InlineKeyboardButton(text='🥤ПОДПИСАТЬСЯ🥤',
                                                   url=f'https://t.me/{name_channel_1}')  # ВАЖНО!!!!!
                markup_2.add(bat_b)
                await bot.send_message(call.message.chat.id, '✅ ДОСТУП ОТКРЫТ\n\n'
                                                             'Все новинки 2021 сливаем на наш приватный канал.<b> Подпишись</b> 👇',
                                       parse_mode='html', reply_markup=markup_2)
            else:
                markup_2 = types.InlineKeyboardMarkup()
                bat_b = types.InlineKeyboardButton(text='🥤ПОДПИСАТЬСЯ🥤', url=f'https://t.me/{name_channel}') # Cсылка на приват канал
                markup_2.add(bat_b)
                await bot.send_message(call.message.chat.id, '✅ ДОСТУП ОТКРЫТ\n\n'
                                                             'Все новинки 2021 сливаем на наш приватный канал.<b> Подпишись</b> 👇',parse_mode='html',reply_markup=markup_2)



    else:
        await bot.send_message(call.message.chat.id, '❌Вы не подписались на каналы ниже\n\n'
                                                     'Проверьте еще раз подписку на всех каналах. И нажми кнопку <b>Я ПОДПИСАЛСЯ</b> для проверки!\n\n'
                                                     f'<b>Канал 1</b> - https://t.me/{name_channel_1}\n'
                                                     f'<b>Канал 2</b> - https://t.me/{name_channel_2}\n'
                                                     f'<b>Канал 3</b> - https://t.me/{name_channel_3}\n', parse_mode='html',reply_markup=markup,disable_web_page_preview=True)