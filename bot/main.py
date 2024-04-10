import os
import time
import threading
import schedule
from bot.config import bot
from telebot.types import Message, CallbackQuery
import bot.keyboards as keyboards
from datetime import datetime
from bot.db import select_doctor_info, check_selected_date, create_record, get_doctor_photo, check_user_existence,\
    add_user, get_all_users_id
from bot.api.GiphyAPI import *
from bot.api.yandexAPI import get_map_image

# Глобальные переменный для каждого Chat.id
globalVar = {

}


# Id Gif в Giphy
gif_id = "6VriQO3GFRwwBVPbi4"


# Старт бота
@bot.message_handler(commands=['start'])
def start(message):
    if not check_user_existence(message.chat.id):
        add_user(message.chat.id)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=keyboards.get_menu_keyboard())


# Меню бота
@bot.message_handler()
def menu(message: Message):
    if message.text == "Запись к врачу":
        bot.send_message(message.chat.id, "Выберите специализацию врача",
                         reply_markup=keyboards.get_specialization_keyboard()
                         )
        bot.register_next_step_handler(message, select_specialization)
    if message.text == "Информация о клинике":
        bot.send_message(message.chat.id, "Многопрофильная медицинская клиника")
    if message.text == "Контакты":
        get_map_image()
        bot.send_photo(message.chat.id, open("src/map.png", "rb"))
        os.remove("src/map.png")
        bot.send_message(message.chat.id, "Адрес: Духовской 19 \nНомер телефона: +79185405614")


# Выбор специализации врача
@bot.message_handler(func=lambda message: message.text == "Запись к врачу")
def select_specialization(message: Message):
    if message.text == 'Хирург':
        bot.send_message(message.chat.id, 'Выберите специалиста', reply_markup=keyboards.get_surgeon_keyboard())
    if message.text == 'Аллерголог':
        bot.send_message(message.chat.id, 'Выберите специалиста', reply_markup=keyboards.get_allergist_keyboard())
    if message.text == 'Терапевт':
        bot.send_message(message.chat.id, 'Выберите специалиста', reply_markup=keyboards.get_therapist_keyboard())
    if message.text == 'Офтальмолог':
        bot.send_message(message.chat.id, 'Выберите специалиста', reply_markup=keyboards.get_ophthalmologist_keyboard())
    if message.text == 'Психиатр':
        bot.send_message(message.chat.id, 'Выберите специалиста', reply_markup=keyboards.get_psychiatrist_keyboard())
    if message.text == 'Диетолог':
        bot.send_message(message.chat.id, 'Выберите специалиста', reply_markup=keyboards.get_nutritionist_keyboard())
    if message.text == "Назад":
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=keyboards.get_menu_keyboard())
        bot.register_next_step_handler(message, menu)


# Обработка выбора врача
@bot.callback_query_handler(func=lambda call: True)
def select_doctor(call: CallbackQuery):
    data = call.data
    if data == "surgeon_1":
        body_msg = select_doctor_info("surgeon_1")
        doctor_photo_url = get_doctor_photo("surgeon_1")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "surgeon_1"
        bot.register_next_step_handler(call.message, check_date)
    if data == "surgeon_2":
        body_msg = select_doctor_info("surgeon_2")
        doctor_photo_url = get_doctor_photo("surgeon_2")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "surgeon_2"
        bot.register_next_step_handler(call.message, check_date)
    if data == "allergist_1":
        body_msg = select_doctor_info("allergist_1")
        doctor_photo_url = get_doctor_photo("allergist_1")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "allergist_1"
        bot.register_next_step_handler(call.message, check_date)
    if data == "allergist_2":
        body_msg = select_doctor_info("allergist_2")
        doctor_photo_url = get_doctor_photo("allergist_2")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "allergist_2"
        bot.register_next_step_handler(call.message, check_date)
    if data == "therapist_1":
        body_msg = select_doctor_info("therapist_1")
        doctor_photo_url = get_doctor_photo("therapist_1")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "therapist_1"
        bot.register_next_step_handler(call.message, check_date)
    if data == "therapist_2":
        body_msg = select_doctor_info("therapist_2")
        doctor_photo_url = get_doctor_photo("therapist_2")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "therapist_2"
        bot.register_next_step_handler(call.message, check_date)
    if data == "ophthalmologist_1":
        body_msg = select_doctor_info("ophthalmologist_1")
        doctor_photo_url = get_doctor_photo("ophthalmologist_1")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "ophthalmologist_1"
        bot.register_next_step_handler(call.message, check_date)
    if data == "ophthalmologist_2":
        body_msg = select_doctor_info("ophthalmologist_2")
        doctor_photo_url = get_doctor_photo("ophthalmologist_2")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "ophthalmologist_2"
        bot.register_next_step_handler(call.message, check_date)
    if data == "psychiatrist_1":
        body_msg = select_doctor_info("psychiatrist_1")
        doctor_photo_url = get_doctor_photo("psychiatrist_1")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "psychiatrist_1"
        bot.register_next_step_handler(call.message, check_date)
    if data == "psychiatrist_2":
        body_msg = select_doctor_info("psychiatrist_2")
        doctor_photo_url = get_doctor_photo("psychiatrist_2")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "psychiatrist_2"
        bot.register_next_step_handler(call.message, check_date)
    if data == "nutritionist_1":
        body_msg = select_doctor_info("nutritionist_1")
        doctor_photo_url = get_doctor_photo("nutritionist_1")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "nutritionist_1"
        bot.register_next_step_handler(call.message, check_date)
    if data == "nutritionist_2":
        body_msg = select_doctor_info("nutritionist_2")
        doctor_photo_url = get_doctor_photo("nutritionist_2")
        doctor_photo = open(doctor_photo_url, 'rb')
        bot.send_photo(call.message.chat.id, doctor_photo)
        bot.send_message(call.message.chat.id, body_msg)
        globalVar[call.message.chat.id] = {}
        globalVar[call.message.chat.id]['service'] = "nutritionist_2"
        bot.register_next_step_handler(call.message, check_date)
    bot.answer_callback_query(call.id)


