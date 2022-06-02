# Node class 
class Node: 
  
    # Hàm khởi tạo dối tượng  node
    def __init__(self, data): 
        self.data = data  # Gán dữ liệu
        self.next = None  # Khởi tạo tiếp theo là null
  
  
# Lớp Danh sách được liên kết chứa một đối tượng Node
class LinkedList: 
  
    # Hàm khởi tạo head 
    def __init__(self): 
        self.head = None
        self.last = None

    # Kiểm tra danh sách rỗng hay không
    def is_empty(self):
        return self.head == None

    # Thêm phẩn tử vào cuối danh sách
    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    # Chèn phần tử vào danh sách
    def insert(self, address,data):
        node = Node(data)
        head = None
        now = self.head
        count = 0
        while count < address and now != None:
            count += 1
            head = now
            now = now.next
        if head == None:
            node.next = self.head
            self.head = node
            if self.last == None:
                self.last = node
        else:
            if now == None:
                self.last.next = node
                self.last = node
            else:
                head.next = node
                node.next = now

    # Xóa phần tử nào đó trong danh sách
    def remove(self, data):
        pass

    # Cập nhật
    def update(self, located,data):
        pass

    # Xóa hết các phần tử có trong danh sách
    def remove_all(self):
        pass
    
    # Tìm giá trị
    def search(self, data):
        pass
    
    # In ra danh sách
    def print_list(self):
        flag = True
        now = self.head
        if now != None:
            while (now): 
                if flag:
                    print("Các phẩn tử trong danh sách là:[", now.data, end = " ")
                    flag = False
                else:
                    print (" -> ", now.data, end = " ") 
                now = now.next
            print("]")
            
        else:
            print("Danh sách trống!")


  
def main():
    # Bắt đầu với ds rỗng 
    ds_don = LinkedList()

    while True:
        print("1. Kiểm tra danh sách rỗng.")
        print("2. Thêm 1 phần tử vào cuối danh sách.")
        print("3. Lấy 1 phần tử từ danh sách.")
        print("5. Tính độ dài của danh sách.")
        print("6. Hiển thị các phần tử của danh sách.")
        print("0. Để thoát!")
    
        key = int(input("Nhập lựa chọn: "))
        if key == 1:
            if ds_don.is_empty():
                print("\nDanh sách rỗng!\n")
            else:
                print("\nDanh sách chứa phần tử!\n")
        if key == 2:
            tmp = int(input("Nhập phần tử muốn thêm: "))
            ds_don.push(tmp)
        if key == 3:
            pass

        if key == 6:
            print(ds_don.print_list())
        if key == 0:
            break
  
if __name__ == "__main__":
    main()