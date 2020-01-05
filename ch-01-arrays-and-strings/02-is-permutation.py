# Determine whether or not one string is a permutation of another.

def is_permutation(str1, str2):
  counter = Counter()
  for letter in str1:
    counter[letter] += 1
  for letter in str2:
    if not letter in counter:
      return False
    counter[letter] -= 1
    if counter[letter] == 0:
      del counter[letter]
  return len(counter) == 0

class Counter(dict):
  def __missing__(self, key):
    return 0

#Ask if string is case sensitive and if whitespace is significant

#By sorting
def is_permutation_sort(str1,str2):
  if len(str1)!=len(str2):
    return False
  for a,b in zip(sorted(str1),sorted(str2)):
    if a!=b:
      return False
  return True

#By dictionary
def is_permutation_dict(str1,str2):
  if len(str1)!=len(str2):
    return False
  ref={}
  for i in str1:
    ref[i] = ref.get(i,0) + 1
  for c in str2:
    if c not in ref:
      return False
    ref[c] = ref[c]-1
  return not sum(ref.values())

#By array
def is_permutation_list(str1,str2):
  if len(str1)!=len(str2):
    return False
  #assuming ASCII
  ref=[0]*128
  for i in str1:
    ref[ord(i)] +=1
  for c in str2:
    if ref[ord(c)]<=0:
      return False
    ref[ord(c)] -=1
  return True

if __name__ == "__main__":
  import sys
  print(is_permutation(sys.argv[-2], sys.argv[-1]))
  print(is_permutation_dict(sys.argv[-2], sys.argv[-1]))
  print(is_permutation_sort(sys.argv[-2], sys.argv[-1]))
  print(is_permutation_list(sys.argv[-2], sys.argv[-1]))