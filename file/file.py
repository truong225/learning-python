# coding: utf-8

"""
    Mở file
    open(file_name, mode)
    Trong đó, mode:
    - r: đọc, default
    - w: ghi
    - a: ghi vào cuối file
    - r+: đọc, ghi. Con trỏ ở đầu file
    - w+: đọc, ghi. Ghi đè nếu có hoặc tạo file mới
    - a+: đọc, thêm vào cuối file. Tạo file mới nếu chưa tồn tại

    Thêm 'b' để đọc file binary
"""

f = open('content.txt', 'r')
"""
    Function open(file_name, mode) trả về object với thuộc tính:
    - closed
    - mode
    - name
    - softspace: cờ đánh dấu softspace khi dùng với print
"""

"""
    Đọc nội dung file
    read(byte): đọc theo byte
    read(): đọc toàn bộ
"""
data = f.read()
print 'Full:', data
data = f.read(1)
print 'Read 1024:', data

"""
    Ghi file
"""
f2 = open('content.txt', 'w')
f2.write('End line')

f.close()
f2.close()

"""
    Đổi tên file
    import os
    os.rename('content.txt', 'content.dat')
    os.remove(file_name)
    
    Tạo thư mục:
    os.mkdir('test')
    
    Xóa thư mục:
    os.rmdir('test')
    
    Lấy danh sách tập tin thư mục:
    os.listdir(dir)
"""
import os

print os.listdir('E:/')

"""
    os.chdir(path): Đổi thư mục hiện hành
    os.getcwd(): Trả về thư mục hiện hành
    os.chmod(path, mode)
    os.chown(path, uid, gid)
    os.makedirs(path[,mode])
    os.removedirs(path)
"""
path = 'D:/'
os.path.exists(path)
os.path.getsize()
os.path.isfile()
os.path.isdir()
os.path.dirname()
os.path.getatime()  # Trả về thời gian truy cập mới nhất
os.path.getmtime()  # Trả về thời gian chỉnh sửa cuối cùng
os.path.getctime()  # Trả về thời gian chỉnh sửa cuối của metadata trên 1 số
# hệ thống, hoặc trả về thời gian tạo file trên Windows
