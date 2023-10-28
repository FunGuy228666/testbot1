import telebot
import time
from telebot import types
import random
import os
os.chdir("\\".join(__file__.split('\\')[:len(__file__.split('\\'))-1]))

bot = telebot.TeleBot('6351771388:AAGZWV6N_usvqaY6thwZSU5uXDBz-3ozhmE',threaded=True)

def write_file(id:int,type:str,new_data:int|str) -> None:
    with open(str(id)+"_"+type+"_clicker.txt" , 'w' , encoding='utf-8') as f_m:f_m.write(str(new_data))

def read_file(id:int,type:str) -> str:
    with open(str(id)+"_"+type+"_clicker.txt" , 'r' , encoding='utf-8') as f_m:data = f_m.read();return int(data)


buy = 0

buy_count = 0

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'Для того чтобы начать новою игру используй команду /start. Эта команда обнуляет всё. Если у тебя есть пассивный доход, то чтобы собрать его напиши команду /passive. Также пиши команду /passive для входа в игру если ты вышел из телеграма. Если у тебя нет пассивного дохода, то для входа пиши start. Буст - это число, которое даётся тебе за 1 клик. Ты можешь увеличить его 5 раз. В кликере кликай на плашку с надписью +.')

@bot.message_handler(commands=['start'])
def start_main(message):
    write_file(message.chat.id,"balance",0)
    balance = int(read_file(message.chat.id,"balance"))
    write_file(message.chat.id,"passive",0)
    write_file(message.chat.id,"boost",1)
    write_file(message.chat.id,"count",5)
    write_file(message.chat.id,"btc",0)
    write_file(message.chat.id,"curs",100000)
    write_file(message.chat.id,"buyed_tekstil",0)
    write_file(message.chat.id,"buyed_auto",0)
    write_file(message.chat.id,"buyed_aircrafts",0)
    write_file(message.chat.id,"buyed_buisnes_impire",0)
    write_file(message.chat.id,"count_passive",20)
    write_file(message.chat.id,"start",round(time.time()))
    main_menu = types.InlineKeyboardMarkup(row_width=2)
    main_menu.add(types.InlineKeyboardButton('Кликер' , callback_data='Goto_Clicker') , types.InlineKeyboardButton('Пассивный доход' , callback_data='Goto_Passive'), types.InlineKeyboardButton('Буст кликер' , callback_data='Goto_boost_clicker'), types.InlineKeyboardButton('Ачивки' , callback_data='Goto_achivments'), types.InlineKeyboardButton('Фондовый рынок' , callback_data='Goto_btc'), types.InlineKeyboardButton('Об игре' , callback_data='Goto_about'), types.InlineKeyboardButton('Моя компания' , callback_data='Goto_buy_company'))
    bot.send_message(message.chat.id, f'Привет, я рад что ты играешь в этот кликер. Гайд по команде /help. Твой баланс: {balance}', reply_markup=main_menu)

