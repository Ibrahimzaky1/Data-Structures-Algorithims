def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe

numbers = [3, 6, 2, 4, 3, 6, 8, 9]
duplicate = None
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i] + " is a dupliacate")
            break

for i in range(len(numbers)):
    if numbers[i] == duplicate:
        print(i)

for i in range(len(numbers)):
    if numbers[i] == 68:
        print(i)

