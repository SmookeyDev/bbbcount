import requests
import time, asyncio


globalresult = []

cookies = {
    'csrftoken': 'NhiDPMVsSGPjM9ueFAnzzfUKFBBubOx0',
    'mid': 'YIhAwwAEAAF4Meb0QFcJbmzK68os-',
    'ig_did': '677E3EEA-E935-4AB2-B219-1CAB0040EF6A',
    'ig_nrcb': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers',
}

params = (
    ('__a', '1'),
)

def excbot():

    while True:
        users = open('./users.txt', 'r').readlines()
        for user in users:
            user_info = requests.get('https://www.instagram.com/{}/'.format(user.replace('\n', '')), headers=headers, params=params, cookies=cookies).json()['graphql']['user']
            result = {'name': user_info['full_name'], 'username': user_info['username'], 'profile_pic': user_info['profile_pic_url_hd'], 'followers': "{:,.0f}".format(int(user_info['edge_followed_by']['count']))}
            if user_info['username'] not in str(globalresult):
                globalresult.append(result)
            else:
                for num, item in enumerate(globalresult):
                    if user_info['username'] in str(globalresult[num]):
                        globalresult[num] = result
        time.sleep(10)