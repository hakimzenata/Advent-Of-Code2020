#!/usr/bin/python3
f = open('day_1.txt','r')
line = f.readline();

x = [line]
while line:
    line = f.readline()
    x.append(line)
def first_task(x):
    for z in range(0, len(x)):
        for y in range(0, len(x)):
            try:
                if (int(x[z])+int(x[y])) == 2020:
                    return print (f'numbers : {int(x[z])}, {int(x[y])}\nmultiplication :{int(x[z])* int(x[y])}')
            except ValueError:
                pass
def second_task(x):
    for z in range(0, len(x)):
        for y in range(0, len(x)):
            for l in range(0, len(x)):
                try:
                    if (int(x[z])+int(x[y])+int(x[l])) == 2020:
                       return  print (f'numbers : {int(x[z])}, {int(x[y])}, {int(x[l])}\nmultiplication :  {int(x[z])*int(x[y])*int(x[l])}')
                except ValueError:
                    pass
first_task(x)
second_task(x)
