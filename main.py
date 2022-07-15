def distinct_substrings(s):
  l = 3

  ptr1 =0
  ptr2 = 3
  count = 0

  while ptr2 <= len(s):
    curr = s[ptr1:ptr2]
    print('Current String', curr)

    string_set = set(curr)
    print(str(string_set))

    if len(set(curr)) == 3:
      count += 1

    ptr1+=1
    ptr2+=1
    
  return count
      
# Test Cases
s = "aababcabc"
print("Input: ", s)
print("Output: ", distinct_substrings(s))

s = "xyzzaz"
print("\nInput: ", s)
print("Output: ", distinct_substrings(s))
