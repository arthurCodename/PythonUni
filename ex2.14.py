def getMax(line):
    return max(line.split(), key=len)


print(getMax(" i love pancakes"))


def getMaxLength(line):
    return len(max(line.split(), key=len))


print(getMaxLength(" i love pancakes"))
