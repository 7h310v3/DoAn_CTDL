def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def main():
    so1 = int(input("Nhap so dau tien: "))
    so2 = int(input("Nhap so thu 2: "))

    ucln = gcd(so1, so2)
    print("Uoc chung lon nhat la: ", ucln)

if __name__ == "__main__":
    main()