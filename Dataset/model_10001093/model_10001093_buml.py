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
Admin = Class(name="Admin")

# Student class attributes and methods
Student_Name: Property = Property(name="Name", type=StringType)
Student_ID: Property = Property(name="ID", type=StringType)
Student.attributes={Student_ID, Student_Name}

# Employee_Interface class attributes and methods

# Teacher class attributes and methods

# HOD class attributes and methods

# Department class attributes and methods
Department_course: Property = Property(name="course", type=Course)
Department_students__: Property = Property(name="students__", type=Student)
Department_teachers__: Property = Property(name="teachers__", type=Teacher)
Department_hod: Property = Property(name="hod", type=HOD)
Department.attributes={Department_teachers__, Department_course, Department_students__, Department_hod}

# Course class attributes and methods
Course_subjects__: Property = Property(name="subjects__", type=Subject)
Course_duration: Property = Property(name="duration", type=StringType)
Course.attributes={Course_duration, Course_subjects__}

# Authentication class attributes and methods

# Access_Information class attributes and methods

# Attendance class attributes and methods

# Subject class attributes and methods
Subject_name: Property = Property(name="name", type=StringType)
Subject.attributes={Subject_name}

# Admin class attributes and methods

# Relationships
Admin_Employee: BinaryAssociation = BinaryAssociation(
    name="Admin_Employee",
    ends={
        Property(name="employee14", type=Employee_Interface, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin15", type=Admin, multiplicity=Multiplicity(0, 1))
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
        Property(name="student4", type=Student, multiplicity=Multiplicity(45, 9999)),
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
        Property(name="admin13", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8484f362_6ece_4b09_9a5d_b1144bcad088",
    types={Student, Employee_Interface, Teacher, HOD, Department, Course, Authentication, Access_Information, Attendance, Subject, Admin},
    associations={Admin_Employee, Access_Information_Attendance, Access_Information_Department, Department_Course, Course_Subject, Department_Student, Department_Employee, Student_Access_Information, Employee_Access_Information, Admin_Student},
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