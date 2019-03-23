#!/usr/bin/python2
#-*- coding: utf-8 -*-
import os
import time
import sys
import time

def expetasi():
		print c+"[1] "+p+"Youtube"
		print c+"[2] "+p+"Website"
		print c+"[3] "+p+"Contact"
		pilih = input("Gak pilih besok mati > ")
		if pilih ==1:
			os.system('clear')
			print(white),("jangan lupa untuk subscribe dan klik lonceng")
			time.sleep(2)
			os.system("termux-open-url https://www.youtube.com/channel/UCnV18haS6MvRkqYbRMYm7Zg")
		elif pilih ==2:
			os.system('clear')
			os.system("termux-open-url https://www.gagapilmu.tech")
		elif pilih ==3:
			os.system('clear') 
			os.system("termux-open-url https://wa.me/+6283807359899")


def blacksmoke():
        print c+"[1] "+p+"Youtube"
        print c+"[2] "+p+"Website"
        print c+"[3] "+p+"Contact"
        pilih = input("Gak pilih besok mati > ")
        if pilih ==1:
                os.system('clear')
                print("~Jangan lupa untuk subscribe dan klik lonceng")
                time.sleep(2)                                                                                     
		os.system("termux-open-url https://www.youtube.com/channel/UC2bPH6mgQg11JNLW23G6T")
        elif pilih==2:
                os.system('clear')
                os.system("termux-open-url http://odiq1337.blogspot.com")
        elif pilih==3:
                os.system('clear')
                os.system("termux-open-url https://wa.me/+6281364873762")

b = '\033[34;1m'
g = '\033[32;1m'
p = '\033[35;1m'
c = '\033[36;1m'
r = '\033[31;1m'
w = '\033[37;1m'
y = '\033[33;1m'
os.system('clear') 
print y+"                               _.._"
print y+"                             .'    '."
print y+"                            (____/`\ \\ "
print y+"                           (  |' ' )  ) .    "
print y+"                           )  _\= _/  (     "
print y+"                 __..---.(`_.'  ` \\    )   "
print y+"                `;-''-._(_( .      `; (     "
print y+"                /       `-`'--'     ; )"
print y+"               /    /  .    ( .  ,| |("
print y+"_.-`'---...__,'    /-,..___.-'--'_| |_)"
print y+"'-'``'-.._       ,'  |   / .........'"
print y+"       ``;--'`;   |   `-`"
print y+"             `'..__.'\n"

print w+"[1].About              "+c+"[3].Lanjut"
print b+"[2].Exit               "+r+"[4].Recode"

pilih = input("pilih > ")

if pilih == 1:
	print c+"[1].Shodiq (BlackSmoke)"
	print p+"[2].Apridal (3XP3T4S1)"
	pilih = input("About > ")
	if pilih ==1:
		blacksmoke()
	elif pilih ==2:
		expetasi()
elif pilih == 3:
	os.system('python2 V-BP.py')

elif pilih == 4:
        print(w+"[1].BlackSmoke")
        print(g+"[2].3XP3T4S1")
        oh = input("Recode > ")
        if oh ==2:
        	os.system("termux-open-url https://wa.me/6283807359899?text=Bang%20Saya%20boleh%20recode%20Tools%20Bokepnya") 
	elif oh ==1:
        	os.system("termux-open-url https://wa.me/6281364873762?text=Bang%20Saya%20boleh%20recode%20Tools%20Bokepnya")
