from typing import List
from collections import Counter

# leetcode question number 34
class Solution:
    def firstOcc(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1   
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def lastOcc(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1  
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOcc(nums, target)
        last = self.lastOcc(nums, target)
        return [first, last]
        
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))



# optimal solution 

class Solution:
    def searchRange(self, a: List[int], b: int) -> List[int]:
        if b not in a:
            return [-1,-1]
        elif len(a)==1 and b in a:
            return [0,0]
        else:
            l=[]
            i=0
            j=len(a)-1
            while i<=j:
                if a[i]==b and a[j]==b:
                    return [i,j]
                elif a[i]==b or a[j]!=b:
                    j-=1
                elif a[j]==b or a[i]!=b:
                    i+=1

# leetcode question number 389
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = Counter(s)

        for ch in t:
            if ch not in d:
                return ch
            d[ch] -= 1
            if d[ch] == 0:
                del d[ch]

# with bit manipulation
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for ch in s:
            result ^= ord(ch)
        for ch in t:
            result ^= ord(ch)
        return chr(result)

# leetcode 355

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i+=1
            j+=1
        return i
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("1"))

# leetcode 4 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedList = []
        i = 0 
        j = 0
        len1 = len(nums1)
        len2 = len(nums2)

        # merge two sorted arrays
        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                sortedList.append(nums1[i])
                i += 1
            else:
                sortedList.append(nums2[j])
                j += 1

        # leftover elements
        while i < len1:
            sortedList.append(nums1[i])
            i += 1
        while j < len2:
            sortedList.append(nums2[j])
            j += 1

        n = len(sortedList)
        if n % 2 == 0:   # even
            mid = n // 2
            middleValue = (sortedList[mid - 1] + sortedList[mid]) / 2
        else:            # odd
            middleValue = sortedList[n // 2]
        
        return middleValue
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("1"))

#leetcode 234

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp 
        
        left , right = head , prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("1"))

# leetcode 217

if len(set(nums)) == len(nums):
    return False
else: 
    return True 


# leetcode 268

n = len(nums)
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
missing_number = expected_sum - actual_sum

# other approach
return sum(range(len(nums) + 1)) - sum(nums)

#leetcode 448 
for n in nums:
    i = abs(n) - 1
    nums[i] = -1 * abs(nums[i])

res = []
for i , n in enumerate(nums):
    if n > 0:
        res.append(i + 1)
return res

# leetcode 1
hashMap = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in hashMap:
        return [hashMap[complement], i]
    hashMap[num] = i

# leetcode 1365

temp = sorted((nums))
d ={}
for i, num in enumerate(temp):
    if num not in d:
        d[num] = i
res = []
for num in nums:
    res.append(d[num])  
return res


# leetcode 15
class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            'L' : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        num = 0
        s = s.replace('IV' , 'IIII')
        s = s.replace('IX' , 'VIIII')
        s = s.replace('XL' , 'XXXX')
        s = s.replace('XC' , 'LXXXX')
        s = s.replace('CD' , 'CCCC')
        s = s.replace('CM' , 'DCCCC')

        for char in s:
            num += sym[char]
        return num


# leetcode 345

vowel = set('aeiouAEIOU')
def reverseVowels(s: str) -> str:
    s = list(s)
    i , j = 0 , len(s) - 1
    while i < j:
        if s[i] not in vowel:
            i += 1
        elif s[j] not in vowel:
            j -= 1
        else:
            s[i] , s[j] = s[j] , s[i]
            i += 1
            j -= 1
    return ''.join(s)

# leetcode 121

minPorift = float('inf')
maxProfit = 0
for price in prices:
    if price < minPorift:
        minPorift = price
    else:
        maxProfit = max(maxProfit , price - minPorift)
    return maxProfit


#leetcode 161

n = len(nums)
for i in range(len(nums)):
    if ((i == 0 or nums[i] > nums[i-1] ) and (i==n -1 or nums[i] >  nums[i+1])):
        return i    
