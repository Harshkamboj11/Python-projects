def even_number():
    print("to which number you want to add even numbers:")
    a = int(input(""))
    sum = 0

    for i in range(1,a):
        if i % 2 == 0:
            sum += i
    print(f"thw sum upto {a} is {sum}")


even_number()