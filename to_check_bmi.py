a = input("enter your weight(kg): ")
b = input("enter your height(m): ")

bmi = float(int(a)/(float(b)*float(b)))
print("your body mass index is:", float(bmi))

if bmi<16:
    print("you are underweight(severe thinness)")
elif 16<bmi<=16.9:
    print("you are underweight(moderate thinness)")
elif 17<bmi<=18.4:
    print("you are underweight(mild thinness)")
elif 18.5<bmi<=24.9:
    print("your bmi is in normal range ")
elif 25<bmi<=29.9:
    print("you are overweight(pre-obese)")
elif 30< bmi <=34.9:
    print("obese(class-1)")
elif 35< bmi <=39.9:
    print("obese(class-2)")
else:
    print("obese(class-3)")


