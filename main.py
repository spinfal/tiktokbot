import os, webbrowser; import time as t; from termcolor import colored as cl

os.system('pyppeteer-install')
print('\033[H\033[J')
print(cl('spintok v1\n', 'green'))
print('choose a tool:\n1. likes\n2. follows\n3. views\n4. shares\n5. about')
choice = input(cl('> ', 'white'))

if choice == '1':
  print(cl('loading...', 'cyan'))
  os.system('python3 files/likes.py')
elif choice == '2':
  print(cl('loading...', 'cyan'))
  os.system('python3 files/follows.py')
elif choice == '3':
  print(cl('loading...', 'cyan'))
  os.system('python3 files/views.py')
elif choice == '4':
  print(cl('loading...', 'cyan'))
  os.system('python3 files/shares.py')
elif choice == '5':
  os.system('python3 files/about.py')
else:
  print(cl(choice + ' is an invalid choice.', 'red'))
  t.sleep(2)
  os.system('python3 main.py')