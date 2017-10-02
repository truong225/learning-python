# coding: utf-8

"""
    Có 3 loại module:
    - Viết bằng Python: *.py
    - Thư viện liên kết động: *.dll, *.pyd, *.so, *.sl, ...
    - C-Module liên kết với trình biên dịch
"""

"""
    Load module
    import module_name
    
    Trình biên dịch sẽ tìm kiếm file module tương ứng theo thứ tự:
    - Thư mục hiện hành script đang gọi
    - Các thư mục trong PYTHONPATH (nếu có set)
    - Các thư mục cài đặt chuẩn trên Linux/Unix
"""

"""
Lấy đường dẫn module đã load
"""
import os
import random

print os.__file__
print random.__file__

# Import file dll bằng ctypes
from ctypes import *

mydll = cdll.LoadLibrary('DllModule.dll')
rel = mydll.sum(1, 2)
print rel
"""
    Lấy danh sách thuộc tính và phương thức của module
    dir(module_name)
"""
import math

print dir(math)

# Gọi hàm dir() không tham số: Lấy thuộc tính và phương thức của scope hiện tại
print dir()

"""
    Khai báo và sử dụng module mymath
"""
import mymath

print 'Cong hai so:', mymath.cong(1, 2)
