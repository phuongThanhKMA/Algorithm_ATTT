def eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False  # 0 và 1 không phải là số nguyên tố

    p = 2
    while p**2 <= n:
        if primes[p] == True:
            for i in range(p**2, n+1, p):
                primes[i] = False
                
        p += 1

    return [i for i in range(n+1) if primes[i]]

# Nhập số nguyên không âm từ người dùng
while True:
    try:
        user_number = int(input("Nhập số nguyên dương n: "))
        if user_number >= 0:
            break
        else:
            print("Vui lòng nhập một số nguyên không âm.")
    except ValueError:
        print("Vui lòng nhập một số nguyên không âm.")
        
print("Các số nguyên tố nhỏ hơn hoặc bằng", user_number, "là: ", eratosthenes(user_number))