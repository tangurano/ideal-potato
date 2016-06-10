
class Person:

  def __init__(self, name):
  	self.name = name

  def __str__(self):
  	return self.name

def introduce(p):
  # print adds an extra space?
  print "Hello everyone, this is", p


#print introduce("Charles")
#print introduce(Person("Charles"))

names = ["Arya", "Sansa", "Ned"]
contacts = [Person(name) for name in names]
#printing array doesn't use __str__ on elements?
# print contacts
for c in contacts:
  print c