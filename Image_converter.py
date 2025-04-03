from fileinput import filename
from PIL import Image
from PIL import ImageDraw, ImageFont
import subprocess
import os

path = "/Users/vladimirchi/PycharmProjects/New_AGer_search_engine/.venv/ZZap"
path2 = "/Users/vladimirchi/PycharmProjects/New_AGer_search_engine/.venv/2ZZap"
dirs = os.listdir(path)
#print(dirs)


for i in range(len(dirs)):
    try:
        path2pict = os.listdir(rf"{path}/{dirs[i]}")
#        print(f"{path2}/{dirs[i]}_{path2pict[0]}")
        print(f"{path}/{dirs[i]}/{path2pict[0]};{path2}/{dirs[i]}_{path2pict[0]}")
        os.rename(rf"{path}/{dirs[i]}/{path2pict[0]}", rf"{path2}/{dirs[i]}_{path2pict[0]}")

    except:
        print("No such file or directory")

# url = "https://disk.yandex.ru/d/sxrAZSaRWNl6gg/120bar161976.png"
#
# data = requests.get(url).content
#
# f = open('120bar161976.png','wb+') # Открываем новый файл
#
# f.write(data) # Сохранение данных изображения в переменную data в файл
#
# f.close() # Закрываем файл
#
# #img = Image.open('20bar.JPG') # Открываем, смотрим
# #img.show()
#
# file_path = '120bar161976.png'
#
# # Загрузка изображения
# urllib.request.urlretrieve(url, file_path)
#
# resource = urlopen(url)
# out = open(url, 'wb')
# out.write(resource.read())
# out.close()
#
# h = httplib2.Http('.cache')
# response, content = h.request(url)
# out = open(url, 'wb')
# out.write(content)
# out.close()
#
# #webbrowser.open(url)