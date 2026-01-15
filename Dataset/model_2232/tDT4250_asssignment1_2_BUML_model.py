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

# Enumerations
Fall_or_spring: Enumeration = Enumeration(
    name="Fall_or_spring",
    literals={
            EnumerationLiteral(name="Fall"),
			EnumerationLiteral(name="Spring")
    }
)

# Classes
tDT4250_asssignment1_2_Program = Class(name="tDT4250::asssignment1::2::Program")
tDT4250_asssignment1_2_Specialization = Class(name="tDT4250::asssignment1::2::Specialization")
tDT4250_asssignment1_2_Program_course = Class(name="tDT4250::asssignment1::2::Program::course")
tDT4250_asssignment1_2_Semester_Course = Class(name="tDT4250::asssignment1::2::Semester::Course")
tDT4250_asssignment1_2_Course = Class(name="tDT4250::asssignment1::2::Course")
tDT4250_asssignment1_2_Semester = Class(name="tDT4250::asssignment1::2::Semester")
tDT4250_asssignment1_2_Department = Class(name="tDT4250::asssignment1::2::Department")

# tDT4250_asssignment1_2_Program class attributes and methods
tDT4250_asssignment1_2_Program_Name: Property = Property(name="Name", type=StringType)
tDT4250_asssignment1_2_Program_Credits: Property = Property(name="Credits", type=StringType)
tDT4250_asssignment1_2_Program.attributes={tDT4250_asssignment1_2_Program_Name, tDT4250_asssignment1_2_Program_Credits}

# tDT4250_asssignment1_2_Specialization class attributes and methods
tDT4250_asssignment1_2_Specialization_Name: Property = Property(name="Name", type=StringType)
tDT4250_asssignment1_2_Specialization.attributes={tDT4250_asssignment1_2_Specialization_Name}

# tDT4250_asssignment1_2_Program_course class attributes and methods
tDT4250_asssignment1_2_Program_course_Fall_or_spring: Property = Property(name="Fall_or_spring", type=StringType)
tDT4250_asssignment1_2_Program_course_Mandatory: Property = Property(name="Mandatory", type=BooleanType)
tDT4250_asssignment1_2_Program_course.attributes={tDT4250_asssignment1_2_Program_course_Fall_or_spring, tDT4250_asssignment1_2_Program_course_Mandatory}

# tDT4250_asssignment1_2_Semester_Course class attributes and methods
tDT4250_asssignment1_2_Semester_Course_Mandatory: Property = Property(name="Mandatory", type=BooleanType)
tDT4250_asssignment1_2_Semester_Course_Fall_or_spring: Property = Property(name="Fall_or_spring", type=StringType)
tDT4250_asssignment1_2_Semester_Course.attributes={tDT4250_asssignment1_2_Semester_Course_Mandatory, tDT4250_asssignment1_2_Semester_Course_Fall_or_spring}

# tDT4250_asssignment1_2_Course class attributes and methods
tDT4250_asssignment1_2_Course_Name: Property = Property(name="Name", type=StringType)
tDT4250_asssignment1_2_Course_Code: Property = Property(name="Code", type=StringType)
tDT4250_asssignment1_2_Course_Credits: Property = Property(name="Credits", type=FloatType)
tDT4250_asssignment1_2_Course_StartDate: Property = Property(name="StartDate", type=StringType)
tDT4250_asssignment1_2_Course_ExamDate: Property = Property(name="ExamDate", type=StringType)
tDT4250_asssignment1_2_Course.attributes={tDT4250_asssignment1_2_Course_StartDate, tDT4250_asssignment1_2_Course_Code, tDT4250_asssignment1_2_Course_Credits, tDT4250_asssignment1_2_Course_ExamDate, tDT4250_asssignment1_2_Course_Name}

# tDT4250_asssignment1_2_Semester class attributes and methods
tDT4250_asssignment1_2_Semester_Number: Property = Property(name="Number", type=IntegerType)
tDT4250_asssignment1_2_Semester_Credits: Property = Property(name="Credits", type=StringType)
tDT4250_asssignment1_2_Semester.attributes={tDT4250_asssignment1_2_Semester_Credits, tDT4250_asssignment1_2_Semester_Number}

