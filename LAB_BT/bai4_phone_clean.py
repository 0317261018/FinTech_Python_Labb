# bai4_phone_clean.py
print("--- HỆ THỐNG CHUẨN HÓA SỐ ĐIỆN THOẠI KHÁCH HÀNG ---")
# 1. Nhập số điện thoại thô
raw_phone = input("Nhập số điện thoại cần làm sạch: ")
# 2. Sử dụng Method Chaining để thay thế liên tục các ký tự thừa
clean_phone = raw_phone.replace("+84", "0").replace("-", "").replace(".", "").replace(" ", "")
# 3. In kết quả đã chuẩn hóa
print(f"Số điện thoại chuẩn hóa: {clean_phone}")
