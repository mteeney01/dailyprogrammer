import math
inputs = ['3.1416rd', '90dr', '212fc', '70cf', '100cr', '315.15kc']

def rd(rads):
    return rads * (180 / math.pi)
def dr(degs):
    return degs * (math.pi / 180)
def fc(fahr):
    return (fahr - 32) * (5/9)
def fk(fahr):
    return (fahr + 459.67) * (5/9)
def cf(cel):
    return (cel * 9/5) + 32
def ck(cel):
    return (cel + 273.15)
def kc(kel):
    return (kel - 273.15)


conversions = {
    'dr': dr,
    'rd': rd,
    'fc': fc,
    'fk': fk,
    'cf': cf,
    'ck': ck,
    'kc': kc
}

for x in inputs:
    units = x[-2:]
    if units not in conversions:
        print('No candidate for conversion')
        continue
    amount = x[:-2]
    print('{:.2f}'.format(conversions[units](float(amount))), units[1], sep='')