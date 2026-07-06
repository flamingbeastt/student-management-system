class Student:
    def __init__(self,id):
        self.id = id
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.department = input("Enter your department: ")
        self.score = input("Enter your score: ")


class StudentManagement:
    def __init__(self):
        self.student = []
        pass
    def add_student(self):
        id = int(input("Enter student ID: "))
        with open("Student_details.txt") as f:
            line = f.readline()
            while line != "":
                if id == int(line.split(" ")[0]):
                    print("Student already exists")
                    break
                line = f.readline()
            else:
                student = Student(id)
                self.student.append(student)
                print("Student added successfully")
                print("")
                with open("Student_details.txt","a") as f:
                    f.write(f"\n{student.id} {student.name} {student.age} {student.department} {student.score}\n")

    def view_all_students(self):
        with open("Student_details.txt") as f:
            line = f.readline()
            i = 1
            while line != "":
                print(f"{i}] {line}")
                line = f.readline()
                i += 1

    def search_by_id(self):
        id = int(input("Enter student ID: "))
        with open("Student_details.txt") as f:
            line = f.readline()
            while line != "":
                if id == int(line.split(" ")[0]):
                    print("Student ID: ",line.split(" ")[0])
                    print("Student name: ",line.split(" ")[1])
                    print("Student age: ",line.split(" ")[2])
                    print("Student department: ",line.split(" ")[3])
                    print("Student score: ",line.split(" ")[4])
                    break
                line = f.readline()

            else:
                print("Student ID not registered")
                print("")
    
    def update_details(self):
        print('''        *** Update *** 
        [1] name
        [2] age
        [3] department
        [4] score
        ''')
        update = int(input("Enter choise: "))
        id = int(input("Enter student ID: "))
        list = []
        with open("Student_details.txt") as f:
            line = f.readline()
            while line != "":
                list.append(line)
                line = f.readline()
        with open("Student_details.txt", "w") as file:
            file.write("")
        if update == 1:
            with open("Student_details.txt","a") as f:
                for i in list:
                    if id == int(i.split(" ")[0]):
                        name = input("Update the name: ")
                        old_name = i.split(" ")[1]
                        list.append(i.replace(old_name,name))
                        list.remove(i)
                        for k in list:
                            f.write(k)
                        print("Name changed successfully")
                        print("Your old name was: ",old_name)
                        print("Your new name is: ",name)
                        break
                else:
                    print("Student ID not registered")
                    print("")
        if update == 2:
            with open("Student_details.txt","a") as f:
                for i in list:
                    if id == int(i.split(" ")[0]):
                        age = input("Update the age: ")
                        old_age = i.split(" ")[2]
                        list.append(i.replace(old_age,age))
                        list.remove(i)
                        for k in list:
                            f.write(k)
                        print("age changed successfully")
                        print("Your old age was: ",old_age)
                        print("Your new age is: ",age)
                        break
                else:
                    print("Student ID not registered")
                    print("")
        if update == 3:
            with open("Student_details.txt","a") as f:
                for i in list:
                    if id == int(i.split(" ")[0]):
                        department = input("Update the department: ")
                        old_department = i.split(" ")[3]
                        list.append(i.replace(old_department,department))
                        list.remove(i)
                        for k in list:
                            f.write(k)
                        print("department changed successfully")
                        print("Your old department was: ",old_department)
                        print("Your new department is: ",department)
                        break
                else:
                    print("Student ID not registered")
                    print("")
        if update == 4:
            with open("Student_details.txt","a") as f:
                for i in list:
                    if id == int(i.split(" ")[0]):
                        score = input("Update the score: ")
                        old_score = i.split(" ")[4]
                        list.append(i.replace(old_score,score))
                        list.remove(i)
                        for k in list:
                            f.write(k)
                        print("score changed successfully")
                        print("Your old score was: ",old_score)
                        print("Your new score is: ",score)
                        break
                else:
                    print("Student ID not registered")
                    print("")
    def delete_student(self):
        id = int(input("Enter student ID: "))
        list = []
        with open("Student_details.txt") as f:
            line = f.readline()
            while line != "":
                list.append(line)
                line = f.readline()
        with open("Student_details.txt", "w") as file:
            file.write("")
        with open("Student_details.txt","a") as f:
                for i in list:
                    if id == int(i.split(" ")[0]):
                        list.remove(i)
                        for k in list:
                            f.write(k)
                        print("Student removed successfully")
                        break
                else:
                    print("Student ID not registered")
                    print("")

print("Student Management System")
manager = StudentManagement()
work = 0
while work != 6:
    print('''        [1] add student
        [2] view all students
        [3] search by id
        [4] update details
        [5] delete a student
        [6] exit the program
    ''')
    work = int(input("Enter choise: "))
    if work == 1:
        manager.add_student()
    elif work == 2:
        manager.view_all_students()
    elif work == 3:
        manager.search_by_id()
    elif work == 4:
        manager.update_details()
    elif work == 5:
        manager.delete_student()
