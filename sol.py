Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

List = [165,248,94,346,299,73,198,221,313,137,205,87,336,110,186,69,223,213,216,216,177,138]

for items in List:
    remainder = items % 37

    if remainder == 36:
        print("_")
    if 0 <= remainder <= 25:
        print (Alphabets[remainder])
    if 26 <= remainder <=35:
        print(Alphabets[remainder])
