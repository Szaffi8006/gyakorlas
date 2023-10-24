# Nagy János, 2023-10-21
print('Nagy János, 2023-10-21')

nap1 = int(input('1 nap: '))
nap2 = int(input('2 nap: '))
nap3 = int(input('3 nap: '))
nap4 = int(input('4 nap: '))
nap5 = int(input('5 nap: '))

osszeg = (nap1 + nap2 + nap3 + nap4 + nap5)
atlag = osszeg/5

if atlag < 5:
    print('Veszélyes volt')
else:
    print('normális a vízállás')
