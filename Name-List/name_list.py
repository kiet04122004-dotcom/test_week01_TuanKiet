"""
Dự án Mini: Quản lý Hồ sơ & Danh sách Cá nhân (Name-List) 📇
==========================================================
Tác giả: Tuấn Kiệt & Trợ lý Python
Mô tả: Ứng dụng dòng lệnh cho phép nhập, lưu trữ, hiển thị,
       tìm kiếm và thống kê thông tin cá nhân.
- Tuổi và Cung hoàng đạo được TỰ ĐỘNG TÍNH TOÁN từ ngày sinh đến thời gian hiện tại.
- Dữ liệu được lưu vĩnh viễn vào tệp 'danh_sach.json' (chuẩn UTF-8).
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Đường dẫn thư mục hiện tại và file lưu dữ liệu
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "danh_sach.json"


def tinh_tuoi_tu_ngay_sinh(ngay: int, thang: int, nam: int) -> int:
    """Tự động tính tuổi chính xác từ ngày, tháng, năm sinh đến thời điểm hiện tại.
    Nếu chưa đến ngày sinh nhật trong năm nay thì trừ đi 1 tuổi.
    """
    hom_nay = datetime.now()
    chua_den_sinh_nhat = (hom_nay.month, hom_nay.day) < (thang, ngay)
    tuoi = hom_nay.year - nam - int(chua_den_sinh_nhat)
    return max(0, tuoi)


def tinh_cung_hoang_dao(ngay: int, thang: int) -> str:
    """Hàm sáng tạo: Xác định cung hoàng đạo dựa trên ngày và tháng sinh."""
    if (thang == 3 and ngay >= 21) or (thang == 4 and ngay <= 19):
        return "Bạch Dương ♈"
    elif (thang == 4 and ngay >= 20) or (thang == 5 and ngay <= 20):
        return "Kim Ngưu ♉"
    elif (thang == 5 and ngay >= 21) or (thang == 6 and ngay <= 21):
        return "Song Tử ♊"
    elif (thang == 6 and ngay >= 22) or (thang == 7 and ngay <= 22):
        return "Cự Giải ♋"
    elif (thang == 7 and ngay >= 23) or (thang == 8 and ngay <= 22):
        return "Sư Tử ♌"
    elif (thang == 8 and ngay >= 23) or (thang == 9 and ngay <= 22):
        return "Xử Nữ ♍"
    elif (thang == 9 and ngay >= 23) or (thang == 10 and ngay <= 23):
        return "Thiên Bình ♎"
    elif (thang == 10 and ngay >= 24) or (thang == 11 and ngay <= 21):
        return "Bọ Cạp ♏"
    elif (thang == 11 and ngay >= 22) or (thang == 12 and ngay <= 21):
        return "Nhân Mã ♐"
    elif (thang == 12 and ngay >= 22) or (thang == 1 and ngay <= 19):
        return "Ma Kết ♑"
    elif (thang == 1 and ngay >= 20) or (thang == 2 and ngay <= 18):
        return "Bảo Bình ♒"
    elif (thang == 2 and ngay >= 19) or (thang == 3 and ngay <= 20):
        return "Song Ngư ♓"
    return "Chưa xác định"


def tai_du_lieu() -> list:
    """Đọc dữ liệu từ file JSON. Tự động cập nhật lại tuổi theo thời gian hiện tại."""
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            danh_sach = json.load(f)
            
        # Tự động cập nhật lại tuổi mới nhất cho từng hồ sơ dựa trên thời gian hiện tại
        for nguoi in danh_sach:
            ns = nguoi.get("ngay_sinh", "")
            parts = ns.replace("-", "/").split("/")
            if len(parts) == 3:
                try:
                    d, m, y = int(parts[0]), int(parts[1]), int(parts[2])
                    nguoi["tuoi"] = tinh_tuoi_tu_ngay_sinh(d, m, y)
                except ValueError:
                    pass
        return danh_sach
    except Exception as e:
        print(f"⚠️ Không thể đọc file dữ liệu: {e}")
        return []


def luu_du_lieu(danh_sach: list):
    """Ghi danh sách hồ sơ vào file JSON."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(danh_sach, f, ensure_ascii=False, indent=4)
        print(f"💾 Đã lưu dữ liệu thành công vào '{DATA_FILE.name}'!")
    except Exception as e:
        print(f"❌ Lỗi khi lưu dữ liệu: {e}")


