def getAllZeros(nobiggie):
    i = 0
    for let in str(nobiggie):
        if let == "0":
            i += 1

    return i

print(getAllZeros(45000000000))
