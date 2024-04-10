from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# Reply клавиатура
# Клавиатура кнопок меню
def get_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("Запись к врачу"),
        KeyboardButton("Информация о клинике"),
        KeyboardButton("Контакты"),
    )
    return keyboard


# Reply клавиатура
# Клавиатура кнопок специализации
def get_specialization_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(
        KeyboardButton("Хирург"),
        KeyboardButton("Аллерголог"),
        KeyboardButton("Терапевт"),
        KeyboardButton("Офтальмолог"),
        KeyboardButton("Психиатр"),
        KeyboardButton("Диетолог"),
        KeyboardButton("Назад")
    )
    return keyboard


# Inline клавиатура
# Клавиаутра с врачами-хирургами
def get_surgeon_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
                InlineKeyboardButton("Шмелев Леонид", callback_data='surgeon_1'),
                InlineKeyboardButton("Круглов Руслан", callback_data='surgeon_2'),
            )
    return keyboard


# Inline клавиатура
# Клавиаутра с врачами-аллергологами
def get_allergist_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
                InlineKeyboardButton("Афанасьев Иван", callback_data='allergist_1'),
                InlineKeyboardButton("Медведев Михаил", callback_data='allergist_2')
            )
    return keyboard


# Inline клавиатура
# Клавиаутра с врачами-терапевтами
def get_therapist_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
                InlineKeyboardButton("Андреев Владимир", callback_data='therapist_1'),
                InlineKeyboardButton("Михайлов Демьян", callback_data='therapist_2'),
    )
    return keyboard


# Inline клавиатура
# Клавиаутра с врачами-офтальмологами
def get_ophthalmologist_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
                InlineKeyboardButton("Архипов Тимур", callback_data='ophthalmologist_1'),
                InlineKeyboardButton("Степанов Никита", callback_data='ophthalmologist_2'),
    )
    return keyboard


# Inline клавиатура
# Клавиаутра с врачами-психиатрами
def get_psychiatrist_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
                InlineKeyboardButton("Ткачев Илья", callback_data='psychiatrist_1'),
                InlineKeyboardButton("Иванов Артём", callback_data='psychiatrist_2'),
    )
    return keyboard


# Inline клавиатура
# Клавиаутра с врачами-диетологами
def get_nutritionist_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
                InlineKeyboardButton("Голубев Тимур", callback_data='nutritionist_1'),
                InlineKeyboardButton("Лазарев Георгий", callback_data='nutritionist_2'),
    )
    return keyboard


# Reply клавиатура
# Клавиатура с динамическим добавлением свободного времени записи на выбранную дату
def get_session_time(free_time):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for e in free_time:
        keyboard.add(
            KeyboardButton(e)
        )
    return keyboard
