# def get_rectangle_area(length, width):
#     square = length * width
#     return square
    
# def get_rectangle_perimeter(length, width):
#     perimeter = (length + width) * 2
#     return perimeter

# # Длина прямоугольника.
# length = 5
# # Ширина прямоугольника.
# width = 10

# info1 = get_rectangle_area(length,width)
# info2 = get_rectangle_perimeter(length,width)
# print('Площадь:',info1)
# print('Периметр:', info2)


# # Опишите параметры функции calculate_watering().

# def calculate_watering(plant_type, number_of_plants, volume_per_plant = 2.5):
#     calculation = number_of_plants * volume_per_plant
#     print(plant_type, number_of_plants,'шт.:', 'для полива требуется', calculation, 'л воды.')
#     return calculation

# # Не изменяйте код ниже этого комментария: 
# # если ваша функция написана правильно - эти вызовы должны успешно сработать.

# # Вызов функции с позиционными аргументами:
# calculate_watering('Артишоки', 20, 4)

# # Вызов функции с позиционными аргументами, без опционального:
# calculate_watering('Кивано', 15, 2.5)

# # Вызов функции с именованными аргументами, без опционального:
# calculate_watering(number_of_plants=15, plant_type='Тыквы')




# # Из модуля math импортируйте функцию, вычисляющую факториал числа
# # и задайте ей псевдоним fact.
# from math import factorial as fact

# # Из модуля random импортируйте функцию, возвращающую случайное число
# # и задайте ей псевдоним rnd.
# from random import randint as rnd

# # С помощью функции под псевдонимом rnd присвойте переменной value
# # случайное значение в диапазоне от 1 до 10 включительно.
# value = rnd(1, 10)


# # С помощью функции под псевдонимом fact вычислите факториал числа, 
# # сохранённого в переменной value.
# result = fact(value)

# # Распечатайте результат в нужном формате. 
# # Для печати нескольких значений перечислите их через запятую.
# print('Факториал', value, ' равен', result)




# bash = 31
# c_and_c_plus_plus = 29
# c_sharp = 11
# html_css = 36
# java = 19
# javascript = 37
# sql = 34

# def analyze_skills():
#     # Среди всех переменных найдите минимальное и максимальное значение.
#     # Напечатайте фразы, описанные в задании (две строки).
#     list = [bash,c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql]
#     print('Доля питонистов, у которых есть наименее популярный навык (в %):', min(list))
#     print('Доля питонистов, у которых есть наиболее популярный навык (в %):', max(list))

# # Не удаляйте вызов функции.
# analyze_skills()




# c_sharp = 375
# java = 546
# javascript = 915
# php = 288
# python = 603

# def analyze_jobs():
#     # Вычислите общее количество исследованных вакансий.
#     total_jobs = c_sharp + java + javascript + php + python
#     # Вычислите процент вакансий для Python от общего числа вакансий
#     # и округлите результат до двух знаков (до сотых долей):
#     python_percent = (python * 100) / total_jobs
#     # Напечатайте фразы, описанные в задании (две строки).
#     print('Общее число исследованных вакансий, в тысячах:', total_jobs)
#     print('Вакансии для Python-разработчиков, в %:', round(python_percent, 2))
#     ...

# analyze_jobs()


\





# # Импортировать функцию для получения случайного значения
# # и присвоить ей псевдоним rnd
# from random import randint as rnd


# # Объявить функцию get_dumplings_recommendation(),
# # которая вернёт (return) случайное число в диапазоне от 10 до 20.
# def get_dumplings_recommendation():
#     namber = rnd(10, 20)
#     print('Оптимальным количеством пельменей на сегодня будет', namber)
#     return namber

# # Вызвать функцию get_dumplings_recommendation() и напечатать заданную фразу.
# get_dumplings_recommendation()



# Импортировать функцию для получения случайного значения
# и присвоить ей псевдоним rnd
# from random import randint as rnd


# # Объявить функцию get_dumplings_recommendation(),
# # которая вернёт (return) случайное число в диапазоне от 10 до 20.
# def get_dumplings_recommendation(min,max):
#     namber = rnd(min, max)
#     print('Оптимальным количеством пельменей на сегодня будет', namber)
#     return namber

