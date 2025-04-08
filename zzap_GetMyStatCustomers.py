from sys import argv
import webbrowser
import base64
import requests
import config
import time
import json
import ast


module, code_templ = argv


login = config.USERNAME
password = config.PASSWD
# code_templ = 350016735	#int код шаблона (пусто - выдаст статистику по всем)
api_key = config.API
#
#print (login)
#print (password)
#print (code_templ)
#print (api_key)

BASE_URL = "https://api.zzap.pro/webservice/datasharing.asmx/GetMyStatCustomers"	#ссылка на сервис
data_to_post = {"login":login,
                "password":password,
                "code_templ":code_templ,
                "api_key":api_key}

response = requests.get("https://api.zzap.pro/webservice/datasharing.asmx/GetMyStatCustomers?login=info@20bar.ru&password=Skar2500!&code_templ=&api_key=MBmE7rdJlQjqwrJjLks15PxWg2raF2h7mjVRxi69pb1fs4Me8ghbY1QJXeX")
#print(response.text)
symb_from = response.text.rfind("[") + 1
symb_to = response.text.rfind("]")
iter_str = response.text[symb_from:symb_to]
iter_list = iter_str.split(sep="},")

stat_date = str
descr_type_stat = str
counter = int
print (len(iter_str))

for i in range(len(iter_str)):
    a = iter_list[i]
    if a[-1] == "}":
        a = a
#        print (a)
    else:
        a = a + "}"
        print (a)
    spltd_dict = ast.literal_eval(a)

    for item in spltd_dict.items():
        if item[0] == 'stat_date':
            stat_date = item[1]
        elif  item[0] == 'descr_type_stat':
            descr_type_stat = item[1]
        elif item[0] == 'counter':
            counter = item[1]
        print(stat_date, descr_type_stat, counter)
    print("--------", end='\n')