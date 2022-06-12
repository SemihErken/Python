x = range(1,101)

roster = [i for i in x]

other = []
i = 3
for i in roster:
    if( i % 3 == 0):
        other.append(i)
print(other)

