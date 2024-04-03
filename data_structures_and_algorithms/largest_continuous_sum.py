def large_cont_sum(arr):

    if len(arr)==0: # edge case
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:

        current_sum = max(current_sum,num)

        max_sum = max(current_sum,max_sum)
    
    return max_sum

print(large_cont_sum([1,2,4,2,4,5,-10,3,1]))