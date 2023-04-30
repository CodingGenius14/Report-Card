from reportCard_functions import *

# gets the number of classes a student is taking
num_of_classes = int(input("How many classes are you taking? "))

# call function to get courses name
classes_array = inputCourses(num_of_classes)

# call function to get grades corresponding to the correct classes
grades_array = inputGrades(classes_array)

# call function to calculate the GPA
final_gpa = gpa_score(grades_array, num_of_classes)

# call function to determine whether or not the student is eligibile for a honor placement
eligible = isEligible(grades_array)

# call function to determine the students final placement
final_honor_rank = honorRank(final_gpa, grades_array)

# call function to print out the final Report Card
finalReportCard(num_of_classes, classes_array, grades_array, final_gpa, final_honor_rank)

