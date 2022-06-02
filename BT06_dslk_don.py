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

    # Kiểm tra danh sách rỗng hay không
    def is_empty(self):
        return self.head == 0
  
    # Hàm này in nội dung của danh sách liên kết 
    # Bắt đầu từ head 
    def print_list(self): 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next

    # Thêm phẩn tử vào danh sách
    def push(self, data):
        pass

    # Xóa phần tử nào đó trong danh sách
    def remove(self, data):
        pass

    # Chèn phần tử vào danh sách
    def insert(self, data):
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

  
def main():
    # Bắt đầu với ds rỗng 
    ds_don = LinkedList()

    print(ds_don.is_empty())


  
if __name__ == "__main__":
    main()