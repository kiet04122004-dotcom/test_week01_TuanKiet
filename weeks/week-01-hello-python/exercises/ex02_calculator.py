"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python

Chạy file này bằng: python ex02_calculator.py
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000
# Dùng toán tử cộng (+) trực tiếp trong hàm print()
tong = 2024 + 1000
print("2024 + 1000 =", tong)

# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.
# Biểu thức: tiền_ban_đầu - số_lượng * giá_tiền
tien_ban_dau = 150000
gia_ca_phe = 35000
so_ly = 3
tien_con_lai = tien_ban_dau - (so_ly * gia_ca_phe)
print("Số tiền còn lại sau khi mua cà phê:", tien_con_lai, "VNĐ")

# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2
# Toán tử ** dùng để tính lũy thừa (mũ)
ban_kinh = 7
dien_tich = 3.14159 * (ban_kinh ** 2)
# Dùng round(..., 2) để làm tròn đến 2 chữ số thập phân
print("Diện tích hình tròn (bán kính = 7):", round(dien_tich, 2))

# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?
# Gợi ý: Dùng toán tử // (chia lấy phần nguyên) và % (chia lấy phần dư)
so_keo = 100
so_nguoi = 7
keo_moi_nguoi = so_keo // so_nguoi
keo_du = so_keo % so_nguoi

print("Mỗi người được:", keo_moi_nguoi, "viên kẹo")
print("Số kẹo còn dư:", keo_du, "viên")

# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
# Công thức: F = C * 9/5 + 32
# In ra kết quả dạng: "37°C = ???°F"
do_c = 37
do_f = do_c * 9 / 5 + 32
print(f"{do_c}°C = {do_f}°F")
