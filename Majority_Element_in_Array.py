# Find the Majority Element in an Array: Boyer–Moore Voting Algorithm
def majarity_element_array(array):
    if not array:
        return None
    
    candidate = None
    element_count = 0
    for num in array:
        if element_count == 0:
            candidate = num
        element_count += (-1 if candidate==num else 1)
    
    if array.count(candidate)>(len(array)/2):
        return candidate
    return None

array_data_1 = [3, 3, 4, 2, 3, 3, 3]
array_data_2 = [1, 1, 1, 2, 2, 2]
array_data_3 = []
array_data_4 = [3]
array_data_5 = [0, 0, 0, 0, 0, 0, 0]


print("Case 1: Majority Element in array: ", majarity_element_array(array_data_1))
print("Case 2: Majority Element in array: ", majarity_element_array(array_data_2))
print("Case 3: Majority Element in array: ", majarity_element_array(array_data_3))
print("Case 4: Majority Element in array: ", majarity_element_array(array_data_4))
print("Case 5: Majority Element in array: ", majarity_element_array(array_data_5))

# Time Complexity: O(n)
# Space Complexity: O(1)