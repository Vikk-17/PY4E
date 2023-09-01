count=0
total = 0
largest=None
smallest=None
num_arr=[3, 41, 12, 9, 74, 15]
for i in num_arr:
    count = count + 1
    total = total + i
    if largest is None or i > largest:
        largest = i
    if smallest is None or i < smallest:
        smallest = i
    # print(f"Loop: {i} {largest}")
print(f"Count: {count}")
print(f"Total: {total}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")