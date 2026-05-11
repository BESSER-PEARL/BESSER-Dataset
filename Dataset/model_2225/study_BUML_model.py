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
FallOrSpring: Enumeration = Enumeration(
    name="FallOrSpring",
    literals={
            EnumerationLiteral(name="Fall"),
			EnumerationLiteral(name="Spring")
    }
)

programmeCode: Enumeration = Enumeration(
    name="programmeCode",
    literals={
            EnumerationLiteral(name="Informatikk"),
			EnumerationLiteral(name="Datateknologi2"),
			EnumerationLiteral(name="Datateknologi5")
    }
)

# Classes
study_Department = Class(name="study_Department")
study_Programme = Class(name="study_Programme")
study_Course = Class(name="study_Course")
study_StudyPlan = Class(name="study_StudyPlan")
study_Specialization = Class(name="study_Specialization")
study_Semester = Class(name="study_Semester")
study_CourseSlot = Class(name="study_CourseSlot")

# study_Department class attributes and methods

# study_Programme class attributes and methods
study_Programme_name: Property = Property(name="name", type=StringType)
study_Programme_programmeCode: Property = Property(name="programmeCode", type=StringType)
study_Programme.attributes={study_Programme_programmeCode, study_Programme_name}

# study_Course class attributes and methods
study_Course_name: Property = Property(name="name", type=StringType)
study_Course_code: Property = Property(name="code", type=StringType)
study_Course_points: Property = Property(name="points", type=FloatType)
study_Course.attributes={study_Course_points, study_Course_name, study_Course_code}

# study_StudyPlan class attributes and methods

# study_Specialization class attributes and methods
study_Specialization_name: Property = Property(name="name", type=StringType)
study_Specialization.attributes={study_Specialization_name}

# study_Semester class attributes and methods
study_Semester_semesterNumber: Property = Property(name="semesterNumber", type=IntegerType)
study_Semester_fallOrSpring: Property = Property(name="fallOrSpring", type=StringType)
study_Semester.attributes={study_Semester_semesterNumber, study_Semester_fallOrSpring}

# study_CourseSlot class attributes and methods
study_CourseSlot_elective: Property = Property(name="elective", type=BooleanType)
study_CourseSlot.attributes={study_CourseSlot_elective}

# Relationships
programme0: BinaryAssociation = BinaryAssociation(
    name="programme0",
    ends={
        Property(name="study_Programme", type=study_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Department", type=study_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course1: BinaryAssociation = BinaryAssociation(
    name="course1",
    ends={
        Property(name="study_Course", type=study_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Department2", type=study_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyPlan3: BinaryAssociation = BinaryAssociation(
    name="studyPlan3",
    ends={
        Property(name="study_StudyPlan", type=study_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Programme4", type=study_StudyPlan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spesialization5: BinaryAssociation = BinaryAssociation(
    name="spesialization5",
    ends={
        Property(name="study_Specialization", type=study_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="study_StudyPlan6", type=study_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester7: BinaryAssociation = BinaryAssociation(
    name="semester7",
    ends={
        Property(name="study_Semester", type=study_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="study_StudyPlan8", type=study_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester9: BinaryAssociation = BinaryAssociation(
    name="semester9",
    ends={
        Property(name="study_Semester11", type=study_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Specialization10", type=study_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseSlot12: BinaryAssociation = BinaryAssociation(
    name="courseSlot12",
    ends={
        Property(name="study_CourseSlot", type=study_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Semester13", type=study_CourseSlot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mandatoryCourse14: BinaryAssociation = BinaryAssociation(
    name="mandatoryCourse14",
    ends={
        Property(name="study_Course16", type=study_CourseSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="study_CourseSlot15", type=study_Course, multiplicity=Multiplicity(0, 1))
    }
)
electiveCourses17: BinaryAssociation = BinaryAssociation(
    name="electiveCourses17",
    ends={
        Property(name="study_Course19", type=study_CourseSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="study_CourseSlot18", type=study_Course, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="study",
    types={study_Department, study_Programme, study_Course, study_StudyPlan, study_Specialization, study_Semester, study_CourseSlot, FallOrSpring, programmeCode},
    associations={programme0, course1, studyPlan3, spesialization5, semester7, semester9, courseSlot12, mandatoryCourse14, electiveCourses17},
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