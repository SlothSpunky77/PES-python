d = {
'Virat':[1,2,3,4],
'Rohit':[5,6,7,8],
'Anil':[9,10,11,12]
}
print(d)
D = dict()
c = 0
for i in d:
    L = d[i]
    m = min(L)
    D.update({i:m})
    c = c + 1
print(D)
