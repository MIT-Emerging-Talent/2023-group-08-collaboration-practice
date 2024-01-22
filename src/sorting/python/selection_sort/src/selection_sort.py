def selectionsort_v1(list):
    # traverse through all array elements 
    for i in range(len(list)):

        # find the minimum element in the remaining unsorted array 
        min_idx = i 

        # iterate through the remaining elements to find the minimum
        for j in range(i + 1, len(list)):
            # Compare the current minimum with the current element
            if list[min_idx] > list[j]:
                # Update the index of the minimum element if a smaller element is found
                min_idx = j 

        # Swap the found minimum element with the first element         
        list[i], list[min_idx] = list[min_idx], list[i]

    # Return the sorted array
    return list