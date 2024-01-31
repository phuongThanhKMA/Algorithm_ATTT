import random
import math

def fermat_test(n, t):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    def fermat_check(a, n):
        if pow(a, n-1, n) != 1: # modulo_power(a, n-1, n)
            return False
        return True
    '''
    def modulo_power(a, b, m):
    if a % m == 0:
        return 0 
    result = 1
    a = a % m 
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b = b // 2
        a = (a * a) % m
    return result
    '''
    for _ in range(t):
        a = random.randint(2, n-2)
        if not fermat_check(a, n):
            return False
    return True
  

# Đảm bảo t nhỏ hơn căn bậc hai của n
def check_t(user_number):
    max_t = math.isqrt(user_number)
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
        user_number = int(input("Nhập số nguyên dương n: "))
        if user_number >= 0:
            break
        else:
            print("Vui lòng nhập một số nguyên không âm.")
    except ValueError:
        print("Vui lòng nhập một số nguyên không âm.")
        
    # Kiểm tra giá trị t, t nhỏ hơn CB2 của số lớn nhất 
t = check_t(user_number) 
     
    # Sử dụng hàm để kiểm tra số nguyên tố
result = fermat_test(user_number, t)

    # In kết quả
if result:
    print(f"Kết quả kiểm tra tính nguyên tố cho {user_number}: là số nguyên tố")
else:
    print(f"Kết quả kiểm tra tính nguyên tố cho {user_number}: không phải số nguyên tố")
    
   
   
#=============================================================================

# Hàm kiểm tra và liệt kê số nguyên tố trong khoảng giới hạn
def list_primes_in_range(start, end, t):
    primes = [num for num in range(start, end + 1) if fermat_test(num, t)]
    return primes

# Nhập số bắt đầu từ người dùng và đảm bảo là số nguyên dương
while True:
    try:
        start_limit = int(input("Nhập số bắt đầu (số nguyên dương): "))
        if start_limit >= 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương.")
    except ValueError:
        print("Vui lòng nhập số nguyên dương.")
    
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
result = fermat_test(prime_numbers, check_t(prime_numbers))

'''
# Nhập giá trị t
t = check_t(end_limit)
#Liệt kê các số trong khoảng giới hạn
prime_numbers = list_primes_in_range(start_limit, end_limit, t)

# In kết quả
print(f"Các số nguyên tố trong khoảng từ {start_limit} đến {end_limit} là: {prime_numbers}")

