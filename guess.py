# Учебная игра "Угадай число"
import random

guessesTaken = 0

print ('Привет, игрок! Представься пожалуйсита.')
myName = input()

number = random.randint(1, 20)
print('Что ж, ' + myName + ' я загадаю число от 1 до 20.')

for guessesTaken in range(6):
	print('Попробуй угадать.')
	guess = int(input())
#	guess = int(guess)

	if guess < number:
		print('Твоё число слишком маленькое')

	if guess > number:
		print('Твоё число слишком большое.')

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')

if guess != number:
	number = str(number)
	print('Увы, я загадал число ' + number + ".")