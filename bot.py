import COVID19Py
import telebot
from telebot import types

covid19 = COVID19Py.COVID19()
TOKEN = '1341223648:AAFx7B-P-q-OxbAJqMoL29q1MLn9gNZahfk'
bot = telebot.TeleBot(TOKEN)


# latest = covid19.getLatest()
# print(latest)
# locations = covid19.getLocations()
# location = covid19.getLocationByCountryCode("CN")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('The World')
    btn2 = types.KeyboardButton('Kazakhstan')
    btn3 = types.KeyboardButton('Russian')
    btn4 = types.KeyboardButton('China')
    btn5 = types.KeyboardButton('USA')
    btn6 = types.KeyboardButton('GB')
    btn7 = types.KeyboardButton('Japan')
    btn8 = types.KeyboardButton('Korea')
    btn9 = types.KeyboardButton('Spain')
    btn10 = types.KeyboardButton('Italy')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)


    send_mess = f"<b>Здравствуйте {message.from_user.first_name}!</b>\nВведите страну о которой хотите знать"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message(message):
    final_message = ""
    get_message_bot = message.text.strip()
    if get_message_bot == 'The World':
        location = covid19.getLatest()
        final_message = f"<b><u>Data from all over the World</u>.\nConfirmed: </b>{location['confirmed']}\n" \
                        f"<b><u>DEATHS: </u></b>{location['deaths']}"
    elif get_message_bot == "Kazakhstan":
        location = covid19.getLocationByCountryCode("KZ")
    elif get_message_bot == "USA":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "China":
        location = covid19.getLocationByCountryCode("CN")
    elif get_message_bot == "Uzbekistan":
        location = covid19.getLocationByCountryCode("UZ")
    elif get_message_bot == 'Great Britain':
        location = covid19.getLocationByCountryCode("GB")
    elif get_message_bot == 'Japan':
        location = covid19.getLocationByCountryCode("JP")
    elif get_message_bot == 'Korea':
        location = covid19.getLocationByCountryCode("KR")
    elif get_message_bot == 'Russian':
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == 'Africa':
        location = covid19.getLocationByCountryCode("ZA")
    elif get_message_bot == 'Italy':
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == 'Spain':
        location = covid19.getLocationByCountryCode("ES")
    else:
        final_message = f"<b>Я, Ислам, прошу прощения за доставленные неудобства. В будущем обязательно рассмотрим эту страну.</b>"

    if final_message == '':
        date = location[0]['last_updated'].split('T')
        time = date[1].split('.')
        final_message = f"<u>Data about {get_message_bot}: </u>\n<b>Population: </b>{location[0]['country_population']}\n" \
                        f"<b>Latest update: </b>Day: {date[0]} | Time: {time[0]}\n" \
                        f"<b>CONFIRMED: </b>{location[0]['latest']['confirmed']}\n" \
                        f"<b><u>DEATHS: </u></b>{location[0]['latest']['deaths']}\n" \

    bot.send_message(message.chat.id, final_message, parse_mode='html')




bot.polling(none_stop=True)


