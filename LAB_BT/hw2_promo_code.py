# hw2_promo_code.py
print("--- HỆ THỐNG TẠO MÃ ƯU ĐÃI (PROMO CODE GENERATOR) ---")
# 1. Nhập Họ Tên đầy đủ và Năm sinh
full_name = input("Nhập họ và tên đầy đủ: ").strip()
birth_year = input("Nhập năm sinh: ").strip()
# 2. Dùng split() tách chuỗi và lấy từ cuối cùng (Tên)
name_parts = full_name.split()
first_name = name_parts[-1] # Lấy phần tử cuối cùng trong danh sách
# 3. Lấy 3 ký tự đầu của Tên và chuyển thành CHỮ HOA
promo_prefix = first_name[0:3].upper()
# 4. Nối chuỗi bằng F-strings theo cấu trúc[TÊN]-[NĂM SINH]-VIP
promo_code = f"{promo_prefix}-{birth_year}-VIP"
# In kết quả ra màn hình
print(f"Mã ưu đãi của bạn: {promo_code}")
