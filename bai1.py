import thuattoancoban

if __name__ == "__main__":
        
    # Nhập giá trị 
    F = int(input("Nhập giá trị p trong Fp: "))
    
    W = int(input("Nhập giá trị W: "))

    a = int(input("Nhập giá trị a: "))

    result = thuattoancoban.so_sang_mang(F, W, a)
    print("Kết quả:", result)