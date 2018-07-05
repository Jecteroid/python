# coding utf-8
# medical questionnaire

print('======= Медицинская анкета =======')
print('======= Данные строго конфиденциальны =======')

name = input('Ваше имя: ')
surname = input('Вашу фамилию: ')
ege = int(input('Ваш возраст: '))
weight = int(input('Ваш вес: '))

if ege < 30 and weight >= 50 and weight <= 120:
    res = 'хорошее состояние'

elif ege > 30 and (weight < 50 or weight > 120):
    res = 'следует заняться собой'

elif ege > 40 and (weight < 50 or weight > 120):
    res = 'следует обратится к врачу!'

print(name, surname + ',', ege, 'год,', 'вес', weight, '-', res)
