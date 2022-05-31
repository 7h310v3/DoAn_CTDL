class Queues:
    def __init__(self):
        self.items = []
        print("- Đã tạo queues -")

    # Kiểm tra queue rỗng hay không
    def is_empty(self):
        return len(self.items) == 0

    # Kiểm tra số phần tử có trong queue
    def __len__(self):
        return len(self.items)
    
    # Thêm 1 phần tử vào đỉnh queue
    def push(self, x):
        self.items.append(x)
        print(" +\n Đã thêm '{}' vào queue.\n queue hiện có {} phần tử\n".format(x, len(self.items)))

    def pops(self):
        self.items.pop(0)

    # Hiển thị các phẩn tử queue
    def __str__(self):
        return "\nCác phần tử trong queue: " + str(self.items) + "\n"
        
def main():
    q = Queues()     # Tạo danh sách với tên biến là q

    while True:
        print("1. Kiểm tra queue rỗng")
        print("2. Thêm 1 phần tử vào queue.")
        print("3. Lấy 1 phần tử từ queue.")
        print("4. Tính độ dài của queue")
        print("5. Hiển thị các phần tử của queue")
        print("0. Để thoát!")

        key = int(input("Nhập lựa chọn: "))
        if key == 1:
            if q.is_empty():
                print("\nqueue rỗng!\n")
            else:
                print("\nqueue chứa phần tử!\n")
        if key == 2:
            tmp = int(input("Nhập phần tử muốn thêm: "))
            q.push(tmp)
        if key == 3:
            if q.is_empty():
                print("\nqueue rỗng!\n")
            else:
                print(" -\n Đã lấy '{}' ra khỏi queue.\n queue hiện có {} phần tử\n".format(q.items[0], len(q.items) - 1))
                q.pops()
        if key == 4:
            if q.is_empty():
                print("\nqueue rỗng!\n")
            else:
                print("\nSố phẩn tử có trong queue: ", q.__len__(), "\n")
        if key == 5:
            if q.is_empty():
                print("\nqueue rỗng!\n")
            else:
                print( q.__str__())
        if key == 0:
            break


if __name__ == "__main__":
    main()
    