import numpy as np

def Time(JD): #переход от юлианских дней к фрмату год.месяц.день время наблюдения

    JDN=float(JD)//1+2400000 #по целой части расчитываем коэффиценты для расчета даты
    a=JDN+32044
    b=(4*a+3)//146097
    c=a-(146097*b)//4
    d=(4*c+3)//1461
    e=c-(1461*d)//4
    m=(5*e+2)//153

    day=e-(153*m+2)//5+1
    month=m+3-12*(m//10)
    year=100*b+d-4800+(m//10)

    JDTime=float(JD)%1 #по дробной находим время
    hour=(JDTime*24)
    minute=(hour%1)*60
    second=(minute%1)*60

    w=[day,month,year,hour//1,minute//1,second//1] #сотавили списк, перевели его из чисел в строки
    for i in range(6):
        if w[i]<10:
            w[i]='0'+str(int(w[i]))
        else:
            w[i]=str(int(w[i]))
    t=w[0]+'.'+w[1]+'.'+w[2]+' '+w[3]+':'+w[4]+':'+w[5]
    return(t)

def sortirovka(sort_list): #сортировать данные по датам
    for N in range(1,len(sort_list)):
        perestav=sort_list[N]
        proverka=0
        for i in range(N,-1,-1):
            if sort_list[N][1]<sort_list[i][1]:
               mesto=i
               proverka=1
        if proverka==1:
             for i in range(N,mesto,-1):
                sort_list[i]=sort_list[i-1]
             sort_list[mesto]=perestav
    return sort_list


file=open('task2_data (1).dat','r').read().split('\n')

data=[]
for i in range(1,len(file)): #создаем массив данных из прочитаного файла
    data.append(file[i].split())

delete_list=[]
stars={}
for i in range(len(file)-1):#преобразовываем названия
    if len(data[i])>4:
        data[i][0]=data[i][0].upper()+'_'+data[i][1].capitalize()
        del(data[i][1])
        if data[i][0] not in stars:#добавляем в словарь с названиями звезд
            stars[data[i][0]]=[]
        if data[i][2].capitalize() not in stars.get(data[i][0]): #доавляем к ключам названия возможные фильтры
            stars.get(data[i][0]).append(data[i][2].capitalize())
    elif len(data[i])<4:
        delete_list.append(i) # запоминаем строки которые необходимо удалить
    else:
        chars=list(data[i][0])
        data[i][0]=chars[0].upper()+chars[1].upper()+'_'+chars[-3].upper()+chars[-2].lower()+chars[-1].lower()
        if data[i][0] not in stars:  # добавляем в словарь с названиями звезд
            stars[data[i][0]] = []
        if data[i][2].capitalize() not in stars.get(data[i][0]):  # доавляем к ключам названия возможные фильтры
            stars.get(data[i][0]).append(data[i][2].capitalize())

#удаляем стрки
schetchik=0
for i in delete_list:
    del(data[i-schetchik])
    schetchik=schetchik+1

for key in stars: #ввыводим на экран звезды и их филльтры
    filters=''
    for i in range(len(stars[key])):
        filters=filters+stars[key][i]+' '
    print('Звезда: ', key,' Фильтры: ', filters)

v=input('Введите звезду и необходимые фильтры: ').split(' ')
name=v[0]
filters=[]
for i in range(1,len(v)):
    filters.append(v[i])

#формируем необходимуе данные для записи в файл

zagolovki=' DD.MM.YY   Time      HJD 24...     ' #создаем строку заголовков
for i in range(len(filters)):
    zagolovki=zagolovki +'       '+ filters[i]
zagolovki=zagolovki + '\n'

data_for_save=zagolovki
data=sortirovka(data) #упорядочили по возрастанию даты

for i in range(len(data)): #вписываем данные
    if data[i][0]==name:
         schetchik=0
         for filter in filters:
            schetchik=schetchik+1
            if data[i][2]==filter:
                data_for_save= data_for_save + Time(data[i][1])+ '    ' + data[i][1] + '        '*schetchik + data[i][3] + '\n'

open('_' + name + '_.dat','w').write(data_for_save)
