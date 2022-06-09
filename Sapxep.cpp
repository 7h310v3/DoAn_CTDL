#include <stdio.h>

#define MAX 100

//Nhap gioi han mang
void  NhapGH( int &n)
{
	do{
		printf("Nhap GH: ");
		scanf("%d", &n);
		if (n < 0 || n >= 100)
			printf("NHAP SAI, NHAP LAI!\n");
	} while (n < 0 || n >= 100);
}

//Nhap mang
void NhapDS(int n, int arr[])
{
    for (int i = 0; i < n; i++)
    {
        printf("Nhap Arr[%d] = ", i);
        scanf("%d", &arr[i]);
    }

}

//Xuat mang
void XuatDS(int n, int arr[])
{
    for (int i = 0; i < n; i++)
    {
        printf("Arr[%d] =  %d\t", i,arr[i]);
    }

}

//Hàm đổi
void Swap(int &x, int &y)
{
    int temp = x;
    x = y;
    y = temp;
}

//SelectionSort
void SelectionSort(int n, int arr[])
{
    int temp;
    for (int i = 0; i < n; i++)
    {
        for (int j = n-1; j > i; j--)
        {
            if (arr[j] < arr[j - 1])
            {
                Swap(arr[j], arr[j-1]);
            }
            
        }
        
    }

    printf("Mang sau khi sap xep: ");
    XuatDS(n, arr);
}

//InsertionSort
void insertionSort(int arr[], int n)
{
   int i, key, j;
   for (i = 1; i < n; i++)
   {
       key = arr[i];
       j = i-1;
  
       while (j >= 0 && arr[j] > key)
       {
           arr[j+1] = arr[j];
           j = j-1;
       }
       arr[j+1] = key;
   }
}

//BubbleSort
void bubbleSort(int arr[], int n)
{
    int i, j;
    bool haveswap = false;
    for (i = 0; i < n-1; i++){
    // i phần tử cuối cùng đã được sắp xếp
        haveswap = false;
        for (j = 0; j < n-i-1; j++){
            if (arr[j] > arr[j+1]){
                Swap(arr[j], arr[j+1]);
                haveswap = true; // Kiểm tra lần lặp này có Swap không
            }
        }
        // Nếu không có Swap nào được thực hiện => mảng đã sắp xếp. Không cần lặp thêm
        if(haveswap == false){
            break;
        }
    }
}


int main()
{
    int n, x, arr[MAX];

    NhapGH(n);

    NhapDS(n, arr);

    printf("Danh sach vua nhap la: \n");
    XuatDS(n, arr);
    printf("\n");

    //SelectionSortp(n, arr);
    
    //insertionSort(arr, n);
    
    bubbleSort(arr, n);
    printf("Danh sach sau khi sap xep: \n");
    XuatDS(n, arr);

    return 0;
}