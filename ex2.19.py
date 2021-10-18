def filling(L):
    for i in L:
        if len(str(i)) < 3:
            print(str(i).zfill(3))
        else:
            print(i)


filling([7, 3, 4, 5, 24, 145, 765, 45])
