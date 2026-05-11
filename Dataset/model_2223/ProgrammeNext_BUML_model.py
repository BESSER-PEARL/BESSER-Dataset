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
SemesterType: Enumeration = Enumeration(
    name="SemesterType",
    literals={
            EnumerationLiteral(name="FALL"),
			EnumerationLiteral(name="SPRING")
    }
)

ProgrammeType: Enumeration = Enumeration(
    name="ProgrammeType",
    literals={
            EnumerationLiteral(name="BACHELOR"),
			EnumerationLiteral(name="MASTER_2_YEARS"),
			EnumerationLiteral(name="INTEGRATED_MASTER"),
			EnumerationLiteral(name="YEAR_STUDY")
    }
)

CourseLevel: Enumeration = Enumeration(
    name="CourseLevel",
    literals={
            EnumerationLiteral(name="HIGHER"),
			EnumerationLiteral(name="PHD"),
			EnumerationLiteral(name="THIRD_YEAR")
    }
)

CourseType: Enumeration = Enumeration(
    name="CourseType",
    literals={
            EnumerationLiteral(name="Obligatory"),
			EnumerationLiteral(name="Elective"),
			EnumerationLiteral(name="M2A"),
			EnumerationLiteral(name="M1A")
    }
)

# Classes
programme_Department = Class(name="programme_Department")
programme_Programme = Class(name="programme_Programme")
programme_Course = Class(name="programme_Course")
programme_Specialization = Class(name="programme_Specialization")
programme_StudyYear = Class(name="programme_StudyYear")
programme_Semester = Class(name="programme_Semester")
programme_SemesterCourse = Class(name="programme_SemesterCourse")

# programme_Department class attributes and methods
programme_Department_name: Property = Property(name="name", type=StringType)
programme_Department.attributes={programme_Department_name}

# programme_Programme class attributes and methods
programme_Programme_name: Property = Property(name="name", type=StringType)
programme_Programme_programmeType: Property = Property(name="programmeType", type=StringType)
programme_Programme_code: Property = Property(name="code", type=StringType)
programme_Programme.attributes={programme_Programme_name, programme_Programme_programmeType, programme_Programme_code}

# programme_Course class attributes and methods
programme_Course_name: Property = Property(name="name", type=StringType)
programme_Course_code: Property = Property(name="code", type=StringType)
programme_Course_taugtIn: Property = Property(name="taugtIn", type=StringType)
programme_Course_level: Property = Property(name="level", type=StringType)
programme_Course_credits: Property = Property(name="credits", type=FloatType)
programme_Course.attributes={programme_Course_taugtIn, programme_Course_code, programme_Course_credits, programme_Course_level, programme_Course_name}

# programme_Specialization class attributes and methods
programme_Specialization_name: Property = Property(name="name", type=StringType)
programme_Specialization.attributes={programme_Specialization_name}

# programme_StudyYear class attributes and methods
programme_StudyYear_year: Property = Property(name="year", type=IntegerType)
programme_StudyYear.attributes={programme_StudyYear_year}

# programme_Semester class attributes and methods
programme_Semester_semesterType: Property = Property(name="semesterType", type=StringType)
programme_Semester.attributes={programme_Semester_semesterType}

# programme_SemesterCourse class attributes and methods
programme_SemesterCourse_courseType: Property = Property(name="courseType", type=StringType)
programme_SemesterCourse.attributes={programme_SemesterCourse_courseType}

# Relationships
studyYears10: BinaryAssociation = BinaryAssociation(
    name="studyYears10",
    ends={
        Property(name="programme_StudyYear12", type=programme_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="programme_Specialization11", type=programme_StudyYear, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programmes0: BinaryAssociation = BinaryAssociation(
    name="programmes0",
    ends={
        Property(name="programme_Programme", type=programme_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="programme_Department", type=programme_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses1: BinaryAssociation = BinaryAssociation(
    name="courses1",
    ends={
        Property(name="programme_Course", type=programme_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="programme_Department2", type=programme_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableSpecializations3: BinaryAssociation = BinaryAssociation(
    name="availableSpecializations3",
    ends={
        Property(name="programme_Specialization", type=programme_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programme_Programme4", type=programme_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyYears5: BinaryAssociation = BinaryAssociation(
    name="studyYears5",
    ends={
        Property(name="programme_StudyYear", type=programme_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programme_Programme6", type=programme_StudyYear, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableSpecializations8: BinaryAssociation = BinaryAssociation(
    name="availableSpecializations8",
    ends={
        Property(name="programme_Specialization9", type=programme_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="programme_Specialization7", type=programme_Specialization, multiplicity=Multiplicity(0, 9999))
    }
)
semesters13: BinaryAssociation = BinaryAssociation(
    name="semesters13",
    ends={
        Property(name="programme_Semester", type=programme_StudyYear, multiplicity=Multiplicity(1, 1)),
        Property(name="programme_StudyYear14", type=programme_Semester, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
courses15: BinaryAssociation = BinaryAssociation(
    name="courses15",
    ends={
        Property(name="programme_SemesterCourse", type=programme_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="programme_Semester16", type=programme_SemesterCourse, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
semesterCourse17: BinaryAssociation = BinaryAssociation(
    name="semesterCourse17",
    ends={
        Property(name="programme_Course19", type=programme_SemesterCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="programme_SemesterCourse18", type=programme_Course, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="programme",
    types={programme_Department, programme_Programme, programme_Course, programme_Specialization, programme_StudyYear, programme_Semester, programme_SemesterCourse, SemesterType, ProgrammeType, CourseLevel, CourseType},
    associations={studyYears10, programmes0, courses1, availableSpecializations3, studyYears5, availableSpecializations8, semesters13, courses15, semesterCourse17},
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