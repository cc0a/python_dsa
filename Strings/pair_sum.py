def pair_sum(arr, k):

    if len(arr)<2:
        return

    seen = set()
    output = set()

    for num in arr:

        target = k - num # target = 5

        if target not in seen: # No, Yes
            seen.add(num) # 2

        else:
            output.add(((min(num, target)), max(num, target))) # SECOND PASS... min 5, 2 - max 5, 2

            print('\n'.join(map(str, list(output)))) # Second pass (2, 5)

print(pair_sum([2, 5, 4, 6], 7))
