checksum = open("checksum.txt", "r")
contenu = checksum.read()
liste = contenu.split("\n")
checksum.close()
a = 0
a = str()
dictionnaire = dict()
for a in liste:
    print(a)
    coupledict = a.split()
    print(coupledict)
    dictionnaire[coupledict[1]] = coupledict[0]
print(dictionnaire)

#a = int()
#while a != 6:
#    print(a)
#    a = a + 1
