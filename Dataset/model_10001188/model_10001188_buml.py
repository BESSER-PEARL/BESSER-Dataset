####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
Admin_Actor = Class(name="Admin_Actor")
Instructor_Actor = Class(name="Instructor_Actor")
Student_Actor = Class(name="Student_Actor")
Login_UseCase = Class(name="Login_UseCase")
Login_UseCase1 = Class(name="Login_UseCase1")
Login_UseCase2 = Class(name="Login_UseCase2")
Logout_UseCase = Class(name="Logout_UseCase")
Add_Student_UseCase = Class(name="Add_Student_UseCase")
Add_Instructor_UseCase = Class(name="Add_Instructor_UseCase")
Add_Course_UseCase = Class(name="Add_Course_UseCase")
Modify_Delete_Courses_UseCase = Class(name="Modify_Delete_Courses_UseCase")
Modify_Delete_Student_UseCase = Class(name="Modify_Delete_Student_UseCase")
Modify_Delete_Instructor_UseCase = Class(name="Modify_Delete_Instructor_UseCase")
Add_Evalutaions_Assignments_Exams_UseCase = Class(name="Add_Evalutaions_Assignments_Exams_UseCase")
Modify_Delete_Evalutaions_Assignments_Exams_UseCase = Class(name="Modify_Delete_Evalutaions_Assignments_Exams_UseCase")
Generate_Report_UseCase = Class(name="Generate_Report_UseCase")
Register_drop_course_UseCase = Class(name="Register_drop_course_UseCase")
Submit_Exam_Assignment_UseCase = Class(name="Submit_Exam_Assignment_UseCase")
View_Grades_UseCase = Class(name="View_Grades_UseCase")
Grade_Evalutations_Assignment_Exams_UseCase = Class(name="Grade_Evalutations_Assignment_Exams_UseCase")
Student = Class(name="Student")
School_Admin = Class(name="School_Admin")
Instructor = Class(name="Instructor")
Student1 = Class(name="Student1")
Course = Class(name="Course")
Exam = Class(name="Exam")
ExamResult = Class(name="ExamResult")
Question = Class(name="Question")
Answer = Class(name="Answer")

# Admin_Actor class attributes and methods

# Instructor_Actor class attributes and methods

# Student_Actor class attributes and methods

# Login_UseCase class attributes and methods

# Login_UseCase1 class attributes and methods

# Login_UseCase2 class attributes and methods

# Logout_UseCase class attributes and methods

# Add_Student_UseCase class attributes and methods

# Add_Instructor_UseCase class attributes and methods

# Add_Course_UseCase class attributes and methods

# Modify_Delete_Courses_UseCase class attributes and methods

# Modify_Delete_Student_UseCase class attributes and methods

# Modify_Delete_Instructor_UseCase class attributes and methods

# Add_Evalutaions_Assignments_Exams_UseCase class attributes and methods

# Modify_Delete_Evalutaions_Assignments_Exams_UseCase class attributes and methods

# Generate_Report_UseCase class attributes and methods

# Register_drop_course_UseCase class attributes and methods

# Submit_Exam_Assignment_UseCase class attributes and methods

# View_Grades_UseCase class attributes and methods

# Grade_Evalutations_Assignment_Exams_UseCase class attributes and methods

# Student class attributes and methods

# School_Admin class attributes and methods

# Instructor class attributes and methods

# Student1 class attributes and methods

# Course class attributes and methods

# Exam class attributes and methods

# ExamResult class attributes and methods

# Question class attributes and methods

# Answer class attributes and methods

