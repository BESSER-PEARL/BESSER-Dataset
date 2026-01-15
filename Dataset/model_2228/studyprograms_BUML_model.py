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

Access: Enumeration = Enumeration(
    name="Access",
    literals={
            EnumerationLiteral(name="O"),
			EnumerationLiteral(name="VA"),
			EnumerationLiteral(name="VB"),
			EnumerationLiteral(name="M1A"),
			EnumerationLiteral(name="M2A"),
			EnumerationLiteral(name="NoAccess")
    }
)

SemesterType: Enumeration = Enumeration(
    name="SemesterType",
    literals={
            EnumerationLiteral(name="Fall"),
			EnumerationLiteral(name="Spring")
    }
)

# Classes
studyprograms_Course = Class(name="studyprograms::Course")
studyprograms_Specialisation = Class(name="studyprograms::Specialisation")
studyprograms_Semester = Class(name="studyprograms::Semester")
studyprograms_Programme = Class(name="studyprograms::Programme")
studyprograms_CourseAccess = Class(name="studyprograms::CourseAccess")
studyprograms_IndividualStudyPlan = Class(name="studyprograms::IndividualStudyPlan")
studyprograms_Department = Class(name="studyprograms::Department")

# studyprograms_Course class attributes and methods
studyprograms_Course_ects: Property = Property(name="ects", type=FloatType)
studyprograms_Course_level: Property = Property(name="level", type=StringType)
studyprograms_Course_code: Property = Property(name="code", type=StringType)
studyprograms_Course_name: Property = Property(name="name", type=StringType)
studyprograms_Course_availableSemester: Property = Property(name="availableSemester", type=StringType)
studyprograms_Course.attributes={studyprograms_Course_name, studyprograms_Course_availableSemester, studyprograms_Course_code, studyprograms_Course_level, studyprograms_Course_ects}

# studyprograms_Specialisation class attributes and methods
studyprograms_Specialisation_name: Property = Property(name="name", type=StringType)
studyprograms_Specialisation_startSemester: Property = Property(name="startSemester", type=IntegerType)
studyprograms_Specialisation.attributes={studyprograms_Specialisation_startSemester, studyprograms_Specialisation_name}

# studyprograms_Semester class attributes and methods
studyprograms_Semester_semesterCode: Property = Property(name="semesterCode", type=StringType)
studyprograms_Semester_year: Property = Property(name="year", type=IntegerType)
studyprograms_Semester_semesterType: Property = Property(name="semesterType", type=StringType)
studyprograms_Semester.attributes={studyprograms_Semester_semesterType, studyprograms_Semester_semesterCode, studyprograms_Semester_year}

# studyprograms_Programme class attributes and methods
studyprograms_Programme_startYear: Property = Property(name="startYear", type=IntegerType)
studyprograms_Programme_duration: Property = Property(name="duration", type=IntegerType)
studyprograms_Programme_name: Property = Property(name="name", type=StringType)
studyprograms_Programme_code: Property = Property(name="code", type=StringType)
studyprograms_Programme.attributes={studyprograms_Programme_name, studyprograms_Programme_code, studyprograms_Programme_startYear, studyprograms_Programme_duration}

# studyprograms_CourseAccess class attributes and methods
studyprograms_CourseAccess_Access: Property = Property(name="Access", type=StringType)
studyprograms_CourseAccess.attributes={studyprograms_CourseAccess_Access}

# studyprograms_IndividualStudyPlan class attributes and methods
studyprograms_IndividualStudyPlan_studentNo: Property = Property(name="studentNo", type=StringType)
studyprograms_IndividualStudyPlan.attributes={studyprograms_IndividualStudyPlan_studentNo}

# studyprograms_Department class attributes and methods
studyprograms_Department_name: Property = Property(name="name", type=StringType)
studyprograms_Department_code: Property = Property(name="code", type=StringType)
studyprograms_Department.attributes={studyprograms_Department_code, studyprograms_Department_name}

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
courseAccess8: BinaryAssociation = BinaryAssociation(
    name="courseAccess8",
    ends={
        Property(name="studyprograms_CourseAccess", type=studyprograms_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Semester9", type=studyprograms_CourseAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters3: BinaryAssociation = BinaryAssociation(
    name="semesters3",
    ends={
        Property(name="studyprograms_Semester5", type=studyprograms_Specialisation, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Specialisation4", type=studyprograms_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters6: BinaryAssociation = BinaryAssociation(
    name="semesters6",
    ends={
        Property(name="studyprograms_Semester7", type=studyprograms_IndividualStudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_IndividualStudyPlan", type=studyprograms_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses10: BinaryAssociation = BinaryAssociation(
    name="courses10",
    ends={
        Property(name="studyprograms_Course", type=studyprograms_CourseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_CourseAccess11", type=studyprograms_Course, multiplicity=Multiplicity(0, 9999))
    }
)
programmes12: BinaryAssociation = BinaryAssociation(
    name="programmes12",
    ends={
        Property(name="studyprograms_Programme13", type=studyprograms_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Department", type=studyprograms_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses14: BinaryAssociation = BinaryAssociation(
    name="courses14",
    ends={
        Property(name="studyprograms_Course16", type=studyprograms_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprograms_Department15", type=studyprograms_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="studyprograms",
    types={studyprograms_Course, studyprograms_Specialisation, studyprograms_Semester, studyprograms_Programme, studyprograms_CourseAccess, studyprograms_IndividualStudyPlan, studyprograms_Department, Level, AvailableSemesters, Access, SemesterType},
    associations={specialisations0, semesters1, courseAccess8, semesters3, semesters6, courses10, programmes12, courses14},
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