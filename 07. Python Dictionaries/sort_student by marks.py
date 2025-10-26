students = [("Rafi", 89), ("Sumi", 95), ("Hasan", 90), ("Nila", 75), ("Anik", 98)]

students_dict = dict(students)

sorted_student = sorted(students_dict.items(), key= lambda x: x[1], reverse= True )

top3 = sorted_student[:3]

for name,mark in top3:
    print(f"{name} - {mark}")