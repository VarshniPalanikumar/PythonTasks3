

list1=['23','45','56','89']
list2=['23','45','84','80']
list3=['22','45','56','89','90']
dup=set()

for x in list1:
    for y in list2:
        for z in list3:
            if z == y and y==x:
                dup.add(z)
print(dup)
