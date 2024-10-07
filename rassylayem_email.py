import smtplib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
password_email = os.getenv('senders_password')
senders_email = os.getenv('senders_email')
recipients_email = os.getenv('recipients_email')

site_name = 'https://dvmn.org/referrals/U46hZWTK0Afeup3hj6GPiBHV5xfoNPWMAeW2K0ny/'
friend_name = 'Artem'
sender_name = 'Aleksandr'

letter_template = ("""Привет, {friend_name}! {sender_name} приглашает тебя на сайт {site_name}!

{site_name} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {site_name}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {site_name}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
                   .format(site_name=site_name, friend_name=friend_name, sender_name=sender_name))

letter = ("""From: {senders_email}
To: {recipients_email}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

{letter_template}"""
          .format(letter_template=letter_template, senders_email=senders_email, recipients_email=recipients_email))
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(senders_email, password_email)
server.sendmail(senders_email, recipients_email, letter)
server.quit()