@bot.message_handler(content_types=['text'])
def handler1(message):
    global buy_count
    balance = read_file(message.chat.id,"balance")
    boost = read_file(message.chat.id,"boost")
    if buy == 1:
        buy_count = message.text
        for i in buy_count:
            if i == ',':
                ind = buy_count.index(i)
                buy_count = buy_count[0:ind]
                # if len(buy_count) - 2 == ind:buy_count = buy_count[0:ind] + '.' + buy_count[ind + 1]
                # else:buy_count = buy_count[0:ind] + '.' + buy_count[ind + 1:len(buy_count)]
                break
        try:
            buy_count = int(buy_count)
        except:
            bot.send_message(message.chat.id,"Введите число")
    if message.text == ('+' + str(boost)):
        balance += boost
        write_file(message.chat.id,'balance',balance)
    elif message.text == 'start':
        write_file(message.chat.id,'start',round(time.time()))
        balance = read_file(message.chat.id,"balance")
        main_menu = types.InlineKeyboardMarkup(row_width=2)
        main_menu.add(types.InlineKeyboardButton('Кликер' , callback_data='Goto_Clicker') , types.InlineKeyboardButton('Пассивный доход' , callback_data='Goto_Passive'), types.InlineKeyboardButton('Буст кликер' , callback_data='Goto_boost_clicker'), types.InlineKeyboardButton('Ачивки' , callback_data='Goto_achivments'), types.InlineKeyboardButton('Фондовый рынок' , callback_data='Goto_btc'), types.InlineKeyboardButton('Об игре' , callback_data='Goto_about'), types.InlineKeyboardButton('Моя компания' , callback_data='Goto_buy_company'))
        bot.send_message(message.chat.id, f'Привет, я рад что ты играешь в этот кликер. Гайд по команде /help. Твой баланс: {balance}', reply_markup=main_menu)
    elif message.text == '/passive':
        start = read_file(message.chat.id,"start")
        get = (round(time.time()) - start) * read_file(message.chat.id,"passive")
        balance = read_file(message.chat.id,"balance") + get
        write_file(message.chat.id,'balance',balance)
        write_file(message.chat.id,'start',round(time.time()))
        main_menu = types.InlineKeyboardMarkup(row_width=2)
        main_menu.add(types.InlineKeyboardButton('Кликер' , callback_data='Goto_Clicker') , types.InlineKeyboardButton('Пассивный доход' , callback_data='Goto_Passive'), types.InlineKeyboardButton('Буст кликер' , callback_data='Goto_boost_clicker'), types.InlineKeyboardButton('Ачивки' , callback_data='Goto_achivments'), types.InlineKeyboardButton('Фондовый рынок' , callback_data='Goto_btc'), types.InlineKeyboardButton('Об игре' , callback_data='Goto_about'), types.InlineKeyboardButton('Моя компания' , callback_data='Goto_buy_company'))
        bot.send_message(message.chat.id, f'Привет, я рад что ты играешь в этот кликер. Твой баланс: {balance}', reply_markup=main_menu)
    elif message.text == '/menu':
        global exit
        exit = 1
        balance = read_file(message.chat.id,"balance")
        main_menu = types.InlineKeyboardMarkup(row_width=2)
        main_menu.add(types.InlineKeyboardButton('Кликер' , callback_data='Goto_Clicker') , types.InlineKeyboardButton('Пассивный доход' , callback_data='Goto_Passive'), types.InlineKeyboardButton('Буст кликер' , callback_data='Goto_boost_clicker'), types.InlineKeyboardButton('Ачивки' , callback_data='Goto_achivments'), types.InlineKeyboardButton('Фондовый рынок' , callback_data='Goto_btc'), types.InlineKeyboardButton('Об игре' , callback_data='Goto_about'), types.InlineKeyboardButton('Моя компания' , callback_data='Goto_buy_company'))
        bot.send_message(message.chat.id, f'Привет, я рад что ты играешь в этот кликер. Твой баланс: {balance}', reply_markup=main_menu)
        time.sleep(0.7)
        exit = 0


