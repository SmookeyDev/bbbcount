import requests
import time, asyncio


globalresult = []

def excbot():

    while True:
        users = open('./users.txt', 'r').readlines()
        for user in users:
            user_info = requests.get('https://www.instagram.com/{}/?__a=1'.format(user.replace('\n', ''))).json()['graphql']['user']
            result = {'name': user_info['full_name'], 'username': user_info['username'], 'profile_pic': user_info['profile_pic_url_hd'], 'followers': "{:,.0f}".format(int(user_info['edge_followed_by']['count']))}
            if user_info['username'] not in str(globalresult):
                globalresult.append(result)
            else:
                for num, item in enumerate(globalresult):
                    if user_info['username'] in str(globalresult[num]):
                        globalresult[num] = result
        time.sleep(10)
