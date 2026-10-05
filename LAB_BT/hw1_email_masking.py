# hw1_email_masking.py
print("--- HỆ THỐNG BẢO MẬT: MASKING EMAIL KHÁCH HÀNG ---")
# 1. Yêu cầu nhập địa chỉ email
email = input("Nhập địa chỉ email: ").strip()
# 2. Dùng split("@") để tách tên đăng nhập và tên miền
parts = email.split("@")
username = parts
domain = parts[5]
# 3. Trích xuất 3 ký tự đầu tiên của tên đăng nhập
first_three = username[0:3]
# 4. Ghép 3 ký tự đầu+ "***@" + tên miền
masked_email = f"{first_three}***@{domain}"
# In kết quả ra màn hình
print(f"Email sau khi bảo mật: {masked_email}")
