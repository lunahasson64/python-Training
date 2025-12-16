from kerem_qa.persons_oop.driver import driver
from kerem_qa.persons_oop.person import person
from kerem_qa.persons_oop.student import student

student_1 = student("john","doe1")
student_2 = student("mike","doe2")
student_3 = student("lona")




avg1 = student_1.get_average_score([77,87,98,67,80])
avg2 = student_2.get_average_score([77,87,99,88,77,97])
student_1.get_average_score([56,88,66,45,99,80])  #example
is_young1 = student_1.age_calculator(66)
is_young2 = student_2.age_calculator(77)
driver_1 = driver("B")
driver_2 = driver("C")

driver_1.get_license_level()
driver_2.get_license_level()

if avg1 > avg2:
    print("avg 1 higher than avg 2")
elif avg1 < avg2:
    print("avg 2 higher than avg 1")




