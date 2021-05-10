import random
print('Привет! Попробуй отгадать число от 1 до 100.')
number = random.randint(1, 100)
info = int(input('Введите число от 1 до 100: '))
count = 0
while info != number:
	count += 1
	if number > info:
		print("Число больше")
	elif number < info:
		print('Число меньше')
	info = int(input('Попробуй еще раз: '))
print('Вы угадали, я загадал число', number)
print("Вы затратили всего", count, 'попыток!')
input("Нажмите Enter для выхода")