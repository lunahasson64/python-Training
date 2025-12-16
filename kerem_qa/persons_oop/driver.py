from kerem_qa.persons_oop.person import person


class driver(person):
    def __init__(self,license_level):
        self.license_level = license_level

    def get_license_level(self):
        print(f"{self.license_level}")
