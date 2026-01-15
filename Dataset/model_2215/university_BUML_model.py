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
SemesterTime: Enumeration = Enumeration(
    name="SemesterTime",
    literals={
            EnumerationLiteral(name="Fall"),
			EnumerationLiteral(name="Spring")
    }
)

SlotType: Enumeration = Enumeration(
    name="SlotType",
    literals={
            EnumerationLiteral(name="O"),
			EnumerationLiteral(name="V"),
			EnumerationLiteral(name="V2")
    }
)

# Classes
university_Programmes = Class(name="university::Programmes")
university_ProgrammeInstances = Class(name="university::ProgrammeInstances")
university_ProgrammeSemesters = Class(name="university::ProgrammeSemesters")
university_Specializations = Class(name="university::Specializations")
university_Courses = Class(name="university::Courses")
university_Semesters = Class(name="university::Semesters")
university_Slot = Class(name="university::Slot")
university_CourseInstances = Class(name="university::CourseInstances")
university_University = Class(name="university::University")

# university_Programmes class attributes and methods
university_Programmes_name: Property = Property(name="name", type=StringType)
university_Programmes_code: Property = Property(name="code", type=StringType)
university_Programmes.attributes={university_Programmes_name, university_Programmes_code}

# university_ProgrammeInstances class attributes and methods
university_ProgrammeInstances_startYear: Property = Property(name="startYear", type=IntegerType)
university_ProgrammeInstances.attributes={university_ProgrammeInstances_startYear}

# university_ProgrammeSemesters class attributes and methods

# university_Specializations class attributes and methods
university_Specializations_name: Property = Property(name="name", type=StringType)
university_Specializations.attributes={university_Specializations_name}

# university_Courses class attributes and methods
university_Courses_code: Property = Property(name="code", type=StringType)
university_Courses_name: Property = Property(name="name", type=StringType)
university_Courses_credits: Property = Property(name="credits", type=FloatType)
university_Courses.attributes={university_Courses_credits, university_Courses_name, university_Courses_code}

# university_Semesters class attributes and methods
university_Semesters_year: Property = Property(name="year", type=IntegerType)
university_Semesters_semesterTime: Property = Property(name="semesterTime", type=StringType)
university_Semesters.attributes={university_Semesters_semesterTime, university_Semesters_year}

# university_Slot class attributes and methods
university_Slot_points: Property = Property(name="points", type=IntegerType)
university_Slot_slotType: Property = Property(name="slotType", type=StringType)
university_Slot_name: Property = Property(name="name", type=StringType)
university_Slot.attributes={university_Slot_name, university_Slot_points, university_Slot_slotType}

# university_CourseInstances class attributes and methods

# university_University class attributes and methods
university_University_name: Property = Property(name="name", type=StringType)
university_University.attributes={university_University_name}