# # Вызвать функцию get_dumplings_recommendation() и напечатать заданную фразу.
# get_dumplings_recommendation(25, 30)








#     # Эта функция должна возвращать слово Hello 
# def say_hello():
#     return 'Hello'


#  # Эта функция должна возвращать строку "World!" (с восклицательным знаком).
# def say_world():
#     return 'World!'

#       # В переменной result должна быть фраза Hello, World!
#       # А функция print() должна вывести эту фразу на экран.
# result = say_hello() + ', ' + say_world()
# print(result)


# # Получаем данные в секундах
# response = 424562

# # Переведите полученное значение в необходимые единицы измерения
# days = response // 86400
# hours = 75600// 3600
# minutes = 3360 // 60  
# seconds = 120 // 60

# print(response, 'секунд - это')
# print('Дней:', days)
# print('Часов:', hours)
# print('Минут:', minutes)
# print('Секунд:', seconds)




# def find_answer():
#     number = 3
#     # Далее проводите операции над number отдельно по шагам
#     number *= 100
#     number /= 5
#     number -= 20
#     number += 2
#     # Верните результат:
#     print('Ответ на главный вопрос жизни, Вселенной и всего такого:', int(number))
#     return int(number)
# find_answer()




# Объявите функцию get_season(), принимающую на вход название месяца;
# функция должна вернуть название сезона, которому принадлежит месяц
# или строку "Ошибка в написании месяца!"

# Место для вашего кода
# def get_season(month):
#     if month == 'июль' or 'июнь' or 'август':
#         print('Лето')
#         return month
#     elif month == 'сентябрь' or 'октябрь' or 'ноябрь':
#         print('Осень')
#         return month
#     elif month == 'декабрь' or 'январь' or 'февраль':
#         print('Зима')
#         return month
#     elif month == 'март' or 'апрель' or 'май':
#         print('Весна')
#         return month
#     else:
#         print('Вы ошиблись')


# # Для контроля вызовем функцию и напечатаем результат.
# print(get_season('июнь'))
# print(get_season('мартобрь'))



# def get_season(month):
#     if month == 'июнь':
#         return 'лето'
#     elif month == 'июль':
#         return 'лето'
#     elif month == 'август':
#         return 'лето'
#     elif month == 'сентябрь':
#         return 'осень'
#     elif month == 'октябрь':
#         return 'осень'
#     elif month == 'ноябрь':
#         return 'осень'
#     elif month == 'декабрь':
#         return 'зима'
#     elif month == 'январь':
#         return 'зима'
#     elif month == 'февраль':
#         return 'зима'
#     elif month == 'март':
#         return 'весна'
#     elif month == 'апрель':
#         return 'весна'
#     elif month == 'май':
#         return 'весна'
#     else:
#         return 'Ошибка в написании месяца!'
 

# # Для контроля вызовем функцию и напечатаем результат.
# print(get_season('июнь'))
# print(get_season('мартобрь'))





# x = -2
# y = 5
# if x > 0 and y > 0:
#     print('Первая четверть')
# elif x > 0 and y < 0:
#     print('Четвертая четверть')
# elif x < 0 and y > 0:
#     print('Вторая четверть')
# else:
#     print('Третья четверть')



# Вместо многоточия укажите необходимые параметры.
# def count_tiles(depth, length, width=None):
#     # Опишите условие, когда ширина бассейна не указана.
#     if width == None:
#         width = length

#     # Посчитайте, сколько понадобится плиток для стенок и дна бассейна.
#     calck_second = (2 * depth * (width + length)) + (length * width)
    
#     # Верните результат работы функции.
#     return calck_second


# total_tiles = count_tiles(1, 1, 1)
# print('Общее количество плиток для строительства бассейна:', total_tiles)




# Код этой функции не меняйте.
# def count_tiles(depth, length, width=None):
#     if width is None:
#         width = length

#     width_side = 2 * width * depth
#     length_side = 2 * length * depth
#     bottom_tiles = length * width
#     total = width_side + length_side + bottom_tiles

#     return total

