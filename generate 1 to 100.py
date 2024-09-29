# Generate values from 1 to 100
values = list(range(1, 101))

# Remove odd numbers
values = [x for x in values if x % 2 == 0]

print(values)
