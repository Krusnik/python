#!/usr/bin/python3.5

import sys
import getpass
from pexpect import pxssh

login = input('login: ')
password = getpass.getpass("password: ")

s = pxssh.pxssh()

if not s.login ('172.16.24.146', login, password):
    print ("SSH session failed on login.")
    print (str(s))
else:
    print ("SSH session login successful")
    s.sendline ('ls -l')
    s.prompt()
    print (s.before)
    s.logout()

