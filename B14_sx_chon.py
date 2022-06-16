def sapxep_chon(n):
    # Giá trị này của i tương ứng với bao nhiêu giá trị đã được sắp xếp
    for i in range(len(n)):
        # Giả định rằng mục đầu tiên của phân đoạn chưa được sắp xếp là mục nhỏ nhất 
        GT_chimucthapnhat = i
        # Vòng lặp này lặp lại các mục chưa được sắp xếp
        for j in range(i + 1, len(n)):
            if n[j] < n[GT_chimucthapnhat]:
                GT_chimucthapnhat = j
        # Hoán đổi các giá trị của phần tử chưa được sắp xếp thấp nhất với phần tử chưa được sắp xếp đầu tiên
        # Phần tử
        n[i], n[GT_chimucthapnhat] = n[GT_chimucthapnhat], n[i]

def main():
    arr_t = [5, 6, 8, 2, 3, 9, 12]
    sapxep_chon(arr_t)
    print(arr_t)

if __name__ == '__main__':
    main()