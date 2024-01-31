import thuattoancoban, phepcongmang, phepnhanmang

W=8
a=23456789
b=98765432
F=2147483647

print(thuattoancoban.so_sang_mang(F,W,a))
print(thuattoancoban.so_sang_mang(F,W,b))
print(phepcongmang.phep_cong_mang(thuattoancoban.so_sang_mang(F,W,a),thuattoancoban.so_sang_mang(F,W,b),4,W))
print(phepcongmang.cong_tren_F(a,b,F,W))