def in_the_ca_nhan(nguoi: dict, stt: int = None):
    """In thông tin 1 cá nhân ra dạng thẻ ASCII đẹp mắt."""
    tieu_de = f" HỒ SƠ #{stt} " if stt else " THÔNG TIN HỒ SƠ "
    print("\n┌" + "─" * 48 + "┐")
    print(f"│{tieu_de:^48}│")
    print("├" + "─" * 48 + "┤")
    print(f"│ 👤 Họ và tên   : {nguoi.get('ho_ten', ''):<31}│")
    print(f"│ 🎂 Ngày sinh   : {nguoi.get('ngay_sinh', ''):<31}│")
    print(f"│ 🔢 Tuổi        : {str(nguoi.get('tuoi', '')) + ' tuổi (Tự động tính)':<31}│")
    print(f"│ ⭐ Cung H.Đạo  : {nguoi.get('cung_hoang_dao', ''):<31}│")
    print(f"│ 🏡 Quê quán    : {nguoi.get('que_quan', ''):<31}│")
    print(f"│ 🎨 Sở thích    : {nguoi.get('so_thich', ''):<31}│")
    print(f"│ 🎯 Mục tiêu    : {nguoi.get('muc_tieu', ''):<31}│")
    print("└" + "─" * 48 + "┘")


def them_ho_so(danh_sach: list):
    """Chức năng 1: Nhập thông tin cá nhân mới từ bàn phím.
    Tuổi được tự động tính từ ngày tháng năm sinh đến năm hiện tại!
    """
    print("\n" + "═" * 55)
    print("➕ NHẬP THÔNG TIN CÁ NHÂN MỚI (TUỔI TỰ ĐỘNG TÍNH)")
    print("═" * 55)

    # 1. Họ và tên
    while True:
        ho_ten = input("1. Nhập Họ và Tên: ").strip()
        if ho_ten:
            break
        print("   ⚠️ Họ tên không được để trống!")

    # 2. Ngày tháng năm sinh & TỰ ĐỘNG TÍNH TUỔI
    cung = "Chưa rõ"
    tuoi = 0
    hom_nay = datetime.now()

    while True:
        ngay_sinh = input("2. Nhập Ngày sinh (định dạng Ngày/Tháng/Năm, vd: 04/12/2004): ").strip()
        try:
            parts = ngay_sinh.replace("-", "/").split("/")
            if len(parts) == 3:
                d, m, y = int(parts[0]), int(parts[1]), int(parts[2])
                
                # Kiểm tra ngày tháng năm hợp lý
                if y > hom_nay.year or y < 1900 or m < 1 or m > 12 or d < 1 or d > 31:
                    print(f"   ⚠️ Năm sinh phải từ 1900 đến {hom_nay.year}! Vui lòng nhập lại.")
                    continue
                
                # TỰ ĐỘNG TÍNH TUỔI: Từ ngày sinh đến thời điểm hiện tại
                tuoi = tinh_tuoi_tu_ngay_sinh(d, m, y)
                cung = tinh_cung_hoang_dao(d, m)
                ngay_sinh = f"{d:02d}/{m:02d}/{y:04d}"
                
                print(f"   ✨ [TỰ ĐỘNG TÍNH TOÁN]:")
                print(f"      • Tuổi hiện tại : {tuoi} tuổi (Năm sinh {y} ➔ Năm {hom_nay.year})")
                print(f"      • Cung Hoàng Đạo: {cung}")
                break
            else:
                print("   ⚠️ Vui lòng nhập đúng dạng Ngày/Tháng/Năm (ví dụ: 04/12/2004)!")
        except ValueError:
            print("   ⚠️ Ngày, tháng, năm phải là các con số hợp lệ!")

    # 3. Các thông tin sáng tạo thêm (không cần nhập tuổi bằng tay nữa)
    que_quan = input("3. Quê quán / Tỉnh thành: ").strip() or "Chưa cập nhật"
    so_thich = input("4. Sở thích cá nhân: ").strip() or "Học lập trình"
    muc_tieu = input("5. Mục tiêu / Châm ngôn sống: ").strip() or "Trở thành lập trình viên giỏi"

    ho_so_moi = {
        "ho_ten": ho_ten,
        "ngay_sinh": ngay_sinh,
        "tuoi": tuoi,
        "cung_hoang_dao": cung,
        "que_quan": que_quan,
        "so_thich": so_thich,
        "muc_tieu": muc_tieu,
        "thoi_gian_tao": hom_nay.strftime("%Y-%m-%d %H:%M:%S")
    }

    danh_sach.append(ho_so_moi)
    luu_du_lieu(danh_sach)
    
    print("\n🎉 Đã thêm hồ sơ thành công:")
    in_the_ca_nhan(ho_so_moi)


