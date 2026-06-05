next_id = 1
car_list = []

while True:

    print('Quản lý bãi xe - smart parking')
    print('1. thêm xe mới vào bãi')
    print('3. hiện thị danh sách xe trong bãi')
    print('3. xóa xe khỏi bãi (Khi có xe)')
    print('4. Thoát chương trình')

    choice = input('Nhập chức năng: ')

    match choice:
        case '1':

            while True:
                plate = input('Nhập loại xe: ').strip()
                if plate:
                    break
                print('Loại xe không được để trống!')

            while True:
                car_owner = input('Nhập tên chủ xe: ').strip()
                if car_owner:
                    break
                print('Tên chủ xe không được để trống!')

            car = {
                'id': next_id,
                'Loại xe': plate,
                'Chủ xe': car_owner
            }

            car_list.append(car)

            print(f'Thêm xe ID {next_id} thành công!')

            next_id += 1
           

        case '2':
            if not car_list:
                print('Bãi xe đang chống! ')
            else:
                print('Thông xin bãi xe hiện tại:')
                print(car_list)
    
        case '3':
            if not car_list:
                print('Không tìm thấy xe để xóa!')
            else:
                found = False
                id_delete = int(input('Nhập id của xe: '))
                for car in car_list:
                    if car['id'] == id_delete:
                        car_list.remove(car)
                        print(f'Đã xóa xe {id_delete} thành công')
                        found = True
                        break
                if not found:
                    print('Không tìm thấy xe để xóa!')
        case '4':
            print('Đã thoát chương trình')
            break

            