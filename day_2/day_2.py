import fileinput
from collections import defaultdict

p1 = 0 #number of valid passwords for the first task
p2 = 0 #number of valid passwords for the second task
lines = list(fileinput.input()) #import lines from the file
for line in lines: 
    word = line.strip().split() #split words by space
    min_pas,max_pass = [int(i) for i in word[0].split('-')] # split the word i-j and extract the min and max number
    car_req = word[1][0] #extract the requested caracter
    password = word[2] #extract the password
    count = defaultdict(int) #number of password to be validated 
    for car in password :
        count[car] += 1 #each letter with it occurence number
    if min_pas <= count[car_req] <= max_pass: #validate if the requested caracter is with in the range
        p1 += 1
    if (password[min_pas-1] == car_req) ^ (password[max_pass-1] == car_req): # validate if the requested caracter is in the position max and nim
        p2 += 1
print(f'the first task : {p1}')
print(f'the second task : {p2}')
