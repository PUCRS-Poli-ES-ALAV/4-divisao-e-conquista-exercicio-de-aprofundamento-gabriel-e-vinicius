import time
import random

def merge_sort(arr):
    global merge_iterations
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    global merge_iterations
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        merge_iterations += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



def max_val1(arr):
    global max1_iterations
    max_val = arr[0]
    for num in arr[1:]:
        max1_iterations += 1
        if num > max_val:
            max_val = num
    return max_val

def max_val2(arr, start, end):
    global max2_iterations
    if start == end:
        return arr[start]
    mid = (start + end) // 2
    max2_iterations += 1
    v1 = max_val2(arr, start, mid)
    v2 = max_val2(arr, mid + 1, end)
    return max(v1, v2)


def multiply(x,y,n):
    global multiply_iterations
    multiply_iterations+=1
    if n == 1:
        return x * y
    else:
        m = (n+1) // 2 #divide
        a = x // (2 ** m)
        b = x % (2 ** m) 
        c = y // (2 ** m) 
        d = y % (2 ** m) 
        e = multiply(a,c,m) # go to smamller problems
        f = multiply(b,d,m)
        g = multiply(b,c,m)
        h = multiply(a,d,m)
        return (2**(2*m))*e + (2**m)*(g+h) + f # combine

#
#Re-implemente o algoritmo de multiplicação de grandes inteiros, agora sobre duas sequências de bits representados como Strings de 0 e 1. Use a assinatura abaixo:
#
def multiply_binary(x: str, y: str) -> str:

    def binary_add(a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len) #zfill adiciona 0 a esquerda para garantir mesmo tamanho
        b = b.zfill(max_len) #AI tip
        carry = 0
        result = []
        
        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if a[i] == '1' else 0
            r += 1 if b[i] == '1' else 0
            result.append(str(r % 2))
            carry = r // 2
            
        if carry:
            result.append('1')
        return ''.join(result[::-1])
    
    # shifta para  esquerda
    def shift_left(s: str, n: int) -> str:
        return s + '0' * n
    
    n = max(len(x), len(y))
    x = x.zfill(n)
    y = y.zfill(n)
    
    # Caso base
    if n == 1:
        return '1' if x == '1' and y == '1' else '0'
    
    m = (n + 1) // 2
    a = x[:-m]
    b = x[-m:]
    c = y[:-m]
    d = y[-m:]
    
    e = multiply_binary(a, c)    # a * c
    f = multiply_binary(b, d)    # b * d
    g = multiply_binary(b, c)    # b * c
    h = multiply_binary(a, d)    # a * d
    
    #estas linhas executam : (2^(2m))*e + (2^m)*(g+h) + f
    term1 = shift_left(e, 2 * m)
    gh = binary_add(g, h)
    term2 = shift_left(gh, m)
    temp = binary_add(term1, term2)
    result = binary_add(temp, f)
    
    return result


def test_algorithms():
    sizes = [32, 2048, 1048576]
    for size in sizes:
        print(f"\nTesting with size {size}:")
        arr = [random.randint(1, 10000) for _ in range(size)]
        
        global merge_iterations, max1_iterations, max2_iterations, multiply_iterations
        merge_iterations = max1_iterations = max2_iterations = multiply_iterations = 0
        

        sorted_arr = merge_sort(arr[:])
        print(f"Merge Sort - Iterations: {merge_iterations}")

        max1 = max_val1(arr)
        # print(f"max value in v1 is {max1}")

        print(f"Max Val1 - Iterations: {max1_iterations}")
        
        max2 = max_val2(arr, 0, len(arr) - 1)
        # print(f"max value in v2 is {max2}")
        print(f"Max Val2 - Iterations: {max2_iterations}")
    
    # Multiplication
    bit_sizes = [4, 16, 64]
    for bits in bit_sizes:
        x = random.randint(1, 2**bits - 1)
        y = random.randint(1, 2**bits - 1)
        result = multiply(x, y, bits)
        # print(f"Result of {x} x {y} is {result}")
        print(f"Multiply {bits}-bit - Iterations: {multiply_iterations}")

if __name__ == "__main__":
    test_algorithms()
