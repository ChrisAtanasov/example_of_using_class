class Person:

    def __init__(self,years,hair,height):
        self.years = years
        self.hair = hair
        self.height = height

    def data(self):

      return f'He is a {self.years}  years old whith {self.hair} and {self.height}cm tall.'


human_profile = Person('100','bold','1.90')

print(human_profile.data())
