# Tri Dao
# 1954347
# Part a: Write a program that reads dates from input, one date per line. Each
# date's format must be as follows: March 1, 1990. Any date not following
# that format is incorrect and should be ignored. Use the find() method to
# parse the string and extract the date. The input ends with -1 on a line
# alone. Output each correct date as: 3/1/1990.

value = 1
months = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']
while value == 1:
  try:
    user_input = input()
  except SyntaxError:
    continue
  if user_input == '-1':
    break

  try:
    arrange = user_input.split()
    digit = len(arrange)
    if digit != 3:
      continue
    month = arrange[0]
    day = arrange[1]
    year = arrange[2]
    d, comma = day.split(',')

    for x in range(len(months)):
      if user_input.find(months[x])>=0:
        new_month = str(x+1)
        print('{}/{}/{}'.format(new_month, d, year))
        break
  except ValueError:
    continue