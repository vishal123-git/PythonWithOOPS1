class student:
      def __init__(self, name, age):
            self.name = name
            self.age = age

      def read(self):
            print(self.name)
            print(self.age)


s1 = student("kprit", 21)
s2 = student("age", 31)
s1.read()
s2.read()