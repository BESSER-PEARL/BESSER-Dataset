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
            EnumerationLiteral(name="Autumn"),
			EnumerationLiteral(name="Spring")
    }
)

CourseType: Enumeration = Enumeration(
    name="CourseType",
    literals={
            EnumerationLiteral(name="MANDATORY"),
			EnumerationLiteral(name="ELECTIVE")
    }
)

StudyLevel: Enumeration = Enumeration(
    name="StudyLevel",
    literals={
            EnumerationLiteral(name="FIRST_YEAR"),
			EnumerationLiteral(name="SECOND_YEAR"),
			EnumerationLiteral(name="THIRD_YEAR"),
			EnumerationLiteral(name="SECOND_DEGREE"),
			EnumerationLiteral(name="POST_GRAD")
    }
)

# Classes
programmes_Course = Class(name="programmes::Course")
programmes_Programme = Class(name="programmes::Programme")
programmes_Specialization = Class(name="programmes::Specialization")
programmes_Semester = Class(name="programmes::Semester")
programmes_CourseGroup = Class(name="programmes::CourseGroup")
Programme = Class(name="Programme")
programmes_University = Class(name="programmes::University")

# programmes_Course class attributes and methods
programmes_Course_code: Property = Property(name="code", type=StringType)
programmes_Course_name: Property = Property(name="name", type=StringType)
programmes_Course_credits: Property = Property(name="credits", type=FloatType)
programmes_Course_level: Property = Property(name="level", type=StringType)
programmes_Course.attributes={programmes_Course_name, programmes_Course_level, programmes_Course_credits, programmes_Course_code}

# programmes_Programme class attributes and methods
programmes_Programme_name: Property = Property(name="name", type=StringType)
programmes_Programme_code: Property = Property(name="code", type=StringType)
programmes_Programme.attributes={programmes_Programme_code, programmes_Programme_name}

# programmes_Specialization class attributes and methods

# programmes_Semester class attributes and methods
programmes_Semester_year: Property = Property(name="year", type=IntegerType)
programmes_Semester_semesterType: Property = Property(name="semesterType", type=StringType)
programmes_Semester.attributes={programmes_Semester_year, programmes_Semester_semesterType}

# programmes_CourseGroup class attributes and methods
programmes_CourseGroup_name: Property = Property(name="name", type=StringType)
programmes_CourseGroup_coursesType: Property = Property(name="coursesType", type=StringType)
programmes_CourseGroup.attributes={programmes_CourseGroup_coursesType, programmes_CourseGroup_name}

# Programme class attributes and methods

# programmes_University class attributes and methods
programmes_University_name: Property = Property(name="name", type=StringType)
programmes_University.attributes={programmes_University_name}

# Relationships
specializations0: BinaryAssociation = BinaryAssociation(
    name="specializations0",
    ends={
        Property(name="Specialization", type=programmes_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="specializesIn", type=programmes_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programmeSemester1: BinaryAssociation = BinaryAssociation(
    name="programmeSemester1",
    ends={
        Property(name="Semester", type=programmes_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programme", type=programmes_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseGroups2: BinaryAssociation = BinaryAssociation(
    name="courseGroups2",
    ends={
        Property(name="programmes_CourseGroup", type=programmes_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programmes_Programme", type=programmes_CourseGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializesIn3: BinaryAssociation = BinaryAssociation(
    name="specializesIn3",
    ends={
        Property(name="Programme", type=programmes_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specializations", type=programmes_Programme, multiplicity=Multiplicity(0, 1))
    }
)
chosenIn4: BinaryAssociation = BinaryAssociation(
    name="chosenIn4",
    ends={
        Property(name="programmes_Semester", type=programmes_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="programmes_Specialization", type=programmes_Semester, multiplicity=Multiplicity(1, 1))
    }
)
programme5: BinaryAssociation = BinaryAssociation(
    name="programme5",
    ends={
        Property(name="Programme6", type=programmes_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="programmeSemester", type=programmes_Programme, multiplicity=Multiplicity(1, 1))
    }
)
courses7: BinaryAssociation = BinaryAssociation(
    name="courses7",
    ends={
        Property(name="programmes_Course", type=programmes_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="programmes_Semester8", type=programmes_Course, multiplicity=Multiplicity(0, 9999))
    }
)
courses9: BinaryAssociation = BinaryAssociation(
    name="courses9",
    ends={
        Property(name="programmes_Course11", type=programmes_CourseGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="programmes_CourseGroup10", type=programmes_Course, multiplicity=Multiplicity(0, 9999))
    }
)
studyProgrammes12: BinaryAssociation = BinaryAssociation(
    name="studyProgrammes12",
    ends={
        Property(name="programmes_Programme13", type=programmes_University, multiplicity=Multiplicity(1, 1)),
        Property(name="programmes_University", type=programmes_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses14: BinaryAssociation = BinaryAssociation(
    name="courses14",
    ends={
        Property(name="programmes_Course16", type=programmes_University, multiplicity=Multiplicity(1, 1)),
        Property(name="programmes_University15", type=programmes_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_programmes_Specialization_Programme = Generalization(general=Programme, specific=programmes_Specialization)

# Domain Model
domain_model = DomainModel(
    name="programmes",
    types={programmes_Course, programmes_Programme, programmes_Specialization, programmes_Semester, programmes_CourseGroup, Programme, programmes_University, SemesterType, CourseType, StudyLevel},
    associations={specializations0, programmeSemester1, courseGroups2, specializesIn3, chosenIn4, programme5, courses7, courses9, studyProgrammes12, courses14},
    generalizations={gen_programmes_Specialization_Programme},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)