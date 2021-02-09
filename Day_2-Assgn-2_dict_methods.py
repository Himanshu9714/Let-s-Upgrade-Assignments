dct = {'name':'Abc','age':2900,'DOB':'21/8'}
dct1 = dct.copy()
print(dct, dct1)

print(dct1.keys())
print(dct1.values())
print(dct1.pop('name'))
print(dct1.items())
dct1.update({'name':'ABC'})
print(dct1)
