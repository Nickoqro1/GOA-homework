name = str(input("enter your name: "))
num1 = int(input("enter first number: "))
num2 = float(input("enter second number: "))
boolean = bool(input("enter calculation: "))

print(type(name))
print(type(num1))
print(type(num2))
print(type(boolean))

# 3
# შექმენით 5+ ცვლადი და ისე შეადარეთ ერთმანეთს რომ დაიბეჭდოს True.

bool1 = 5
bool2 = 2
bool3 = 6
bool4 = 5
bool5 = 9

print(bool1 > bool2 < bool3 > bool4 < bool5)

# 4
# დაწერეთ True და False ყველა შესაძლო ვარიანტი and და or ოპერატორებზე

False and True # False
False and False # False
True and False # False
True and True # True

False or False # False
False or True # True
True or False # True
True or True # True

print(False and True) # False
print(False and False) # False
print(True and False) # False
print(True and True) # True

print(False or False) # False
print(False or True) # True
print(True or False) # True
print(True or True) # True