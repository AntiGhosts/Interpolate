i = int(input ("Quer interpolar quantas vezes?\n"))
v = int(input("Qual é o primeiro valor da ponta?\n"))
v2 = int(input("Qual é o segundo valor da ponta?\n"))
cb = input ("Pra cima ou pra baixo?(c/b)\n").upper()
a = 0
if cb == 'c':
  r1 = v+v2
  r2 = r1/2
  for a in range(0,i,a+1):
    rf = v2+r2
    rf2 = rf/2
    t = rf2+v2
    tf = t/2
    print(rf2)

if cb == 'b':
  r1 = v+v2
  r2 = r1/2
  for a in range(0,i,a+1):
    a+1
    rf = v+r2
    rf2 = rf/2
    print(rf2)