# Проверка свободного времени на указанную дату
@bot.message_handler()
def check_date(message: Message):
    try:
        if datetime.strptime(message.text, '%d.%m.%Y') > datetime.now():
            globalVar[message.chat.id]['date'] = message.text

            times = check_selected_date(globalVar[message.chat.id]['date'], globalVar[message.chat.id]['service'])
            all_time = {'10.00', '11.00', '12.00', '13.00', '14.00', '15.00', '16.00', '17.00'}
            for t in times:
                if t in all_time:
                    all_time.remove(t)
            all_time = sorted(all_time)
            keyboard = keyboards.get_session_time(all_time)
            bot.send_message(message.chat.id, 'Выберите дату', reply_markup=keyboard)
            bot.register_next_step_handler(message, get_time)
        else:
            bot.send_message(message.chat.id, 'Введите дату, которая еще не настала')
            bot.register_next_step_handler(message, check_date)

    except ValueError:
        bot.send_message(message.chat.id, 'Введите дату в верном формате!')
        bot.register_next_step_handler(message, check_date)


@bot.message_handler()
def get_time(message: Message):
    all_time = {'10.00', '11.00', '12.00', '13.00', '14.00', '15.00', '16.00', '17.00'}
    globalVar[message.chat.id]['time'] = message.text
    record_data = {
        "date": globalVar[message.chat.id]['date'],
        "time": globalVar[message.chat.id]['time'],
        "visitor_id": message.chat.id,
        "doctor_specialization": globalVar[message.chat.id]['service']
    }
    if (globalVar[message.chat.id]['time'] in check_selected_date(globalVar[message.chat.id]['date'],
                                                                  globalVar[message.chat.id]['service'])) or \
            (globalVar[message.chat.id]['time'] not in all_time):
        bot.send_message(message.chat.id, "Выберите дату из предложенных")
        bot.register_next_step_handler(message, get_time)
    else:
        create_record(record_data)
        bot.send_message(message.chat.id, f"Вы успешно записаны на прием\nДата: {globalVar[message.chat.id]['date']}\n"
                                          f"Время: {globalVar[message.chat.id]['time']}")
        globalVar.pop(message.chat.id)
        # GET Запрос к Giphy
        gif = get_gif(gif_id)
        # Отправка Gif
        bot.send_video(message.chat.id, gif)
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=keyboards.get_menu_keyboard())
        bot.register_next_step_handler(message, menu)


# Функция рассылки сообщения
def send_advertisement_message():
    users_id = get_all_users_id()
    for user_id in users_id:
        bot.send_message(user_id[0], "Запишитесь на прием и узнайте свое состояние здоровья")


# Создание потока
def sending():
    schedule.every(60).seconds.do(send_advertisement_message)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    my_thread = threading.Thread(target=sending)
    my_thread.start()
    bot.polling(none_stop=True)
