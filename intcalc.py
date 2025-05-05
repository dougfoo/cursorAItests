'''
Given an integer n, return an array of n unique integers that sum to 0.

For example:
n=3 -> [-1,0,1]  
n=5 -> [-2,-1,0,1,2]
'''
from typing import List

'''
Design:
For an input n, generate n unique integers that sum to 0 by:
1. For n=1, return [0]
2. For n>1:
   - Add pairs of positive and negative integers from 1 to n//2 
   - If n is odd, append 0 at the end
   
Time Complexity: O(n) - we iterate from 1 to n/2 once
Space Complexity: O(n) - we store n integers in the result array
'''

def sumZero(n: int) -> List[int]:
    if (n == 1):
        return [0]

    res = []
    for i in range(1, (n//2)+1):
        res.append(i)
        res.append(-i)

    if (n % 2 != 0):
        res.append(0)        

    return res


def main():
    test_cases = [1, 2, 3, 4, 5, 6, 7, 100, 101]
    
    for n in test_cases:
        result = sumZero(n)
        total = sum(result)
        unique = len(set(result)) == len(result)
        
        print(f"Input: n = {n}")
        print(f"Output: {result}")
        print("Status: " + ("PASS" if total == 0 and len(result) == n and unique else "FAIL"))
        print()

if __name__ == "__main__":
    main()


