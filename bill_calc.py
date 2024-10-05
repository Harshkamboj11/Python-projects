
units = int(input("enter the units consumed: "))

if 0<units <= 100:
    bill =int (0.5*units)
elif 100<units<=200:
    bill = int(units*0.75)
elif 200<units<=300:
    bill = int(1.20*units)
elif units>300:
    bill = int(1.50*units)

if units>0:
  print(f"total units consumed = {units}")
else:
    print("units are invalid.....")

print(f"total bill is {bill}")