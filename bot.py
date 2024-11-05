import ptbot
import os
from dotenv import load_dotenv, find_dotenv
from pytimeparse import parse


def render_progressbar(total, iteration, prefix='', suffix='', length=20, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def wait(chat_id, message):
    timer = parse(message)
    bot.create_timer(timer, bot_answer, chat_id=chat_id, message=message)


def countdown(chat_id, message):
    timer = parse(message)
    message_id = bot.send_message(TG_CHAT_ID, f'Таймер запущен, осталось {timer} сек')
    bot.create_countdown(timer, countdown_result, chat_id=message_id, timer=timer)


def countdown_result(secs_left, chat_id, timer):
    bot.update_message(TG_CHAT_ID, chat_id, f'Таймер запущен, осталось {secs_left} сек\n'
                                            f'{render_progressbar(timer, timer - secs_left)}')


def bot_answer(chat_id, message):
    bot.send_message(TG_CHAT_ID, 'Время вышло!')


def wait_countdown(chat_id, message):
    countdown(chat_id, message)
    wait(chat_id, message)


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    TG_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TG_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

    bot = ptbot.Bot(TG_TOKEN)
    bot.send_message(TG_CHAT_ID, 'Бот запущен!\nНа сколько поставить таймер?')
    bot.reply_on_message(wait_countdown)
    bot.run_bot()

