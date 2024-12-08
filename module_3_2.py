# Задача "Рассылка писем"
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if "@" not in sender or (sender[-4:] != ".com" and sender[-4:] != ".ru" and sender[-4:] != ".net"):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'mrjlekc466@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'mrjlekc466@gmail.com', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'mrjlekc466@gmail.com', sender='urban.teacher@mail.uk')
send_email('Я объязательно не забуду о вебинаре', 'mrjlekc466@gmail.com', sender='mrjlekc466@gmail.com')
