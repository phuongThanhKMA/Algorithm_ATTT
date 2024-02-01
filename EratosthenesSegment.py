def segmented_sieve(limit):
    import math

    def sieve_in_range(low, high):
        limit = int(math.sqrt(high))
        n = high - low + 1
        mark = [True] * (n)
        
        if low < 2:
            for i in range(1):
                mark[i] = False
    
        for prime in range(2, limit+1):
            low_limit = max(prime * prime, (low + prime - 1) // prime * prime)
            for i in range(low_limit, high + 1, prime):
                mark[i - low] = False

        result = [low + i for i in range(n) if mark[i]]
        return result

    while True:
        try:
            lower_limit = int(input("Nhập số bắt đầu (số nguyên dương): "))
            if lower_limit >=0 and lower_limit < limit:
                break
            else:
                print("Vui lòng nhập một số nguyên dương trong phạm vi tìm kiếm.")
        except ValueError:
            print("Vui lòng nhập số nguyên dương.")
        
    while True:
        try:
            upper_limit = int(input("Nhập số kết thúc (số nguyên dương và lớn hơn số bắt đầu): "))
            if upper_limit > lower_limit and upper_limit <= limit:
                break
            else:
                print("Vui lòng nhập một số nguyên dương trong phạm vi tìm kiếm.")
        except ValueError:
            print("Vui lòng nhập số nguyên dương.")
            

    primes_in_range = sieve_in_range(lower_limit, upper_limit)

    print(f"Prime numbers between {lower_limit} and {upper_limit}: {primes_in_range}")

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
