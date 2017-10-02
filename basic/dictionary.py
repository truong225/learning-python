point = {'name': 'Kobayashi', 'age': 681, 'salary': 1000}
print point['name']

point['country'] = 'vietnam'
print point

"""Xoa toan bo du lieu trong doi tuong"""
dict.clear(point)
point.clear()
print point

"""Copy"""
dict.copy(point)

"""Tao doi tuong voi danh sach key tu seq va lay value lam gia tri neu co"""
sequence = ['name', 'age', 'count']
point = point.fromkeys(sequence, 'Value')
print point

"""Kiem tra key co ton tai hay khong"""
print point.has_key('name')

"""Tra ve list key hoac value"""
print point.keys()
print point.values()
