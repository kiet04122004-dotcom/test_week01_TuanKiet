"""
Ứng dụng điều hướng bài tập Tuần 01 🚀
======================================
Dự án: test_week01_TuanKiet
Vị trí file: Name-List/tuan1.py

Menu tương tác điều khiển bằng bàn phím:
- Bấm 1: Chạy Bài 01 (ex01_hello.py trong thư mục Exercises)
- Bấm 2: Chạy Bài 02 (ex02_calculator.py trong thư mục Exercises)
- Bấm 3: Chạy Bài 03 (ex03_input.py trong thư mục Exercises)
- Bấm 4: Chạy Mini-project thẻ ASCII (mini_project_card.py trong Exercises)
- Bấm 5: Chạy AutoGrade tự chấm điểm
- Bấm 6: Chạy Dự án Name-List (name_list.py)
- Bấm 0: Thoát ứng dụng
"""

import os
import subprocess
import sys
from pathlib import Path

# Thư mục hiện tại chứa script này
BASE_DIR = Path(__file__).resolve().parent

def tim_duong_dan_file(ten_file: str) -> Path | None:
    """Tìm đường dẫn thực tế của file bài tập trong các thư mục khả dĩ."""
    cac_vi_tri = [
        BASE_DIR / ten_file,                                               # Cùng thư mục
        BASE_DIR.parent / "Exercises" / ten_file,                         # Thư mục Exercises ở cấp cha
        BASE_DIR / "Exercises" / ten_file,                                # Thư mục Exercises ở cấp hiện tại
        BASE_DIR.parent / ten_file,                                       # Cấp cha
        BASE_DIR / "weeks" / "week-01-hello-python" / "exercises" / ten_file,
        BASE_DIR.parent / "weeks" / "week-01-hello-python" / "exercises" / ten_file,
    ]
    for p in cac_vi_tri:
        if p.exists():
            return p
    return None

def chay_file(ten_file: str, mo_ta: str):
    """Hàm chạy một file Python cụ thể và in phân cách rõ ràng."""
    duong_dan = tim_duong_dan_file(ten_file)
    
    if duong_dan is None:
        print(f"\n❌ Lỗi: Không tìm thấy file '{ten_file}' trong các thư mục Exercises hoặc Name-List!")
        return

    print("\n" + "=" * 60)
    print(f"▶️ ĐANG CHẠY: {mo_ta}")
    print(f"📁 Tệp: {duong_dan.name} (tại: {duong_dan.parent.name}/{duong_dan.name})")
    print("=" * 60)
    
    try:
        subprocess.run([sys.executable, str(duong_dan)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n⚠️ File kết thúc với mã lỗi: {e.returncode}")
    except Exception as e:
        print(f"\n❌ Đã xảy ra lỗi khi chạy: {e}")
        
    print("=" * 60)
    print("✅ Đã hoàn thành phần chạy bài!")

def chay_autograde():
    """Chạy trình tự kiểm tra AutoGrade chuẩn của khóa học nếu có."""
    print("\n" + "=" * 60)
    print("🎯 ĐANG CHẠY AUTOGRADE TỰ CHẤM ĐIỂM TUẦN 01...")
    print("=" * 60)
    # Tìm thư mục gốc của repository (nơi chứa assessment)
    thu_muc_goc = BASE_DIR if (BASE_DIR / "assessment").exists() else BASE_DIR.parent
    try:
        subprocess.run(
            [sys.executable, "-m", "assessment", "grade", "--week", "01", "--acknowledge-local-code"],
            cwd=str(thu_muc_goc),
            check=False
        )
    except Exception as e:
        print(f"❌ Lỗi khi chạy AutoGrade: {e}")
    print("=" * 60)

def hien_thi_menu():
    """In giao diện menu trực quan ra màn hình terminal."""
    print("\n" + "╔" + "═" * 58 + "╗")
    print("║        🐍 TRÌNH ĐIỀU HƯỚNG BÀI TẬP TUẦN 01 - TUẤN KIỆT 🐍        ║")
    print("╠" + "═" * 58 + "╣")
    print("║  [1] Bài 01: Hello Python & Hình chữ nhật ASCII          ║")
    print("║  [2] Bài 02: Máy tính Python & Các phép toán số học      ║")
    print("║  [3] Bài 03: Trò chuyện nhập liệu input() & Mad Libs     ║")
    print("║  [4] Mini-project: Thẻ danh thiếp ASCII tĩnh             ║")
    print("║  [5] 🎯 Chạy máy chấm điểm AutoGrade                     ║")
    print("║  [6] 📇 Mở dự án Name-List (Quản lý hồ sơ cá nhân)       ║")
    print("║  [0] Thoát chương trình                                  ║")
    print("╚" + "═" * 58 + "╝")

def main():
    while True:
        hien_thi_menu()
        lua_chon = input("👉 Nhập số bạn muốn chọn (0-6) rồi nhấn Enter: ").strip()
        
        if lua_chon == "1":
            chay_file("ex01_hello.py", "Bài 01 - Hello World & ASCII Art")
        elif lua_chon == "2":
            chay_file("ex02_calculator.py", "Bài 02 - Máy tính & Biểu thức số học")
        elif lua_chon == "3":
            chay_file("ex03_input.py", "Bài 03 - Tương tác input & Mad Libs")
        elif lua_chon == "4":
            chay_file("mini_project_card.py", "Mini-project - Thẻ danh thiếp ASCII")
        elif lua_chon == "5":
            chay_autograde()
        elif lua_chon == "6":
            chay_file("name_list.py", "Dự án Name-List - Quản lý hồ sơ cá nhân")
        elif lua_chon == "0" or lua_chon.lower() == "q":
            print("\n👋 Cảm ơn Tuấn Kiệt đã sử dụng. Hẹn gặp lại trong Tuần 02!")
            break
        else:
            print("\n⚠️ Lựa chọn không hợp lệ! Vui lòng chỉ bấm các phím từ 0 đến 6.")
            
        input("\n👉 Nhấn phím Enter để tiếp tục quay về menu...")

if __name__ == "__main__":
    main()
