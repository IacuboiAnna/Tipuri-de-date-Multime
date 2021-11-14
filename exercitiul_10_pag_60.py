import itertools
m={1,2,3,4}
sub_m=[]
for i in range(len(m)+1):
    elem=itertools.combinations(m,i)
    sub_m+=elem
print(sub_m)