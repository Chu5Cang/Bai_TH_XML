from lxml import etree

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Đọc file XML
tree = etree.parse("sv.xml")

# sv.xml
print("In ra tất cả sinh viên:",tree.xpath("//student"))

print("Liệt kê tên tất cả sinh viên:",tree.xpath("//student/name/text()"))

print("Lấy tất cả id của sinh viên:",tree.xpath("//student/id/text()"))

print("Lấy ngày sinh SV01:",tree.xpath("//student[id = 'SV01']/date/text()"))

print("Lấy các khóa học:",tree.xpath("//enrollment/course/text()"))

print("Lấy toàn bộ thông tin của sinh viên đầu tiên:",tree.xpath("//student[1]"))

print("Lấy mã sinh viên đăng ký khóa học 'Vatly203':",tree.xpath("//student[id = //enrollment[course='Vatly203']/studentRef]/id/text()"))

print("Lấy tên sinh viên học môn 'Toan101':",tree.xpath("//student[id = //enrollment[course='Toan101']/studentRef]/name/text()"))

print("Lấy tên sinh viên học môn 'Vatly203':",tree.xpath("//student[id = //enrollment[course='Vatly203']/studentRef]/name/text()"))

print("Lấy ngày sinh của sinh viên có id='SV01':",tree.xpath("//student[id='SV01']/date/text()"))

print("Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997:",tree.xpath("//student[starts-with(date, '1997')]/name/text() | //student[starts-with(date,'1997')]/date/text()"))

print("Lấy tên của các sinh viên có ngày sinh trước năm 1998:",tree.xpath("//student[substring(date,1,4)<'1998']/name/text()"))

print("Tổng số sinh viên là:",int(tree.xpath("count(//student)")))

print("Các sinh viên chưa đăng ký môn:", tree.xpath("//student[not(id=//enrollment/studentRef)]/name/text()"))

print("phần tử <date> anh em sau <name> của SV01:", tree.xpath("//student[id = 'SV01']/name/following-sibling::date[1]/text()"))

print("Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03':", tree.xpath("//enrollment[studentRef = 'SV03']/course/text()"))

print("Lấy sinh viên có họ là “Trần”:", tree.xpath("//student[starts-with(name, 'Trần')]/name/text()"))

print("Lấy năm sinh của sinh viên SV01:", tree.xpath("substring(//student[id='SV01']/date,1,4)"))

print("-"*100)
# quanlybanan.xml
tree = etree.parse("quanlybanan.xml")
print("Lấy tất cả bàn:", tree.xpath("//BAN"))

print("Lấy tất cả nhân viên:", tree.xpath("//NHANVIEN"))

print("Lấy tất cả tên món:", tree.xpath("//MON/TENMON/text()"))

print("Lấy tên nhân viên có mã NV02:", tree.xpath("//NHANVIEN[MANV='NV02']/TENV/text()"))

print("Lấy tên và số điện thoại của nhân viên NV03:", tree.xpath("//NHANVIEN[MANV='NV03']/TENV/text() | //NHANVIEN[MANV='NV03']/SDT/text()"))

print("Lấy tên món có giá > 50,000:", tree.xpath("//MON[number(GIA) > 50000]/TENMON/text()"))

print("Lấy số bàn của hóa đơn HD03:", tree.xpath("//HOADON[SOHD='HD03']/SOBAN/text()"))

print("Lấy tên món có mã M02:", tree.xpath("//MON[MAMON='M02']/TENMON/text()"))

print("Lấy ngày lập của hóa đơn HD03:", tree.xpath("//HOADON[SOHD='HD03']/NGAYLAP/text()"))

print("Lấy tất cả mã món trong hóa đơn HD01:", tree.xpath("//HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON/text()"))

print("Lấy tên món trong hóa đơn HD01:", tree.xpath("//MON[MAMON=//HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON]/TENMON/text()"))

print("Lấy tên nhân viên lập hóa đơn HD02:", tree.xpath("//NHANVIEN[MANV=//HOADON[SOHD='HD02']/MANV]/TENV/text()"))

print("Đếm số bàn:", int(tree.xpath("count(//BAN)")))

print("Đếm số hóa đơn lập bởi NV01:", int(tree.xpath("count(//HOADON[MANV='NV01'])")))

print("Lấy tên tất cả món có trong hóa đơn của bàn số 2:", tree.xpath("//MON[MAMON=//HOADON[SOBAN='2']/CTHDS/CTHD/MAMON]/TENMON/text()"))

print("Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3:", tree.xpath("//NHANVIEN[MANV=//HOADON[SOBAN='3']/MANV]/TENV/text()"))

print("Lấy tất cả hóa đơn mà nhân viên nữ lập:", tree.xpath("//HOADON[MANV=//NHANVIEN[GIOITINH='Nữ']/MANV]"))

print("Lấy tất cả nhân viên từng phục vụ bàn số 1:", tree.xpath("//NHANVIEN[MANV=//HOADON[SOBAN='1']/MANV]/TENV/text()"))

print("Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn:", tree.xpath("//MON[MAMON=//CTHD[number(SOLUONG) > 1]/MAMON]/TENMON/text()"))

print("Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02':", tree.xpath("concat(//BAN[SOBAN=//HOADON[SOHD='HD02']/SOBAN]/TENBAN, ' - ', //HOADON[SOHD='HD02']/NGAYLAP)"))