# Relationships
Admin_Login: BinaryAssociation = BinaryAssociation(
    name="Admin_Login",
    ends={
        Property(name="login0", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin1", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Logout: BinaryAssociation = BinaryAssociation(
    name="Admin_Logout",
    ends={
        Property(name="logout2", type=Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin3", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Instructor_Logout: BinaryAssociation = BinaryAssociation(
    name="Instructor_Logout",
    ends={
        Property(name="logout4", type=Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="instructor5", type=Instructor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Logout: BinaryAssociation = BinaryAssociation(
    name="Student_Logout",
    ends={
        Property(name="logout6", type=Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student7", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Instructor_Login: BinaryAssociation = BinaryAssociation(
    name="Instructor_Login",
    ends={
        Property(name="login8", type=Login_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="instructor9", type=Instructor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Login_Student: BinaryAssociation = BinaryAssociation(
    name="Login_Student",
    ends={
        Property(name="student10", type=Student_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login11", type=Login_UseCase2, multiplicity=Multiplicity(0, 1))
    }
)
Login_Add_Student: BinaryAssociation = BinaryAssociation(
    name="Login_Add_Student",
    ends={
        Property(name="add_Student12", type=Add_Student_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="login13", type=Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Login_Add_Instructor: BinaryAssociation = BinaryAssociation(
    name="Login_Add_Instructor",
    ends={
        Property(name="add_Instructor14", type=Add_Instructor_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="login15", type=Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Login_Add_Course: BinaryAssociation = BinaryAssociation(
    name="Login_Add_Course",
    ends={
        Property(name="add_Course16", type=Add_Course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="login17", type=Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Login_Add_Evalutaions_Assignments_Exams: BinaryAssociation = BinaryAssociation(
    name="Login_Add_Evalutaions_Assignments_Exams",
    ends={
        Property(name="add_Evalutaions_Assignments_Exams18", type=Add_Evalutaions_Assignments_Exams_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="login19", type=Login_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Login_Generate_Report: BinaryAssociation = BinaryAssociation(
    name="Login_Generate_Report",
    ends={
        Property(name="generate_Report20", type=Generate_Report_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="login21", type=Login_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Login_Register_drop_course: BinaryAssociation = BinaryAssociation(
    name="Login_Register_drop_course",
    ends={
        Property(name="register_drop_course22", type=Register_drop_course_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="login23", type=Login_UseCase2, multiplicity=Multiplicity(0, 1))
    }
)
Login_View_Grades: BinaryAssociation = BinaryAssociation(
    name="Login_View_Grades",
    ends={
        Property(name="view_Grades24", type=View_Grades_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="login25", type=Login_UseCase2, multiplicity=Multiplicity(0, 1))
    }
)
Submit_Exam_Assignment_Login: BinaryAssociation = BinaryAssociation(
    name="Submit_Exam_Assignment_Login",
    ends={
        Property(name="login26", type=Login_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="submit_Exam_Assignment27", type=Submit_Exam_Assignment_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
School_Admin_Course: BinaryAssociation = BinaryAssociation(
    name="School_Admin_Course",
    ends={
        Property(name="course28", type=Course, multiplicity=Multiplicity(1, 9999)),
        Property(name="school_Admin29", type=School_Admin, multiplicity=Multiplicity(1, 9999))
    }
)
Student_Course: BinaryAssociation = BinaryAssociation(
    name="Student_Course",
    ends={
        Property(name="course30", type=Course, multiplicity=Multiplicity(1, 9999)),
        Property(name="student31", type=Student1, multiplicity=Multiplicity(1, 9999))
    }
)
Exam_Question: BinaryAssociation = BinaryAssociation(
    name="Exam_Question",
    ends={
        Property(name="question32", type=Question, multiplicity=Multiplicity(1, 9999)),
        Property(name="exam33", type=Exam, multiplicity=Multiplicity(1, 9999))
    }
)
Question_Answer: BinaryAssociation = BinaryAssociation(
    name="Question_Answer",
    ends={
        Property(name="answer34", type=Answer, multiplicity=Multiplicity(1, 1)),
        Property(name="question35", type=Question, multiplicity=Multiplicity(1, 1))
    }
)
Course_Exam: BinaryAssociation = BinaryAssociation(
    name="Course_Exam",
    ends={
        Property(name="exam36", type=Exam, multiplicity=Multiplicity(1, 9999)),
        Property(name="course37", type=Course, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_905da09d_03aa_4224_963a_047d8f51448d",
    types={Admin_Actor, Instructor_Actor, Student_Actor, Login_UseCase, Login_UseCase1, Login_UseCase2, Logout_UseCase, Add_Student_UseCase, Add_Instructor_UseCase, Add_Course_UseCase, Modify_Delete_Courses_UseCase, Modify_Delete_Student_UseCase, Modify_Delete_Instructor_UseCase, Add_Evalutaions_Assignments_Exams_UseCase, Modify_Delete_Evalutaions_Assignments_Exams_UseCase, Generate_Report_UseCase, Register_drop_course_UseCase, Submit_Exam_Assignment_UseCase, View_Grades_UseCase, Grade_Evalutations_Assignment_Exams_UseCase, Student, School_Admin, Instructor, Student1, Course, Exam, ExamResult, Question, Answer},
    associations={Admin_Login, Admin_Logout, Instructor_Logout, Student_Logout, Instructor_Login, Login_Student, Login_Add_Student, Login_Add_Instructor, Login_Add_Course, Login_Add_Evalutaions_Assignments_Exams, Login_Generate_Report, Login_Register_drop_course, Login_View_Grades, Submit_Exam_Assignment_Login, School_Admin_Course, Student_Course, Exam_Question, Question_Answer, Course_Exam},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)