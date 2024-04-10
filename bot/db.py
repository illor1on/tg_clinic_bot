import sqlite3
conn = sqlite3.connect('clinic.sqlite3', check_same_thread=False)


# Функция выборки данных о враче
def select_doctor_info(specialization):
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctor_info WHERE specialization=?", (specialization, ))
    info = cur.fetchall()
    doctor_name = info[0][1]
    doctor_description = info[0][2]
    price = info[0][4]
    msg_text = f"{doctor_name} \n{doctor_description} \nЦена: {price} /сеанс \n--- " \
               f"\nВВЕДИТЕ ДАТУ ПРИЕМА В ФОРМАТЕ 09.09.2024"
    return msg_text


# Функция получения url фото доктора
def get_doctor_photo(specialization):
    cur = conn.cursor()
    cur.execute("SELECT photo_path FROM doctor_info WHERE specialization=?", (specialization,))
    info = cur.fetchone()
    doctor_photo = info[0]
    return doctor_photo


# Функция получения даты и свободных сеансов на эту дату
def check_selected_date(date, doctor):
    cur = conn.cursor()
    cur.execute("SELECT * FROM session WHERE date=? AND doctor_specialization=?", (date, doctor))
    time = cur.fetchall()
    arr = []
    for e in time:
        arr.append(e[2])
    return arr


# Функция записи на сеанс
def create_record(record_data):
    cur = conn.cursor()
    cur.execute("INSERT INTO session (date, time, visitor_id, doctor_specialization) VALUES (?, ?, ?, ?)",
                (record_data['date'], record_data['time'], record_data['visitor_id'],
                 record_data['doctor_specialization']))
    conn.commit()


# Функция проверки, существует ли пользователь в базе
def check_user_existence(tg_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE user_id=?", (tg_id,))
    user_list = cur.fetchall()
    if not user_list:
        return False
    return True


# Функция добавления новых пользователей в базу
def add_user(tg_id):
    cur = conn.cursor()
    cur.execute("INSERT INTO user (user_id) VALUES (?)", (tg_id,))
    conn.commit()


# Функция получения id всех пользователей
def get_all_users_id():
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM user")
    users_id = cur.fetchall()
    return users_id
