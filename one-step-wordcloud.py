import os
import shutil
import webbrowser
import main
import wordcloudgenerate
flag=0
usee='Iridescent'
projroute=r"C:\Users\阮乐天\Desktop\shuiyuan\shuiyuanwordcloud"
try:
    os.mkdir(f'{projroute}/{usee}')
except FileExistsError:
    flag=1
if os.path.exists(f'{projroute}/{usee}/word.json')==0:
    main.requ(usee)
    wordcloudgenerate.wc(usee)
else:
    wordcloudgenerate.wc(usee,path=f'{projroute}/{usee}/word.json')
name=[f'{usee}.png','record.json','word.json']
try:
    for na in name:
        shutil.move(f'{projroute}/{na}',f'{projroute}/{usee}/{na}')
except FileNotFoundError:
    flag=1
os.system(f'{projroute}/{usee}/{usee}.png')

