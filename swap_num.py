#swaping integer without using temp variable

def swap(x,y):
  x = x + y
  y = x - y
  x = x - y
  return x,y

x = 20
y = 30
print(f'BEFORE: x = {x} y = {y}')
x,y=swap(x,y)
print(f'AFTER:  x = {x} y = {y}')