# tDT4250_asssignment1_2_Department class attributes and methods
tDT4250_asssignment1_2_Department_Name: Property = Property(name="Name", type=StringType)
tDT4250_asssignment1_2_Department.attributes={tDT4250_asssignment1_2_Department_Name}

# Relationships
specialization0: BinaryAssociation = BinaryAssociation(
    name="specialization0",
    ends={
        Property(name="tDT4250_asssignment1_2_Specialization", type=tDT4250_asssignment1_2_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="tDT4250_asssignment1_2_Program", type=tDT4250_asssignment1_2_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program_course1: BinaryAssociation = BinaryAssociation(
    name="program_course1",
    ends={
        Property(name="tDT4250_asssignment1_2_Program_course", type=tDT4250_asssignment1_2_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="tDT4250_asssignment1_2_Program2", type=tDT4250_asssignment1_2_Program_course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester5: BinaryAssociation = BinaryAssociation(
    name="semester5",
    ends={
        Property(name="tDT4250_asssignment1_2_Semester7", type=tDT4250_asssignment1_2_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="tDT4250_asssignment1_2_Specialization6", type=tDT4250_asssignment1_2_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specialization9: BinaryAssociation = BinaryAssociation(
    name="specialization9",
    ends={
        Property(name="tDT4250_asssignment1_2_Specialization10", type=tDT4250_asssignment1_2_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="tDT4250_asssignment1_2_Specialization8", type=tDT4250_asssignment1_2_Specialization, multiplicity=Multiplicity(0, 9999))
    }
)
semester_course11: BinaryAssociation = BinaryAssociation(
    name="semester_course11",
    ends={
        Property(name="tDT4250_asssignment1_2_Semester_Course", type=tDT4250_asssignment1_2_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="tDT4250_asssignment1_2_Semester12", type=tDT4250_asssignment1_2_Semester_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course13: BinaryAssociation = BinaryAssociation(
    name="course13",
    ends={
        Property(name="tDT4250_asssignment1_2_Course", type=tDT4250_asssignment1_2_Semester_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="tDT4250_asssignment1_2_Semester_Course14", type=tDT4250_asssignment1_2_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester3: BinaryAssociation = BinaryAssociation(
    name="semester3",
    ends={
        Property(name="tDT4250_asssignment1_2_Semester", type=tDT4250_asssignment1_2_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="tDT4250_asssignment1_2_Program4", type=tDT4250_asssignment1_2_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course15: BinaryAssociation = BinaryAssociation(
    name="course15",
    ends={
        Property(name="tDT4250_asssignment1_2_Course17", type=tDT4250_asssignment1_2_Program_course, multiplicity=Multiplicity(1, 1)),
        Property(name="tDT4250_asssignment1_2_Program_course16", type=tDT4250_asssignment1_2_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course18: BinaryAssociation = BinaryAssociation(
    name="course18",
    ends={
        Property(name="tDT4250_asssignment1_2_Course19", type=tDT4250_asssignment1_2_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="tDT4250_asssignment1_2_Department", type=tDT4250_asssignment1_2_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program20: BinaryAssociation = BinaryAssociation(
    name="program20",
    ends={
        Property(name="tDT4250_asssignment1_2_Program22", type=tDT4250_asssignment1_2_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="tDT4250_asssignment1_2_Department21", type=tDT4250_asssignment1_2_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="tDT4250_asssignment1_2",
    types={tDT4250_asssignment1_2_Program, tDT4250_asssignment1_2_Specialization, tDT4250_asssignment1_2_Program_course, tDT4250_asssignment1_2_Semester_Course, tDT4250_asssignment1_2_Course, tDT4250_asssignment1_2_Semester, tDT4250_asssignment1_2_Department, Fall_or_spring},
    associations={specialization0, program_course1, semester5, specialization9, semester_course11, course13, semester3, course15, course18, program20},
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