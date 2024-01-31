import uocchunglonnhat

if __name__ == "__main__":
    a = int(input("Nhập số nguyên dương thứ nhất (>0): "))
    b = int(input("Nhập số nguyên dương thứ hai (>0): "))

    while a <= 0 or b <= 0:
        print("Cả hai số phải lớn hơn 0. Vui lòng nhập lại.")
        a = int(input("Nhập số nguyên dương thứ nhất (>0): "))
        b = int(input("Nhập số nguyên dương thứ hai (>0): "))
    
    if a==1 or b==1:
        print(f"Ước chung lớn nhất gcd({a},{b})=1")
    elif a==b:
        print(f"Ước chung lớn nhất gcd({a},{b})={a}")
    else:
        if a<b:
            a,b=b,a
        print(f"Ước chung lớn nhất gcd({a},{b})=",uocchunglonnhat.gcd(a,b))
    