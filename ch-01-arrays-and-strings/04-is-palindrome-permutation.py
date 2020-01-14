# Determine whether or not a string is a permutation of a palindrome,
# ignoring spaces.

# First define what is the permutation of a palindrome, which must have either
# even size with all characters of even counts or odd size with exactly one odd character
# and the rest count is even

# By dictionary
### Time: O(n) where n is the length of string
def is_palindrome_permutation_1(string):
  ref = {}
  for i in "".join(string.split()): # building a char freq dict
    ref[i] = ref.get(i,0)+1
  odd_ct = 0
  for c in ref.values(): # check if there is more than one odd character
    if c%2!=0:
      odd_ct+=1
  if odd_ct>1:
    return False
  return True

#TODO bit vector

if __name__ == "__main__":
  t1 = "tact coa"
  t2 = "WhattahW"
  print(f"Test case 1:{t1}")
  print(is_palindrome_permutation_1(t1))
  print(f"Test case 2:{t2}")
  print(is_palindrome_permutation_1(t2))