# # Передайте в функцию нужный параметр и напишите её код.
# def make_phrase(information,):
#     if information == 11 or information == 12 or information == 13 or information == 14:
#         text = 'плиток'
#     elif information % 10 == 1:
#         text = ' плитку '
#     elif information % 10 == 2 or information % 10 == 3 or information % 10 == 4:
#         text = ' плитки '
#     else:
#         text = ' плиток '
#     return str(information) + ' ' + text 


# total_tiles = count_tiles(2, 2, 2)
# ab = make_phrase(total_tiles)
# # Выведите на экран нужное сообщение.
# print('Для строительства бассейна нужно заготовить', ab )






# # Вместо многоточия укажите нужные параметры.
# def find_pool_capacity(num_of_people, length,width = None,):
#     # Опишите условие, когда передано отрицательное значение длины.
#     if length < 0:
#         length = abs(length)

#     # Опишите условие, когда передано отрицательное значение 
#     # количества людей.
#     if num_of_people <= 0:
#         num_of_people = abs(num_of_people)

#     # Опишите условие, когда ширина бассейна не указана, когда указано
#     # отрицательное значение, и когда положительное.
#     if width == None:
#         width = length
#     elif width < 0:
#         width = abs(width)

#     # Опишите условие вывода сообщений и распечатайте эти сообщения.
#     kvm = length * width
#     if num_of_people / kvm <=2 :
#         print('Бассейн площадью', kvm, 'кв. м. вмещает', num_of_people, 'чел.')
#     else:
#         print('Бассейн площадью', kvm, 'кв. м. не вмещает', num_of_people, 'чел.')

# # Проверьте работу функции, можете подставить свои значения.
# find_pool_capacity(15, 3, 3)
# find_pool_capacity(4, 5, 10)
# find_pool_capacity(-10, -5, -2)



# Из модуля decimal импортируйте тип данных Decimal и параметр getcontext.
# Из модуля math импортируйте константу "пи".

# from decimal import Decimal, getcontext

# from math import pi

# Pi = Decimal(str(pi))
# # Приведите константу "пи" к типу Decimal.
# # Помните, что Decimal() принимает строку, а константа "пи" - это число.
# # Установите необходимую точность для вычислений.

# getcontext().prec = 10

# # Объявите функцию find_ellipse_area() с двумя параметрами.

# def find_ellipse_area(r1, r2):
#     return r1*r2*Pi

# # Объявите три переменные типа Decimal -
# # две длины полуосей эллипса и глубину пруда.r
# r1 = Decimal('1.75')
# r2 = Decimal('2.5')
# h = Decimal('0.35')
# # Вызовите функцию find_ellipse_area(), в аргументах передайте длины полуосей эллипса.
# area = find_ellipse_area(r1, r2)

# # Вычислите объём пруда: площадь * глубина.
# V = area * h
# print('Площадь эллипса:', area, 'кв.м.')
# print('Объём воды для наполнения пруда:', V, 'куб.м.')



# Допишите нужные импорты.
# import datetime

# def timedelta_days(datetime_str_1, datetime_str_2):

#     d1 = datetime.datetime.strptime(datetime_str_1, '%Y/%m/%d %H:%M:%S')
#     d2 = datetime.datetime.strptime(datetime_str_2, '%Y/%m/%d %H:%M:%S')

#     return (d2 - d1).days

# difference = timedelta_days('2019/05/10 00:00:00', '2019/10/04 00:00:00')

# print('От начала посевной до начала сбора урожая прошло', difference, 'дней.')





# # Пропишите нужные импорты.
# def get_weekday_name(day_number):
#     weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
#     return weekdays[day_number]
# import datetime

# def get_day_after_tomorrow(date_string):
#     date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
#     new_date = date + datetime.timedelta(days=2)
#     print ("Послезавтра будет", new_date.strftime('%A'))



# # Проверьте работу программы, можете подставить свои значения.
# get_day_after_tomorrow('2024-01-01')
# get_day_after_tomorrow('2024-01-02')
# get_day_after_tomorrow('2024-01-03')
# get_day_after_tomorrow('2024-01-04')
# get_day_after_tomorrow('2024-01-05')
# get_day_after_tomorrow('2024-01-06')




# import datetime

