def anagram(s1,s2):

    s1 = s1.replace(' ','').lower() # remove spaces and replace w/no space
    s2 = s2.replace(' ','').lower() # remove spaces and replace w/no space

    if len(s1) != len(s2): # edge case, if the length of s1 and s2 are not equal, an anagram is impossible
        return False

    return sorted(s1) == sorted(s2) # finally we sort the contents of both strings and see if they are equal

print(anagram('cat','tac'))
