# Replace spaces in the middle of a string with "%20" assuming the end of the 
# string contains twice as many spaces as are in the middle.

# By built-in function
def escape_spaces_1(string):
  return string.strip().replace(" ", "%20")

# By built-in function  
def escape_spaces_2(string):
  return "%20".join(string.split())

# By working backwards from the end
def escape_spaces_3(string):
  l = list(string) # using list as string is immutable
  pt1 = len(l)-1
  pt2 = pt1
  while l[pt1] ==" ": # moving the first pointer to the end of the string (non whitespace)
    pt1-=1
  while pt1>=0:
    if l[pt1] == " ": # start building the list by checking if it is space
      l[pt2] = "0"
      l[pt2-1] = "2"
      l[pt2-2] = "%"
      pt2-=3
      pt1-=1
    else:
      l[pt2] = l[pt1]
      pt2-=1
      pt1-=1
  return "".join(l)

if __name__ == "__main__":
  t1="hello you  "
  t2="world war three    "
  print(f"Test case 1:{t1}")
  print(escape_spaces_1(t1))
  print(escape_spaces_2(t1))
  print(escape_spaces_3(t1))
  print(f"Test case 2:{t2}")
  print(escape_spaces_1(t2))
  print(escape_spaces_2(t2))
  print(escape_spaces_3(t2))