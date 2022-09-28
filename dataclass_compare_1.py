
class OreClass:
    def __init__(self, name:str, age:int = 30):
        self.name = name
        self.age = age

ore = OreClass(name="Ore")
print(ore.name)
print(ore.age)

