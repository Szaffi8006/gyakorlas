# Nagy János, 2023-10-21
print('Nagy János, 2023-10-21')


def szamit_negyzet_kerulet(oldal):
    kerulet = oldal * 4
    return kerulet

print('Egy négyzet kerületének számátása')
oldal = float(input('Négyzet oldala: '))
kerulet = szamit_negyzet_kerulet(oldal)
print('Kerület: %.1f' % kerulet)

# Lehet így is:
#print(f'Kerület: {kerulet:.1f}')



