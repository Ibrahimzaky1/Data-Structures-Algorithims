######### LESSON 3 #########
expenses = [2200, 2350, 2600, 2130, 2190]

print("extra spent in Febuary compared to January is:", expenses[1] - expenses[0])
print("total expenses in first quarter(first three months) is:", expenses[0] + expenses[1] + expenses[2])

if 2000 in expenses:
    print(" you spent excactlly 2000 in one of the months ")

else:
    print(" no month has excalctly 2000 in expenses ")

expenses.append("1980")
print(expenses)

expenses[3] -= 200
print(expenses)