# def get_weekday_name(weekday_number):
#     if weekday_number == 0:
#         return 'понедельник'
#     elif weekday_number == 1:
#         return 'вторник'
#     elif weekday_number == 2:
#         return 'среда'
#     elif weekday_number == 3:
#         return 'четверг'
#     elif weekday_number == 4:
#         return 'пятница'
#     elif weekday_number == 5:
#         return 'суббота'
#     elif weekday_number == 6:
#         return 'воскресенье'
#     else:
#         return 'Попробуй еще раз' 

# def get_day_after_tomorrow(date_string):
#     # Напишите код функции.
#     date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
#     today_weekday_name = get_weekday_name(date.weekday())
#     day_after_tomorrow = date + datetime.timedelta(days=2)
#     day_after_tomorrow_name = get_weekday_name(day_after_tomorrow.weekday())
#     print(f'Сегодня {date_string}, {today_weekday_name}, а послезавтра будет {day_after_tomorrow_name}')

# # Проверьте работу программы, можете подставить свои значения.
# get_day_after_tomorrow('2024-01-01')
# get_day_after_tomorrow('2024-01-02')
# get_day_after_tomorrow('2024-01-03')
# get_day_after_tomorrow('2024-01-04')
# get_day_after_tomorrow('2024-01-05')
# get_day_after_tomorrow('2024-01-06')



# from datetime import datetime
# def get_results(leader_time, your_time):
#     if leader_time == your_time:
#         print(
#             'Вы пробежали за',
#             your_time,
#             'и победили!'
#         )
#         return
#     time_format = '%H:%M:%S'
#     leader_time_object = datetime.strptime(leader_time, time_format)
#     your_time_object = datetime.strptime(your_time, time_format)
#     difference = your_time_object - leader_time_object
#     print(
#         'Вы пробежали за',
#         your_time,
#         'с отставанием от лидера',
#         str(difference)
#     )
# get_results('02:02:02', '02:02:02')
# get_results('02:02:02', '03:04:05')




# from decimal import Decimal, getcontext
# getcontext().prec = 3
# def get_monthly_payment(total_sum, months_count, percents):
#     monthly_raw = Decimal(total_sum) / Decimal(str(months_count))
#     monthly_addition = monthly_raw * Decimal(str(percents / 100))
#     total = monthly_addition + monthly_raw
#     return total
# payment_value = get_monthly_payment(54, 24, 9)
# print('Ежемесячный платёж:', payment_value, 'ВтК')




# movie_name_sequence = [
#     'Д', 'ж', 'о', 'н', 'н', 'и', ' ', 'М', 'н', 'е', 'м', 'о', 'н', 'и', 'к'
# ]
# # Место для вашего кода
# print(movie_name_sequence[0])яя
# print(movie_name_sequence[1])
# print(movie_name_sequence[7])
# print(movie_name_sequence[13])
# print(movie_name_sequence[14])
# print(movie_name_sequence[0])






# apple_tree_yields = 150, 210, 90, 120, 140, 190, 130, 150, 110, 210, 150

# # Объявите функцию reversed_sort(), 
# # которая вернёт отсортированный по убыванию кортеж.
# def reversed_sort(tpl):
#     return tuple(sorted(tpl, reverse=True))
# result = reversed_sort(apple_tree_yields)
# # Напечатайте:
# print(result[0])  # наибольшее значение из кортежа result,
# print(result[1])  # второй элемент из кортежа result,
# print(result[2])  # третий элемент из кортежа result.


# def assess_yield(number_of_plants, average_weight):
#     # Ваш код здесь
#     total_weight = (number_of_plants * average_weight)/1000
    
#     if total_weight > 100:
#         rating = 'Ожидается отличный урожай.'
                   
#     elif total_weight > 50 and total_weight <=100:
#         rating = 'Ожидается хороший урожай.'
        
#     elif total_weight > 0 and total_weight <=50:
#         rating = 'Урожай будет так себе.'
#     else:
#         rating = 'Урожая не будет.'
       
#     return total_weight, rating

# # Пример вызова функции

# # Вызываем функцию и распаковываем кортеж:
# total_weight, rating = assess_yield(50, 200)
# # Печатаем результат:
# print(total_weight, 'кг.', rating)




