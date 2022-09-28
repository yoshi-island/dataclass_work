from dataclasses import dataclass

@dataclass
class OreClass:
    name: str
    age: int = 30

ore = OreClass(name="Ore")
print(ore.name)
print(ore.age)

