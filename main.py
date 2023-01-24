#!/usr/bin/python
import os as root
import requests
import threading 
root.system('clear')
fp = open('wordlist.txt')
banner ='''

\033[1;31m   ___                        
 \033[1;31m/ ___|___  _ __   __ _ _ __   \033[1;33m |\033[1;31m MY telegram :\033[1;32m @x93_sh
\033[1;31m| |   / _ \| '_ \ / _` | '_ \   \033[1;33m|\033[1;31m MY insta    :\033[1;32m @9x3_sh 
\033[1;31m| |__| (_) | | | | (_| | | | |  \033[1;33m|\033[1;31m MY github   :\033[1;32m @9x3-sh
 \033[1;31m\____\___/|_| |_|\__,_|_| |_|  \033[1;33m|\033[1;31m MY discoed  :\033[1;32m @00000
                              

'''
def main():
    print(banner)
    url = input("\033[1;34mEnter the url : ")
    print('\n')
    for i in fp.read().split('\n'):
        t = '/'   
        r = requests.get(url+t,i)
        print('\033[1;34m',url+t+i,'\033[1;32m',r.status_code)
main()
T1 = threading.Thread(target=main,args=())
T1.start()

