def segmented_sieve(limit):
    import math

    def simple_sieve(limit, primes):
        
        mark = [True] * (limit + 1)
        p = 2
        while p * p <= limit:
            if mark[p] == True:
                for i in range(p * p, limit + 1, p):
                    mark[i] = False
            p += 1

        for p in range(2, limit + 1):
            if mark[p]:
                primes.append(p)

    def sieve_in_range(low, high, primes):
        limit = int(math.sqrt(high))
        primes = []
        simple_sieve(limit, primes)
        
        n = high - low + 1
        mark = [True] * (n)
        mark[0] = mark[1] = False 
    
        for prime in primes:
            low_limit = max(prime * prime, (low + prime - 1) // prime * prime)
            for i in range(low_limit, high + 1, prime):
                mark[i - low] = False

        result = [low + i for i in range(n) if mark[i]]
        return result

    # Find prime numbers between 10 and 50
    # Xác định phạm vi tìm số nguyên tố
    while True:
        try:
            lower_limit = int(input("Nhập số bắt đầu (số nguyên dương): "))
            if lower_limit >=0 and lower_limit < user_number:
                break
            else:
                print("Vui lòng nhập một số nguyên dương trong phạm vi tìm kiếm.")
        except ValueError:
            print("Vui lòng nhập số nguyên dương.")
        
    # Nhập số kết thúc từ người dùng và đảm bảo là số nguyên dương và lớn hơn số bắt đầu
    while True:
        try:
            upper_limit = int(input("Nhập số kết thúc (số nguyên dương và lớn hơn số bắt đầu): "))
            if upper_limit > lower_limit and upper_limit <= user_number:
                break
            else:
                print("Vui lòng nhập một số nguyên dương trong phạm vi tìm kiếm.")
        except ValueError:
            print("Vui lòng nhập số nguyên dương.")
            

    primes_in_range = sieve_in_range(lower_limit, upper_limit, [])

    print(f"Prime numbers between {lower_limit} and {upper_limit}: {primes_in_range}")

# Nhập số lượng số nguyên tố muốn tìm từ người dùng
while True:
    try:
        user_number = int(input("Số giới hạn phạm vi tìm kiếm: "))
        if user_number >=0:
            break
        else:
            print("Vui lòng nhập một số nguyên không âm.")
    except ValueError:
        print("Vui lòng nhập một số nguyên không âm.")
            
print(segmented_sieve(user_number))
