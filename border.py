#!/usr/bin/python3.5

import sys
import getpass
import subprocess

login = input('login: ')
hostname = '212.49.96.88'

class RemoteShell:
    def __init__(self, hostname = hostname, port=514, username=login, encoding='ascii'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.encoding = encoding
        self.rsh = ['/usr/bin/rsh', '-l', username, hostname]

    def exec_command(self, command, get_exit_code=True):
        if get_exit_code:
            command += '; echo $?'
        p = subprocess.Popen(self.rsh + [ command ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

        stdout, stderr = p.communicate()
        stdout = stdout.decode(self.encoding)
        stderr = stderr.decode(self.encoding)
        if not get_exit_code or p.returncode != 0:
            return stdout, stderr, p.returncode
        return stdout, stderr

sr = RemoteShell()
for i in sr.exec_command('show version'):
    print (str(i))
