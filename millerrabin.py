import random
import math

def miller_rabin(n, t):
    
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False  
       
    s = 0
    x = n - 1

    # Bước 1: Chuẩn bị số n-1 để kiểm tra
    while x % 2 == 0:
        x = x // 2
        s = s + 1
    r = x # r cần là số lẻ để đảm bảo n-1 = 2^s * r, n là số lẻ , 2^s là số chẵn

    # Bước 2: Kiểm tra Miller-Rabin t lần
    print("Giá trị y để theo dõi:")
    
    for _ in range(t):
        a = random.randint(2, n - 2) # n > 3 
        y = pow(a, r, n)

        if (y != 1) and (y != n - 1):
            j = 1
            # Kiểm tra lặp s-1 lần
            while (j <= s - 1) and (y != n - 1):
                y = pow(y, 2, n)
                print(y)  # In giá trị y để theo dõi quá trình thực hiện
                if y == 1:
                    return False # Hợp số
                j += 1
            if y != n - 1:
                return False # Hợp số

    # Bước 3: Kết luận
    return True # Nguyên tố


# Đảm bảo t nhỏ hơn căn bậc hai của n
def check_t(user_input_n):
    max_t = math.isqrt(user_input_n)
    while True:
        try:
            user_input_t = int(input(f"Nhập giá trị t (t <= căn n với căn n bằng {max_t}): "))
            if 0 <= user_input_t <= max_t:
                break
            else:
                print(f"Vui lòng nhập một giá trị t từ 0 đến <= căn n với căn n bằng {max_t}.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")
            
    return user_input_t

# Nhập số nguyên không âm từ người dùng
while True:
    try:
        user_input_n = int(input("Nhập số nguyên dương (n nên >=3): "))
        if user_input_n >= 0:
            break
        else:
            print("Vui lòng nhập một số nguyên không âm (n nên >=3).")
    except ValueError:
        print("Vui lòng nhập một số nguyên không âm (n nên >=3).")
        
           
    # Kiểm tra giá trị t 
t = check_t(user_input_n) 
    # Kiểm tra số nguyên tố
result = miller_rabin(user_input_n, t)

    # In kết quả
if result:
    print(f"Kết quả kiểm tra tính nguyên tố cho {user_input_n}: là số nguyên tố")
else:
    print(f"Kết quả kiểm tra tính nguyên tố cho {user_input_n}: không phải số nguyên tố")

#===============================================================

# Hàm kiểm tra và liệt kê số nguyên tố trong khoảng giới hạn
def list_primes_in_range(start, end, t):
    primes = [num for num in range(start, end + 1) if miller_rabin(num, t)]
    return primes


# Nhập số bắt đầu từ người dùng và đảm bảo là số nguyên dương
while True:
    try:
        start_limit = int(input("Nhập số bắt đầu (số nguyên dương, n nên >=3): "))
        if start_limit >=0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương n nên >=3.")
    except ValueError:
        print("Vui lòng nhập số nguyên dương n nên >=3.")
    
# Nhập số kết thúc từ người dùng và đảm bảo là số nguyên dương và lớn hơn số bắt đầu
while True:
    try:
        end_limit = int(input("Nhập số kết thúc (số nguyên dương và lớn hơn số bắt đầu): "))
        if end_limit > start_limit:
            break
        else:
            print("Vui lòng nhập một số nguyên dương lớn hơn số bắt đầu.")
    except ValueError:
        print("Vui lòng nhập số nguyên dương.")


'''
# Sinh số ngẫu nhiên trong khoảng giới hạn để kiểm tra tính nguyên tố 
prime_numbers = random.randint(start_limit, end_limit)
# In ra số sinh ngẫu nhiên
print(f"Số kiểm tra ngẫu nhiên trong khoảng giới hạn: {prime_numbers}")

# Kiểm tra giá trị t  
# Sử dụng hàm để kiểm tra số nguyên tố
result = miller_rabin(prime_numbers, check_t(prime_numbers))

# In kết quả
print(f"Kết quả kiểm tra tính nguyên tố cho {prime_numbers}: {result}")

'''
# giá trị t nhỏ hơn CB2 của số lớn nhất
t = check_t(end_limit)

#Liệt kê các số trong khoảng giới hạn
prime_numbers = list_primes_in_range(start_limit, end_limit, t)

# In kết quả
print(f"Các số nguyên tố trong khoảng từ {start_limit} đến {end_limit} là: {prime_numbers}")
