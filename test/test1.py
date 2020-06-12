from math import sqrt
class Ptbh():
     def __init__(self, a, b, c):
          self.a= a
          self.b= b
          self.c= c

     def gpt(self):
          self.delta = self.b**2 - 4*self.a*self.c
          if self.delta >0:
               print("pt co nghiem x1= ", (-self.b + sqrt(self.delta)) / (2 * self.a))
               print("pt co nghiem x2= ", (-self.b - sqrt(self.delta)) / (2 * self.a))
          elif self.delta ==0:
               print("phuong trinh co nghiem x=", -self.b/(2*self.a))
          else:
               print("pt vo nghiem")

mypt= Ptbh(1, -3, 2)
mypt.gpt()
ư