# Relationships
instances0: BinaryAssociation = BinaryAssociation(
    name="instances0",
    ends={
        Property(name="ProgrammeInstances", type=university_Programmes, multiplicity=Multiplicity(1, 1)),
        Property(name="programme", type=university_ProgrammeInstances, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programme1: BinaryAssociation = BinaryAssociation(
    name="programme1",
    ends={
        Property(name="Programmes", type=university_ProgrammeInstances, multiplicity=Multiplicity(1, 1)),
        Property(name="instances", type=university_Programmes, multiplicity=Multiplicity(1, 1))
    }
)
programmeSemesters2: BinaryAssociation = BinaryAssociation(
    name="programmeSemesters2",
    ends={
        Property(name="ProgrammeSemesters", type=university_ProgrammeInstances, multiplicity=Multiplicity(1, 1)),
        Property(name="programmeInstance", type=university_ProgrammeSemesters, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
specializations3: BinaryAssociation = BinaryAssociation(
    name="specializations3",
    ends={
        Property(name="Specializations", type=university_ProgrammeInstances, multiplicity=Multiplicity(1, 1)),
        Property(name="programmeInstance4", type=university_Specializations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course6: BinaryAssociation = BinaryAssociation(
    name="course6",
    ends={
        Property(name="Courses", type=university_CourseInstances, multiplicity=Multiplicity(1, 1)),
        Property(name="instances7", type=university_Courses, multiplicity=Multiplicity(1, 1))
    }
)
semester8: BinaryAssociation = BinaryAssociation(
    name="semester8",
    ends={
        Property(name="university_Semesters", type=university_CourseInstances, multiplicity=Multiplicity(1, 1)),
        Property(name="university_CourseInstances", type=university_Semesters, multiplicity=Multiplicity(1, 1))
    }
)
programmeInstance9: BinaryAssociation = BinaryAssociation(
    name="programmeInstance9",
    ends={
        Property(name="ProgrammeInstances10", type=university_ProgrammeSemesters, multiplicity=Multiplicity(1, 1)),
        Property(name="programmeSemesters", type=university_ProgrammeInstances, multiplicity=Multiplicity(0, 1))
    }
)
slots11: BinaryAssociation = BinaryAssociation(
    name="slots11",
    ends={
        Property(name="Slot", type=university_ProgrammeSemesters, multiplicity=Multiplicity(1, 1)),
        Property(name="programmeSemester", type=university_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester12: BinaryAssociation = BinaryAssociation(
    name="semester12",
    ends={
        Property(name="Semesters", type=university_ProgrammeSemesters, multiplicity=Multiplicity(1, 1)),
        Property(name="programmeSemesters13", type=university_Semesters, multiplicity=Multiplicity(1, 1))
    }
)
specialization14: BinaryAssociation = BinaryAssociation(
    name="specialization14",
    ends={
        Property(name="Specializations16", type=university_ProgrammeSemesters, multiplicity=Multiplicity(1, 1)),
        Property(name="programmeSemester15", type=university_Specializations, multiplicity=Multiplicity(0, 1))
    }
)
programmeSemester17: BinaryAssociation = BinaryAssociation(
    name="programmeSemester17",
    ends={
        Property(name="ProgrammeSemesters18", type=university_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slots", type=university_ProgrammeSemesters, multiplicity=Multiplicity(1, 1))
    }
)
instances5: BinaryAssociation = BinaryAssociation(
    name="instances5",
    ends={
        Property(name="CourseInstances", type=university_Courses, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=university_CourseInstances, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programmeSemesters21: BinaryAssociation = BinaryAssociation(
    name="programmeSemesters21",
    ends={
        Property(name="ProgrammeSemesters22", type=university_Semesters, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=university_ProgrammeSemesters, multiplicity=Multiplicity(0, 9999))
    }
)
programmeInstance23: BinaryAssociation = BinaryAssociation(
    name="programmeInstance23",
    ends={
        Property(name="ProgrammeInstances24", type=university_Specializations, multiplicity=Multiplicity(1, 1)),
        Property(name="specializations", type=university_ProgrammeInstances, multiplicity=Multiplicity(1, 1))
    }
)
programmeSemester25: BinaryAssociation = BinaryAssociation(
    name="programmeSemester25",
    ends={
        Property(name="ProgrammeSemesters26", type=university_Specializations, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization", type=university_ProgrammeSemesters, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programmes27: BinaryAssociation = BinaryAssociation(
    name="programmes27",
    ends={
        Property(name="university_Programmes", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University", type=university_Programmes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
avaliableCourses19: BinaryAssociation = BinaryAssociation(
    name="avaliableCourses19",
    ends={
        Property(name="university_CourseInstances20", type=university_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Slot", type=university_CourseInstances, multiplicity=Multiplicity(0, 9999))
    }
)
courses28: BinaryAssociation = BinaryAssociation(
    name="courses28",
    ends={
        Property(name="university_Courses", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University29", type=university_Courses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters30: BinaryAssociation = BinaryAssociation(
    name="semesters30",
    ends={
        Property(name="university_Semesters32", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University31", type=university_Semesters, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="university",
    types={university_Programmes, university_ProgrammeInstances, university_ProgrammeSemesters, university_Specializations, university_Courses, university_Semesters, university_Slot, university_CourseInstances, university_University, SemesterTime, SlotType},
    associations={instances0, programme1, programmeSemesters2, specializations3, course6, semester8, programmeInstance9, slots11, semester12, specialization14, programmeSemester17, instances5, programmeSemesters21, programmeInstance23, programmeSemester25, programmes27, avaliableCourses19, courses28, semesters30},
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