import itertools
m={'A','B','C','D'}
sub_m=[]
for i in range(len(m)+1):
    elem=itertools.combinations(m,i)
    sub_m+=elem
print(sub_m)