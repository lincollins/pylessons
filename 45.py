# In here, we deal with differences between a class and an object.
# Before then, we're supposed to research about other peoples code on the internet.
# Obviously that would be in python language as well.
# The idea is to be able to work on other programemrs code as well as ours with ease
# Fecth some different dtyles of coding, some errors they amde among others.
# As of writing this comment, we havn't though :)
# But we shall. Even our own codes that seems to have given us problems needs to be worked upon.
# Unfortunatley though, we'vnt found out any yet.

# Boss Dawn, a reminder please.
# We use 'is-a' when the object is related to the class in a class relationship
# We use 'has-a' when the object is related to the class only because it has been referenced
# Remember, is-a is the relationship between Fish and Salmon, while has-a is the relationship between Salmon and Gills.
# In the first exaamle as in Fish and Salmon: It exists because Salmon is a Fish. Class relationship
# In the second example, between Salmon and Gills, the assumpton is that all Gilly things are fish and type of fish is Salmon
# This types of relationships occur because it has been referenced.
# Lets try this example

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a class of Animal (yes, we say this becasue a Dog is a subset of a type of an Animal which is the relationship)

class Dog(Animal):

	def __init__(Self, name):
		## ??
		self.name = name

## Cat is-a class of Animal
class Cat(Animal):

	def __init__(self, name):
		## 
		self.name = name

## Person has-a class of pet (this is because Person and pet are only referenced in terms of a relationship)
class Person(object):

	def __init__(self, name):
		##??
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a class of Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a class of Super Employee. // Hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a class of salary
		self.salary = salary

## Fish is-a class of object
class Fish(object):
	pass

## Salmon is-a class of Fish
class Salmon(Fish):
	pass

## Halibut is-a class of Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan has-a class of Cat
satan = Cat("Satan")

## mary is-a class of Person
mary = Person("Mary")

## mary has-a clas of pet and is-a class of Satan
mary.pet = satan

## frank is-a class of Employee
frank = Employee("Frank", 120000)

## frank has-a class of pet and has-a class of rover
frank.pet = rover

## We do not write anything here becasue we don not know what flippr is
flipper.pet = rover

## Here, we do not know what crouse is. So we can not tell if its  'is-a' or 'has-a'
crouse = Salmon()

## hairy has-a class of Halibut
hairy = Halibut()

# Boss Dawn, when you're on the internet kindly research about the use of the is-a and has-a.
# Is it possible to use a Class as an Object
# And well what are multiple inheritance

# Do we've a thing like has-many and is-many?
# All these should be soorted out as soon as you can