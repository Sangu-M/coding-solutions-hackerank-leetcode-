if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        parts=input().split()
        cmd=parts[0]
        
        if cmd=="insert":
            arr.insert(int(parts[1]),int(parts[2]))
        elif cmd=="print":
            print(arr)
        elif cmd=="remove":
            arr.remove(int(parts[1]))
        elif cmd=="append":
            arr.append(int(parts[1]))
        elif cmd=="sort":
            arr.sort()
        elif cmd=="pop":
            arr.pop()
        elif cmd=="reverse":
            arr.reverse()
                
