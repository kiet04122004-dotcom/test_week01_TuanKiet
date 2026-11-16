"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng

Chạy file này bằng: python ex03_input.py
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Hàm input() luôn trả về kiểu dữ liệu là chuỗi (string)
ten = input("Nhập tên của bạn: ")
print(f"Xin chào, {ten}!")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int! Vì dữ liệu từ input() là chuỗi.
tuoi_str = input("Nhập tuổi của bạn: ")
tuoi = int(tuoi_str)
nam_hien_tai = 2026
nam_sinh = nam_hien_tai - tuoi
print(f"Năm sinh ước tính của bạn là: {nam_sinh}")

# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Chuyển đổi chuỗi nhập vào thành số nguyên (int) để thực hiện phép cộng toán học
so_thu_nhat = int(input("Nhập số thứ nhất: "))
so_thu_hai = int(input("Nhập số thứ hai: "))
tong_hai_so = so_thu_nhat + so_thu_hai
print(f"Tổng: {so_thu_nhat} + {so_thu_hai} = {tong_hai_so}")

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
print("\n--- Trò chơi Mad Libs mini ---")
ten_nhan_vat = input("Nhập một tên người: ")
tinh_tu = input("Nhập một tính từ (ví dụ: vui vẻ, khổng lồ, lười biếng): ")
con_vat = input("Nhập một loài động vật: ")
so_luong = input("Nhập một con số: ")

cau_chuyen = (
    f"Hôm nay, {ten_nhan_vat} nhìn thấy một con {con_vat} vô cùng {tinh_tu}. "
    f"Nó đã ăn hết sạch {so_luong} cái bánh rán rồi chạy biến đi!"
)
print(cau_chuyen)