@bot.callback_query_handler(func = lambda call:True)
def callback_1(call):
    global buy, exit
    if call.data == 'Goto_Clicker':
        boost = read_file(call.message.chat.id,"boost")
        click = types.ReplyKeyboardMarkup()
        click1 = types.KeyboardButton(('+' + str(boost)))
        click.add(click1)
        click2 = types.InlineKeyboardMarkup()
        click2.add(types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
        bot.send_message(call.message.chat.id, 'Хотите выйти?', reply_markup=click2)
        bot.send_message(call.message.chat.id, 'Начинай кликать', reply_markup=click)
    elif call.data == 'Goto_main_menu':
        exit = 1
        hide_click = types.ReplyKeyboardRemove()
        balance = read_file(call.message.chat.id,"balance")
        main_menu = types.InlineKeyboardMarkup(row_width=2)
        main_menu.add(types.InlineKeyboardButton('Кликер' , callback_data='Goto_Clicker') , types.InlineKeyboardButton('Пассивный доход' , callback_data='Goto_Passive'), types.InlineKeyboardButton('Буст кликер' , callback_data='Goto_boost_clicker'), types.InlineKeyboardButton('Ачивки' , callback_data='Goto_achivments'), types.InlineKeyboardButton('Фондовый рынок' , callback_data='Goto_btc'), types.InlineKeyboardButton('Об игре' , callback_data='Goto_about'), types.InlineKeyboardButton('Моя компания' , callback_data='Goto_buy_company'))
        bot.send_message(call.message.chat.id, 'Выхожу...', reply_markup=hide_click)
        bot.send_message(call.message.chat.id, f'Привет, я рад что ты играешь в этот кликер. Твой баланс: {balance}', reply_markup=main_menu)
    elif call.data == 'Goto_about':
        back = types.InlineKeyboardMarkup()
        back.add(types.InlineKeyboardButton('Назад', callback_data='Goto_main_menu'))
        bot.send_message(call.message.chat.id, 'Clicker v1.4.0 Создатель: fun inc.\n \nЮтуб создателя: https://youtube.com/channel/UCitSGnImoL1vXkr3C3KSnug', reply_markup=back)
    elif call.data == 'Goto_buy_company':
        btc = read_file(call.message.chat.id,"btc")
        my_company_k = types.InlineKeyboardMarkup()
        my_company_k.add(types.InlineKeyboardButton('Текстиль', callback_data='buy_tekstil'), types.InlineKeyboardButton('Автомобилестроение', callback_data='buy-auto'),types.InlineKeyboardButton('Самолётостроение', callback_data='buy_aircrafts'),types.InlineKeyboardButton('Бизнес империя', callback_data='buy_buisnes_impire'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
        bot.send_message(call.message.chat.id, f'Здесь вы можете улучшать свою компанию, улучшения можно купить только один раз. Текстильное производство за 1000 btc - оно приносит 5000/сек. Автомобилестроение за 6000 btc - оно приносит 50000/сек. Самолётостроение за 35000 btc - оно приносит 200000/сек. Бизнес империю за 3000000 btc - она приносит 10000000/сек. У тебя {btc} btc', reply_markup=my_company_k)
    elif call.data == 'buy_tekstil':
        buyed_tekstil = read_file(call.message.chat.id,"buyed_tekstil")
        btc = read_file(call.message.chat.id,"btc")
        if btc >= 1000 and buyed_tekstil != 1:
            btc -= 1000
            passive = read_file(call.message.chat.id,"passive") + 5000
            write_file(call.message.chat.id,"btc",btc)
            write_file(call.message.chat.id,"passive",passive)
            write_file(call.message.chat.id,"buyed_tekstil",1)
            my_company_k = types.InlineKeyboardMarkup()
            my_company_k.add(types.InlineKeyboardButton('Текстиль', callback_data='buy_tekstil'), types.InlineKeyboardButton('Автомобилестроение', callback_data='buy-auto'),types.InlineKeyboardButton('Самолётостроение', callback_data='buy_aircrafts'),types.InlineKeyboardButton('Бизнес империя', callback_data='buy_buisnes_impire'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Здесь вы можете улучшать свою компанию, улучшения можно купить только один раз. Текстильное производство за 1000 btc - оно приносит 5000/сек. Автомобилестроение за 6000 btc - оно приносит 50000/сек. Самолётостроение за 35000 btc - оно приносит 200000/сек. Бизнес империю за 3000000 btc - она приносит 10000000/сек. У тебя {btc} btc', reply_markup=my_company_k)
        elif btc < 1000:bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
        elif buyed_tekstil == 1:bot.answer_callback_query(callback_query_id=call.id, text='Эту опцию можно купить только раз')
    elif call.data == 'buy-auto':
        buyed_auto = read_file(call.message.chat.id,"buyed_auto")
        btc = read_file(call.message.chat.id,"btc")
        if btc >= 6000 and buyed_auto != 1:
            btc -= 6000
            passive = read_file(call.message.chat.id,"passive") + 50000
            write_file(call.message.chat.id,"btc",btc)
            write_file(call.message.chat.id,"passive",passive)
            write_file(call.message.chat.id,"buyed_auto",1)
            my_company_k = types.InlineKeyboardMarkup()
            my_company_k.add(types.InlineKeyboardButton('Текстиль', callback_data='buy_tekstil'), types.InlineKeyboardButton('Автомобилестроение', callback_data='buy-auto'),types.InlineKeyboardButton('Самолётостроение', callback_data='buy_aircrafts'),types.InlineKeyboardButton('Бизнес империя', callback_data='buy_buisnes_impire'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Здесь вы можете улучшать свою компанию, улучшения можно купить только один раз. Текстильное производство за 1000 btc - оно приносит 5000/сек. Автомобилестроение за 6000 btc - оно приносит 50000/сек. Самолётостроение за 35000 btc - оно приносит 200000/сек. Бизнес империю за 3000000 btc - она приносит 10000000/сек. У тебя {btc} btc', reply_markup=my_company_k)
        elif btc < 6000:bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
        elif buyed_auto == 1:bot.answer_callback_query(callback_query_id=call.id, text='Эту опцию можно купить только раз')
    elif call.data == 'buy_aircrafts':
        buyed_aircrafts = read_file(call.message.chat.id,"buyed_aircrafts")
        btc = read_file(call.message.chat.id,"btc")
        if btc >= 35000 and buyed_aircrafts != 1:
            btc -= 35000
            passive = read_file(call.message.chat.id,"passive") + 200000
            write_file(call.message.chat.id,"btc",btc)
            write_file(call.message.chat.id,"passive",passive)
            write_file(call.message.chat.id,"buyed_aircrafts",1)
            my_company_k = types.InlineKeyboardMarkup()
            my_company_k.add(types.InlineKeyboardButton('Текстиль', callback_data='buy_tekstil'), types.InlineKeyboardButton('Автомобилестроение', callback_data='buy-auto'),types.InlineKeyboardButton('Самолётостроение', callback_data='buy_aircrafts'),types.InlineKeyboardButton('Бизнес империя', callback_data='buy_buisnes_impire'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Здесь вы можете улучшать свою компанию, улучшения можно купить только один раз. Текстильное производство за 1000 btc - оно приносит 5000/сек. Автомобилестроение за 6000 btc - оно приносит 50000/сек. Самолётостроение за 35000 btc - оно приносит 200000/сек. Бизнес империю за 3000000 btc - она приносит 10000000/сек. У тебя {btc} btc', reply_markup=my_company_k)
        elif btc < 35000:bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
        elif buyed_aircrafts == 1:bot.answer_callback_query(callback_query_id=call.id, text='Эту опцию можно купить только раз')
    elif call.data == 'buy_buisnes_impire':
        buyed_buisnes_impire = read_file(call.message.chat.id,"buyed_buisnes_impire")
        btc = read_file(call.message.chat.id,"btc")
        if btc >= 3000000 and buyed_buisnes_impire != 1:
            btc -= 3000000
            passive = read_file(call.message.chat.id,"passive") + 10000000
            write_file(call.message.chat.id,"btc",btc)
            write_file(call.message.chat.id,"passive",passive)
            write_file(call.message.chat.id,"buyed_buisnes_impire",1)
            my_company_k = types.InlineKeyboardMarkup()
            my_company_k.add(types.InlineKeyboardButton('Текстиль', callback_data='buy_tekstil'), types.InlineKeyboardButton('Автомобилестроение', callback_data='buy-auto'),types.InlineKeyboardButton('Самолётостроение', callback_data='buy_aircrafts'),types.InlineKeyboardButton('Бизнес империя', callback_data='buy_buisnes_impire'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Здесь вы можете улучшать свою компанию, улучшения можно купить только один раз. Текстильное производство за 1000 btc - оно приносит 5000/сек. Автомобилестроение за 6000 btc - оно приносит 50000/сек. Самолётостроение за 35000 btc - оно приносит 200000/сек. Бизнес империю за 3000000 btc - она приносит 10000000/сек. У тебя {btc} btc', reply_markup=my_company_k)
        elif btc < 3000000:bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
        elif buyed_buisnes_impire == 1:bot.answer_callback_query(callback_query_id=call.id, text='Эту опцию можно купить только раз')
    elif call.data == 'Goto_btc':
        curs = read_file("","curs")
        btc = read_file(call.message.chat.id,"btc")
        exit = 0
        if call.data != 'Goto_btc':
            exit = 1
        with open("last_updated.txt",'r') as file:last_update = int(file.read())
        if round(time.time()) - last_update > 500:
            up_or_down = random.randint(1,2)
            procent = random.randint(1,10)
            if up_or_down == 1:
                curs += (curs / 100) * procent
                write_file("","curs",round(curs))
            elif up_or_down == 2:
                curs -= (curs / 100) * procent
                write_file("","curs",round(curs))
            with open("last_updated.txt",'w') as file:file.write(str(int(round(time.time()))))
        btc = read_file(call.message.chat.id,"btc")
        btc_k = types.InlineKeyboardMarkup()
        btc_k.add(types.InlineKeyboardButton('Купить' , callback_data='Buy_btc'), types.InlineKeyboardButton('Продать' , callback_data='Sell_btc'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
        bot.send_message(call.message.chat.id, f'Ты можешь купить биткоин за {curs}. У тебя {btc} криптовалюты(-а)', reply_markup=btc_k)
    elif call.data == 'Buy_btc':
        exit = 1
        balance = read_file(call.message.chat.id,"balance")
        curs = read_file("","curs")
        buy = 1
        btc_k2 = types.InlineKeyboardMarkup()
        btc_k2.add(types.InlineKeyboardButton('Да', callback_data='continue'))
        bot.send_message(call.message.chat.id, 'Продолжить?', reply_markup=btc_k2)
    elif call.data == 'continue':
        balance = read_file(call.message.chat.id,"balance")
        curs = read_file("","curs")
        btc = read_file(call.message.chat.id,"btc")
        buy_c = buy_count * curs
        if balance >= buy_c:
            balance -= int(round(buy_c))
            write_file(call.message.chat.id,'balance',balance)
            write_file(call.message.chat.id,'btc',int(round(buy_count + btc)))
            btc_k = types.InlineKeyboardMarkup()
            btc_k.add(types.InlineKeyboardButton('Купить' , callback_data='Buy_btc'), types.InlineKeyboardButton('Продать' , callback_data='Sell_btc'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Ты можешь купить биткоин за {curs}. У тебя {btc} криптовалюты(-а)', reply_markup=btc_k)
        elif buy_c == 0:
            bot.answer_callback_query(callback_query_id=call.id, text='Сначала отправьте количество, потом нажмите Да')
            btc_k = types.InlineKeyboardMarkup()
            btc_k.add(types.InlineKeyboardButton('Купить' , callback_data='Buy_btc'), types.InlineKeyboardButton('Продать' , callback_data='Sell_btc'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Ты можешь купить биткоин за {curs}. У тебя {btc} криптовалюты(-а)', reply_markup=btc_k)
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
            btc_k = types.InlineKeyboardMarkup()
            btc_k.add(types.InlineKeyboardButton('Купить' , callback_data='Buy_btc'), types.InlineKeyboardButton('Продать' , callback_data='Sell_btc'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Ты можешь купить биткоин за {curs}. У тебя {btc} криптовалюты(-а)', reply_markup=btc_k)
        buy = 0
    elif call.data == 'Sell_btc':
        exit = 1
        balance = read_file(call.message.chat.id,"balance")
        btc = read_file(call.message.chat.id,"btc")
        curs = read_file("","curs")
        buy = 1
        btc_k3 = types.InlineKeyboardMarkup()
        btc_k3.add(types.InlineKeyboardButton('Да', callback_data='continue1'))
        bot.send_message(call.message.chat.id, 'Продолжить?', reply_markup=btc_k3)
    elif call.data == 'continue1':
        balance = read_file(call.message.chat.id,"balance")
        btc = read_file(call.message.chat.id,"btc")
        curs = read_file("","curs")
        if btc >= buy_count:
            buy_c = int(round(buy_count * curs))
            btc -= buy_count
            balance += buy_c
            write_file(call.message.chat.id,'balance',int(round(balance)))
            write_file(call.message.chat.id,'btc',int(round(btc)))
            btc_k = types.InlineKeyboardMarkup()
            btc_k.add(types.InlineKeyboardButton('Купить' , callback_data='Buy_btc'), types.InlineKeyboardButton('Продать' , callback_data='Sell_btc'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Ты можешь купить биткоин за {curs}. У тебя {btc} криптовалюты(-а)', reply_markup=btc_k)
        elif buy_c == 0:
            bot.answer_callback_query(callback_query_id=call.id, text='Сначала отправьте количество, потом нажмите Да')
            btc_k = types.InlineKeyboardMarkup()
            btc_k.add(types.InlineKeyboardButton('Купить' , callback_data='Buy_btc'), types.InlineKeyboardButton('Продать' , callback_data='Sell_btc'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Ты можешь купить биткоин за {curs}. У тебя {btc} криптовалюты(-а)', reply_markup=btc_k)
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
            btc_k = types.InlineKeyboardMarkup()
            btc_k.add(types.InlineKeyboardButton('Купить' , callback_data='Buy_btc'), types.InlineKeyboardButton('Продать' , callback_data='Sell_btc'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Ты можешь купить биткоин за {curs}. У тебя {btc} криптовалюты(-а)', reply_markup=btc_k)
        buy = 0
    elif call.data == 'Goto_achivments':
        balance = read_file(call.message.chat.id,"balance")
        bot.send_message(call.message.chat.id, 'Ачивки: 1.100 на балансе 2.1000 на балансе. 3.10000 на балансе. 4.1000000 на баансе. 5.10000000 на балансе. 6.1000000000 на балансе.')
        if balance >= 100:
            sticker = open('sticker_for_100.webp', 'rb')
            bot.send_sticker(call.message.chat.id, sticker)
        if balance >= 1000:
            sticker = open('sticker_for_1000.webp', 'rb')
            bot.send_sticker(call.message.chat.id, sticker)
        if balance >= 1000000:
            sticker = open('sticker_for_1000000.webp', 'rb')
            bot.send_sticker(call.message.chat.id, sticker)
        if balance >= 10000000:
            sticker = open('sticker_for_10000000.webp', 'rb')
            bot.send_sticker(call.message.chat.id, sticker)
        if balance >= 1000000000:
            sticker = open('sticker_for_1000000000.webp', 'rb')
            bot.send_sticker(call.message.chat.id, sticker)
        if balance >= 10000000000:
            sticker = open('sticker_for_10000000000.webp', 'rb')
            bot.send_sticker(call.message.chat.id, sticker)
    elif call.data == 'Goto_boost_clicker':
        count = read_file(call.message.chat.id,"count")
        boost = read_file(call.message.chat.id,"boost")
        boost1 = types.InlineKeyboardMarkup(row_width=2)
        boost1.add(types.InlineKeyboardButton('Удвоить' , callback_data='Double'), types.InlineKeyboardButton('Утроить' , callback_data='Triple'), types.InlineKeyboardButton('Учетверить' , callback_data='Quadruple'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
        bot.send_message(call.message.chat.id, f'Твой буст: {boost}, Ты можешь удвоить его за 500, утроить за 3000 и учетверить за 7000.(Ты можешь сделать это только 5 раз). У тебя осталось: {count} раз(-а)',reply_markup=boost1)
    elif call.data == 'Double':
        balance = read_file(call.message.chat.id,"balance")
        count = read_file(call.message.chat.id,"count")
        if balance >= 500 and count > 0:
            boost = read_file(call.message.chat.id,"boost") * 2
            write_file(call.message.chat.id,"boost",boost)
            balance -= 500
            write_file(call.message.chat.id,"balance",balance)
            count -= 1
            write_file(call.message.chat.id,"count",count)
            bot.answer_callback_query(callback_query_id=call.id, text='Покупка прошла успешно')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
            boost = read_file(call.message.chat.id,"boost")
            boost1 = types.InlineKeyboardMarkup(row_width=2)
            boost1.add(types.InlineKeyboardButton('Удвоить' , callback_data='Double'), types.InlineKeyboardButton('Утроить' , callback_data='Triple'), types.InlineKeyboardButton('Учетверить' , callback_data='Quadruple'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Твой буст: {boost}, Ты можешь удвоить его за 500, утроить за 3000 и учетверить за 7000.(Ты можешь сделать это только 5 раз). У тебя осталось: {count} раз(-а)', reply_markup=boost1)
    elif call.data == 'Triple':
        balance = read_file(call.message.chat.id,"balance")
        count = read_file(call.message.chat.id,"count")
        if balance >= 3000 and count > 0:
            boost = read_file(call.message.chat.id,"boost") * 3
            write_file(call.message.chat.id,"boost",boost)
            balance -= 3000
            write_file(call.message.chat.id,"balance",balance)
            count -= 1
            write_file(call.message.chat.id,"count",count)
            bot.answer_callback_query(callback_query_id=call.id, text='Покупка прошла успешно')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
            boost = read_file(call.message.chat.id,"boost")
            boost1 = types.InlineKeyboardMarkup(row_width=2)
            boost1.add(types.InlineKeyboardButton('Удвоить' , callback_data='Double'), types.InlineKeyboardButton('Утроить' , callback_data='Triple'), types.InlineKeyboardButton('Учетверить' , callback_data='Quadruple'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Твой буст: {boost}, Ты можешь удвоить его за 500, утроить за 3000 и учетверить за 7000.(Ты можешь сделать это только 5 раз). У тебя осталось: {count} раз(-а)', reply_markup=boost1)
    elif call.data == 'Quadruple':
        balance = read_file(call.message.chat.id,"balance")
        count = read_file(call.message.chat.id,"count")
        if balance >= 7000 and count > 0:
            boost = read_file(call.message.chat.id,"boost") * 4
            write_file(call.message.chat.id,"boost",boost)
            balance -= 7000
            write_file(call.message.chat.id,"balance",balance)
            count -= 1
            write_file(call.message.chat.id,"count",count)
            bot.answer_callback_query(callback_query_id=call.id, text='Покупка прошла успешно')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
            boost = read_file(call.message.chat.id,"boost")
            boost1 = types.InlineKeyboardMarkup(row_width=2)
            boost1.add(types.InlineKeyboardButton('Удвоить' , callback_data='Double'), types.InlineKeyboardButton('Утроить' , callback_data='Triple'), types.InlineKeyboardButton('Учетверить' , callback_data='Quadruple'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Твой буст: {boost}, Ты можешь удвоить его за 500, утроить за 3000 и учетверить за 7000.(Ты можешь сделать это только 5 раз). У тебя осталось: {count} раз(-а)', reply_markup=boost1)
    elif call.data == 'Goto_Passive':
        count_passive = read_file(call.message.chat.id,"count_passive")
        passive = read_file(call.message.chat.id,"passive")
        passive_buy = types.InlineKeyboardMarkup()
        passive_buy.add(types.InlineKeyboardButton('Купить Буфет' , callback_data='Buy_buffet'), types.InlineKeyboardButton('Купить Магазин' , callback_data='Buy_shop'), types.InlineKeyboardButton('Купить Завод' , callback_data='Buy_factory'), types.InlineKeyboardButton('Купить Бизнес центр' , callback_data='Buy_buisnes_centr'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
        bot.send_message(call.message.chat.id, f'Твой пассивный доход: {passive}/сек. Для его увеличения ты можешь купить: Буфет - дающий 100/сек, Магазин - дающий 250/сек, Завод - дающий 650/сек, Бизнес центр - дающий 3500/сек. Цены: Буффет - 7000, Магазин - 40000, Завод - 200000, Бизнес центр - 10000000. Ты можешь купить это 20 раз. У тебя {count_passive} раз(-а)', reply_markup=passive_buy)
    elif call.data == 'Buy_buffet':
        balance = read_file(call.message.chat.id,"balance")
        count_passive = read_file(call.message.chat.id,"count_passive")
        if balance >= 7000 and count_passive > 0:
            balance -= 7000
            write_file(call.message.chat.id,"balance",balance)
            passive = read_file(call.message.chat.id,"passive") + 100
            write_file(call.message.chat.id,"passive",passive)
            write_file(call.message.chat.id,"count_passive",count_passive-1)
            bot.answer_callback_query(callback_query_id=call.id, text='Покупка прошла успешно')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
            passive = read_file(call.message.chat.id,"passive")
            passive_buy = types.InlineKeyboardMarkup()
            passive_buy.add(types.InlineKeyboardButton('Купить Буфет' , callback_data='Buy_buffet'), types.InlineKeyboardButton('Купить Магазин' , callback_data='Buy_shop'), types.InlineKeyboardButton('Купить Завод' , callback_data='Buy_factory'), types.InlineKeyboardButton('Купить Бизнес центр' , callback_data='Buy_buisnes_centr'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Твой пассивный доход: {passive}/сек. Для его увеличения ты можешь купить: Буфет - дающий 100/сек, Магазин - дающий 250/сек, Завод - дающий 650/сек, Бизнес центр - дающий 3500/сек. Цены: Буффет - 7000, Магазин - 40000, Завод - 200000, Бизнес центр - 10000000. Ты можешь купить это 20 раз. У тебя {count_passive} раз(-а)', reply_markup=passive_buy)
    elif call.data == 'Buy_shop':
        balance = read_file(call.message.chat.id,"balance")
        count_passive = read_file(call.message.chat.id,"count_passive")
        if balance >= 40000 and count_passive > 0:
            balance -= 40000
            write_file(call.message.chat.id,"balance",balance)
            passive = read_file(call.message.chat.id,"passive") + 250
            write_file(call.message.chat.id,"passive",passive)
            write_file(call.message.chat.id,"count_passive",count_passive-1)
            bot.answer_callback_query(callback_query_id=call.id, text='Покупка прошла успешно')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
            passive = read_file(call.message.chat.id,"passive")
            passive_buy = types.InlineKeyboardMarkup()
            passive_buy.add(types.InlineKeyboardButton('Купить Буфет' , callback_data='Buy_buffet'), types.InlineKeyboardButton('Купить Магазин' , callback_data='Buy_shop'), types.InlineKeyboardButton('Купить Завод' , callback_data='Buy_factory'), types.InlineKeyboardButton('Купить Бизнес центр' , callback_data='Buy_buisnes_centr'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Твой пассивный доход: {passive}/сек. Для его увеличения ты можешь купить: Буфет - дающий 100/сек, Магазин - дающий 250/сек, Завод - дающий 650/сек, Бизнес центр - дающий 3500/сек. Цены: Буффет - 7000, Магазин - 40000, Завод - 200000, Бизнес центр - 10000000. Ты можешь купить это 20 раз. У тебя {count_passive} раз(-а)', reply_markup=passive_buy)        
    elif call.data == 'Buy_factory':
        balance = read_file(call.message.chat.id,"balance")
        count_passive = read_file(call.message.chat.id,"count_passive")
        if balance >= 200000 and count_passive > 0:
            balance -= 200000
            write_file(call.message.chat.id,"balance",balance)
            passive = read_file(call.message.chat.id,"passive") + 650
            write_file(call.message.chat.id,"passive",passive)
            write_file(call.message.chat.id,"count_passive",count_passive-1)
            bot.answer_callback_query(callback_query_id=call.id, text='Покупка прошла успешно')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
            passive = read_file(call.message.chat.id,"passive")
            passive_buy = types.InlineKeyboardMarkup()
            passive_buy.add(types.InlineKeyboardButton('Купить Буфет' , callback_data='Buy_buffet'), types.InlineKeyboardButton('Купить Магазин' , callback_data='Buy_shop'), types.InlineKeyboardButton('Купить Завод' , callback_data='Buy_factory'), types.InlineKeyboardButton('Купить Бизнес центр' , callback_data='Buy_buisnes_centr'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Твой пассивный доход: {passive}/сек. Для его увеличения ты можешь купить: Буфет - дающий 100/сек, Магазин - дающий 250/сек, Завод - дающий 650/сек, Бизнес центр - дающий 3500/сек. Цены: Буффет - 7000, Магазин - 40000, Завод - 200000, Бизнес центр - 10000000. Ты можешь купить это 20 раз. У тебя {count_passive} раз(-а)', reply_markup=passive_buy)
    elif call.data == 'Buy_buisnes_centr':
        balance = read_file(call.message.chat.id,"balance")
        count_passive = read_file(call.message.chat.id,"count_passive")
        if balance >= 10000000 and count_passive > 0:
            balance -= 10000000
            write_file(call.message.chat.id,"balance",balance)
            passive = read_file(call.message.chat.id,"passive") + 3500
            write_file(call.message.chat.id,"passive",passive)
            write_file(call.message.chat.id,"count_passive",count_passive-1)
            bot.answer_callback_query(callback_query_id=call.id, text='Покупка прошла успешно')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Нехватает средств')
            passive = read_file(call.message.chat.id,"passive")
            passive_buy = types.InlineKeyboardMarkup()
            passive_buy.add(types.InlineKeyboardButton('Купить Буфет' , callback_data='Buy_buffet'), types.InlineKeyboardButton('Купить Магазин' , callback_data='Buy_shop'), types.InlineKeyboardButton('Купить Завод' , callback_data='Buy_factory'), types.InlineKeyboardButton('Купить Бизнес центр' , callback_data='Buy_buisnes_centr'), types.InlineKeyboardButton('Назад' , callback_data='Goto_main_menu'))
            bot.send_message(call.message.chat.id, f'Твой пассивный доход: {passive}/сек. Для его увеличения ты можешь купить: Буфет - дающий 100/сек, Магазин - дающий 250/сек, Завод - дающий 650/сек, Бизнес центр - дающий 3500/сек. Цены: Буффет - 7000, Магазин - 40000, Завод - 200000, Бизнес центр - 10000000. Ты можешь купить это 20 раз. У тебя {count_passive} раз(-а)', reply_markup=passive_buy)

bot.polling(non_stop=True, timeout=2147483)