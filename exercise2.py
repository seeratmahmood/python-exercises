n = 1
while n < 10:
  print(f'n = {n}')
  print(f'n + 10 = {n + 10}')
  n += 1
  
  
n = 1
while n < 10:
  print(f'n = {n}')
  print(f'2 ^ n = {2 ** n}')
  n += 1
  
 
n = 5
if n < 6:
  print('Today is a weekday')
else:
  print('Today is the weekend')
  


for i in range(1, 8):
  if i < 6:
    print('Today is a weekday')
  else:
    print('Today is the weekend')
    

year = 2048

isLeap = False
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
  isLeap = True
if isLeap:
  print(f'The year: {year} is a leap year')
else:
  print(f'The year: {year} is not a leap year')
  
  
  
for year in range(1900, 2023):
  isLeap = False
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    isLeap = True
  if isLeap:
    print(f'The year: {year} is a leap year')
  else:
    print(f'The year: {year} is not a leap year')