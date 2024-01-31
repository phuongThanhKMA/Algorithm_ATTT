import thuattoancoban,phepcongmang,math

if __name__ == "__main__":
        
    # Nhập giá trị 
    F = int(input("Nhập giá trị p trong Fp: "))
    
    W = int(input("Nhập giá trị W: "))

    a = int(input("Nhập giá trị a: "))

    b = int(input("Nhập giá trị b: "))

    A =thuattoancoban.so_sang_mang(F, W, a)
    B =thuattoancoban.so_sang_mang(F, W, b)
    C =phepcongmang.cong_tren_F(a,b,F,W)

    print("Mảng a:", A)
    print("Mảng b:", B)
    print("Kết quả tổng của a+b trên Fp dưới dạng mảng:", C)
    print("Kết quả tổng của a+b trên Fp dưới dạng số:", thuattoancoban.mang_sang_so(F,W,C))