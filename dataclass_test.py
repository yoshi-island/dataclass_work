from dataclasses import dataclass
from datetime import date
from math import floor

@dataclass(frozen=True)
class OreClass:
    name: str
    gender: str
    birthday: date

    def __post_init__(self):
        print("post_init")
        if self.gender not in ["male", "female", "unknown"]:
            raise ValueError("gender is no valid")

    @property
    def age(self) -> int:
        age_timedelta  = date.today() - self.birthday
        return floor(age_timedelta.days / 365 )


ore = OreClass(name="Ore", gender="male", birthday=date(1990,7,2))
print(ore)
print(f"name: {ore.name}")
print(f"age: {ore.age}")

omae = OreClass(name="Omae", gender="female", birthday=date(1985,6,20))
print(omae)
print(f"name: {omae.name}")
print(f"age: {omae.age}")
