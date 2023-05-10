day_text = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']


def get_weekday(day: int):
    return day_text[day]


class Dish:
    item = 'dish__item'
    photo = 'dish__photo-wrap'
    name = 'dish__name'
    weight = 'dish__weight'
    desc = 'dish_description'

