name = input("What is your name? ")
student_grade = input("What grade are you in? ")


# Input classes into an array
def inputCourses(num_of_classes):
    arr_classes = []

    for number in range(num_of_classes):
        classes = input(f"What is your class {number + 1} name? ")
        arr_classes.append(classes)

    return arr_classes


# Input grades based on the class taken from a list
def inputGrades(arr_classes):
    arr_grades = []
    grades = ''

    for i in range(len(arr_classes)):
        grades = input(f"What is your letter grade in {arr_classes[i]}? ").upper()
        arr_grades.append(grades)

    return arr_grades


# Calculating the GPA of the student based on what grades they got
def gpa_score(arr_grades, num_of_classes):
    total = 0

    for grade in arr_grades:
        if grade == 'A':
            total += 4
        elif grade == 'B':
            total += 3
        elif grade == 'C':
            total += 2
        elif grade == 'D':
            total += 1

    gpa = round(total / num_of_classes, 2)

    return gpa


# Checks whether or not the student got an F, then returns an eligibile boolean value
def isEligible(arr_grades):
    eligible = True

    for grade in arr_grades:
        if grade == "F":
            eligible = False

    return eligible


# Determines what honor rank the student gets placed in based on their GPA
def honorRank(gpa, arr_grades):
    placement = ["High Honor Roll", "'A' Honor Roll", "'B' Honor Roll",
                 "Sorry you are ineligible because you got an F for one of your classes",
                 "Sorry your grades did not qualify you for any of the honor positions"]

    if isEligible(arr_grades):
        if gpa > 3.8:
            placement = f"Congrats you made the {placement[0]}"
        elif gpa >= 3.5:
            placement = f"Congrats you made the {placement[1]}"
        elif gpa >= 3.25:
            placement = f"Congrats you made the {placement[2]}"
        else:
            placement = placement[4]
    else:
        placement = "Since you got an F in one of your classes you are ineligible to be placed in any honor ranks."

    return placement


# Prints out the final report card and placement statement
def finalReportCard(num_of_classes, arr_classes, arr_grades, gpa, placement):
    print("\tReport Card")
    for info in range(num_of_classes):
        print(f"{arr_classes[info]}\t{arr_grades[info]}")
    print()
    print(name)
    print(f"Grade {student_grade}")
    print(f"Your gpa is {gpa}")
    print(placement)
