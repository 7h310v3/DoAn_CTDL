def giaithua(tmp):
    if tmp == 1:
        return 1
    else:
        return tmp * giaithua(tmp - 1)

def main():
    num = int(input("Nhập số cần tính giai thừa: "))
    print("Giai thừa của", num, "=",giaithua(num))

if __name__ == "__main__":
    main()