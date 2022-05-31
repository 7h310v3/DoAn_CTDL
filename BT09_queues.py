class Queues:
    def __init__(self):
        self.items = []
        print("- Đã tạo danh sách -")

    # Kiểm tra queue rỗng hay không
    def is_empty(self):
        return len(self.items) == 0

    # Kiểm tra số phần tử có trong queue
    def __len__(self):
        return len(self.items)
    
    # Thêm 1 phần tử vào đỉnh stack
    def push(self, x):
        self.items.append(x)
        print(" +\n Đã thêm '{}' vào danh sách\n Danh sách hiện có {} phần tử\n".format(item, len(self.items)))

    def Lấy_phần_tử(self):
        """
            Lấy phần tử ra hàng chờ
        """ 
        item = self.items.pop(0)
        print(" -\n Đã lấy '{}' ra khỏi danh sách\n Danh sách hiện có {} phần tử\n".format(item, len(self.items)))

if __name__ == "__main__":
    que = Queues()     # Tạo danh sách với tên biến là a

    que.Tình_trạng_danh_sách()    # Xem tình trạng danh sách
	
    que.Thêm_phần_tử(5.1)
    que.Thêm_phần_tử('hien')
    que.Thêm_phần_tử(False)
    que.Thêm_phần_tử(10)

    que.Lấy_phần_tử()
    que.Lấy_phần_tử()
    que.Lấy_phần_tử()
    que.Lấy_phần_tử()