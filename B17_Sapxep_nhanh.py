def sort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:  # xử lý phần ở cuối đệ quy - khi chỉ có một phần tử trong mảng của mình, chỉ cần trả về mảng. 
        return array

def main():
    arr_t = [5, 6, 8, 2, 3, 9, 12]
    print(sort(arr_t))

if __name__ == '__main__':
    main()