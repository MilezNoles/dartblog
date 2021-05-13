import os
from slugify import slugify


# функции для отправки на почту
def get_mail_subject(nick):
    return f"{nick}, ты зарегистрировался на littlebitofawesomeness.ru"


def normalizer_bd(word):
    """
    заменяет "-" на " "
    и делает все заглавными
     буквами(для единого вида)
    """
    return word.replace("-"," ").title()

def get_mail_context(nick, email, password):
    """
    создает html для письма с данными о пользователе
    """
    slug = slugify(nick)

    html = ""
    html += f'<h3>Привет, {nick}!</h3>'
    html += f'<p>Ты успешно зарегистрировался на проекте по сбору и рассылке вакансий;)</p>'
    html += f'<p>Вот данные которые ты указал при регистрации:<br>'
    html += f"Логин: {nick}<br>"
    html += f"Почта: {email}<br>"
    html += f"Пароль: {password}</p>"
    html += "Не забудь указать в профиле город и специальность(для того чтобы сервис загрузил свежие вакансии для тебя)<br>"
    html += f"<a class='btn btn-primary' href='https://littlebitofawesomeness.ru/profile/{slug}/' role='button'>Профиль</a><br>"
    html += "<a class='btn btn-primary' href='https://littlebitofawesomeness.ru/vacancies/' role='button'>К вакансиям</a>"

    return html
