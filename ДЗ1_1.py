__author__ = "Мельникова Яна"

n = int(input("Введите целое число:"))
while n>10:
    x = n%10
    print (x)
    n = n//10
print (n)
