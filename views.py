import os, random, requests; import time as t; from termcolor import colored as cl; from TikTokApi import TikTokApi
api = TikTokApi()

print('\033[H\033[J')
print(cl('spintok v1\n', 'green'))

user = input(cl('link to video: ', 'white'))
print(cl('\nfetching the video ' + user + '...', 'cyan'))
api.getTikTokByUrl(user, language='en', proxy=None)
print(cl('successfully fetched ' + user + '!\n', 'green'))
r = requests.get(user)
if r.status_code != 200:
  print(cl('there was an error fetching the video', 'red'))
  t.sleep(2)
  os.system('python3 views.py')
amount = input(cl('amount of views: ', 'white'))
if amount == '0':
  print(cl('you cannot provide 0 as an input'))
  t.sleep(2)
  os.system('python3 views.py')

sleep = [0, 1]
views = 0
while int(views) <= int(amount):
  print(cl('\nsending views...', 'green'))
  print(cl('sent ' + str(views), 'cyan'))
  views = views + 1
  t.sleep(random.choice(sleep))
  print('\033[H\033[J')
print(cl('complete', 'green'))
t.sleep(2)
os.system('python3 main.py')