def xem_tat_ca(danh_sach: list):
    """Chức năng 2: Hiển thị toàn bộ danh sách hồ sơ."""
    print("\n" + "═" * 50)
    print(f"📋 DANH SÁCH HỒ SƠ ĐÃ LƯU (Tổng số: {len(danh_sach)})")
    print("═" * 50)

    if not danh_sach:
        print("👉 Hiện tại chưa có hồ sơ nào trong danh sách. Hãy chọn [1] để thêm mới!")
        return

    for i, nguoi in enumerate(danh_sach, start=1):
        in_the_ca_nhan(nguoi, stt=i)


def tim_kiem(danh_sach: list):
    """Chức năng 3: Tìm kiếm hồ sơ theo họ tên."""
    print("\n" + "═" * 50)
    print("🔍 TÌM KIẾM HỒ SƠ THEO TÊN")
    print("═" * 50)

    tu_khoa = input("Nhập tên bạn cần tìm: ").strip().lower()
    if not tu_khoa:
        print("⚠️ Bạn chưa nhập từ khóa tìm kiếm!")
        return

    ket_qua = [p for p in danh_sach if tu_khoa in p.get("ho_ten", "").lower()]

    if not ket_qua:
        print(f"❌ Không tìm thấy hồ sơ nào chứa từ khóa '{tu_khoa}'.")
    else:
        print(f"✅ Tìm thấy {len(ket_qua)} kết quả phù hợp:")
        for i, nguoi in enumerate(ket_qua, start=1):
            in_the_ca_nhan(nguoi, stt=i)


def thong_ke(danh_sach: list):
    """Chức năng 4: Thống kê số liệu về danh sách."""
    print("\n" + "═" * 50)
    print("📊 THỐNG KÊ DANH SÁCH HỒ SƠ")
    print("═" * 50)

    if not danh_sach:
        print("👉 Chưa có dữ liệu để thống kê.")
        return

    tong = len(danh_sach)
    danh_sach_tuoi = [p["tuoi"] for p in danh_sach if "tuoi" in p]
    tuoi_tb = sum(danh_sach_tuoi) / tong if danh_sach_tuoi else 0
    nguoi_lon_nhat = max(danh_sach, key=lambda x: x["tuoi"])
    nguoi_tre_nhat = min(danh_sach, key=lambda x: x["tuoi"])

    print(f"• Tổng số hồ sơ        : {tong} người")
    print(f"• Độ tuổi trung bình   : {tuoi_tb:.1f} tuổi")
    print(f"• Người lớn tuổi nhất  : {nguoi_lon_nhat['ho_ten']} ({nguoi_lon_nhat['tuoi']} tuổi)")
    print(f"• Người nhỏ tuổi nhất  : {nguoi_tre_nhat['ho_ten']} ({nguoi_tre_nhat['tuoi']} tuổi)")


