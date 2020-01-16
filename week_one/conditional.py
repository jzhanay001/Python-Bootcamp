"""number= int(input("Enter a number:"))
min_num=3
max_num=10
if number>min_num and number < max_num:
    print("nice")
elif number > (min_num-2) and number < (max_num+2):
    print("Kinda nice")
else:
    print("not nice")"""
"""
class Hello:
    def __init__ (self, name):
        self.name=name
        self.age=10

hello = Hello ('bob')


print (hello.name, hello.age)
#print (hello.age)
a=[2,10,4,7,8,1,7,6]
print(a[:3])
print(a[3:])
"""
def boo():
    x=3
    y=2
    return x, y
def vix():
    x,y=boo()
    return x,y

print(vix())
