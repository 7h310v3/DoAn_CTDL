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
    def insert(self, data):
        pass

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
        now = self.head
        if self.head != None:
            print("Các phẩn tử trong danh sách là:", end = " ")
            while (now): 
                print (now.data, end = "\t") 
                now = now.next
        else:
            print("Danh sách trống!")


  
def main():
    # Bắt đầu với ds rỗng 
    ds_don = LinkedList()

    print(ds_don.is_empty())

    ds_don.push(6)
    ds_don.push(8)
    ds_don.push(10)

    print(ds_don.is_empty())

    ds_don.print_list()

  
if __name__ == "__main__":
    main()

    