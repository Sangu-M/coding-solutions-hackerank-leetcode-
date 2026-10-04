if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s =  set(arr)
    arr1 = list(s)
    arr1.sort()
    print(arr1[-2])
        
