# Problem 5 – Find the Majority Element in an Array

###  Problem Description
Given an array of integers, find the **majority element**, i.e., the element that appears **more than ⌊n/2⌋ times** in the array.  
If no such element exists, return `None`.

The array can contain both positive and negative integers.  
Your solution should be optimized for **time and space**.

---

###  Example

**Example 1**

---
Input: [3, 3, 4, 2, 3, 3, 3]
Output: 3
Explanation: 3 appears 5 times in a list of length 7 (> 7/2)

---


**Example 2**

---

Input: [1, 1, 1, 2, 2, 2]
Output: None
Explanation: No element appears more than n/2 times.

---


---

### ⚙️ Approach 1 — Brute Force (O(n²))
You can check each element’s frequency using `array.count(num)` inside a loop.  
However, this results in a **quadratic time complexity**, which is not efficient for large arrays.

---

###  Approach 2 — Boyer–Moore Voting Algorithm (O(n) Time, O(1) Space)
This is an **optimal** approach to finding the majority element.

**Steps:**
1. **Find a candidate** that could be the majority element.
2. **Verify** if that candidate actually appears more than n/2 times.

**Algorithm logic:**
- Keep a `candidate` and a `count`.
- Iterate through the array:
  - If `count == 0`, set the current number as `candidate`.
  - If current number equals `candidate`, increment `count`.
  - Otherwise, decrement `count`.
- After one pass, `candidate` holds the potential majority.
- Verify it by counting its occurrences once.

---

###  Code Implementation

```python
def majority_element(array):
    if not array:
        return None
    
    candidate = None
    e_count = 0

    # Step 1: Find the candidate
    for num in array:
        if count == 0:
            candidate = num
        e_count += (-1 if candidate==num else -1)
    
    # Step 2: Verify the candidate
    if array.count(candidate)>(len(array)/2):
        return candidate
    return None

# Test Cases
print(majority_element([3, 3, 4, 2, 3, 3, 3]))  # Output: 3
print(majority_element([1, 1, 1, 2, 2, 2]))    # Output: None
print(majority_element([]))                     # Output: None
print(majority_element([3]))                    # Output: 3

```

### Time and Space Complexity

---

| Step | Operation | Time | Space |
|--------|--------|
| `Candidate Selection` | `Single traversal` | `O(n)` | `O(1)` |
| `Verification` | `Counting candidate` | `O(n)` | `O(1)` |
| `Total` | `O(n)` | `O(1)` |

---