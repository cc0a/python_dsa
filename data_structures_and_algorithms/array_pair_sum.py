# Given an integer array, output all the unique pairs tht sum up to
# a value of k

def pair_sum(arr,k):

    if len(arr)<2: # edge case
        return

    # sets to track pairs
    seen = set()
    output = set()

    for num in arr:

        target = k-num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num,target)), max(num,target))
    
    return len(output)