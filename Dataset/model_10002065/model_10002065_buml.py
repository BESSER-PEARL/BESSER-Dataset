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
Admin = Class(name="Admin")
Person = Class(name="Person")
Stuff = Class(name="Stuff")
str = Class(name="str")
Finance = Class(name="Finance")
Instructor = Class(name="Instructor")
Student = Class(name="Student")
Binary_File = Class(name="Binary_File")
Department = Class(name="Department")
ILogin_Interface = Class(name="ILogin_Interface")
User = Class(name="User")
T = Class(name="T")
Course = Class(name="Course")
Exam = Class(name="Exam")
Email = Class(name="Email")
Report = Class(name="Report")
Exceptions = Class(name="Exceptions")

# Admin class attributes and methods

# Person class attributes and methods
Person_PhoneNum: Property = Property(name="PhoneNum", type=StringType)
Person_Id: Property = Property(name="Id", type=StringType)
Person.attributes={Person_Id, Person_PhoneNum}

# Stuff class attributes and methods
Stuff_Salary: Property = Property(name="Salary", type=StringType)
Stuff_WorkHours: Property = Property(name="WorkHours", type=StringType)
Stuff.attributes={Stuff_Salary, Stuff_WorkHours}

# str class attributes and methods

# Finance class attributes and methods

# Instructor class attributes and methods

# Student class attributes and methods
Student_SAge: Property = Property(name="SAge", type=IntegerType)
Student_SGender: Property = Property(name="SGender", type=StringType)
Student.attributes={Student_SGender, Student_SAge}

# Binary_File class attributes and methods

# Department class attributes and methods
Department_deptName: Property = Property(name="deptName", type=StringType)
Department_deptId: Property = Property(name="deptId", type=StringType)
Department.attributes={Department_deptId, Department_deptName}

# ILogin_Interface class attributes and methods

# User class attributes and methods
User_email: Property = Property(name="email", type=StringType)
User_Fname: Property = Property(name="Fname", type=StringType)
User_Lname: Property = Property(name="Lname", type=StringType)
User_Password: Property = Property(name="Password", type=StringType)
User.attributes={User_Password, User_Lname, User_email, User_Fname}

# T class attributes and methods

# Course class attributes and methods
Course_CName: Property = Property(name="CName", type=StringType)
Course_CPrice: Property = Property(name="CPrice", type=StringType)
Course_CCode: Property = Property(name="CCode", type=StringType)
Course_CInstructor: Property = Property(name="CInstructor", type=StringType)
Course.attributes={Course_CName, Course_CInstructor, Course_CPrice, Course_CCode}

# Exam class attributes and methods
Exam_ETime: Property = Property(name="ETime", type=StringType)
Exam_EName: Property = Property(name="EName", type=StringType)
Exam_MaxGrade: Property = Property(name="MaxGrade", type=StringType)
Exam.attributes={Exam_MaxGrade, Exam_ETime, Exam_EName}

# Email class attributes and methods

# Report class attributes and methods

# Exceptions class attributes and methods

