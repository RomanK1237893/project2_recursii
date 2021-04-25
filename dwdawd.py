nums1 = input("Введите список чисел, разделенных пробелом: ").split()
nums = list(map(int, nums1))
print("Список чисел: ", nums)
print(nums.sort())