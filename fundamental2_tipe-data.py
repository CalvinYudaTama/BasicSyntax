print('Tipe data skalar => Tipe data sederhana')
anak1 = 'mamad'
anak2 = 'ucup'
anak3 = 'somad'
anak4 = 'santi'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nTipe Data list/dafta/array')
anak = ['mamad', 'ucup', 'somad', 'santi']
print(anak)
anak.append('bambang')
print(anak)

print('\nSapa Anak ke-2')
print(f'Hai anak {anak[1]}!')

print('\nSapaa Anak ke-5')
print(f'Hai anak {anak[4]}!')

print('\nSapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa Semua Anak Cara Ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}!')