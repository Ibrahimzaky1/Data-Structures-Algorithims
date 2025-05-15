
########################### LESSON 17 ###########################
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # Calculate midpoint first
    left = arr[:mid]     # Split into left and right
    right = arr[mid:]

    left = merge_sort(left)   # Recursively sort left
    right = merge_sort(right) # Recursively sort right

    return merge_two_sorted_lists(left, right)  # Merge the sorted halves

def merge_two_sorted_lists(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    while j < len_b:  # Fixed: use `j`, not `i`
        sorted_list.append(b[j])
        j += 1

    return sorted_list

if __name__ == '__main__':
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    print(merge_sort(arr))









def merge_sort(elements, key, descending=False):
    size = len(elements)

    if size == 1:
        return elements

    left_list = merge_sort(elements[0:size//2], key, descending)
    right_list = merge_sort(elements[size//2:], key, descending)
    sorted_list = merge(left_list, right_list, key, descending)

    return sorted_list

    
def merge(left_list, right_list, key, descending=False):
    merged = []
    if descending:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] >= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    else:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] <= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    merged.extend(left_list)
    merged.extend(right_list)
    return merged

if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    sorted_list = merge_sort(elements, key='time_hours', descending=True)
    print(sorted_list)