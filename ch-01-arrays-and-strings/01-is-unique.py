# Determine whether or not a given string contains no duplicate characters.

def contains_no_duplicates(string):
  letters = {}
  for letter in string:
    if letter in letters:
      return False
    letters[letter] = True
  return True

# First clarify what is the encoding, is it ASCII or Unicode. Is the string in ASCII or Unicode

#By dictionary
def is_unique_dict(string):
  temp = {}
  for i in string:
    temp[i]=temp.get(i,0)+1
  for f in temp.values():
    if f >1:
      return False
  return True

#By array
###Time: O(n) where n is the length of string, however it could be said to be O(1),
#since n will be smaller than 128.
###Space: O(1)

def is_unique_list(string):
  #assume that we are working with 256 (0-255) ASCII
  #create an array of boolean values
  ref = [False]*128
  #it is impossible to create unique strings longer than the length
  #of possible base
  if len(string)>256:
    return False
  for i in string:
    val = ord(i)
    if ref[val]:
      return False
    ref[val]=True
  return True
  
#By bit vector
#TODO

  


if __name__ == "__main__":
  t1="hello"
  t2="world"
  print('dict')
  print(is_unique_dict(t1))
  print(is_unique_dict(t2))
  print('list')
  print(is_unique_list(t1))
  print(is_unique_list(t2))
