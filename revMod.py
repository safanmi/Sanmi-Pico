from string import ascii_uppercase
#Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

List = [104,372,110,436,262,173,354,393,351,297,241,86,262,359,256,441,124,154,165,165,219,288,42]

Alphabets ="0"+ ascii_uppercase + "0123456789_"
for items in List:
  #RevMod = pow((items % 41), -1, 41)
  
  print (Alphabets[pow(items, -1, 41)], end="")
