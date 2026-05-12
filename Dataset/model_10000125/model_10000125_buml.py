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
Subject = Class(name="Subject")
Admin = Class(name="Admin")
Student = Class(name="Student")
Lecturer = Class(name="Lecturer")
HOD = Class(name="HOD")
Department = Class(name="Department")
Course = Class(name="Course")
Authentication = Class(name="Authentication")
Access_Information = Class(name="Access_Information")
Attendance = Class(name="Attendance")

# Subject class attributes and methods
Subject_name: Property = Property(name="name", type=StringType)
Subject.attributes={Subject_name}

# Admin class attributes and methods

# Student class attributes and methods
Student_Name: Property = Property(name="Name", type=StringType)
Student_ID: Property = Property(name="ID", type=StringType)
Student.attributes={Student_Name, Student_ID}

# Lecturer class attributes and methods

# HOD class attributes and methods

# Department class attributes and methods
Department_course: Property = Property(name="course", type=Course)
Department_students__: Property = Property(name="students__", type=Student)
Department_lecturer__: Property = Property(name="lecturer__", type=Lecturer)
Department_hod: Property = Property(name="hod", type=HOD)
Department.attributes={Department_students__, Department_course, Department_lecturer__, Department_hod}

# Course class attributes and methods
Course_subjects__: Property = Property(name="subjects__", type=Subject)
Course_duration: Property = Property(name="duration", type=StringType)
Course.attributes={Course_subjects__, Course_duration}

# Authentication class attributes and methods

# Access_Information class attributes and methods

# Attendance class attributes and methods

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
        Property(name="Department_Student_04", type=Student, multiplicity=Multiplicity(0, 9999)),
        Property(name="department5", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Student_Access_Information: BinaryAssociation = BinaryAssociation(
    name="Student_Access_Information",
    ends={
        Property(name="Having_Attendance6", type=Access_Information, multiplicity=Multiplicity(0, 1)),
        Property(name="student7", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Student: BinaryAssociation = BinaryAssociation(
    name="Admin_Student",
    ends={
        Property(name="student8", type=Student, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin9", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Access_Information_Attendance: BinaryAssociation = BinaryAssociation(
    name="Access_Information_Attendance",
    ends={
        Property(name="attendance10", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="access_Information11", type=Access_Information, multiplicity=Multiplicity(0, 1))
    }
)
Access_Information_Department: BinaryAssociation = BinaryAssociation(
    name="Access_Information_Department",
    ends={
        Property(name="department12", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="access_Information13", type=Access_Information, multiplicity=Multiplicity(0, 1))
    }
)
HOD_Department: BinaryAssociation = BinaryAssociation(
    name="HOD_Department",
    ends={
        Property(name="department14", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="hOD15", type=HOD, multiplicity=Multiplicity(0, 1))
    }
)
Lecturer_Department: BinaryAssociation = BinaryAssociation(
    name="Lecturer_Department",
    ends={
        Property(name="department16", type=Department, multiplicity=Multiplicity(0, 1)),
        Property(name="lecturer17", type=Lecturer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0f7a5154_27e6_471d_accc_3f8625d7cd80",
    types={Subject, Admin, Student, Lecturer, HOD, Department, Course, Authentication, Access_Information, Attendance},
    associations={Department_Course, Course_Subject, Department_Student, Student_Access_Information, Admin_Student, Access_Information_Attendance, Access_Information_Department, HOD_Department, Lecturer_Department},
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