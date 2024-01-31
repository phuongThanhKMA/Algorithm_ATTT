import kiemtrachuoi

if __name__ == "__main__":
      
    # Nhập giá trị 
    T = input("Nhập giá trị chuỗi T: ")
    while not T:
        T = input("Nhập lại giá trị chuỗi T: ")

    P = input("Nhập giá trị chuỗi P: ")
    while not P:
        P = input("Nhập lại giá trị chuỗi P: ")
        
    k= kiemtrachuoi.kmp(P,T)
    if k == -1:
        print("Không mẫu P trong đoạn văn bản T")
    else:
        print("Mẫu P có trong đoạn văn bản T và bắt đầu từ vị trí: ",k)