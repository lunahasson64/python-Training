class person:
    def __init__(self,age):
        self.age = age


    def age_calculator(self,age):
        is_young = False
        if age >= 18:
            print("You are more than 18")
            is_young =False
        else:
            print("You are less than 18")
            is_young =True

        return is_young


