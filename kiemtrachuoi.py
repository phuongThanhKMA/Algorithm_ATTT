# dùng thuật toán boyer moore kiểm tra chuỗi P trong T
def boyer(P,T):
    if len(P)>len(T):
        return -1
    m=len(P)
    i=j=m-1
    while i<len(T):
        if P[j] == T[i]: # kiểm tra 2 kí tự có giống nhau ko
            if j == 0: # kiểm tra nếu j=0 (hàm kiểm tra đã tới kí tự cuối cùng (đầu tiên của P)) thì end
                return i
            else: # kiểm tra kí tự kế tiếp (trc đó)
                i -= 1
                j -= 1
        else: # nếu ko giống thì thực hiện bước nhảy
            i = i + m - min(j, 1 + last_oc(T[i+1],P))
            j = m - 1
    return -1 # khi không tìm thấy
    
# hàm kiểm tra vị trí cuối cùng của kí tự trong P
def last_oc(ki_tu,P):
    vi_tri = -1
    for i in range(0,len(P)):
        if ki_tu == P[i]:
            vi_tri = i
    return vi_tri

# dùng thuật toán KMP kiểm tra chuỗi P trong T
def kmp(P,T):
    if len(P)>len(T):
        return -1
    m = len(P)
    n = len(T)
    i=j=0
    while i < n:
        if P[j] == T[i]: # kiểm tra 2 kí tự có giống nhau ko
            if j == m-1: # kiểm tra nếu j=m-1 (hàm kiểm tra đã tới kí tự cuối cùng của P) thì end
                return i - m + 1
            else: # kiểm tra kí tự kế tiếp 
                i += 1
                j += 1
        else: # nếu ko giống thì thực hiện bước nhảy
            i = i + j - failure(j,P)
            if failure(j,P) == -1:
                j = 0
            else:
                j = failure(j,P)
    return -1

# hàm kiểm tra tiền xử lý mẫu
def failure(k,P):
    #print("k=",k)
    if k <= 0:
        return -1
    A=P[:k]  
    #print("tiền tố A=",A)
    x=0
    for i in range(k):
        if A[:i] == A[-i:] : # kiểm tra tiền tố = hậu tố
            x += 1
    return x

#T= "abacaabaccabacabaabb"
#print(kmp(P,T))
#for i in range(0,6):
    #print(failure(i,P))
