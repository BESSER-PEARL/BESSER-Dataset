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
oving1APD_Department = Class(name="oving1APD::Department")
oving1APD_StudyProgram = Class(name="oving1APD::StudyProgram")
oving1APD_Course = Class(name="oving1APD::Course")
oving1APD_Specialization = Class(name="oving1APD::Specialization")
oving1APD_Semester = Class(name="oving1APD::Semester")
oving1APD_Slot = Class(name="oving1APD::Slot")

# oving1APD_Department class attributes and methods
oving1APD_Department_name: Property = Property(name="name", type=StringType)
oving1APD_Department_shortName: Property = Property(name="shortName", type=StringType)
oving1APD_Department.attributes={oving1APD_Department_name, oving1APD_Department_shortName}

# oving1APD_StudyProgram class attributes and methods
oving1APD_StudyProgram_name: Property = Property(name="name", type=StringType)
oving1APD_StudyProgram_shortName: Property = Property(name="shortName", type=StringType)
oving1APD_StudyProgram.attributes={oving1APD_StudyProgram_shortName, oving1APD_StudyProgram_name}

# oving1APD_Course class attributes and methods
oving1APD_Course_name: Property = Property(name="name", type=StringType)
oving1APD_Course_credit: Property = Property(name="credit", type=FloatType)
oving1APD_Course_code: Property = Property(name="code", type=StringType)
oving1APD_Course_level: Property = Property(name="level", type=IntegerType)
oving1APD_Course.attributes={oving1APD_Course_name, oving1APD_Course_credit, oving1APD_Course_level, oving1APD_Course_code}

# oving1APD_Specialization class attributes and methods
oving1APD_Specialization_name: Property = Property(name="name", type=StringType)
oving1APD_Specialization.attributes={oving1APD_Specialization_name}

# oving1APD_Semester class attributes and methods
oving1APD_Semester_number: Property = Property(name="number", type=IntegerType)
oving1APD_Semester.attributes={oving1APD_Semester_number}

# oving1APD_Slot class attributes and methods
oving1APD_Slot_name: Property = Property(name="name", type=StringType)
oving1APD_Slot.attributes={oving1APD_Slot_name}

# Relationships
studyProgram0: BinaryAssociation = BinaryAssociation(
    name="studyProgram0",
    ends={
        Property(name="StudyProgram", type=oving1APD_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=oving1APD_StudyProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course1: BinaryAssociation = BinaryAssociation(
    name="course1",
    ends={
        Property(name="oving1APD_Course", type=oving1APD_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="oving1APD_Department", type=oving1APD_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specialization2: BinaryAssociation = BinaryAssociation(
    name="specialization2",
    ends={
        Property(name="Specialization", type=oving1APD_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram", type=oving1APD_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester3: BinaryAssociation = BinaryAssociation(
    name="semester3",
    ends={
        Property(name="Semester", type=oving1APD_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram4", type=oving1APD_Semester, multiplicity=Multiplicity(0, 1))
    }
)
department5: BinaryAssociation = BinaryAssociation(
    name="department5",
    ends={
        Property(name="Department", type=oving1APD_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram6", type=oving1APD_Department, multiplicity=Multiplicity(0, 1))
    }
)
courseInSemester7: BinaryAssociation = BinaryAssociation(
    name="courseInSemester7",
    ends={
        Property(name="Semester8", type=oving1APD_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="hasCourse", type=oving1APD_Semester, multiplicity=Multiplicity(0, 9999))
    }
)
specialization9: BinaryAssociation = BinaryAssociation(
    name="specialization9",
    ends={
        Property(name="Specialization10", type=oving1APD_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=oving1APD_Specialization, multiplicity=Multiplicity(0, 1))
    }
)
slot11: BinaryAssociation = BinaryAssociation(
    name="slot11",
    ends={
        Property(name="Slot", type=oving1APD_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course12", type=oving1APD_Slot, multiplicity=Multiplicity(0, 1))
    }
)
semester32: BinaryAssociation = BinaryAssociation(
    name="semester32",
    ends={
        Property(name="Semester34", type=oving1APD_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot33", type=oving1APD_Semester, multiplicity=Multiplicity(0, 1))
    }
)
hasCourse13: BinaryAssociation = BinaryAssociation(
    name="hasCourse13",
    ends={
        Property(name="Course", type=oving1APD_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="courseInSemester", type=oving1APD_Course, multiplicity=Multiplicity(0, 9999))
    }
)
slot14: BinaryAssociation = BinaryAssociation(
    name="slot14",
    ends={
        Property(name="Slot15", type=oving1APD_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=oving1APD_Slot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
studyProgram16: BinaryAssociation = BinaryAssociation(
    name="studyProgram16",
    ends={
        Property(name="StudyProgram18", type=oving1APD_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester17", type=oving1APD_StudyProgram, multiplicity=Multiplicity(0, 1))
    }
)
specialization19: BinaryAssociation = BinaryAssociation(
    name="specialization19",
    ends={
        Property(name="Specialization21", type=oving1APD_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester20", type=oving1APD_Specialization, multiplicity=Multiplicity(0, 1))
    }
)
semester22: BinaryAssociation = BinaryAssociation(
    name="semester22",
    ends={
        Property(name="Semester23", type=oving1APD_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization", type=oving1APD_Semester, multiplicity=Multiplicity(0, 1))
    }
)
course24: BinaryAssociation = BinaryAssociation(
    name="course24",
    ends={
        Property(name="Course26", type=oving1APD_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization25", type=oving1APD_Course, multiplicity=Multiplicity(0, 9999))
    }
)
studyProgram27: BinaryAssociation = BinaryAssociation(
    name="studyProgram27",
    ends={
        Property(name="StudyProgram29", type=oving1APD_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization28", type=oving1APD_StudyProgram, multiplicity=Multiplicity(0, 1))
    }
)
course30: BinaryAssociation = BinaryAssociation(
    name="course30",
    ends={
        Property(name="Course31", type=oving1APD_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=oving1APD_Course, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="oving1APD",
    types={oving1APD_Department, oving1APD_StudyProgram, oving1APD_Course, oving1APD_Specialization, oving1APD_Semester, oving1APD_Slot},
    associations={studyProgram0, course1, specialization2, semester3, department5, courseInSemester7, specialization9, slot11, semester32, hasCourse13, slot14, studyProgram16, specialization19, semester22, course24, studyProgram27, course30},
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