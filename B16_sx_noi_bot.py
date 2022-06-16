def bubbleSort(arr):
    n = len(arr)
    # flag
    swapped = False
    # Duyệt qua tất cả các phần tử mảng
    for i in range(n - 1):
        # Duyệt qua mảng từ 0 đến n-i-1
        for j in range(0, n - i - 1):
            # Hoán đổi nếu phần tử tìm được lớn hơn phần tử tiếp theo
            if arr[j] > arr[j + 1]:
                # flag
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # nếu chúng ta không cần thực hiện một lần hoán đổi,
            # chúng ta có thể thoát khỏi vòng lặp chính.
            break


def main():
    arr_t = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr_t)

    print("Mảng đã sắp xếp:", end="")
    for i in range(len(arr_t)):
        print("% d" % arr_t[i], end="\t")


if __name__ == "__main__":
    main()


