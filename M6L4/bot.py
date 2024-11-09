import telebot
from config import TOKEN
import random

bot = telebot.TeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['math'])
def calculator(message):
    key = telebot.util.extract_arguments(message.text)
    bot.send_message(message.chat.id, eval(str(key)))


@bot.message_handler(commands=['random_fact'])
def random_facts(message):
    facts = [
        'Изначально Крипер не был мобом - он появился в результате ошибки при создании свиньи. Позже ему изменили текстуру и добавили способность взрываться.',
        'С шансом в 0.01% в главном меню вместо большой надписи "Minecraft" появится название с ошибкой "Minceraft".',
        'Верстак в мире Minecraft можно использовать как компас - на северной его части всегда будет текстура с пилой и молотком, независимо от положения игрока в момент установки блока.',
        'Если ударить молнией в Крипера, то он станет заряженным. Сила и радиус взрыва будут увеличены.',
        'Иероглифы в столе зачарования - не спонтанно нарисованные буквы, а настоящий шифр, имеющий смысл.',
        'На 24-25 декабря сундуки приобретают праздничный рождественский вид.'
    ]
    bot.send_message(message.chat.id, str(random.choice(facts)))

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()