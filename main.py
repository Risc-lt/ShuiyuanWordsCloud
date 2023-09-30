import json
import requests
from time import sleep
username='Iridescent'
def requ(username):
    offset=[0,31,62,92]
    for i in range(5800):
        offset.append(offset[i+3]+30)
    headers={
        'Cookie': "_t=aRls2HJnfpyCLuhZ0%2F1NlDQtJiE4a6p8KopOqiN8rka86oiQnqNeLD282coyuQgrQf9d1iR08dYIlwLNGwpj83TvJHSPKbqK%2BSQPpl%2F%2Fpqx65u7BjyHc%2F8dH3hMkYbKNEShEM1nM%2BAi1%2BXhcqQXE8ekcGAO47DRXVjlVvaGYNH2fWLd5gzzBvD1TX4RtiiRP3igcjNRQgLDLXzCeXHO8WgZHFHIGMhDbK0FTr%2FL%2FMkrq%2BJx2zFGG3zY8m6b1zbf2AjKDKLeWf1H2P7u%2Baso1Kg%3D%3D--hLttJO%2F3CnNzrCNo--HBYBt7OfTHfFAlUaMfEi5Q%3D%3D",
        'Content-Type': 'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    timelist=[]
    words=[]
    i=0
    while 1:
        index=offset[i]
        url=f'https://shuiyuan.sjtu.edu.cn/user_actions.json?offset={index}&username={username}&filter=4,5'
        res=requests.get(url, headers=headers).json()
        print(res)
        try:
            for k in range(30):
                timelist.append(res['user_actions'][k]['created_at'])
                print(res['user_actions'][k]['created_at'])
                words.append(res['user_actions'][k]['excerpt'])
        except IndexError:
            break
        i+=1
        sleep(0.1)
    with open('record.json','w') as file:
        json.dump(timelist,file)
    with open('word.json','w') as file:
        json.dump(words,file)