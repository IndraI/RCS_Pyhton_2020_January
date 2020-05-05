def vsaoi(alga):
    return 0.11 * alga

def neapliekamais_minimums(alga):
    if alga < 440:
        return 200
    if alga >= 440 and alga <= 1000:
        return 100
    if alga > 1000:
        return 0

def apgadajamas_personas(n):
    return 200 * n

def atvieglojumi(i1=False, i2=False, p=False):
    res = 0
    if i1:
        res += 154
    if i2:
        res += 120
    if p:
        res += 154
    return res

    

def iin(alga, apl_a, apgd_pers=0, inv1=False, inv2=False, p=False):
    if alga <= 1667:
        return 0.2 * apl_a
    else:
        aaaa = apliekama_alga(1667, apgd_pers, inv1, inv2, p)
        return 0.23 * (apl_a - aaaa) + 0.2 * apl_a

def apliekama_alga(alga, apgd_pers=0, inv1=False, inv2=False, p=False):
    v = vsaoi(alga)
    neapl = neapliekamais_minimums(alga)
    apg_pers = apgadajamas_personas(apgd_pers)
    atv = atvieglojumi(inv1, inv2, p)
    apl_alga = alga - v - neapl - apg_pers - atv
    return apl_alga

def algu_kalkulators(alga, apgd_pers=0, inv1=False, inv2=False, p=False):
    apl_alga = apliekama_alga(alga, apgd_pers, inv1, inv2, p)
    neto_alga = apl_alga - iin(alga, apl_alga, apgd_pers, inv1, inv2, p)
    return neto_alga
