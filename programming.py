#
# li = [12,13, 123, 123, 31]
#
# print(li.count(123))  # 2
# print(li.insert(2, 1223))   # None
# print(li.remove(12))  # None
# print(li.index(13))   # None
# print(li.sort())   # None
# print(li.sort(reverse= True))   # None
# print(li.append(12315))
# print(li.pop())
# print(li.pop(3))
# print(li.clear())
# print(li)
#
# del li
# print(li)


# def factorial(n):
#
#     return n * factorial(n-1)
#
# n = factorial(5)
# print(n)

# def cunting(n):
#
#     if(n==0):
#         return
#
#
#     cunting(n-1)
#     print(n)
#
# cunting(10)

# def sayDigit(n , arr):
#     if n==0:
#         return
#     digit = int(n%10)
#
#     n = int(n/10)
#
#     sayDigit(n, arr)
#     print(arr[digit])
#
# arr = ["zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
#
# sayDigit(1234,arr)


# s = input()
# s1 = set()
# for i in s:
#     if i in s1 or i in " ":
#         pass
#
#     else:
#         s1.add(i)
#
# print(s1)
# print(len(s1))


# array is sorted or not by recursion

# def isSorted(arr, size):
#     if size==0 or size==1:
#         return True
#
#     if arr[0]> arr[1]:
#         return False
#     else:
#         arr.pop(0)
#         remaining = isSorted(arr, size-1)
#         return remaining
#
# if __name__ == "__main__":
#     li = [1, 9, 4, 34, 36]
#     n = len(li)
#     print(isSorted(li , n))


# def Sum(arr, size):
#
#     if len(arr)==0:
#         return sum
#
#     sum = sum + arr[size-1]+arr[size-2]
#     size = size-1


# merge sort

# def merge(li, s, e, mid):
#     li1= []
#     li2= []
#
#     for i in range(s, mid+1):
#         li1.append(li[i])
#
#     for i in range(mid+1, e+1):
#         li2.append(li[i])
#
#     len1 = len(li1)
#     len2 = len(li2)
#
#     i = 0
#     j = 0
#
#     while i < len1 and j< len2:
#
#         if li1[i] >= li2[j]:
#             li.append(li2[j])
#             j+=1
#
#         else:
#             li.append(li1[i])
#             i+=1
#
#     while i < len1:
#         li.append(li1[i])
#
#     while j < len2:
#         li.append(li2[j])
#
#     print(li)
#
#
# def merge_sort(li, s, e):
#
#     if s < e:
#         mid = s + (e-1) // 2
#
#         merge_sort(li, s, mid)
#         merge_sort(li, mid + 1, e)
#         merge(li, s, e, mid)
#
#
#
#
# if __name__ == "__main__":
#
#     lii = [38, 27, 43, 3, 9, 82, 10]
#     l = len(lii)
#     merge_sort(lii, 0, l-1)

nums = [0,1,2,2,3,0,4,2]
val = 2
li = []
count = 0
for i in range(len(nums)):
    if nums[i] != val:
        li.append(nums[i])

n = len(li)
# for i in range(count):
#     li.append('_')
nums = li
print(n)
print(nums)

