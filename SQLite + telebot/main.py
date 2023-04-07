import telebot
import test_db_SQLiteStudio

# Установка бота
bot = telebot.TeleBot("6034420797:AAHEjTuev9sWhr2PgKWpbIsH0SY_bV1I07Q")

# Приветственное сообщение от бота
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Test_DB_for_BuildBuddy')

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text.lower() == 'привет':
            bot.send_message(message.from_user.id, 'Привет! Ваше имя добавленно в базу данных!')
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        test_db_SQLiteStudio.db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

bot.polling(non_stop=True)

