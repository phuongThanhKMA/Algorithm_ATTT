import uocchunglonnhat

def nghich_dao(a,p):
    u=a
    v=p
    x1=1
    x2=0
    while u != 1:
        q = v//u
        r = v-q*u
        x = x2-q*x1
        v = u
        u = r
        x2=x1
        x1=x
    return x1%p

if __name__ == "__main__":
    p = int(input("Nhập giá trị p trong Fp: "))

    a = int(input("Nhập giá trị a: "))

    print(f"Giá trị nghịch đảo của {a} trong trường F({p})là ", nghich_dao(a,p))