# # Количество корзин с овощами, шт.
# baskets = 462 
# # Средний вес овощей в одной корзине, кг.
# average_weight = 25
# # Стоимость одного килограмма урожая, в монетах.
# price_per_kg = 175 


# def calc(baskets, average_weight, price_per_kg):
#     total_weight = baskets * average_weight
#     total_cost = total_weight * price_per_kg
#     return total_weight, total_cost

# baskets = 462
# average_weight = 25
# price_per_kg = 175

# total_weight, total_cost = calc(baskets, average_weight, price_per_kg)

# print(f"Общий вес урожая: {total_weight} кг. Оценённая стоимость урожая: {total_cost}.")







# def compare_sequences(spisok_first, spisok_second):
#     if spisok_first > spisok_second:
#         return f'Список {spisok_first} больше.'
#     elif spisok_second > spisok_first:
#         return f'Список {spisok_second} больше.'
#     else:
#         return f'Списки равны.'

# sequence_1 = [69, 59, 57, 60, 63, 44, 46, 69]
# sequence_2 = [33, 73, 50, 25, 36, 68, 52, 76]
# # Вызовите функцию compare_sequences(),
# # передайте в неё списки sequence_1 и sequence_2.
# # Напечатайте результат, который вернёт функция.

# print(compare_sequences(sequence_1, sequence_2))

# Функция для создания словаря информации об овощах

# def create_vegetable_info(vegetables, varieties, yields):
#     vegetable_zip = zip(varieties,yields)    
#     vegetable_zip_second = zip(vegetables, vegetable_zip)
#     vegetable_info = dict(vegetable_zip_second)
#     return vegetable_info

# # Тестовые данные:
# vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
# varieties = ['Красный куб', 'Аллигатор', 'Василёк', 'Тропический закат', 'Арктик']
# yields = [6.5, 4.3, 2.8, 2.2, 3.5]



# # Вызов функции:
# print(create_vegetable_info(vegetables, varieties, yields))


# not_uniq_str = 'съешь же ещё этих мягких французских булок да выпей чаю'
# count_char_ferst = not_uniq_str.replace(' ', '')
# count_char = set(count_char_ferst)
# print(len(not_uniq_str))
# print(len(count_char))


# num_string_1 = '100 13 2 143 12 3 55 4 64 18 56'
# num_string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'

# separation_first = num_string_1.split()
# separation_second = num_string_2.split()

# a_bunch_of_first = set(separation_first)
# a_bunch_of_second = set(separation_second)
# common = set.intersection(a_bunch_of_first, a_bunch_of_second)
# print(len(common))

# Объявите функцию check_winners с параметрами scores и student_score.
# Функция должна напечатать результат в заданном формате.




# Объявите функцию check_winners с параметрами scores и student_score.
# Функция должна напечатать результат в заданном формате.

# # Вызовы для проверки работы функции check_winners().
# # Три набора данных - для проверки разных ситуаций.
# first_olympiad_scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28, 42, 40, 39, 1, 45, 37, 10, 31, 27, 17, 46, 2, 22, 35, 55]
# check_winners(first_olympiad_scores, 52)

# second_olympiad_scores = [22, 4, 42, 5, 54, 28, 19, 33, 8, 16, 23, 40, 39, 58, 9, 13, 48, 2, 51, 41, 21, 36, 55, 25, 31, 45, 44, 30, 1, 10]
# check_winners(second_olympiad_scores, 4)

# third_olympiad_scores = [36, 1, 49, 27, 8, 23, 13, 56, 46, 33, 45, 30, 16, 11, 41, 19, 43, 54, 39, 38, 40, 48, 34, 26, 5, 28, 21, 3, 51, 44]
# check_winners(third_olympiad_scores, 21)





# Объявите функцию get_stickers_comparison() с параметрами collection_1 и collection_2.
# Эта функция должна возвращать кортеж из трёх коллекций:
# - уникальные_стикеры из collection_1,
# - уникальные_стикеры из collection_2,
# - стикеры, которые есть в collection_1 и в collection_2.
# def get_stickers_comparison(collection_1, collection_2):
#     stas_stickers = list(sorted(set(collection_1) - set(collection_2)))
#     anton_stickers = list(sorted(set(collection_2) - set(collection_1)))
#     common_sticker = list(sorted(set(collection_1).intersection(set(collection_2))))

