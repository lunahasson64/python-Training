from kerem_qa.persons_oop.person import person


class student(person):
    def __init__(self, first_name, last_name="doe"):
        self.first_name = first_name
        self.last_name = last_name

    def get_average_score(self,grades):
        sum = 0
        for grade in grades:
            sum = sum + grade
        avg = sum / len(grades)
        print(avg)
        return avg

    def comaare_score(self,avg1,avg2):
        sum = 0
        if avg1 > avg2:
            print("avg 1 higher than avg 2")
        elif avg1 < avg2:
            print("avg 2 higher than avg 1")