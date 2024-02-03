Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

List = [165,248,94,346,299,73,198,221,313,137,205,87,336,110,186,69,223,213,216,216,177,138]

for items in List:
    mod = items % 37

    if ((mod == 36) | (0 <= mod <= 25) | (26 <= mod <= 35)):
       print (Alphabets[mod])

   




 #print("_")
   # if 0 <= mod <= 25:
    # if 26 <= mod <=35:
        #print(Alphabets[mod])