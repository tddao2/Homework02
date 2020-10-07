# Tri Dao
# 1954347

#Part b: After the program is working as above, modify the program so that it
# reads all dates from an input file “inputDates.txt” (an Example file is attached).

Openfile = open('inputDates.txt','r')
Readfile = Openfile.readlines()

months = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']

for string in Readfile:
  if string == '-1':
    break

  try:
    arrange = string.split()
    digit = len(arrange)
    if digit != 3:
      continue
    month = arrange[0]
    day = arrange[1]
    year = arrange[2]
    d, comma = day.split(',')

    for x in range(len(months)):
      if string.find(months[x]) >= 0:
        new_month = str(x+1)
        print('{}/{}/{}'.format(new_month, d, year))
        break
  except ValueError:
    continue

Openfile.close()
