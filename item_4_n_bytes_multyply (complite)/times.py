import calculation
import generate
import time


nums = generate.generate()
nums2 = generate.generate_more()

def time_binary_multiplication():
    result = {}
    total_iter = len(nums)
    for index, i in enumerate(nums):
        start_time = time.time()
        calculation.binary_multiplication(i[0], i[1])
        end_time = time.time()
        result[2**(index+6)] = end_time - start_time
        print(f"Выполнено {index+1} из {total_iter}")
    return result

# print(time_binary_multiplication())
def time_multiply_recursive():
    result = {}
    total_iter = len(nums)
    for index, i in enumerate(nums):
        start_time = time.time()
        calculation.naive_recursive(i[0], i[1])
        end_time = time.time()
        result[2**(index+6)] = end_time - start_time
        print(f"Выполнено {index+1} из {total_iter}")
    return result

# print(time_multiply_recursive())

def time_karatsuba():
    result = {}
    total_iter = len(nums)
    for index, i in enumerate(nums):
        start_time = time.time()
        calculation.karatsuba(i[0], i[1])
        end_time = time.time()
        result[2**(index+6)] = end_time - start_time
        print(f"Выполнено {index+1} из {total_iter}")
    return result

# print(time_karatsuba())

