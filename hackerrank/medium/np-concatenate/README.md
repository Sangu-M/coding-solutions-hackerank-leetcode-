# Python If-Else

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

[__Concatenate__](http://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html)  

Two or more arrays can be concatenated together using the *concatenate* function with a
tuple of the arrays to be joined:

    import numpy

    array_1 = numpy.array([1,2,3])
    array_2 = numpy.array([4,5,6])
    array_3 = numpy.array([7,8,9])

    print numpy.concatenate((array_1, array_2, array_3))	
    
    #Output
    [1 2 3 4 5 6 7 8 9]
    
If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.

    import numpy

    array_1 = numpy.array([[1,2,3],[0,0,0]])
    array_2 = numpy.array([[0,0,0],[7,8,9]])

    print numpy.concatenate((array_1, array_2), axis = 1)	
    
    #Output
    [[1 2 3 0 0 0]
     [0 0 0 7 8 9]]    
     
---
__Task__  

You are given two integer arrays of size $ N $X$ P $ and $ M $X$ P$ ($N$ & $ M $ are rows, and $P$ is the column).  Your task is to *concatenate* the arrays along axis $0$.

**Input Format**

The first line contains space separated integers $N$, $M$ and $P$.  
The next $N$ lines contains the space separated elements of the $P$ columns.  
After that, the next $M$ lines contains the space separated elements of the $P$ columns.


**Output Format**

Print the concatenated array of size $(N+M) $X$ P$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-04T15:55:15.142Z  

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

[View on HackerRank](https://www.hackerrank.com/challenges/np-concatenate/problem)