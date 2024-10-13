name1 = input("what is your name? ")
name2 = input("what is his/her name? ")

combine_string = name1 + name2
lower_case_string = combine_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l + o + v + e

love_score = str(true) + str(love)

print(love_score,"%")

if int(love_score)<=10:
    print("katega sabar rkh...")

elif 10<int(love_score)<=90:
    print("theek hi hai jada khush mat ho...")
else:
    print("shi chl rha h tension mt lo")
