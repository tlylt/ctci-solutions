# Compress a string made up of letters by replacing each substring containing
# a single type of letter by that letter followed by the count if the result
# is shorter than the original.

# By two pointers
### Time: O(n)
def compress_1(string):
  back=0
  front=0
  ref = []
  while back <len(string) and front <= len(string):
    if front==len(string) or string[front]!=string[back]: # terminate if pointer reaches the end or no longer identifical
      ref.append(string[back]) # append the char
      ref.append(str(front-back)) # append the freq
      back=front # update the back pointer to the new char
    front+=1 # updates the front pointer
  compressed = "".join(ref)
  if len(compressed)< len(string): # compare length of compressed vs original
    return compressed
  else:
    return string

if __name__ == "__main__":
  t1="aabcccccaaa"
  t2="abcd"
  print(f'Test case 1:{t1}')
  print(compress_1(t1))
  print(f'Test case 2:{t2}')
  print(compress_1(t2))
