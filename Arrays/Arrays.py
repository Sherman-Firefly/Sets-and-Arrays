import array as arr

mar=["car", "banana", 2, 4, 1.2, (4,32,1), 2, 2, 4]
print(mar)

print(mar.count(2))
mar.append("Hola")
print(mar)

mar.insert(0, "yes")
print(mar)

mar.reverse()
print(mar)

mar.copy()
print(mar)

mar.clear()
print("\n", mar)

mar2=[8,12,53,33,21]
mar3=[99,21,45,66,88]
mylist=list(set(mar2)|set(mar3))
print(mylist)

mar4=mar2+mar3
print(mar4)