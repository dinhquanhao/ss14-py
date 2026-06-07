"""
HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY

PHẦN 1 - PHÂN TÍCH & THIẾT KẾ

1. validate_score(score_input)
- Input: score_input (str)
- Output: bool
- Chức năng: Kiểm tra điểm có phải số từ 0 đến 10 hay không.

2. find_student_by_id(student_list, student_id)
- Input:
    + student_list (list)
    + student_id (str)
- Output:
    + index (int) nếu tìm thấy
    + -1 nếu không tìm thấy

3. get_rank(average_score)
- Input: average_score (float)
- Output: str
- Chức năng: Trả về xếp loại học lực.

4. display_students(student_list)
- Input: student_list (list)
- Output: None
- Chức năng: Hiển thị danh sách học viên.

5. add_student(student_list)
- Input: student_list (list)
- Output: None
- Chức năng: Thêm học viên mới.

6. update_score(student_list)
- Input: student_list (list)
- Output: None
- Chức năng: Cập nhật điểm học viên.

7. evaluate_students(student_list)
- Input: student_list (list)
- Output: None
- Chức năng: Đánh giá học lực toàn bộ học viên.

LỢI ÍCH TÁCH HÀM
- Dễ đọc và bảo trì.
- Dễ kiểm thử từng chức năng.
- Tái sử dụng code.
- Giảm spaghetti code.
- Dễ nâng cấp hệ thống.
"""

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]


def validate_score(score_input):
    """Kiểm tra điểm hợp lệ từ 0 đến 10."""
    try:
        score = float(score_input)
        return 0 <= score <= 10
    except ValueError:
        return False


def input_score(subject_name):
    """Nhập điểm và bắt lỗi cho đến khi hợp lệ."""
    while True:
        score_input = input(f"Nhập điểm {subject_name}: ")
        if validate_score(score_input):
            return float(score_input)

        print("Điểm không hợp lệ, phải là số từ 0 đến 10!")


def find_student_by_id(student_list, student_id):
    """Tìm vị trí học viên theo mã."""
    student_id = student_id.strip().upper()

    for index, student in enumerate(student_list):
        if student["student_id"] == student_id:
            return index

    return -1


def get_rank(average_score):
    """Trả về xếp loại học lực."""
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


def display_students(student_list):
    """Hiển thị danh sách học viên."""
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return

    print("\n===== DANH SÁCH HỌC VIÊN =====")

    for index, student in enumerate(student_list, start=1):
        print(
            f"{index}. Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"Toán: {student['math_score']} | "
            f"Anh: {student['english_score']}"
        )


def add_student(student_list):
    """Thêm học viên mới."""

    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()

        if find_student_by_id(student_list, student_id) != -1:
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
            continue

        break

    while True:
        name = input("Nhập tên học viên: ").strip().title()

        if name:
            break

        print("Tên học viên không được để trống!")

    math_score = input_score("Toán")
    english_score = input_score("Tiếng Anh")

    student_list.append(
        {
            "student_id": student_id,
            "name": name,
            "math_score": math_score,
            "english_score": english_score
        }
    )

    print("Thêm học viên thành công!")


def update_score(student_list):
    """Cập nhật điểm học viên theo mã."""

    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()

    index = find_student_by_id(student_list, student_id)

    if index == -1:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return

    print("Nhập điểm mới:")

    student_list[index]["math_score"] = input_score("Toán")
    student_list[index]["english_score"] = input_score("Tiếng Anh")

    print("Cập nhật điểm thành công!")


def evaluate_students(student_list):
    """Đánh giá học lực toàn bộ học viên."""

    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return

    print("\n===== KẾT QUẢ ĐÁNH GIÁ =====")

    for student in student_list:
        average = (
            student["math_score"] +
            student["english_score"]
        ) / 2

        rank = get_rank(average)

        print(
            f"Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"ĐTB: {average:.2f} | "
            f"Xếp loại: {rank}"
        )


def display_menu():
    """Hiển thị menu."""

    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")


def main():
    """Luồng chính của chương trình."""

    while True:
        display_menu()

        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            display_students(students)

        elif choice == "2":
            add_student(students)

        elif choice == "3":
            update_score(students)

        elif choice == "4":
            evaluate_students(students)

        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


if __name__ == "__main__":
    main()
