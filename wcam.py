from time import sleep
import os
from colorama import init, Fore, Back, Style
import subprocess
import sys

init()

input("Открой окно в полный экран\n\n(Enter)")

os.system ('clear')

print(Fore.RED)
sleep (1.4)
#Здесь возможна оптимизацая.... НУЖНО УБРАТЬ ЭТИ ДОЛБАННЫЕ ПРИНТЫ!!1!!!1!!1
print("""
 ██╗██╗███╗░░░███╗  ░█████╗░██╗░░░░░░██╗░░░░░░░██╗░█████╗░██╗░░░██╗░██████╗
 ██║╚█║████╗░████║  ██╔══██╗██║░░░░░░██║░░██╗░░██║██╔══██╗╚██╗░██╔╝██╔════╝
 ██║░╚╝██╔████╔██║  ███████║██║░░░░░░╚██╗████╗██╔╝███████║░╚████╔╝░╚█████╗░
 ██║░░░██║╚██╔╝██║  ██╔══██║██║░░░░░░░████╔═████║░██╔══██║░░╚██╔╝░░░╚═══██╗
 ██║░░░██║░╚═╝░██║  ██║░░██║███████╗░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░██████╔╝
 ╚═╝░░░╚═╝░░░░░╚═╝  ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░

 ░██╗░░░░░░░██╗░█████╗░████████╗░█████╗░██╗░░██╗██╗░██████╗░  ██╗░░░██╗░█████╗░██╗░░░██╗
 ░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║██║██╔════╝░  ╚██╗░██╔╝██╔══██╗██║░░░██║
 ░╚██╗████╗██╔╝███████║░░░██║░░░██║░░╚═╝███████║██║██║░░██╗░  ░╚████╔╝░██║░░██║██║░░░██║
 ░░████╔═████║░██╔══██║░░░██║░░░██║░░██╗██╔══██║██║██║░░╚██╗  ░░╚██╔╝░░██║░░██║██║░░░██║
 ░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░╚█████╔╝██║░░██║██║╚██████╔╝  ░░░██║░░░╚█████╔╝╚██████╔╝
 ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚═════╝░ 
""")
print(Fore.RESET+" V - 0.9. Открытый альфа тест")
print("									   (c) (づ￣ ³￣)づ")
sleep (1.4)

print("Читать лицензионное соглашение? Y/n")
fff = input("(незнание его не освобожадет ответственности)\n: ")
ffff = fff.replace(' ', '')
def sda():
	print(Fore.YELLOW)
	print("")
	print("")
	print("")
	print("					Внимание! ")
	sleep (1.4)
	print("			Создатель данного ПО не несёт ответственности")
	sleep (1.4)
	print("			За совершённые пользвоателем действия. ")
	sleep (1.4)
	print("			И не призывает заниматься противозаконными дияниями!")
	sleep (1.4)
	print("			Это уголовно наказуемо, да и в общем глупо...")
	print("")
	sleep (1.4)
	print("			Данная программа-скрипт, которая всего лишь")
	sleep (1.4)
	print("			Автоматизирует процесс проверки Wi-Fi на устойчивость")
	sleep (1.4)
	print('			Так же, я всего лишь очередной "Скрипткиди".')
	sleep (1.4)
	print("			Поэтому извиняюсь за костыли и/или говнокод.")

	input(Fore.RESET+"\n(Enter)")

	sleep (1.4)

if ffff == "y":
	sda()
elif ffff == "Y":
	sda()
elif ffff == "n":
	sleep (1.4)
	print('')
elif ffff == "N":
	sleep (1.4)
	print('')
else:
	print('Но никто не пришёл')
#УХУ Я ПОФИКСИЛ ЕТОТ СУПЕР БАХ
sleep(1)
os.system ("clear")
sleep(1)
print(Fore.CYAN)
print("""							╭╮╭╮╭╮  ╭━━━╮  ╭━━━╮  ╭━╮╭━╮
							┃┃┃┃┃┃╱╱┃╭━╮┃╱╱┃╭━╮┃╱╱┃┃╰╯┃┃
							┃┃┃┃┃┃╱╱┃┃╱╰╯╱╱┃┃╱┃┃╱╱┃╭╮╭╮┃
							┃╰╯╰╯┃╱╱┃┃╱╭╮╱╱┃╰━╯┃╱╱┃┃┃┃┃┃
							╰╮╭╮╭╯╭╮┃╰━╯┃╭╮┃╭━╮┃╭╮┃┃┃┃┃┃
							 ╰╯╰╯ ╰╯╰━━━╯╰╯╰╯ ╰╯╰╯╰╯╰╯╰╯""")

sleep (1.4)
#/sys/class/net os.listdir()
print(Fore.RED+"[*]"+Fore.RESET+" Подготовка к работе.... ")
sleep (1.4)

print(Fore.RED+"[К]"+Fore.RESET+" Введите пароль суперпользователя если потребуется")
sleep (1.8)

subprocess.run (["sudo", "whoami"], stdout=subprocess.DEVNULL)
sleep(1.4)

print(Fore.RED+"[*]"+Fore.RESET+" Готово!")
sleep(1.4)

os.system("clear")
sleep(1.4)
os.system ("python3 modes.py")
