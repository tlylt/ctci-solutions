# Implement a cat and dog queue for an animal shelter.
# able to perform return oldest animal, oldest cat, oldest dog according to time of arrival to shelter

class AnimalShelterQueue():
  def __init__(self):
    self.cats = []
    self.dogs = []
    self.order = 0
  
  def enqueue(self,animal):
    animal.order = self.order
    self.order+=1 # added order so which ever has the smallest order number is the oldest
    if animal.__class__ == Cat_1:
      self.cats.append(animal)
    else:
      self.dogs.append(animal)
  
  def dequeueAny(self):
    if not self.dogs and not self.cats:
      return None
    elif not self.dogs:
      cat = self.cats[0]
      self.cats=self.cats[1:]
      return cat
    elif not self.cats:
      dog = self.dogs[0]
      self.dogs =self.dogs[1:]
      return dog
    else:
      if self.cats[0].order < self.dogs[0].order: # check for oldest animal
        cat = self.cats[0]
        self.cats = self.cats[1:]
        return cat
      dog = self.dogs[0]
      self.dogs= self.dogs[1:]
      return dog
  def dequeueCat(self):
    if self.cats:
      cat = self.cats[0]
      self.cats = self.cats[1:]
      return cat
    return None
  def dequeueDog(self):
    if self.dogs:
      dog = self.dogs[0]
      self.dogs = self.dogs[1:]
      return dog
    return None

class Animal_1():
  def __init__(self,name):
    self.name = name
    self.order = None

class Cat_1(Animal_1):
  pass
class Dog_1(Animal_1):
  pass

##############################################################

class AnimalShelter():
  def __init__(self):
    self.cats, self.dogs = [], []
  
  def enqueue(self, animal):
    if animal.__class__ == Cat: self.cats.append(animal)
    else:                       self.dogs.append(animal)
  
  def dequeueAny(self):
    if len(self.cats): return self.dequeueCat()
    return self.dequeueDog()
  
  def dequeueCat(self):
    if len(self.cats) == 0: return None
    cat = self.cats[0]
    self.cats = self.cats[1:]
    return cat
    
  def dequeueDog(self):
    if len(self.dogs) == 0: return None
    dog = self.dogs[0]
    self.dogs = self.dogs[1:]
    return dog

class Animal():
  def __init__(self, name):
    self.name = name
  
  def __str__(self):
    return self.name

class Cat(Animal): pass
class Dog(Animal): pass

import unittest

class Test(unittest.TestCase):
  def test_animal_shelter(self):
    shelter = AnimalShelter()
    shelter.enqueue(Cat("Hanzack"))
    shelter.enqueue(Dog("Pluto"))
    shelter.enqueue(Cat("Garfield"))
    shelter.enqueue(Cat("Tony"))
    shelter.enqueue(Dog("Clifford"))
    shelter.enqueue(Dog("Blue"))
    self.assertEqual(str(shelter.dequeueAny()), "Hanzack")
    self.assertEqual(str(shelter.dequeueAny()), "Garfield")
    self.assertEqual(str(shelter.dequeueDog()), "Pluto")
    self.assertEqual(str(shelter.dequeueDog()), "Clifford")
    self.assertEqual(str(shelter.dequeueCat()), "Tony")
    self.assertEqual(str(shelter.dequeueCat()), "None")
    self.assertEqual(str(shelter.dequeueAny()), "Blue")
    self.assertEqual(str(shelter.dequeueAny()), "None")

if __name__ == "__main__":
  unittest.main()