#     return (stas_stickers, anton_stickers, common_sticker)
# # Списки стикеров:
# stas_collection = ['Тим Бернерс-Ли', 'Линус Торвальдс', 'Ада Лавлейс', 'Линус Торвальдс', 'Маргарет Гамильтон', 'Бьярн Страуструп']
# anton_collection = ['Тим Бернерс-Ли', 'Гвидо ван Россум', 'Линус Торвальдс', 'Бьярн Страуструп', 'Бьярн Страуструп', 'Кен Томпсон', 'Деннис Ричи']

# # Вызываем функцию и распаковываем полученный кортеж в три переменные:
# stas_stickers, anton_stickers, common_stickers = get_stickers_comparison(stas_collection, anton_collection)
# # Печатаем результаты:
# print('Стикеры, которые есть только у Стаса:', stas_stickers)
# print('Стикеры, которые есть только у Антона:', anton_stickers)
# print('Стикеры, которые есть и у Стаса, и у Антона:', common_stickers)



# def is_palindrome(strin):
#     s = str.lower(strin).replace(' ', '')
#     return s == s[::-1]

# # Должно быть напечатано True:
# print(is_palindrome('А роза упала на лапу Азора'))
# # Должно быть напечатано False:
# print(is_palindrome('Не палиндром'))



# def pay_bills(month, bills):
#     if month % 3 == 0:  
#         return bills[1:-1]  
#     else:  # иначе
#         return [bills[0], bills[-1]]  


# # Вызов функции:

# print(pay_bills(1, ['Интернет', 'Коммуналка', 'Телефон', 'Страховка']))






# from random import randint

# # Начальная температура чая
# current_temperature = 85
# # Объявите цикл while

# while current_temperature > 60:
#     temperature_change = randint(1, 3)
#     current_temperature -= temperature_change
#     print(f'Прошла минута.')
#     print(f'Чай остыл ещё на {temperature_change} °C. Текущая температура: {current_temperature} °C')
# # В теле цикла получите случайное значение температуры, 
# # на которое остыл чай в этой итерации (в диапазоне от 1 до 3).
# # Уменьшите температуру чая на полученное значение.
# # Напечатайте нужные сообщения.
# print(f'Время пить чай!')
# # Напечатайте сообщение, которое должно быть выведено после завершения цикла.



# fruit_yields = [164.8, 105.0, 124.3, 113.8]  # Урожайность, кг на дерево.
# # Объявляем новый список, в него будем складывать изменённые значения.
# corrected_fruit_yields = []

# for fruit_yield in fruit_yields:
#     new_value = fruit_yields + 1.2
#     corrected_fruit_yields.append(new_value)

# # Объявите цикл, в нём переберите список fruit_yields.
# # В теле цикла к каждому значению списка добавьте 1.2,
# # затем получившееся значение сохраните в список corrected_fruit_yields.

# # Чтобы увидеть, что получилось, 
# # напечатаем список с откорректированными значениями.
# print(corrected_fruit_yields)


# vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
# # Сперва выполним эту задачу в обычном цикле
# new_sequence = []

# for vegetable in vegetables:
#     # Если в очередном элементе хранится строка с числом элементов меньше 7,
#     # в список new_sequence будет добавлен элемент со значением False,
#     # иначе - True.
#     list.append(new_sequence, len(vegetable) >= 7)

# print(new_sequence)

# # А теперь то же самое запишем в сокращённой форме:
# new_sequence_better = [len(vegetable) >= 7 for vegetable in vegetables]
# # Результат тот же, а код короче!
# print(new_sequence_better)

# def print_pack_report(starting_value):
#     for starting_values in range(starting_value, 0, -1):
#         if starting_values % 5 == 0 and starting_values % 3 == 0:
#             print(starting_values, '-', 'расфасуем по 3 или по 5')
#         elif starting_values % 5 == 0:
#             print(starting_values, '-', 'расфасуем по 5')
#         elif starting_values % 3 == 0:
#             print(starting_values, '-', 'расфасуем по 3')
#         else:
#             print(starting_values, '-', 'не заказываем!')

