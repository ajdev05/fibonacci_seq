#Febonacci Sequence 
# AJ
number = int(input("Enter the amount of numbers: "))
def fibonacci(number):
    num1 = 0
    num2 = 1
    print(num1)
    print(num2)
    for x in range(2,number):
        num3 = num1+num2
        num1 = num2
        num2 = num3
        print(num3)
fibonacci(number)