# Relationships
Instructor_Department: BinaryAssociation = BinaryAssociation(
    name="Instructor_Department",
    ends={
        Property(name="department0", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="instructor1", type=Instructor, multiplicity=Multiplicity(0, 1))
    }
)
User_ILogin: BinaryAssociation = BinaryAssociation(
    name="User_ILogin",
    ends={
        Property(name="User_ILogin_02", type=ILogin_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_Binary_File: BinaryAssociation = BinaryAssociation(
    name="User_Binary_File",
    ends={
        Property(name="binary_File4", type=Binary_File, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Course_Binary_File: BinaryAssociation = BinaryAssociation(
    name="Course_Binary_File",
    ends={
        Property(name="binary_File6", type=Binary_File, multiplicity=Multiplicity(0, 1)),
        Property(name="course7", type=Course, multiplicity=Multiplicity(0, 1))
    }
)
Exam_Course: BinaryAssociation = BinaryAssociation(
    name="Exam_Course",
    ends={
        Property(name="course8", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="exam9", type=Exam, multiplicity=Multiplicity(0, 1))
    }
)
User_Exceptions: BinaryAssociation = BinaryAssociation(
    name="User_Exceptions",
    ends={
        Property(name="exceptions10", type=Exceptions, multiplicity=Multiplicity(0, 1)),
        Property(name="user11", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Department_Binary_File: BinaryAssociation = BinaryAssociation(
    name="Department_Binary_File",
    ends={
        Property(name="binary_File12", type=Binary_File, multiplicity=Multiplicity(0, 1)),
        Property(name="department13", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Student_Report: BinaryAssociation = BinaryAssociation(
    name="Student_Report",
    ends={
        Property(name="report14", type=Report, multiplicity=Multiplicity(0, 1)),
        Property(name="student15", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Report: BinaryAssociation = BinaryAssociation(
    name="Admin_Report",
    ends={
        Property(name="report16", type=Report, multiplicity=Multiplicity(0, 1)),
        Property(name="admin17", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Report_Course: BinaryAssociation = BinaryAssociation(
    name="Report_Course",
    ends={
        Property(name="course18", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="report19", type=Report, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Email: BinaryAssociation = BinaryAssociation(
    name="Admin_Email",
    ends={
        Property(name="email20", type=Email, multiplicity=Multiplicity(0, 1)),
        Property(name="admin21", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Email_Student: BinaryAssociation = BinaryAssociation(
    name="Email_Student",
    ends={
        Property(name="student22", type=Student, multiplicity=Multiplicity(0, 1)),
        Property(name="email23", type=Email, multiplicity=Multiplicity(0, 1))
    }
)
Finance__Student: BinaryAssociation = BinaryAssociation(
    name="Finance__Student",
    ends={
        Property(name="student24", type=Student, multiplicity=Multiplicity(0, 1)),
        Property(name="finance25", type=Finance, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Student: BinaryAssociation = BinaryAssociation(
    name="Admin_Student",
    ends={
        Property(name="student26", type=Student, multiplicity=Multiplicity(0, 1)),
        Property(name="admin27", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Instructor: BinaryAssociation = BinaryAssociation(
    name="Admin_Instructor",
    ends={
        Property(name="instructor28", type=Instructor, multiplicity=Multiplicity(0, 1)),
        Property(name="admin29", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Course: BinaryAssociation = BinaryAssociation(
    name="Admin_Course",
    ends={
        Property(name="course30", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="admin31", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Department_Course: BinaryAssociation = BinaryAssociation(
    name="Department_Course",
    ends={
        Property(name="course32", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="department33", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Student_Course: BinaryAssociation = BinaryAssociation(
    name="Student_Course",
    ends={
        Property(name="course34", type=Course, multiplicity=Multiplicity(0, 1)),
        Property(name="student35", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
ILogin_Email: BinaryAssociation = BinaryAssociation(
    name="ILogin_Email",
    ends={
        Property(name="email36", type=Email, multiplicity=Multiplicity(0, 1)),
        Property(name="iLogin37", type=ILogin_Interface, multiplicity=Multiplicity(0, 1))
    }
)
Course_Report: BinaryAssociation = BinaryAssociation(
    name="Course_Report",
    ends={
        Property(name="report38", type=Report, multiplicity=Multiplicity(0, 1)),
        Property(name="course39", type=Course, multiplicity=Multiplicity(0, 1))
    }
)
Finance__Report: BinaryAssociation = BinaryAssociation(
    name="Finance__Report",
    ends={
        Property(name="report40", type=Report, multiplicity=Multiplicity(0, 1)),
        Property(name="finance41", type=Finance, multiplicity=Multiplicity(0, 1))
    }
)
Binary_File_Report: BinaryAssociation = BinaryAssociation(
    name="Binary_File_Report",
    ends={
        Property(name="report42", type=Report, multiplicity=Multiplicity(0, 1)),
        Property(name="binary_File43", type=Binary_File, multiplicity=Multiplicity(0, 1))
    }
)
Exam_Binary_File: BinaryAssociation = BinaryAssociation(
    name="Exam_Binary_File",
    ends={
        Property(name="binary_File44", type=Binary_File, multiplicity=Multiplicity(0, 1)),
        Property(name="exam45", type=Exam, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_mTkfoNz3EeeAyLDAJ12_fg",
    types={Admin, Person, Stuff, str, Finance, Instructor, Student, Binary_File, Department, ILogin_Interface, User, T, Course, Exam, Email, Report, Exceptions},
    associations={Instructor_Department, User_ILogin, User_Binary_File, Course_Binary_File, Exam_Course, User_Exceptions, Department_Binary_File, Student_Report, Admin_Report, Report_Course, Admin_Email, Email_Student, Finance__Student, Admin_Student, Admin_Instructor, Admin_Course, Department_Course, Student_Course, ILogin_Email, Course_Report, Finance__Report, Binary_File_Report, Exam_Binary_File},
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