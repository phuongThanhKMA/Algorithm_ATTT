import thuattoancoban,phepnhanmang,math

if __name__ == "__main__":
        
    # Nhập giá trị 
    F = int(input("Nhập giá trị p trong Fp: "))
    
    W = int(input("Nhập giá trị W: "))

    a = int(input("Nhập giá trị a: "))

    b = int(input("Nhập giá trị b: "))

    A =thuattoancoban.so_sang_mang(F, W, a)
    B =thuattoancoban.so_sang_mang(F, W, b)
    t =math.ceil(math.ceil(math.log2(F)/W))
    C =phepnhanmang.phep_nhan_mang(A,B,t,W)

    print("Mảng a:", A)
    print("Mảng b:", B)
    print("Kết quả tích a*b dưới dạng mảng:", C)