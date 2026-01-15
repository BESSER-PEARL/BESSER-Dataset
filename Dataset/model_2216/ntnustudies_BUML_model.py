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
courseType: Enumeration = Enumeration(
    name="courseType",
    literals={
            EnumerationLiteral(name="mandatory"),
			EnumerationLiteral(name="elective")
    }
)

semesterType: Enumeration = Enumeration(
    name="semesterType",
    literals={
            EnumerationLiteral(name="fall"),
			EnumerationLiteral(name="spring")
    }
)

courseLevel: Enumeration = Enumeration(
    name="courseLevel",
    literals={
            EnumerationLiteral(name="high"),
			EnumerationLiteral(name="basic"),
			EnumerationLiteral(name="medium")
    }
)

# Classes
ntnustudies_Course = Class(name="ntnustudies::Course")
ntnustudies_Programme = Class(name="ntnustudies::Programme")
ntnustudies_Specialization = Class(name="ntnustudies::Specialization")
ntnustudies_Semester = Class(name="ntnustudies::Semester")
ntnustudies_ChosenSemester = Class(name="ntnustudies::ChosenSemester")
ntnustudies_StudyPlan = Class(name="ntnustudies::StudyPlan")
ntnustudies_Department = Class(name="ntnustudies::Department")

# ntnustudies_Course class attributes and methods
ntnustudies_Course_code: Property = Property(name="code", type=StringType)
ntnustudies_Course_name: Property = Property(name="name", type=StringType)
ntnustudies_Course_credtis: Property = Property(name="credtis", type=FloatType)
ntnustudies_Course_semesters: Property = Property(name="semesters", type=StringType)
ntnustudies_Course_level: Property = Property(name="level", type=StringType)
ntnustudies_Course_type: Property = Property(name="type", type=StringType)
ntnustudies_Course.attributes={ntnustudies_Course_level, ntnustudies_Course_code, ntnustudies_Course_type, ntnustudies_Course_credtis, ntnustudies_Course_name, ntnustudies_Course_semesters}

# ntnustudies_Programme class attributes and methods
ntnustudies_Programme_name: Property = Property(name="name", type=StringType)
ntnustudies_Programme_years: Property = Property(name="years", type=IntegerType)
ntnustudies_Programme.attributes={ntnustudies_Programme_years, ntnustudies_Programme_name}

# ntnustudies_Specialization class attributes and methods
ntnustudies_Specialization_name: Property = Property(name="name", type=StringType)
ntnustudies_Specialization_specializationChoicePointSemester: Property = Property(name="specializationChoicePointSemester", type=IntegerType)
ntnustudies_Specialization.attributes={ntnustudies_Specialization_name, ntnustudies_Specialization_specializationChoicePointSemester}

# ntnustudies_Semester class attributes and methods
ntnustudies_Semester_type: Property = Property(name="type", type=StringType)
ntnustudies_Semester_year: Property = Property(name="year", type=IntegerType)
ntnustudies_Semester.attributes={ntnustudies_Semester_year, ntnustudies_Semester_type}

# ntnustudies_ChosenSemester class attributes and methods

# ntnustudies_StudyPlan class attributes and methods

# ntnustudies_Department class attributes and methods
ntnustudies_Department_name: Property = Property(name="name", type=StringType)
ntnustudies_Department_shortName: Property = Property(name="shortName", type=StringType)
ntnustudies_Department.attributes={ntnustudies_Department_name, ntnustudies_Department_shortName}

# Relationships
courses4: BinaryAssociation = BinaryAssociation(
    name="courses4",
    ends={
        Property(name="ntnustudies_Course", type=ntnustudies_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_Specialization", type=ntnustudies_Course, multiplicity=Multiplicity(0, 9999))
    }
)
requiredSpecialization6: BinaryAssociation = BinaryAssociation(
    name="requiredSpecialization6",
    ends={
        Property(name="ntnustudies_Specialization7", type=ntnustudies_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_Specialization5", type=ntnustudies_Specialization, multiplicity=Multiplicity(0, 1))
    }
)
specializations0: BinaryAssociation = BinaryAssociation(
    name="specializations0",
    ends={
        Property(name="Specialization", type=ntnustudies_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programme", type=ntnustudies_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters1: BinaryAssociation = BinaryAssociation(
    name="semesters1",
    ends={
        Property(name="Semester", type=ntnustudies_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programme2", type=ntnustudies_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programme3: BinaryAssociation = BinaryAssociation(
    name="programme3",
    ends={
        Property(name="Programme", type=ntnustudies_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specializations", type=ntnustudies_Programme, multiplicity=Multiplicity(0, 1))
    }
)
semester15: BinaryAssociation = BinaryAssociation(
    name="semester15",
    ends={
        Property(name="ntnustudies_Semester16", type=ntnustudies_ChosenSemester, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_ChosenSemester", type=ntnustudies_Semester, multiplicity=Multiplicity(0, 1))
    }
)
semesters8: BinaryAssociation = BinaryAssociation(
    name="semesters8",
    ends={
        Property(name="ntnustudies_Semester", type=ntnustudies_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_Specialization9", type=ntnustudies_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
possibleCourses10: BinaryAssociation = BinaryAssociation(
    name="possibleCourses10",
    ends={
        Property(name="ntnustudies_Course12", type=ntnustudies_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_Semester11", type=ntnustudies_Course, multiplicity=Multiplicity(0, 9999))
    }
)
programme13: BinaryAssociation = BinaryAssociation(
    name="programme13",
    ends={
        Property(name="Programme14", type=ntnustudies_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semesters", type=ntnustudies_Programme, multiplicity=Multiplicity(0, 1))
    }
)
courses17: BinaryAssociation = BinaryAssociation(
    name="courses17",
    ends={
        Property(name="ntnustudies_Course19", type=ntnustudies_ChosenSemester, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_ChosenSemester18", type=ntnustudies_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programme20: BinaryAssociation = BinaryAssociation(
    name="programme20",
    ends={
        Property(name="ntnustudies_Programme", type=ntnustudies_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_StudyPlan", type=ntnustudies_Programme, multiplicity=Multiplicity(0, 1))
    }
)
specializations21: BinaryAssociation = BinaryAssociation(
    name="specializations21",
    ends={
        Property(name="ntnustudies_Specialization23", type=ntnustudies_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_StudyPlan22", type=ntnustudies_Specialization, multiplicity=Multiplicity(0, 9999))
    }
)
chosenSemesters24: BinaryAssociation = BinaryAssociation(
    name="chosenSemesters24",
    ends={
        Property(name="ntnustudies_ChosenSemester26", type=ntnustudies_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_StudyPlan25", type=ntnustudies_ChosenSemester, multiplicity=Multiplicity(0, 9999))
    }
)
courses27: BinaryAssociation = BinaryAssociation(
    name="courses27",
    ends={
        Property(name="ntnustudies_Course28", type=ntnustudies_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_Department", type=ntnustudies_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programmes29: BinaryAssociation = BinaryAssociation(
    name="programmes29",
    ends={
        Property(name="ntnustudies_Programme31", type=ntnustudies_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="ntnustudies_Department30", type=ntnustudies_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ntnustudies",
    types={ntnustudies_Course, ntnustudies_Programme, ntnustudies_Specialization, ntnustudies_Semester, ntnustudies_ChosenSemester, ntnustudies_StudyPlan, ntnustudies_Department, courseType, semesterType, courseLevel},
    associations={courses4, requiredSpecialization6, specializations0, semesters1, programme3, semester15, semesters8, possibleCourses10, programme13, courses17, programme20, specializations21, chosenSemesters24, courses27, programmes29},
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