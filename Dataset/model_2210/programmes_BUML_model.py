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
Access: Enumeration = Enumeration(
    name="Access",
    literals={
            EnumerationLiteral(name="O"),
			EnumerationLiteral(name="M2A"),
			EnumerationLiteral(name="M1A"),
			EnumerationLiteral(name="VA"),
			EnumerationLiteral(name="NA")
    }
)

SemesterSeason: Enumeration = Enumeration(
    name="SemesterSeason",
    literals={
            EnumerationLiteral(name="Spring"),
			EnumerationLiteral(name="Fall")
    }
)

# Classes
StudyProgrammes_Department = Class(name="StudyProgrammes::Department")
StudyProgrammes_Semester = Class(name="StudyProgrammes::Semester")
StudyProgrammes_CourseAccess = Class(name="StudyProgrammes::CourseAccess")
StudyProgrammes_Programme = Class(name="StudyProgrammes::Programme")
StudyProgrammes_Course = Class(name="StudyProgrammes::Course")
StudyProgrammes_Specialization = Class(name="StudyProgrammes::Specialization")

# StudyProgrammes_Department class attributes and methods
StudyProgrammes_Department_name: Property = Property(name="name", type=StringType)
StudyProgrammes_Department.attributes={StudyProgrammes_Department_name}

# StudyProgrammes_Semester class attributes and methods
StudyProgrammes_Semester_code: Property = Property(name="code", type=StringType)
StudyProgrammes_Semester_year: Property = Property(name="year", type=IntegerType)
StudyProgrammes_Semester_semesterSeason: Property = Property(name="semesterSeason", type=StringType)
StudyProgrammes_Semester.attributes={StudyProgrammes_Semester_semesterSeason, StudyProgrammes_Semester_year, StudyProgrammes_Semester_code}

# StudyProgrammes_CourseAccess class attributes and methods
StudyProgrammes_CourseAccess_access: Property = Property(name="access", type=StringType)
StudyProgrammes_CourseAccess.attributes={StudyProgrammes_CourseAccess_access}

# StudyProgrammes_Programme class attributes and methods
StudyProgrammes_Programme_name: Property = Property(name="name", type=StringType)
StudyProgrammes_Programme_code: Property = Property(name="code", type=StringType)
StudyProgrammes_Programme_startYear: Property = Property(name="startYear", type=IntegerType)
StudyProgrammes_Programme_totalNumberOfSemesters: Property = Property(name="totalNumberOfSemesters", type=IntegerType)
StudyProgrammes_Programme_semestersBeforeSpecialization: Property = Property(name="semestersBeforeSpecialization", type=IntegerType)
StudyProgrammes_Programme.attributes={StudyProgrammes_Programme_semestersBeforeSpecialization, StudyProgrammes_Programme_name, StudyProgrammes_Programme_startYear, StudyProgrammes_Programme_totalNumberOfSemesters, StudyProgrammes_Programme_code}

# StudyProgrammes_Course class attributes and methods
StudyProgrammes_Course_name: Property = Property(name="name", type=StringType)
StudyProgrammes_Course_code: Property = Property(name="code", type=StringType)
StudyProgrammes_Course_credits: Property = Property(name="credits", type=FloatType)
StudyProgrammes_Course_availableSemesters: Property = Property(name="availableSemesters", type=StringType)
StudyProgrammes_Course.attributes={StudyProgrammes_Course_credits, StudyProgrammes_Course_availableSemesters, StudyProgrammes_Course_name, StudyProgrammes_Course_code}

# StudyProgrammes_Specialization class attributes and methods
StudyProgrammes_Specialization_name: Property = Property(name="name", type=StringType)
StudyProgrammes_Specialization_startSemester: Property = Property(name="startSemester", type=IntegerType)
StudyProgrammes_Specialization_lengthInSemesters: Property = Property(name="lengthInSemesters", type=IntegerType)
StudyProgrammes_Specialization.attributes={StudyProgrammes_Specialization_name, StudyProgrammes_Specialization_lengthInSemesters, StudyProgrammes_Specialization_startSemester}

# Relationships
semesters5: BinaryAssociation = BinaryAssociation(
    name="semesters5",
    ends={
        Property(name="StudyProgrammes_Semester", type=StudyProgrammes_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgrammes_Programme6", type=StudyProgrammes_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters7: BinaryAssociation = BinaryAssociation(
    name="semesters7",
    ends={
        Property(name="StudyProgrammes_Semester9", type=StudyProgrammes_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgrammes_Specialization8", type=StudyProgrammes_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseAccesses10: BinaryAssociation = BinaryAssociation(
    name="courseAccesses10",
    ends={
        Property(name="StudyProgrammes_CourseAccess", type=StudyProgrammes_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgrammes_Semester11", type=StudyProgrammes_CourseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programmes0: BinaryAssociation = BinaryAssociation(
    name="programmes0",
    ends={
        Property(name="StudyProgrammes_Programme", type=StudyProgrammes_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgrammes_Department", type=StudyProgrammes_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses1: BinaryAssociation = BinaryAssociation(
    name="courses1",
    ends={
        Property(name="StudyProgrammes_Course", type=StudyProgrammes_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgrammes_Department2", type=StudyProgrammes_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializations3: BinaryAssociation = BinaryAssociation(
    name="specializations3",
    ends={
        Property(name="StudyProgrammes_Specialization", type=StudyProgrammes_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgrammes_Programme4", type=StudyProgrammes_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course12: BinaryAssociation = BinaryAssociation(
    name="course12",
    ends={
        Property(name="StudyProgrammes_Course14", type=StudyProgrammes_CourseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgrammes_CourseAccess13", type=StudyProgrammes_Course, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="StudyProgrammes",
    types={StudyProgrammes_Department, StudyProgrammes_Semester, StudyProgrammes_CourseAccess, StudyProgrammes_Programme, StudyProgrammes_Course, StudyProgrammes_Specialization, Access, SemesterSeason},
    associations={semesters5, semesters7, courseAccesses10, programmes0, courses1, specializations3, course12},
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