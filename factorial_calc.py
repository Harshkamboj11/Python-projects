fac = int(input("which number's factorial you want? "))
multiply = 1
for i in range(1,fac+1):
    multiply *= i

print(f"the factorial of {fac} is {multiply}")