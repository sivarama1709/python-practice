class Animals:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))
Animals.walk('dog')
Animals.walk('goat')