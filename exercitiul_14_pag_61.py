a=input("Dati primul sir de caractere:")
b=input("Dati al doilea sir de caractere:")
A=set(a)
B=set(b)
print('Caracterele care se intalnesc in cel putin unul dintre siruri sunt:', A.union(B)) #a
print('Caracterele care apar in ambele siruri sunt:', A.intersection(B)) #b
print('Caracterele care apar in primul si nu apar in sirul al doilea sunt:', A.difference(B)) #c