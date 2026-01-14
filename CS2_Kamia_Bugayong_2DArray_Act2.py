steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

names = ["Me", "Lia", "Jake"]

for i in range(len(steps)):
    print(names[i], "steps:", steps[i])
    total = sum(steps[i])
    average = total / len(steps[i])
    print("Total:", total)
    print("Average:", average)
    print()

all_values = []
for row in steps:
    for value in row:
        all_values.append(value)

maximum = max(all_values)
minimum = min(all_values)

print("Maximum value in dataset:", maximum)
print("Minimum value in dataset:", minimum)
