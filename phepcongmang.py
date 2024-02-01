import math
import thuattoancoban

#A=[157, 0, 173, 23]
#B=[169, 1, 0, 64]
#W=8
#F=2147483647
#t=4
def phep_cong_mang(A,B,t,W):
    # tạo bit nhớ và mảng
    epsilon = 0
    list = [0] * t
    # chạy mảng từ t-1 tới 0 (mảng lưu ngược lại A0 -> A3)
    for i in range(t-1,-1,-1):
        x = 2 ** (W)
        list[i]=(A[i]+B[i]+epsilon)
        if list[i]>=x:
            epsilon = 1
            list[i]=list[i]%x
        else:
            epsilon = 0
    return epsilon, list

#print(phep_cong_mang(A,B,t,W))

#A=[0,11,173,248]
#B=[0,1,226,64]
# phép trừ hai mảng a và b
def phep_tru_mang(A,B,t,W):
    epsilon = 0
    list = [0] * t
    for i in range(t-1,-1,-1):
        x = 2 ** (W)
        list[i] = A[i]-B[i]-epsilon
        if list[i]<0:
            epsilon = 1
            list[i]=list[i]%x
        else:
            epsilon = 0
    return epsilon, list

#print(phep_tru_mang(A,B,t,W))
# phép cộng hai mảng a và b trên Fp
def cong_tren_F(A,B,F,W):
    t = math.ceil(math.ceil(math.log2(F))/W)
    a = thuattoancoban.so_sang_mang(F,W,A)
    b = thuattoancoban.so_sang_mang(F,W,B)
    p = thuattoancoban.so_sang_mang(F,W,F)

    e,c = phep_cong_mang(a,b,t,W)
    if e==1:
        e,c = phep_tru_mang(c,p,t,W)
    elif e==0:
        e,c = phep_tru_mang(c,p,t,W)
    return c

# phép cộng hai mảng a và b trên Fp
def tru_tren_F(A,B,F,W):
    t = math.ceil(math.ceil(math.log2(F))/W)
    a = thuattoancoban.so_sang_mang(F,W,A)
    b = thuattoancoban.so_sang_mang(F,W,B)

    e,c = phep_tru_mang(a,b,t,W)
    if e == 1 :
        p=thuattoancoban.so_sang_mang(F,W,F)
        e,c = phep_cong_mang(c,p,t,W)
    return c
