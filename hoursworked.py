print("Hours?")

hours = input(">")
hours = float(hours)


print("Rate?")
rate = input(">")
rate = float(rate)

pay = hours * rate 

if hours > 40:
    bonus = (hours-40) * rate / 2 
else:
    bonus = 0

total = pay + bonus 

print("Pay = ", pay)
print("Bonus =", bonus)
print("Total = ", total)