def xoa_ho_so(danh_sach: list):
    """Chức năng 5: Xóa hồ sơ theo họ tên."""
    print("\n" + "═" * 50)
    print("🗑️ XÓA HỒ SƠ")
    print("═" * 50)

    ten_xoa = input("Nhập chính xác họ tên người cần xóa: ").strip()
    tim_thay = None
    for nguoi in danh_sach:
        if nguoi.get("ho_ten", "").strip().lower() == ten_xoa.lower():
            tim_thay = nguoi
            break

    if not tim_thay:
        print(f"❌ Không tìm thấy người có tên '{ten_xoa}' để xóa.")
        return

    xac_nhan = input(f"❓ Bạn có chắc chắn muốn xóa hồ sơ của '{tim_thay['ho_ten']}' không? (c/k): ").strip().lower()
    if xac_nhan in ["c", "co", "y", "yes"]:
        danh_sach.remove(tim_thay)
        luu_du_lieu(danh_sach)
        print(f"✅ Đã xóa hồ sơ của '{tim_thay['ho_ten']}' thành công!")
    else:
        print("❎ Đã hủy thao tác xóa.")


def hien_thi_menu():
    """In giao diện bảng chọn chính."""
    print("\n" + "╔" + "═" * 48 + "╗")
    print("║     📇 HỆ THỐNG QUẢN LÝ DANH SÁCH CÁ NHÂN      ║")
    print("╠" + "═" * 48 + "╣")
    print("║  [1] ➕ Nhập thêm thông tin cá nhân mới        ║")
    print("║  [2] 📋 Xem tất cả hồ sơ đã lưu                ║")
    print("║  [3] 🔍 Tìm kiếm hồ sơ theo họ tên             ║")
    print("║  [4] 📊 Xem thống kê (độ tuổi, số lượng)       ║")
    print("║  [5] 🗑️ Xóa một hồ sơ theo tên                ║")
    print("║  [0] 🚪 Thoát chương trình                     ║")
    print("╚" + "═" * 48 + "╝")


def main():
    # Tự động tải dữ liệu cũ khi khởi động chương trình và cập nhật tuổi
    danh_sach = tai_du_lieu()

    # Thêm sẵn 1 hồ sơ mẫu nếu chưa có dữ liệu để bạn dễ trải nghiệm ngay
    if not danh_sach:
        hom_nay = datetime.now()
        tuoi_mau = tinh_tuoi_tu_ngay_sinh(4, 12, 2004)
        ho_so_mau = {
            "ho_ten": "Mai Tuấn Kiệt",
            "ngay_sinh": "04/12/2004",
            "tuoi": tuoi_mau,
            "cung_hoang_dao": "Nhân Mã ♐",
            "que_quan": "TP. Hồ Chí Minh",
            "so_thich": "Lập trình Python & Khám phá AI",
            "muc_tieu": "Trở thành lập trình viên xuất sắc",
            "thoi_gian_tao": hom_nay.strftime("%Y-%m-%d %H:%M:%S")
        }
        danh_sach.append(ho_so_mau)
        luu_du_lieu(danh_sach)

    while True:
        hien_thi_menu()
        lua_chon = input("👉 Mời bạn chọn chức năng (0-5): ").strip()

        if lua_chon == "1":
            them_ho_so(danh_sach)
        elif lua_chon == "2":
            xem_tat_ca(danh_sach)
        elif lua_chon == "3":
            tim_kiem(danh_sach)
        elif lua_chon == "4":
            thong_ke(danh_sach)
        elif lua_chon == "5":
            xoa_ho_so(danh_sach)
        elif lua_chon == "0" or lua_chon.lower() == "q":
            print("\n👋 Cảm ơn bạn đã sử dụng chương trình Name-List! Tạm biệt!")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ, vui lòng chọn số từ 0 đến 5!")

        input("\n👉 Nhấn Enter để tiếp tục quay về menu...")


if __name__ == "__main__":
    main()
