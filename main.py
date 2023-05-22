i = int(input ("How many times do you want to interpolate?\n"))
v = int(input("What is the first tip value?\n"))
v2 = int(input("What is the second tip value?\n"))
cb = input ("up or down?(u/d)\n").upper()
a = 0
if cb == 'u':
  r1 = v+v2
  r2 = r1/2
  for a in range(0,i,a+1):
    rf = v2+r2
    rf2 = rf/2
    t = rf2+v2
    tf = t/2
    print(rf2)

if cb == 'd':
  r1 = v+v2
  r2 = r1/2
  for a in range(0,i,a+1):
    a+1
    rf = v+r2
    rf2 = rf/2
    print(rf2)
