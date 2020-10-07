#Tri Dao
#1954347
#6.22 CIS 2348 LAB: Brute force equation solver

#''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

#''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

#''' Type your code here. '''
Result = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if a*x + b*y == c and d*x + e*y == f:
           print(x, y)
           Result = True

if not Result:
    print('No solution')