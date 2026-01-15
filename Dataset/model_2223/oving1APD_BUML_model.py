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
CourseStatus: Enumeration = Enumeration(
    name="CourseStatus",
    literals={
            EnumerationLiteral(name="Mandatory"),
			EnumerationLiteral(name="Elective")
    }
)

# Classes
oving1APD_Department = Class(name="oving1APD::Department")
oving1APD_Specialization = Class(name="oving1APD::Specialization")
oving1APD_Semester = Class(name="oving1APD::Semester")
oving1APD_Course = Class(name="oving1APD::Course")
oving1APD_StudyProgram = Class(name="oving1APD::StudyProgram")
oving1APD_Slot = Class(name="oving1APD::Slot")

# oving1APD_Department class attributes and methods
oving1APD_Department_name: Property = Property(name="name", type=StringType)
oving1APD_Department_shortName: Property = Property(name="shortName", type=StringType)
oving1APD_Department.attributes={oving1APD_Department_name, oving1APD_Department_shortName}

# oving1APD_Specialization class attributes and methods
oving1APD_Specialization_name: Property = Property(name="name", type=StringType)
oving1APD_Specialization.attributes={oving1APD_Specialization_name}

# oving1APD_Semester class attributes and methods
oving1APD_Semester_number: Property = Property(name="number", type=IntegerType)
oving1APD_Semester.attributes={oving1APD_Semester_number}

# oving1APD_Course class attributes and methods
oving1APD_Course_name: Property = Property(name="name", type=StringType)
oving1APD_Course_credit: Property = Property(name="credit", type=FloatType)
oving1APD_Course_code: Property = Property(name="code", type=StringType)
oving1APD_Course_level: Property = Property(name="level", type=IntegerType)
oving1APD_Course.attributes={oving1APD_Course_name, oving1APD_Course_level, oving1APD_Course_credit, oving1APD_Course_code}

# oving1APD_StudyProgram class attributes and methods
oving1APD_StudyProgram_name: Property = Property(name="name", type=StringType)
oving1APD_StudyProgram_shortName: Property = Property(name="shortName", type=StringType)
oving1APD_StudyProgram.attributes={oving1APD_StudyProgram_name, oving1APD_StudyProgram_shortName}

# oving1APD_Slot class attributes and methods
oving1APD_Slot_name: Property = Property(name="name", type=StringType)
oving1APD_Slot.attributes={oving1APD_Slot_name}

# Relationships
specialization1: BinaryAssociation = BinaryAssociation(
    name="specialization1",
    ends={
        Property(name="Specialization", type=oving1APD_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram", type=oving1APD_Specialization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
semester2: BinaryAssociation = BinaryAssociation(
    name="semester2",
    ends={
        Property(name="Semester", type=oving1APD_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram3", type=oving1APD_Semester, multiplicity=Multiplicity(0, 1))
    }
)
department4: BinaryAssociation = BinaryAssociation(
    name="department4",
    ends={
        Property(name="Department", type=oving1APD_StudyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="studyProgram5", type=oving1APD_Department, multiplicity=Multiplicity(0, 1))
    }
)
courseInSemester6: BinaryAssociation = BinaryAssociation(
    name="courseInSemester6",
    ends={
        Property(name="Semester7", type=oving1APD_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="hasCourse", type=oving1APD_Semester, multiplicity=Multiplicity(0, 1))
    }
)
specialization8: BinaryAssociation = BinaryAssociation(
    name="specialization8",
    ends={
        Property(name="Specialization9", type=oving1APD_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=oving1APD_Specialization, multiplicity=Multiplicity(0, 1))
    }
)
studyProgram0: BinaryAssociation = BinaryAssociation(
    name="studyProgram0",
    ends={
        Property(name="StudyProgram", type=oving1APD_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=oving1APD_StudyProgram, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hasCourse12: BinaryAssociation = BinaryAssociation(
    name="hasCourse12",
    ends={
        Property(name="Course", type=oving1APD_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="courseInSemester", type=oving1APD_Course, multiplicity=Multiplicity(0, 9999))
    }
)
slot13: BinaryAssociation = BinaryAssociation(
    name="slot13",
    ends={
        Property(name="Slot14", type=oving1APD_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=oving1APD_Slot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
studyProgram15: BinaryAssociation = BinaryAssociation(
    name="studyProgram15",
    ends={
        Property(name="StudyProgram17", type=oving1APD_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester16", type=oving1APD_StudyProgram, multiplicity=Multiplicity(0, 1))
    }
)
specialization18: BinaryAssociation = BinaryAssociation(
    name="specialization18",
    ends={
        Property(name="Specialization20", type=oving1APD_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester19", type=oving1APD_Specialization, multiplicity=Multiplicity(0, 1))
    }
)
semester21: BinaryAssociation = BinaryAssociation(
    name="semester21",
    ends={
        Property(name="Semester22", type=oving1APD_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization", type=oving1APD_Semester, multiplicity=Multiplicity(0, 1))
    }
)
course23: BinaryAssociation = BinaryAssociation(
    name="course23",
    ends={
        Property(name="Course25", type=oving1APD_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization24", type=oving1APD_Course, multiplicity=Multiplicity(0, 1))
    }
)
slot10: BinaryAssociation = BinaryAssociation(
    name="slot10",
    ends={
        Property(name="Slot", type=oving1APD_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course11", type=oving1APD_Slot, multiplicity=Multiplicity(0, 1))
    }
)
semester31: BinaryAssociation = BinaryAssociation(
    name="semester31",
    ends={
        Property(name="Semester33", type=oving1APD_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot32", type=oving1APD_Semester, multiplicity=Multiplicity(0, 1))
    }
)
studyProgram26: BinaryAssociation = BinaryAssociation(
    name="studyProgram26",
    ends={
        Property(name="StudyProgram28", type=oving1APD_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization27", type=oving1APD_StudyProgram, multiplicity=Multiplicity(0, 1))
    }
)
course29: BinaryAssociation = BinaryAssociation(
    name="course29",
    ends={
        Property(name="Course30", type=oving1APD_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=oving1APD_Course, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="oving1APD",
    types={oving1APD_Department, oving1APD_Specialization, oving1APD_Semester, oving1APD_Course, oving1APD_StudyProgram, oving1APD_Slot, CourseStatus},
    associations={specialization1, semester2, department4, courseInSemester6, specialization8, studyProgram0, hasCourse12, slot13, studyProgram15, specialization18, semester21, course23, slot10, semester31, studyProgram26, course29},
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