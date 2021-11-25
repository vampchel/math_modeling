a=int(input("Введите целое число: "))
b=int(input("Введите ещё одно целое число: "))
c=a//b
d=a%b
if b!=0:
  print(c)
  print(d)
if b==0:
  print("На ноль делить нельзя")
