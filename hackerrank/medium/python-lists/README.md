# Python If-Else

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Consider a list (`list = []`). You can perform the following commands:   

1. `insert i e`: Insert integer $e$ at position $i$.
2. `print`: Print the list.
3. `remove e`: Delete the first occurrence of integer $e$.
4. `append e`: Insert integer $e$ at the end of the list.  
5. `sort`: Sort the list.
6. `pop`: Pop the last element from the list.
7. `reverse`: Reverse the list.

Initialize your list and read in the value of $n$ followed by $n$ lines of commands where each command will be of the $7$ types listed above. Iterate through each command in order and perform the corresponding operation on your list.  

**Example**  
$N = 4$  
$\text{append 1}$  
$\text{append 2}$  
$\text{insert 1 3}$  
$\text{print}$   
</br >
</br >
   
- $\text{append 1}$: Append $1$ to the list, $arr = [1]$.  
- $\text{append 2}$: Append $2$ to the list, $arr = [1, 2]$.  
- $\text{insert 1 3}$: Insert $3$ at index $1$, $arr = [1, 3, 2]$.  
- $\text{print}$: Print the array.  
</br >
Output:
<pre>
[1, 3, 2]
</pre>

**Input Format**

The first line contains an integer, $n$, denoting the number of commands.	
Each line $i$ of the $n$ subsequent lines contains one of the commands described above.


**Constraints**

- The elements added to the list must be *integers*.

**Output Format**

For each command of type `print`, print the list on a new line.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-04T14:07:41.096Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if(n%2!=0):
    print("Weird")
elif(n>=2 and n<=5):
    print("Not Weird")
elif(n>=6 and n<=20):
    print("Weird")
else:
    print("Not Weird")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-lists/problem)