import os, getpass; from termcolor import colored as cl

print(cl('this is a fake tool. yes that is stupid, but i got bored.\nit does use tiktoks api, but it doesnt actually do anything!', 'red'))
bruh = getpass.getpass(cl('- enter to exit -', 'cyan'))
if bruh == '' or bruh != '':
  os.system('python3 main.py')