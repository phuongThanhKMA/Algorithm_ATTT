import math

def phep_nhan_mang(A,B,t,W):
    C = [0]*(2*t)
    a=dao_nguoc_mang(A)
    b=dao_nguoc_mang(B)

    def dao_nguoc_mang(arr):
        return arr[::-1]

    def cat_so(n, bits):
        num_bits = 1 << bits
        high_bits = n >> bits
        low_bits = n & (num_bits - 1)
        return high_bits, low_bits
    
    # Bước 1
    for i in range(0,t,1):
        C[i]=0

    # Bước 2
    for i in range(0,t,1):
        # Bước 2.1
        U=0
        
        # Bước 2.2
        for j in range(0,t,1):
            UV = C[i+j] + a[i]*b[j] + U
            U,V = cat_so(UV,W)
            C[i+j]=V
            print(U,V,UV)

        # Bước 2.3
        C[i+t]=U

    # Bước 3
    return dao_nguoc_mang(C)

#a = [0, 11, 173, 248]
#b = [0, 1, 226, 64] 

#x = phep_nhan_mang(a,b,4,8)
#print(x)
        


