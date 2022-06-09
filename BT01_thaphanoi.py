def SapXep(n, a, b, c):
    if(n == 1):
        print(a," --> ",c)
    else:
        SapXep(n - 1, a, c, b)
        SapXep(1, a, b, c)
        SapXep(n - 1, b, a, c)

def main():
    dau = "A"
    giua = "B"
    cuoi = "C"
    ct = int(input("Nhập số đĩa: "))
    SapXep(ct, dau, giua, cuoi)

if __name__ == "__main__":
    main()