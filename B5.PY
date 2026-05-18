# Bảng thiết kế dữ liệu đầu vào (Input)
# STT    |Tên biến (snake_case)  |Kiểu dữ liệu  |Câu hỏi gợi ý (Prompt chi tiết)|
# 1      |patient_name           |   str        |  Nhập họ và tên bệnh nhân (Ví dụ: Nguyen Van A):
# 2      | patient_age           |    int       |   Nhập tuổi bệnh nhân (Ví dụ: 35):
# 3      | spo2_level            |      int     |    Nhập nồng độ oxy trong máu SpO2 % (Ví dụ: 96):
# 4      |  heart_rate           |    int       |     Nhập nhịp tim - nhịp/phút (Ví dụ: 80):
# 5      | has_insurance         |   str        |     Bạn có thẻ BHYT không? (Vui lòng chỉ gõ 'yes' hoặc 'no'):

# Thiết kế luồng chương trình (Các bước thực hiện)
# Bước 1: Kiosk hiển thị lời nhắc, thu thập 5 thông tin đầu vào từ người dùng dựa theo bảng thiết kế dữ liệu.
# Chuyển đổi định dạng chữ nhập của câu hỏi BHYT về chữ thường để tránh lỗi viết hoa.
# Bước 2: Xét điều kiện phân luồng y khoa từ mức nghiêm trọng nhất (ĐỎ \(\rightarrow \) VÀNG \(\rightarrow \) XANH).
# Bước 3: Xét điều kiện tính toán viện phí dựa trên tuổi và trạng thái bảo hiểm y tế.
# Bước 4: Xuất kết quả ra màn hình thành 2 phần: Phiếu khám bệnh trực quan cho bệnh nhân và Log kỹ thuật cho hệ thống.


print("--- KIOSK TỰ ĐỘNG KHÁM BỆNH ---")

patient_name = input("Nhập họ và tên (Ví dụ: Nguyen Van A): ")
patient_age = int(input("Nhập tuổi (Ví dụ: 15): "))
spo2_level = int(input("Nhập chỉ số oxy SpO2 (Ví dụ: 96): "))
heart_rate = int(input("Nhập nhịp tim (Ví dụ: 80): "))
has_insurance = input("Bạn có thẻ bảo hiểm không? (Gõ yes hoặc no): ")

if spo2_level < 90 or heart_rate > 120:
    triage_status = "MÀU ĐỎ - CẤP CỨU KHẨN CẤP!"
elif spo2_level <= 95 or heart_rate >= 100:
    triage_status = "MÀU VÀNG - THEO DÕI SÁT"
else:
    triage_status = "MÀU XANH - KHÁM THƯỜNG"

if patient_age < 6 or patient_age >= 80:
    hospital_fee = 0  
elif has_insurance == "yes":
    hospital_fee = 250000  
else:
    hospital_fee = 500000 

print("\n--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")
print("Tên bệnh nhân:", patient_name)
print("Tuổi bệnh nhân:", patient_age)
print("Xếp loại khám:", triage_status)
print("Tiền viện phí:", hospital_fee, "VNĐ")

print("---------------------------------")
print("\n--- LOG HỆ THỐNG CỦA LẬP TRÌNH VIÊN ---")
print("Tên biến: patient_name | Kiểu dữ liệu:", type(patient_name))
print("Tên biến: patient_age  | Kiểu dữ liệu:", type(patient_age))
print("Tên biến: spo2_level   | Kiểu dữ liệu:", type(spo2_level))
print("Tên biến: heart_rate   | Kiểu dữ liệu:", type(heart_rate))
print("Tên biến: hospital_fee | Kiểu dữ liệu:", type(hospital_fee))
