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
Level: Enumeration = Enumeration(
    name="Level",
    literals={
            EnumerationLiteral(name="Bachelor"),
			EnumerationLiteral(name="Master")
    }
)

AvailableSemesters: Enumeration = Enumeration(
    name="AvailableSemesters",
    literals={
            EnumerationLiteral(name="Fall"),
			EnumerationLiteral(name="Spring"),
			EnumerationLiteral(name="Both")
    }
)

SemesterType: Enumeration = Enumeration(
    name="SemesterType",
    literals={
            EnumerationLiteral(name="Fall"),
			EnumerationLiteral(name="Spring")
    }
)

Access: Enumeration = Enumeration(
    name="Access",
    literals={
            EnumerationLiteral(name="M1A"),
			EnumerationLiteral(name="M2A"),
			EnumerationLiteral(name="NoAccess"),
			EnumerationLiteral(name="O"),
			EnumerationLiteral(name="VA"),
			EnumerationLiteral(name="VB")
    }
)

# Classes
studyprograms_Specialisation = Class(name="studyprograms::Specialisation")
studyprograms_Semester = Class(name="studyprograms::Semester")
studyprograms_Course = Class(name="studyprograms::Course")
studyprograms_Programme = Class(name="studyprograms::Programme")
studyprograms_CourseAccess = Class(name="studyprograms::CourseAccess")
studyprograms_Department = Class(name="studyprograms::Department")

# studyprograms_Specialisation class attributes and methods
studyprograms_Specialisation_name: Property = Property(name="name", type=StringType)
studyprograms_Specialisation_startSemester: Property = Property(name="startSemester", type=IntegerType)
studyprograms_Specialisation.attributes={studyprograms_Specialisation_startSemester, studyprograms_Specialisation_name}

# studyprograms_Semester class attributes and methods
studyprograms_Semester_semesterType: Property = Property(name="semesterType", type=StringType)
studyprograms_Semester_semesterCode: Property = Property(name="semesterCode", type=StringType)
studyprograms_Semester_year: Property = Property(name="year", type=IntegerType)
studyprograms_Semester.attributes={studyprograms_Semester_year, studyprograms_Semester_semesterType, studyprograms_Semester_semesterCode}

# studyprograms_Course class attributes and methods
studyprograms_Course_code: Property = Property(name="code", type=StringType)
studyprograms_Course_name: Property = Property(name="name", type=StringType)
studyprograms_Course_ects: Property = Property(name="ects", type=FloatType)
studyprograms_Course_level: Property = Property(name="level", type=StringType)
studyprograms_Course_availableSemester: Property = Property(name="availableSemester", type=StringType)
studyprograms_Course.attributes={studyprograms_Course_availableSemester, studyprograms_Course_ects, studyprograms_Course_name, studyprograms_Course_code, studyprograms_Course_level}

# studyprograms_Programme class attributes and methods
studyprograms_Programme_name: Property = Property(name="name", type=StringType)
studyprograms_Programme_code: Property = Property(name="code", type=StringType)
studyprograms_Programme_startYear: Property = Property(name="startYear", type=IntegerType)
studyprograms_Programme_duration: Property = Property(name="duration", type=IntegerType)
studyprograms_Programme.attributes={studyprograms_Programme_name, studyprograms_Programme_duration, studyprograms_Programme_startYear, studyprograms_Programme_code}

# studyprograms_CourseAccess class attributes and methods
studyprograms_CourseAccess_Access: Property = Property(name="Access", type=StringType)
studyprograms_CourseAccess.attributes={studyprograms_CourseAccess_Access}

# studyprograms_Department class attributes and methods
studyprograms_Department_code: Property = Property(name="code", type=StringType)
studyprograms_Department_name: Property = Property(name="name", type=StringType)
studyprograms_Department.attributes={studyprograms_Department_name, studyprograms_Department_code}

# Relationships
specialisations0: BinaryAssociation = BinaryAssociation(
    name="specialisations0",
    ends={
        Property(name="studyprograms_Specialisation", type=studyprograms_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Programme", type=studyprograms_Specialisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters1: BinaryAssociation = BinaryAssociation(
    name="semesters1",
    ends={
        Property(name="studyprograms_Semester", type=studyprograms_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Programme2", type=studyprograms_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses11: BinaryAssociation = BinaryAssociation(
    name="courses11",
    ends={
        Property(name="studyprograms_Course", type=studyprograms_CourseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_CourseAccess12", type=studyprograms_Course, multiplicity=Multiplicity(0, 9999))
    }
)
semesters3: BinaryAssociation = BinaryAssociation(
    name="semesters3",
    ends={
        Property(name="studyprograms_Semester5", type=studyprograms_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Specialisation4", type=studyprograms_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializations7: BinaryAssociation = BinaryAssociation(
    name="specializations7",
    ends={
        Property(name="studyprograms_Specialisation8", type=studyprograms_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Specialisation6", type=studyprograms_Specialisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseAccess9: BinaryAssociation = BinaryAssociation(
    name="courseAccess9",
    ends={
        Property(name="studyprograms_CourseAccess", type=studyprograms_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Semester10", type=studyprograms_CourseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programmes13: BinaryAssociation = BinaryAssociation(
    name="programmes13",
    ends={
        Property(name="studyprograms_Programme14", type=studyprograms_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Department", type=studyprograms_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses15: BinaryAssociation = BinaryAssociation(
    name="courses15",
    ends={
        Property(name="studyprograms_Course17", type=studyprograms_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Department16", type=studyprograms_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="studyprograms",
    types={studyprograms_Specialisation, studyprograms_Semester, studyprograms_Course, studyprograms_Programme, studyprograms_CourseAccess, studyprograms_Department, Level, AvailableSemesters, SemesterType, Access},
    associations={specialisations0, semesters1, courses11, semesters3, specializations7, courseAccess9, programmes13, courses15},
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