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
programmeCode: Enumeration = Enumeration(
    name="programmeCode",
    literals={
            EnumerationLiteral(name="Datateknologi5"),
			EnumerationLiteral(name="Informatikk"),
			EnumerationLiteral(name="Datateknologi2")
    }
)

FallOrSpring: Enumeration = Enumeration(
    name="FallOrSpring",
    literals={
            EnumerationLiteral(name="Fall"),
			EnumerationLiteral(name="Spring")
    }
)

# Classes
study_StudyPlan = Class(name="study::StudyPlan")
study_Specialization = Class(name="study::Specialization")
study_Department = Class(name="study::Department")
study_Programme = Class(name="study::Programme")
study_Course = Class(name="study::Course")
study_CourseSlot = Class(name="study::CourseSlot")
study_Semester = Class(name="study::Semester")

# study_StudyPlan class attributes and methods

# study_Specialization class attributes and methods
study_Specialization_name: Property = Property(name="name", type=StringType)
study_Specialization.attributes={study_Specialization_name}

# study_Department class attributes and methods

# study_Programme class attributes and methods
study_Programme_name: Property = Property(name="name", type=StringType)
study_Programme_programmeCode: Property = Property(name="programmeCode", type=StringType)
study_Programme.attributes={study_Programme_programmeCode, study_Programme_name}

# study_Course class attributes and methods
study_Course_name: Property = Property(name="name", type=StringType)
study_Course_code: Property = Property(name="code", type=StringType)
study_Course_points: Property = Property(name="points", type=FloatType)
study_Course.attributes={study_Course_name, study_Course_points, study_Course_code}

# study_CourseSlot class attributes and methods
study_CourseSlot_elective: Property = Property(name="elective", type=BooleanType)
study_CourseSlot.attributes={study_CourseSlot_elective}

# study_Semester class attributes and methods
study_Semester_fallOrSpring: Property = Property(name="fallOrSpring", type=StringType)
study_Semester_semesterNumber: Property = Property(name="semesterNumber", type=IntegerType)
study_Semester.attributes={study_Semester_semesterNumber, study_Semester_fallOrSpring}

# Relationships
studyPlan3: BinaryAssociation = BinaryAssociation(
    name="studyPlan3",
    ends={
        Property(name="study_StudyPlan", type=study_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="study_Programme4", type=study_StudyPlan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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

# Domain Model
domain_model = DomainModel(
    name="study",
    types={study_StudyPlan, study_Specialization, study_Department, study_Programme, study_Course, study_CourseSlot, study_Semester, programmeCode, FallOrSpring},
    associations={studyPlan3, programme0, course1, courseSlot12, mandatoryCourse14, electiveCourses17, spesialization5, semester7, semester9},
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