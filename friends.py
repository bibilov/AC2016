from urllib.request import urlopen
from json import loads
from time import sleep


friends = []

data = urlopen('http://api.vk.com/method/friends.get?user_id=270619647').read().decode('utf8')
data = loads(data)
friends_id = data['response']

for f_id in friends_id:
    data = urlopen('http://api.vk.com/method/friends.get?user_id=' + str(f_id)).read().decode('utf8')
    data = loads(data)
    friends_friends_id = data['response']
    friends.append([f_id, set(friends_id) & set(friends_friends_id)])
    sleep(0.3)
    print(".", end="")
    
