#codding utf-8
import re
# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
email = input('Введите ваш email: ')

user = {'name': name, 'surname': surname, 'email': email}

pattern_name_surname = re.compile('^[A-ZА-ЯЁ][а-яa-zё]*$')

result_name = pattern_name_surname.findall(user['name'])

result_surname = pattern_name_surname.findall(user['surname'])

if result_name and result_surname:
    print(f'{user["surname"]} {user["name"]} - имя и фамилия указаны верно', end=', ')

elif result_name == [] and result_surname:
    print(f'{user["surname"]} {user["name"]} - неверно указано имя', end=', ')

elif result_surname == [] and result_name:
    print(f'{user["surname"]} {user["name"]} - неверно указана фамилия', end=', ')

elif result_surname == [] and result_name == []:
    print(f'{user["surname"]} {user["name"]} - неверно указаны фамилия и имя', end=', ')

pattern_email = re.compile('^([a-zа-я]+|_|\.|[0-9]+)+@([a-zа-я]+|[0-9]+)+\.(ru|org|com)$')

result_email = pattern_email.search(user['email'])

if result_email:
    print(f'{user["email"]} - email указан верно')

else:
    pattern_email = re.compile('^.*@.*\.(.+)$')

    result_email = pattern_email.search(user['email'])

    if result_email:
        if result_email.group(1) != 'com' and result_email.group(1) != 'ru' and result_email.group(1) != 'org':
            email_domen = f', .{result_email.group(1)} - неправильный домен'

        else:
            email_domen = ''

    else:
        email_domen = ', нет домена'

    print(f'{user["email"]} - неверно указан email (спецсимвол, заглавная буква{email_domen}, или неверный формат)')


# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

pattern = re.compile('')
result = pattern.findall(some_str)

if result:
    print('В тексте есть идущие подряд точки')

else:
    print('В тексте нет идущих подряд точек')