#inheritance

class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

  #Child class

class Child(Parent):
      def greeting(self):
          return f"my name is {self.name},i am {self.age} years old"
      #instance
child=Child("Susan",10)
print(child.greeting())
