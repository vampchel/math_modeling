print("Дано квадратное уравнение")
a=int(input("Введите значение коэффицента a: "))
b=int(input("Введите значение коэффицента b: "))
c=int(input("Введите значение коэффицента c: "))
D=b**2-4*a*c
x1=b*(-1)+D/2*a
x2=b*(-1)-D/2*a

if D>0:
  print(x1)
  print(x2)
if D<0:
  print("Нет решений")
if D==0:
  print(x1)



  