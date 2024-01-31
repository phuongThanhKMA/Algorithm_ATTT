def boyer(P,T):
    if len(P)>len(T):
        return -1
    m=len(P)
    i=j=m-1
    while i<len(T):
        if P[j] == T[i]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            i += m - min(j, 1 + last_oc(T[i+1],P))
            j = m - 1
    return -1
    

def last_oc(ki_tu,P):
    vi_tri = -1
    for i in range(0,len(P)):
        if ki_tu == P[i]:
            vi_tri = i
    return vi_tri

def kmp(P,T):
    if len(P)>len(T):
        return -1
    m = len(P)
    n = len(T)
    i=j=0
    while i < n:
        if P[j] == T[i]:
            if j == m-1:
                return i - m + 1
            else:
                i += 1
                j += 1
        else:
            i = i + j - failure(j,P)
            if failure(j,P) == -1:
                j = 0
            else:
                j = failure(j,P)
    return -1

def failure(k,P):
    if k <= 0:
        return -1
    
    for i in range(k+1):
        x=0
        A = P[:i]  
        for j in range(0,i):
            if A[:j] == A[-j:] :
                x += 1
    return x

#P= "abacab"
#T= "abacaabaccabacabaabb"
#print(kmp(P,T))