"""Indexing in array"""
numbers = [1, 2, 3]
arr = ['Genius', 'Sirius']
print numbers[0]
print arr[-1]  # From last
print len(arr)

"""Check element exist in array"""
arr = ['a', 'b', 'c', 'c', 'd', 'e', 'f', 'g']


# Look before you leap (LBYL)
def look_before_you_leap(array, index):
    if index < len(array):
        return array[index]


# Easier to ask forgiveness than permission (EAFP)
def easier_ask_forgiveness(array, index):
    try:
        array[index]
    except IndexError:
        # handle exception
        return '[IndexError] There is no index in array'


print look_before_you_leap(arr, 16)
print easier_ask_forgiveness(arr, 16)

"""Check if exist in array"""
mylist = ['a', 'b', 'c']
print 'a' in mylist
print 'c' not in mylist

del mylist[2]
print mylist

"""Cong 2 mang"""
arr1 = ['noi', 'dung']
arr2 = ['cua', 'mang']
arr_sum = arr1 + arr2
print arr_sum

"""Them phan tu vao mang"""
mang = [1, 2, 3]
mang.append(4)
print mang

"""Lay phan tu cuoi cung ra khoi mang"""
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print 'Lay phan tu cuoi cung cua mang:'
print number
new_number = number.pop()
print new_number
print number

"""Tim gia tri trong mang"""
number = [1, 2, 3, 4]
print 'Index for 2', number.index(2)
# print 'Index for 5', number.index(5)

"""Reverse mang"""
print 'Dao nguoc gia tri cua mang:'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.reverse()
print numbers

"""Sap xep mang"""
numbers = [1, 3, 5, 6, 7, 0, 10, 9, 11, 20, 100]
numbers.sort()
print numbers
