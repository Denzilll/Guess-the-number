import random
print('Привет! Попробуй отгадать число от 1 до 100.')
number = random.randint(1, 100)
levelselect = int(input('Введите сколько Вам нужно попыток (если вы достигните этого количества, то проиграете)' ))
level = levelselect
info = int(input('Введите число от 1 до 100: '))
count = 0
victory = 1
while info != number:
	count += 1
	if level == count:
		victory =- 1
		break
	if number > info:
		print("Число больше")
	elif number < info:
		print('Число меньше')
	info = int(input('Попробуй еще раз: '))
if victory == 1:
	print('Вы угадали, я загадал число', number)
	print("Вы затратили всего", count, 'попыток!')
else:
	print('Вы проиграли :(')
input("Нажмите Enter для выхода")