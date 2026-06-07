# Vận dụng cơ bản - Lỗi Phạm Vi Biến (Scope) Trong Hệ Thống Tích Điểm

# (1) Phân tích lỗi
# 1. total_points được khai báo ngoài hàm nên là biến toàn cục (Global Variable).
# 2. Python thấy có phép gán:
#       total_points = total_points + points_earned
#    nên tự hiểu total_points trong hàm là biến cục bộ.
#    Tuy nhiên biến cục bộ này chưa được gán giá trị trước khi sử dụng,
#    dẫn đến lỗi UnboundLocalError.
# 3. Nếu chỉ đọc (print(total_points)) mà không gán lại giá trị,
#    chương trình sẽ không bị lỗi.
# 4. Cách sửa 1 dùng từ khóa global:
#       global total_points
# 5. Cách sửa 2 (khuyến nghị):
#    Truyền tổng điểm cũ và điểm mới vào hàm,
#    sau đó dùng return để trả về kết quả.

# (2) Source code đúng chuẩn (Cách 2)

def add_reward_points(current_points, points_earned):
    total_points = current_points + points_earned
    print(f"Đã cộng thêm {points_earned} điểm.")
    return total_points

# Khách hàng hiện có 100 điểm
total_points = 100

# Khách mua hàng được thưởng thêm 50 điểm
total_points = add_reward_points(total_points, 50)

# In kết quả
print("Tổng điểm hiện tại của khách hàng:", total_points)
