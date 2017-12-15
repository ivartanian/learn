bri = {'Бразилия', 'Россия', 'Индия'}

bric = bri.copy()

bric.add('Ukraine')
bri.add('Bavariya')

print(bri)
print(bric)

bri.remove('Россия')

print(bric.issuperset(bri))

print(bri.intersection(bric))