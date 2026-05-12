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
Student = Class(name="Student")
Employee_Interface = Class(name="Employee_Interface")
Teacher = Class(name="Teacher")
HOD = Class(name="HOD")
Department = Class(name="Department")
Course = Class(name="Course")
Authentication = Class(name="Authentication")
Access_Information = Class(name="Access_Information")
Attendance = Class(name="Attendance")
Subject = Class(name="Subject")
Faculty = Class(name="Faculty")

# Student class attributes and methods
Student_firstName: Property = Property(name="firstName", type=StringType)
Student_ID: Property = Property(name="ID", type=StringType)
Student_lastNAme: Property = Property(name="lastNAme", type=StringType)
Student_socialsecurity: Property = Property(name="socialsecurity", type=StringType)
Student_middleNAme: Property = Property(name="middleNAme", type=StringType)
Student.attributes={Student_socialsecurity, Student_lastNAme, Student_middleNAme, Student_firstName, Student_ID}

# Employee_Interface class attributes and methods

# Teacher class attributes and methods

# HOD class attributes and methods

# Department class attributes and methods
Department_course: Property = Property(name="course", type=Course)
Department_students__: Property = Property(name="students__", type=Student)
Department_teachers__: Property = Property(name="teachers__", type=Teacher)
Department_courseID: Property = Property(name="courseID", type=StringType)
Department_CourseName: Property = Property(name="CourseName", type=StringType)
Department.attributes={Department_students__, Department_teachers__, Department_CourseName, Department_courseID, Department_course}

# Course class attributes and methods
Course_subjects__: Property = Property(name="subjects__", type=Subject)
Course_courseDuration: Property = Property(name="courseDuration", type=StringType)
Course_CourseStartDate: Property = Property(name="CourseStartDate", type=DateType)
Course_CourseEndDate: Property = Property(name="CourseEndDate", type=DateType)
Course_courseName: Property = Property(name="courseName", type=StringType)
Course.attributes={Course_CourseStartDate, Course_CourseEndDate, Course_courseDuration, Course_courseName, Course_subjects__}

# Authentication class attributes and methods

# Access_Information class attributes and methods

# Attendance class attributes and methods

# Subject class attributes and methods
Subject_name: Property = Property(name="name", type=StringType)
Subject_subjectType: Property = Property(name="subjectType", type=StringType)
Subject_subjectCategory: Property = Property(name="subjectCategory", type=StringType)
Subject_subjectID: Property = Property(name="subjectID", type=StringType)
Subject_subjectTest: Property = Property(name="subjectTest", type=StringType)
Subject.attributes={Subject_subjectID, Subject_name, Subject_subjectType, Subject_subjectCategory, Subject_subjectTest}

# Faculty class attributes and methods

# Relationships
Department_Course: BinaryAssociation = BinaryAssociation(
    name="Department_Course",
    ends={
        Property(name="course0", type=Course, multiplicity=Multiplicity(1, 1)),
        Property(name="department1", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Course_Subject: BinaryAssociation = BinaryAssociation(
    name="Course_Subject",
    ends={
        Property(name="subject2", type=Subject, multiplicity=Multiplicity(0, 9999)),
        Property(name="course3", type=Course, multiplicity=Multiplicity(0, 1))
    }
)
Department_Student: BinaryAssociation = BinaryAssociation(
    name="Department_Student",
    ends={
        Property(name="student4", type=Student, multiplicity=Multiplicity(0, 9999)),
        Property(name="department5", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Department_Employee: BinaryAssociation = BinaryAssociation(
    name="Department_Employee",
    ends={
        Property(name="employee6", type=Employee_Interface, multiplicity=Multiplicity(0, 9999)),
        Property(name="department7", type=Department, multiplicity=Multiplicity(0, 9999))
    }
)
Student_Access_Information: BinaryAssociation = BinaryAssociation(
    name="Student_Access_Information",
    ends={
        Property(name="Having_Attendance8", type=Access_Information, multiplicity=Multiplicity(0, 1)),
        Property(name="student9", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Access_Information: BinaryAssociation = BinaryAssociation(
    name="Employee_Access_Information",
    ends={
        Property(name="access_Information10", type=Access_Information, multiplicity=Multiplicity(0, 1)),
        Property(name="employee11", type=Employee_Interface, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Student: BinaryAssociation = BinaryAssociation(
    name="Admin_Student",
    ends={
        Property(name="student12", type=Student, multiplicity=Multiplicity(0, 9999)),
        Property(name="faculty13", type=Faculty, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Employee: BinaryAssociation = BinaryAssociation(
    name="Admin_Employee",
    ends={
        Property(name="employee14", type=Employee_Interface, multiplicity=Multiplicity(0, 9999)),
        Property(name="faculty15", type=Faculty, multiplicity=Multiplicity(0, 1))
    }
)
Access_Information_Attendance: BinaryAssociation = BinaryAssociation(
    name="Access_Information_Attendance",
    ends={
        Property(name="attendance16", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="access_Information17", type=Access_Information, multiplicity=Multiplicity(0, 1))
    }
)
Access_Information_Department: BinaryAssociation = BinaryAssociation(
    name="Access_Information_Department",
    ends={
        Property(name="department18", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="access_Information19", type=Access_Information, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="effdab1f_a902_4102_ab13_81dabf1cff91",
    types={Student, Employee_Interface, Teacher, HOD, Department, Course, Authentication, Access_Information, Attendance, Subject, Faculty},
    associations={Department_Course, Course_Subject, Department_Student, Department_Employee, Student_Access_Information, Employee_Access_Information, Admin_Student, Admin_Employee, Access_Information_Attendance, Access_Information_Department},
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