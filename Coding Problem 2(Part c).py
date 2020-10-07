# Tri Dao
# 1954347

#Part c: Modify your program further so that after parsing all dates from the
#input file “inputDates.txt”, it writes out the correct ones into an
#output file called: “parsedDates.txt”.

Openfile = open('inputDates.txt','r')
Readfile = Openfile.readlines()
file2 = open('parsedDates.txt','w')

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
        content = new_month + '/' + d + '/' + year
        print(content)
        file2.write(content + '\n')
      else:
        continue

  except ValueError:
    continue

Openfile.close()
file2.close()
