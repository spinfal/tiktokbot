import os, random; import time as t; from termcolor import colored as cl; from TikTokApi import TikTokApi
api = TikTokApi()

print('\033[H\033[J')
print(cl('spintok v1\n', 'green'))

user = input(cl('username: ', 'white'))
print(cl('\nsearching for ' + user + '...', 'cyan'))
api.byUsername(user)
print(cl('successfully found ' + user + '!\n', 'green'))
amount = input(cl('amount of followers: ', 'white'))
if amount == '0':
  print(cl('you cannot provide 0 as an input'))
  t.sleep(2)
  os.system('python3 follows.py')

sleep = [1, 2, 3]
follows = 0
while int(follows) <= int(amount):
  print(cl('\nsending followers...', 'green'))
  print(cl('sent ' + str(follows), 'cyan'))
  follows = follows + 1
  t.sleep(random.choice(sleep))
  print('\033[H\033[J')
print(cl('complete', 'green'))
t.sleep(2)
os.system('python3 main.py')