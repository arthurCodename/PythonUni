def getTotalLength(line):
    return sum(map(len, line.split()))


print(getTotalLength("Hello from the other side"))
