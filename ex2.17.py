def sortLine(line):
    print(sorted(line.split(), key=str.lower))
    print(sorted(line.split(), key=len))


print(sortLine('Juss wakin up in the morning gotta thank god i dont know but today seems kinda odd'))