# # Пример использования функции
# print_pack_report(3)




# def count_canisters(temperatures_per_day):
#     hot_days_counter = 0
#     for forecast_temperature in temperatures_per_day:
#         if forecast_temperature > 29:
#             hot_days_counter += 1
#     print(f'Нужно канистр: {hot_days_counter}')
#     return hot_days_counter

# forecast_temperatures = [26, 28, 30, 31, 29, 31, 28, 26, 44]
# count_canisters(forecast_temperatures)



# def print_multiplication_table(multiplication):
#     # Напишите код, который напечатает таблицу умножения.
#     multiplication_first = [multiplication 1 * ]


# print_multiplication_table(multiplication)





# Напишите функцию get_competition_data().


# def get_competition_data(data):
#     first_race = data[0]
#     teams = first_race.keys()
#     print('Команды, участвовавшие в гонке:', ', '.join(sorted(teams)))
# races_data = [
#     {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
#     {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
#     {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
# ]
# get_competition_data(races_data)






# def get_competition_data(data):
#     first_race = data[0]
#     teams = first_race.keys()
#     print('Команды, участвовавшие в гонке:', ', '.join(sorted(teams)))

#     # вычисляем сумму баллов для каждой команды
#     scores = {team: sum([race[team] for race in data]) for team in teams}

#     winner = max(scores, key=scores.get)  # находим команду с наибольшей суммой баллов
#     print(f'В гонке победила команда {winner} с результатом {scores[winner]} баллов')

# races_data = [
#     {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
#     {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
#     {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
# ]
# get_competition_data(races_data)





                    # ХОЛОДИЛЬНИК






from datetime import date, timedelta, datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'

goods = {}


def add(items, title, amount, expiration_date=None):
    if title in items.keys() and expiration_date != None:
        items[title].append(
            {'amount': Decimal(amount), 'expiration_date': datetime.strptime(expiration_date, DATE_FORMAT).date()})
    elif title in items.keys() and expiration_date == None:
        items[title].append({'amount': Decimal(amount), 'expiration_date': None})
    elif title not in items.keys() and expiration_date != None:
        items[title] = (
        [{'amount': Decimal(amount), 'expiration_date': datetime.strptime(expiration_date, DATE_FORMAT).date()}])
    else:
        items[title] = ([{'amount': Decimal(amount), 'expiration_date': None}])
    return goods


print(add(goods, 'хлеб', 0.5, '2022-4-01'))
print(add(goods, 'Огурцы', 5, '2023-1-01'))


def add_by_note(items, note):
    notes = str.split(note, ' ')
    if len(str.split(notes[-1], '-')) == 3:
        title = str.join(' ', notes[0: -2])
        amount = Decimal(notes[-2])
        expiration_date = notes[-1]
        add(items, title, amount, expiration_date)
    elif len(str.split(notes[-1], '-')) != 3:
        amount = Decimal(notes[-1])
        title = str.join(' ', notes[0: -1])
        add(items, title, amount)
    return goods

print(add_by_note(goods, 'икра 1 2024-04-04'))
print(add_by_note(goods, 'хлеб 2 2024-01-01'))

def find(items, needle):
    finder = []
    for title in items:
        if str.lower(needle) in str.lower(title):
            finder.append(title)
    return finder

def amount(items, needle):
    total_amount = Decimal('0') 
    for item in find(items, needle):
        dict_list = items[item]
        total_amount += sum(dict_n['amount'] for dict_n in dict_list)  
    return total_amount

def expire(items, in_advance_days=0):
    today = date.today()
    today_in_advance = today + timedelta(days=in_advance_days)
    expire_name = []
    expire_amount = []

    for item in items:
        needle = item
        for i_dict in items[item]:
            expiration_date = i_dict.get("expiration_date", None)
            if expiration_date is not None: 
                exp_date = datetime.strptime(str(expiration_date), DATE_FORMAT).date()        
                if exp_date <= today_in_advance:
                    expire_name.append(needle)
                    expire_amount.append(amount(items, needle))                

    return list(zip(expire_name, expire_amount))
     
print(expire(goods,0))
