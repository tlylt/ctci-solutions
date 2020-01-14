# Determine whether or not a given string contains no duplicate characters.

# First clarify with interviewer what is the encoding, is it ASCII or Unicode?

# By dictionary
### Time: O(n) where n is the length of string
### Space: O(n)

def is_unique_1(string):
  ref = {} # reference dictionary
  for letter in string:
    if letter in ref: # if letter is already added into dictionary
      return False
    ref[letter] = None # add letter into dictionary
  return True


# By array
### Time: O(n) where n is the length of string, however it could be said to be O(1),
#since n will always be smaller than 128 and loop will never iterate more than 128 times
### Space: O(1)

def is_unique_2(string):
  #assuming that we are working with ASCII,
  #create an array of boolean values
  ref = [False]*128
  #it is impossible to create unique strings longer than the length
  #of possible unique character set
  if len(string)>128:
    return False
  for i in string:
    val = ord(i) # return unicode point of a character
    if ref[val]: # if the character has been set as true
      return False
    ref[val]=True
  return True 

# By bit vector
#TODO

if __name__ == "__main__":
  t1="hello"
  t2="world"
  print(f"Test case 1:{t1}")
  print(is_unique_1(t1))
  print(is_unique_2(t1))
  print(f"Test case 2:{t2}")
  print(is_unique_1(t2))
  print(is_unique_2(t2))

