def mergeTwoLists(list1, list2):
    i, j = 0, 0
    merged_list = []
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

# Test cases
print(mergeTwoLists([1, 2, 4], [1, 3, 4]))  
print(mergeTwoLists([], []))                
print(mergeTwoLists([], [0]))               
print(mergeTwoLists([], [1, 2, 3, 4, 5]))   
print(mergeTwoLists([0, 1, 9], [3, 4, 5]))  
