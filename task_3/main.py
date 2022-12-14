
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def cutX(x,y,d):  # cрез звезды по оси X
    Ox = list(range(x-d,x+d+1))
    Oz = data[y][(x-d):(x+d+1)]

    fig = plt.figure()  # создали пространство
    ax = plt.axes()
    title_cutX = 'Срез звезды с координатами (' + str(x) + ',' + str(y) + ') по оси X'
    ax.set_title(title_cutX)

    plt.plot(Ox,Oz,'r-')
    plt.show()


def cutY(x,y,d):  # срез звезды по оси Y
    Oy = list(range(y-d,y+d+1))
    Oz=[]
    for i in range(y-d,y+d+1):
        Oz.append(data[i][x])
        
    fig = plt.figure()  # создали пространство
    ax = plt.axes()
    title_cutY = 'Срез звезды с координатами (' + str(x) + ',' + str(y) + ') по оси Y'
    ax.set_title(title_cutY)

    plt.plot(Oy,Oz,'b-')
    plt.show()

def grafik_star_3d(x,y,d): #функция для 3Д графика

    fig=plt.figure()  #создали пространство
    ax=plt.axes(projection='3d')
    title_3d = '3-х мерный график звезды с координатами ('+str(x)+','+str(y)+')'
    ax.set_title(title_3d)

    #пространство заначений для х и y
    Ox=list(range(x-d,x+d+1))
    Oy=list(range(y-d,y+d+1))
    X,Y=np.meshgrid(Ox,Oy)

    Z=np.zeros((len(Ox),len(Oy))) #заполняем данный массив значениями по оси Oz.
    for i in range(len(Oy)):      #как бы смотря на пл-ть xOy сверху
        for j in range(len(Ox)):  #точка (x-d,y-d) в левом верхнем углу
            Z[i][j]=data[Oy[i]][Ox[j]]

    ax.plot_surface(X,Y,Z,cmap='cividis')
    plt.show()




image = fits.open('v523cas60s-001.fit') #читаем файл
data = image[0].data #вытаскиваем список числовых данных
plt.imshow(data, cmap='gray',vmin=1E3, vmax=2E3) #исходное изображение
plt.colorbar()
plt.show()

koordinat=input('Введите координаты интересующей звезды:').split()
x=int(koordinat[0])
y=int(koordinat[1])

cutX(x,y,30)
cutY(x,y,30)
grafik_star_3d(x,y,30)