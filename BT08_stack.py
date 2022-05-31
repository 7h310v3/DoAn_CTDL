class Stack:

    # Khởi tạo Stack
    def __init__(self):
        self.StkArray = []

    # Thêm 1 phần tử vào đỉnh stack
    def push(self, x):
        self.StkArray.append(x)

    # Lấy 1 phần tử từ đỉnh stack
    def pop(self):
        return self.StkArray.pop()

    # Kiểm tra stack rỗng hay không
    def is_empty(self):
        return len(self.StkArray) == 0

    # Hàm trả về giá trị đỉnh
    def top(self):
        return self.StkArray[-1]

    # Tính độ dài stack
    def __len__(self):
        return len(self.StkArray)

    # Hiển thị các phẩn tử stack
    def __str__(self):
        return "\nCác phần tử trong stack: " + str(self.StkArray) + "\n"


def main():
    # Khai báo đổi tượng
    StkArray = Stack()

    while True:
        print("1. Kiểm tra stack rỗng")
        print("2. Thêm 1 phần tử vào đỉnh stack.")
        print("3. Lấy 1 phần tử từ đỉnh stack.")
        print("4. Lấy giá trị đỉnh của stack")
        print("5. Tính độ dài của stack")
        print("6. Hiển thị các phần tử của stack")
        print("0. Để thoát!")
    
        key = int(input("Nhập lựa chọn: "))
        if key == 1:
            if StkArray.is_empty():
                print("\nStack rỗng!\n")
            else:
                print("\nStack chứa phần tử!\n")
        if key == 2:
            tmp = int(input("Nhập phần tử muốn thêm: "))
            StkArray.push(tmp)
        if key == 3:
            if StkArray.is_empty():
                print("\nStack rỗng!\n")
            else:
                StkArray.pop()
                print("\nĐã lấy 1 phần tử!\n")
        if key == 4:
            if StkArray.is_empty():
                print("\nStack rỗng!\n")
            else:
                print("\nĐỉnh là: ", StkArray.top(), "\n")
        if key == 5:
            if StkArray.is_empty():
                print("\nStack rỗng!\n")
            else:
                print("\nSố phẩn tử có trong stack: ", StkArray.__len__(), "\n")
        if key == 6:
            if StkArray.is_empty():
                print("\nStack rỗng!\n")
            else:
                print( StkArray.__str__())
        if key == 0:
            break


if __name__ == "__main__":
    main()
