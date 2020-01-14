# Determine whether the edit distance between two strings is less than 2.

# Replacement: the strings are only different in one place
# Insertion: the strings are identical except for a shift at some point
# Removal: inverse of insertion
# Length of string will indicate which check to perform

# By checking separately for Replace and insert/removal 
### Time: O(n)
def one_away_1(str1, str2):
  if len(str1) == len(str2):
    return oneEditReplace(str1,str2)
  elif len(str1) + 1 == len(str2):
    return oneEditInsert(str1,str2)
  elif len(str1) - 1 == len(str2):
    return oneEditInsert(str2,str1)
  else:
    return False

def oneEditReplace(str1,str2):
  diff = False
  pt = 0
  while pt < len(str1):
    if str1[pt] != str2[pt]:
      if diff:
        return False
      diff = True
    pt+=1
  return True

def oneEditInsert(str1,str2):
  pt1 = 0
  pt2 = 0
  while pt1<len(str1) and pt2<len(str2):
    if str1[pt1] != str2[pt2]:
      if pt1 != pt2: # if pointer 2 has already been moved once
        return False
      pt2+=1
    else:
      pt1+=1
      pt2+=1
  return True

# By combining the checks together
def one_away_2(str1,str2):
  len1, len2 =len(str1), len(str2)
  dif = abs(len1-len2)
  if dif>1:
    return False
  if len1 > len2: 
    longer, shorter = str1, str2
  else:
    longer, shorter = str2, str1
  pt1=0
  pt2=0
  edit = False
  while pt1<len(longer) and pt2 <len(shorter):
    if longer[pt1]!=shorter[pt2]:
      if edit: # checks for replacement
        return False
      edit = True
      if dif: # checks for insertion/removal
        pt1+=1
      else:
        pt1+=1
        pt2+=1  
    else:
      pt1+=1
      pt2+=1
  return True

if __name__ == "__main__":
  t1 = "pales"
  x1 = "pale"
  t2 = "bale"
  x2 = "pale"
  print(f"Test case 1:{t1,x1}")
  print(one_away_1(t1,x1))
  print(one_away_2(t1,x1))
  print(f"Test case 2:{t2,x2}")
  print(one_away_1(t2,x2))
  print(one_away_2(t2,x2))