print("May tinh phuong trinh bac 2 ax^2 + bx + c = 0 tot nhat VN")
print("Viec cua may la nhap a, b, c cho tao")
import math
a = input("nhap A: ")
b = input("nhap B: ")
c = input("nhap C: ")
a = float(a)
b = float(b)
c = float(c)


if a == 0: 
  x = -c/b 
  print("x1 = x2 = ", x)
else:
  delta = b*b - 4*a*c 
  delta = float(delta)
  print(delta)
  if delta < 0:
    print("No solution")
  elif delta == 0:
    x=-b/2*a
    print("x1 = x2 = ", x)
  elif delta > 0:
    x1=(-b+ math.sqrt(delta))/(2*a)
    x2=(-b- math.sqrt(delta))/(2*a)
    print("x1= ", x1)
    print("x2= ", x2)

