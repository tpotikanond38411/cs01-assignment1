workscores = int(input("Enter your work score (30 full):"))
Midtermscores = int(input('Enter your midterm scores (30 full): '))
Finalscores = int(input('Enter your midterm scores (40 full):'))
grade = workscores + Midtermscores + Finalscores
print('Your total score is :',grade)
if 80<= grade <= 100:
  print('A')
elif 75<= grade <= 79:
  print('B+')
elif 70<= grade <= 74:
  print('B')
elif 65<= grade <= 69:
  print('C+')
elif 60<= grade <= 64:
  print('C')
elif 55<= grade <= 59:
  print('D+')
elif 50<= grade <= 44:
  print('D')
elif 0<= grade <= 49:
  print('F')