class Person:
   def __init__(self, name):
       self.name = name

   def talk(self):
        print(f"Hi, I am {self.name}")


li = Person("Lily Lee")
li.talk()

bob = Person("Bob Smith")
bob.talk()