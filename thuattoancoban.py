import math

# Ví dụ:
#F = 2147483647
#W = 8 # bội số của 8, độ rộng của từng phần tử trong mảng 
#a = 23456789

# Thuật toán chuyển từ số sang mảng:
def so_sang_mang(F, W, a):
    list = []
    m = math.ceil(math.log2(F)) # số bit cần biểu diễn
    t = math.ceil(m / W) # số lượng phần tử trong mảng đầu ra

    for i in range(1, t + 1):
        x = 2 ** ((t - i) * W)
        b = a // x
        a = a % x
        list.append(b)

    return list

#ket_qua = so_sang_mang(F, W, 765432)
#print("Kết quả chuyển từ số sang mảng:", ket_qua)

# Thuật toán chuyển từ mảng sang số:
def mang_sang_so(F, W, A):
    m = math.ceil(math.log2(F))
    t = math.ceil(m / W)

    result = 0
    for i in range(0, t ):
        x = 2 ** ((t - 1 - i) * W)
        result += A[i]* x

    return result

#ket_qua = mang_sang_so(F, W, ket_qua)
#print("Kết quả chuyển từ mảng sang số:", ket_qua)