# Determine whether or not one string is a permutation of another.

#Ask if string is case sensitive and if whitespace is significant

# By sorting
### Time: O(nlgn) where n is the length of the longer string
### Space: O(1) if it is inplace sorting
def is_permutation_1(str1,str2):
  if len(str1)!=len(str2): # fail fast if length is not equal
    return False
  for a,b in zip(sorted(str1),sorted(str2)): # sort and compare char at the same index
    if a!=b:
      return False
  return True

# By dictionary
### Time: O(n)
### Space: O(n)
def is_permutation_2(str1,str2):
  if len(str1)!=len(str2): # fail fast
    return False
  ref={}
  for i in str1:
    ref[i] = ref.get(i,0) + 1 # store char frequency in str1 into dictionary 
  for c in str2:
    if c not in ref:
      return False
    ref[c] = ref[c]-1
  return not sum(ref.values())

# By array
### Time: O(n)
### Space: O(1)
def is_permutation_3(str1,str2):
  if len(str1)!=len(str2): #fail fast
    return False
  ref=[0]*128 #assuming ASCII character set
  for i in str1:
    ref[ord(i)] +=1
  for c in str2:
    if ref[ord(c)]<=0:
      return False
    ref[ord(c)] -=1
  return True

if __name__ == "__main__":
  s1="hello"
  b1="world"
  a2="John"
  c2="ohnJ"
  print(f"Test case 1:{s1,b1}")
  print(is_permutation_1(s1,b1))
  print(is_permutation_2(s1,b1))
  print(is_permutation_3(s1,b1))
  print(f"Test case 2:{a2,c2}")
  print(is_permutation_1(a2,c2))
  print(is_permutation_2(a2,c2))
  print(is_permutation_3(a2,c2))