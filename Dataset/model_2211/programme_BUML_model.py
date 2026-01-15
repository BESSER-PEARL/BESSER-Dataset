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

# Classes
StudyProgramme_Programme = Class(name="StudyProgramme::Programme")
StudyProgramme_Semester = Class(name="StudyProgramme::Semester")
StudyProgramme_Specialization = Class(name="StudyProgramme::Specialization")
StudyProgramme_Course = Class(name="StudyProgramme::Course")
StudyProgramme_CourseGroup = Class(name="StudyProgramme::CourseGroup")
StudyProgramme_Department = Class(name="StudyProgramme::Department")

# StudyProgramme_Programme class attributes and methods
StudyProgramme_Programme_name: Property = Property(name="name", type=StringType)
StudyProgramme_Programme_code: Property = Property(name="code", type=StringType)
StudyProgramme_Programme_duration: Property = Property(name="duration", type=IntegerType)
StudyProgramme_Programme.attributes={StudyProgramme_Programme_duration, StudyProgramme_Programme_code, StudyProgramme_Programme_name}

# StudyProgramme_Semester class attributes and methods
StudyProgramme_Semester_totalCredits: Property = Property(name="totalCredits", type=FloatType)
StudyProgramme_Semester_season: Property = Property(name="season", type=StringType)
StudyProgramme_Semester_creditConstraint: Property = Property(name="creditConstraint", type=StringType)
StudyProgramme_Semester_number: Property = Property(name="number", type=IntegerType)
StudyProgramme_Semester.attributes={StudyProgramme_Semester_season, StudyProgramme_Semester_number, StudyProgramme_Semester_creditConstraint, StudyProgramme_Semester_totalCredits}

# StudyProgramme_Specialization class attributes and methods
StudyProgramme_Specialization_name: Property = Property(name="name", type=StringType)
StudyProgramme_Specialization.attributes={StudyProgramme_Specialization_name}

# StudyProgramme_Course class attributes and methods
StudyProgramme_Course_name: Property = Property(name="name", type=StringType)
StudyProgramme_Course_code: Property = Property(name="code", type=StringType)
StudyProgramme_Course_credits: Property = Property(name="credits", type=FloatType)
StudyProgramme_Course_level: Property = Property(name="level", type=StringType)
StudyProgramme_Course.attributes={StudyProgramme_Course_credits, StudyProgramme_Course_code, StudyProgramme_Course_level, StudyProgramme_Course_name}

# StudyProgramme_CourseGroup class attributes and methods
StudyProgramme_CourseGroup_status: Property = Property(name="status", type=StringType)
StudyProgramme_CourseGroup.attributes={StudyProgramme_CourseGroup_status}

# StudyProgramme_Department class attributes and methods
StudyProgramme_Department_name: Property = Property(name="name", type=StringType)
StudyProgramme_Department_code: Property = Property(name="code", type=StringType)
StudyProgramme_Department.attributes={StudyProgramme_Department_name, StudyProgramme_Department_code}

# Relationships
programmeSemester0: BinaryAssociation = BinaryAssociation(
    name="programmeSemester0",
    ends={
        Property(name="StudyProgramme_Semester", type=StudyProgramme_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgramme_Programme", type=StudyProgramme_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programmeSpecializaton1: BinaryAssociation = BinaryAssociation(
    name="programmeSpecializaton1",
    ends={
        Property(name="StudyProgramme_Specialization", type=StudyProgramme_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgramme_Programme2", type=StudyProgramme_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseList3: BinaryAssociation = BinaryAssociation(
    name="courseList3",
    ends={
        Property(name="StudyProgramme_Course", type=StudyProgramme_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgramme_Semester4", type=StudyProgramme_Course, multiplicity=Multiplicity(0, 9999))
    }
)
courseGroups5: BinaryAssociation = BinaryAssociation(
    name="courseGroups5",
    ends={
        Property(name="StudyProgramme_CourseGroup", type=StudyProgramme_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgramme_Semester6", type=StudyProgramme_CourseGroup, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
specializationCourse7: BinaryAssociation = BinaryAssociation(
    name="specializationCourse7",
    ends={
        Property(name="StudyProgramme_Course9", type=StudyProgramme_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgramme_Specialization8", type=StudyProgramme_Course, multiplicity=Multiplicity(0, 1))
    }
)
semesters10: BinaryAssociation = BinaryAssociation(
    name="semesters10",
    ends={
        Property(name="StudyProgramme_Semester12", type=StudyProgramme_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgramme_Specialization11", type=StudyProgramme_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializations14: BinaryAssociation = BinaryAssociation(
    name="specializations14",
    ends={
        Property(name="StudyProgramme_Specialization15", type=StudyProgramme_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgramme_Specialization13", type=StudyProgramme_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coursesInGroup16: BinaryAssociation = BinaryAssociation(
    name="coursesInGroup16",
    ends={
        Property(name="StudyProgramme_Course18", type=StudyProgramme_CourseGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgramme_CourseGroup17", type=StudyProgramme_Course, multiplicity=Multiplicity(1, 9999))
    }
)
programmes19: BinaryAssociation = BinaryAssociation(
    name="programmes19",
    ends={
        Property(name="StudyProgramme_Programme20", type=StudyProgramme_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgramme_Department", type=StudyProgramme_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course21: BinaryAssociation = BinaryAssociation(
    name="course21",
    ends={
        Property(name="StudyProgramme_Course23", type=StudyProgramme_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="StudyProgramme_Department22", type=StudyProgramme_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="StudyProgramme",
    types={StudyProgramme_Programme, StudyProgramme_Semester, StudyProgramme_Specialization, StudyProgramme_Course, StudyProgramme_CourseGroup, StudyProgramme_Department},
    associations={programmeSemester0, programmeSpecializaton1, courseList3, courseGroups5, specializationCourse7, semesters10, specializations14, coursesInGroup16, programmes19, course21},
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