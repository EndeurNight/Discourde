def fusion(t1, t2):
    t= []
    i= 0
    j= 0
    while i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            t.append(t1[i])
            i += 1
        else:
            t.append(t2[j])
            j += 1
    if i > j:
        for n in t2[j:]:
            t.append(n)
    else:
        for n in t1[i:]:
            t.append(n)        
    return t


def trifusion(t):
    léna = len(t)
    if léna <= 1:
        return t    
    return fusion(trifusion(t[:léna//2]), trifusion(t[léna//2:]))


