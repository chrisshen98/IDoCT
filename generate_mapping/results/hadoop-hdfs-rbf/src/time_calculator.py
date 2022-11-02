file = "../logs/time-record"
f = open(file)
f = f.readlines()
sum = 0.0
for line in f:
    temp = line.split(" ")[1]
    sum += float(temp)
print(sum)
