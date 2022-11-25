
# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI

from telebot import TeleBot, types

bot= TeleBot(token='Вставьте свой токен', parse_mode='html') # создание бота

# объект клавиаутры
keybaord = types.ReplyKeyboardMarkup(one_time_keyboard=True)
# первый ряд кнопок
keybaord.row(
    types.KeyboardButton(text='Да'),
    types.KeyboardButton(text='Нет'),
)
# второй ряд кнопок
keybaord.row(
    types.KeyboardButton(text='В поиске'),
    types.KeyboardButton(text='Еще учусь'),
)


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):

    
    # отправляем ответ на команду '/start'
 bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет, я Морской Котик! Если ты читаешь это сообщение, то наверняка уже закончил курс, и отправился в самостоятельное плавание. Расскажи, ты уже работаешь?', # текст сообщения
     reply_markup=keybaord,
    )


@bot.message_handler()
def message_handler(message: types.Message):
    # проверяем текст сообщения на совпадение с текстом какой либо из кнопок
    # в зависимости от выбора, приходит сообщение
    if message.text == 'Да':
        bot.send_message(message.chat.id, text="Круто🔥 Напиши в ответном сообщении вой отзыв, какой у тебя офер и как все прошло? И не забудь похвалить ментора😊")
        bot.register_next_step_handler(message, send_z)
    
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, text="Напиши в одном сообщении, кто был твоим ментором и сколько собесов было?")
        bot.register_next_step_handler(message, send_d)
    
    elif message.text == 'В поиске':
        bot.send_message(message.chat.id, text="Ты молодец👍 Продолжай, у тебя все получится!💛 Напиши в ответном сообщении, как прошел курс?")
        bot.register_next_step_handler(message, send_p)
    
    elif message.text == 'Еще учусь':
        bot.send_message(message.chat.id, text="Напиши в одном сообщении, из какой ты группы и как дается учеба?")
        bot.register_next_step_handler(message, send_f)
    else:
        # если текст не совпал ни с одной из кнопок 
        # выводим ошибку
        bot.send_message(
            chat_id=message.chat.id,
            text='Не понимаю тебя. Тебе поможет КИТ @cto_takoe_escapada 🐋',
        )


        
# настраиваем оповещения и ответы
# выводим ник пользователя, который прислал отзыв
# можно настроить вывод имени пользователя, который прислал отзыв
def send_z (message):
    first_name=message.chat.first_name
    chat_id=message.chat.id
    user_name=message.from_user.username 
    z=message.text
    admin_id= # пишем айди админа
    app_text=[]
    app_name=[]
    app_username=[]
    app_name.append(first_name)
    app_username.append(user_name)
    app_text.append(z)
    
    bot.send_message(admin_id, message.text)

    bot.send_message(admin_id, f'---> Еще один офер! Пришел новый отзыв от @{app_username[0]}')

    img_z = open('img_z.jpg', 'rb')
    bot.send_photo(message.chat.id, img_z)

    app_name.clear()
    app_username.clear()
    app_text.clear()
    bot.send_message(chat_id, text='Спасибо💛 Твой отзыв уже у нас, и скоро его прочитает Герман')


def send_d (message):
    first_name=message.chat.first_name
    chat_id=message.chat.id
    user_name=message.from_user.username 
    d=message.text
    admin_id=# пишем айди админа
    app_text=[]
    app_name=[]
    app_username=[]
    app_name.append(first_name)
    app_username.append(user_name)
    app_text.append(d)
    
    
    bot.send_message(admin_id, message.text)

    bot.send_message(admin_id, f'---> Алярм! Возможно, нужно помочь @{app_username[0]}')

    img_d = open('img_d.jpg', 'rb')
    bot.send_photo(message.chat.id, img_d)

    app_name.clear()
    app_username.clear()
    app_text.clear()
    bot.send_message(chat_id, text='Спасибо, что написал(а). Мы скоро с тобой свяжемся 💛')

def send_p (message):
    first_name=message.chat.first_name
    chat_id=message.chat.id
    user_name=message.from_user.username 
    p=message.text
    admin_id=# пишем айди админа
    app_text=[]
    app_name=[]
    app_username=[]
    app_name.append(first_name)
    app_username.append(user_name)
    app_text.append(p)
    
    
    bot.send_message(admin_id, message.text)

    bot.send_message(admin_id, f'---> Пришел новый отзыв! @{app_username[0]} - Еще в поиске работы')
    
    img_p = open('img_p.jpg', 'rb')
    bot.send_photo(message.chat.id, img_p)

    app_name.clear()
    app_username.clear()
    app_text.clear()
    bot.send_message(chat_id, text='Мы увидели, что ты в поиске работы. Герман, наставники и ребята в чатике всегда ответят на любой твой вопрос и помогут🧠')

def send_f (message):
    first_name=message.chat.first_name
    chat_id=message.chat.id
    user_name=message.from_user.username 
    f=message.text
    admin_id=# пишем айди админа
    app_text=[]
    app_name=[]
    app_username=[]
    app_name.append(first_name)
    app_username.append(user_name)
    app_text.append(f)
    
    
    bot.send_message(admin_id, message.text)

    bot.send_message(admin_id, f'---> Пришел новый отзыв от учащегося @{app_username[0]} 💛')

    img_f = open('img_f.jpg', 'rb')
    bot.send_photo(message.chat.id, img_f)

    app_name.clear()
    app_username.clear()
    app_text.clear()
    bot.send_message(chat_id, text='Рады, что ты у нас на курсе💛 Уже отправили твой отзыв Герману 😊')



    # главная функция программы
def main():
    # запускаем нашего бота
        bot.infinity_polling()


if __name__ == '__main__':
    main()
