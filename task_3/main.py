
from astropy.io import fits
import matplotlib.pyplot as plt

def cutX(x,y,d):  # cрез звезды по оси X
    Ox = list(range(x-d,x+d))
    Oz = data[y][(x-d):(x+d)]


def cutY(x,y,d):  # срез звезды по оси Y
    Oy = list(range(y-d,y+d))
    Oz=[]
    for i in range(y-d,y+d):
        Oz.append(data[i][x])
    print(Oz)




image = fits.open('v523cas60s-001.fit') #читаем файл
data = image[0].data #вытаскиваем список числовых данных

cutX(1024,1024,20)
cutY(1024,1024,20)
