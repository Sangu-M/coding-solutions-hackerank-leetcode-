# Lists

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

**Task**  
Given an integer, $n$, and $n$ space-separated integers as input, create a tuple, $t$, of those $n$ integers. Then compute and print the result of $hash(t)$.  

**Note:** [hash()](https://docs.python.org/3/library/functions.html#hash) is one of the functions in the `__builtins__` module, so it need not be imported.  

**Input Format**

The first line contains an integer, $n$, denoting the number of elements in the tuple.	 			
The second line contains $n$ space-separated integers describing the elements in tuple $t$.  

**Constraints**

 

**Output Format**

Print the result of $hash(t)$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T16:54:15.856Z  

```py
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
                

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-tuples/problem)