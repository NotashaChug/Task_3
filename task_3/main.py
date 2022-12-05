
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def cutX(x,y,d):  # cрез звезды по оси X
    Ox = list(range(x-d,x+d+1))
    Oz = data[y][(x-d):(x+d+1)]
    plt.plot(Ox,Oz,'r-')
    plt.show()


def cutY(x,y,d):  # срез звезды по оси Y
    Oy = list(range(y-d,y+d+1))
    Oz=[]
    for i in range(y-d,y+d+1):
        Oz.append(data[i][x])
    plt.plot(Oy,Oz,'b-')
    plt.show()

def grafik_star_3d(x,y,d): #функция для 3Д графика

    fig=plt.figure()  #создали пространство
    ax=plt.axes(projection='3d')

    #пространство заначений для х и y
    Ox=list(range(x-d,x+d+1))
    Oy=list(range(y-d,y+d+1))
    X,Y=np.meshgrid(Ox,Oy)

    Z=np.zeros((len(Ox),len(Oy))) #заполняем данный массив значениями по оси Oz.
    for i in range(len(Oy)):      #как бы смотря на пл-ть xOy сверху
        for j in range(len(Ox)):  #точка (x-d,y-d) в левом верхнем углу
            Z[j][i]=data[Oy[i]][Ox[j]]

    ax.plot_surface(X,Y,Z)
    plt.show()




image = fits.open('v523cas60s-001.fit') #читаем файл
data = image[0].data #вытаскиваем список числовых данных


cutX(1024,1024,20)
cutY(1024,1024,20)
grafik_star_3d(1024,1024,20)