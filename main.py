print("***Window Cleaning Calculator***")

win = int(input("How many windows do you need cleaned?"))

if win <= 5: 
  print(2.00*win+10.00)
elif win >= 6 and win <= 10:
  min = win-5 
  print(min*1.50+20.00)
elif win >= 11:
  minn = win-10
  print(minn*1.00+27.50)
else:
  print("Please reset code and try again.")
