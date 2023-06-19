set1 = {"rock","pop","soul","hard rock","r&b","pop","soul"}
print(set1)

lst1 =[3,4,5,6,3,5,453,5,3,5,3465]
lst1 = set(lst1)
print(lst1)

lst1.add(3432)
print(lst1)
lst1.remove(3432)
print(3432 in lst1)
lst2 ={3,5,6,4,4,5,6,56,564}
# lay ra nhung phan tu chung cua 2 set
lst3 = lst1 & lst2
print(lst3)
lst4 = lst1.union(lst2)
print(lst4)