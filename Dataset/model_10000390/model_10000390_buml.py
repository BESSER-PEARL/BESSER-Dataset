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
Department = Class(name="Department")
Course = Class(name="Course")
Admin = Class(name="Admin")
MyClass = Class(name="MyClass")

# Student class attributes and methods
Student_Name: Property = Property(name="Name", type=StringType)
Student_ID: Property = Property(name="ID", type=StringType)
Student.attributes={Student_ID, Student_Name}

# Employee_Interface class attributes and methods

# Teacher class attributes and methods

# Department class attributes and methods
Department_course: Property = Property(name="course", type=Course)
Department_students__: Property = Property(name="students__", type=Student)
Department_teachers__: Property = Property(name="teachers__", type=Teacher)
Department_hod: Property = Property(name="hod", type=StringType)
Department.attributes={Department_hod, Department_teachers__, Department_course, Department_students__}

# Course class attributes and methods
Course_subjects__: Property = Property(name="subjects__", type=StringType)
Course_duration: Property = Property(name="duration", type=StringType)
Course.attributes={Course_duration, Course_subjects__}

# Admin class attributes and methods

# MyClass class attributes and methods

# Relationships
Department_Course: BinaryAssociation = BinaryAssociation(
    name="Department_Course",
    ends={
        Property(name="course0", type=Course, multiplicity=Multiplicity(1, 1)),
        Property(name="department1", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Department_Student: BinaryAssociation = BinaryAssociation(
    name="Department_Student",
    ends={
        Property(name="student2", type=Student, multiplicity=Multiplicity(0, 9999)),
        Property(name="department3", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
Department_Employee: BinaryAssociation = BinaryAssociation(
    name="Department_Employee",
    ends={
        Property(name="employee4", type=Employee_Interface, multiplicity=Multiplicity(0, 9999)),
        Property(name="department5", type=Department, multiplicity=Multiplicity(0, 9999))
    }
)
Admin_Student: BinaryAssociation = BinaryAssociation(
    name="Admin_Student",
    ends={
        Property(name="student6", type=Student, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin7", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Employee: BinaryAssociation = BinaryAssociation(
    name="Admin_Employee",
    ends={
        Property(name="employee8", type=Employee_Interface, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin9", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3138ac23_c50e_4474_807f_be2b8e0239be",
    types={Student, Employee_Interface, Teacher, Department, Course, Admin, MyClass},
    associations={Department_Course, Department_Student, Department_Employee, Admin_Student, Admin_Employee},
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