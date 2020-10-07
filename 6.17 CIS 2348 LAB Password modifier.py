#Tri Dao
#1954347
#6.16 LAB: Password modifier

word = input()
password = ''

for y in word:
    if(y == 'i'):
        password+='!'
    elif(y == 'a'):
        password += '@'
    elif (y == 'm'):
        password += 'M'
    elif (y == 'B'):
        password += '8'
    elif (y == 'o'):
        password += '.'
    else:
        password += y
password += "q*s"
print(password)