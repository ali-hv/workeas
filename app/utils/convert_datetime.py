import jdatetime
import re


def to_persian(date):
    num_word = {'01': 'فروردین', '02': 'اردیبهشت', '03': 'خرداد', '04': 'تیر', '05': 'مرداد', '06': 'شهریور',
                '07': 'مهر', '08': 'آبان', '09': 'آذر', '10': 'دی', '11': 'بهمن', '12': 'اسفند'}

    farsi_nums = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}

    date, time = str(date).split(' ')
    date = date.split('-')
    date[1] = num_word[date[1]]
    date[0], date[2] = date[2], date[0]
    date = ' '.join(date)

    r = f"{date} ساعت {time}"
    return r
    


def to_persian_digits(number):
    persian_digits = '۱۲۳۴۵۶۷۸۹۰'
    normal_digits = '1234567890'
    translation_table = str.maketrans(normal_digits, persian_digits)
    translated_number = str(number).translate(translation_table)
    return translated_number


def to_jalali(tasks):
    for i in range(len(tasks)):
            date = tasks[i].date
            tasks[i].date = jdatetime.datetime.fromgregorian(year=date.year, month=date.month, day=date.day,
                                                            hour=date.hour, minute=date.minute, second=date.second)
            tasks[i].date = to_persian(tasks[i].date)
            
    return tasks