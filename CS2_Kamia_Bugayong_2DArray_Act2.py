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

Using an array made it easier to organize and access the step count data for each person. Loops allowed me to calculate totals and averages quickly without manually adding each value. Finding the highest and lowest numbers was also simpler because the data was grouped in an organised format. For me, the easiest part was calculating totals using sum(), while the kinda harder part was gathering all values for the max/min operation.
