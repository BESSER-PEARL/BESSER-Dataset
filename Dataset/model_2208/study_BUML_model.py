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
Season: Enumeration = Enumeration(
    name="Season",
    literals={
            EnumerationLiteral(name="FALL"),
			EnumerationLiteral(name="SPRING")
    }
)

IsMandatory: Enumeration = Enumeration(
    name="IsMandatory",
    literals={
            EnumerationLiteral(name="MANDATORY"),
			EnumerationLiteral(name="ELECTIVE")
    }
)

# Classes
study_SemesterCourse = Class(name="study::SemesterCourse")
study_Programme = Class(name="study::Programme")
study_Semester = Class(name="study::Semester")
study_Specialization = Class(name="study::Specialization")
study_Department = Class(name="study::Department")
study_Course = Class(name="study::Course")

# study_SemesterCourse class attributes and methods
study_SemesterCourse_mandatory: Property = Property(name="mandatory", type=StringType)
study_SemesterCourse.attributes={study_SemesterCourse_mandatory}

# study_Programme class attributes and methods
study_Programme_name: Property = Property(name="name", type=StringType)
study_Programme_code: Property = Property(name="code", type=StringType)
study_Programme_duration: Property = Property(name="duration", type=IntegerType)
study_Programme.attributes={study_Programme_code, study_Programme_duration, study_Programme_name}

# study_Semester class attributes and methods
study_Semester_year: Property = Property(name="year", type=IntegerType)
study_Semester_Season: Property = Property(name="Season", type=StringType)
study_Semester.attributes={study_Semester_Season, study_Semester_year}

# study_Specialization class attributes and methods
study_Specialization_name: Property = Property(name="name", type=StringType)
study_Specialization.attributes={study_Specialization_name}

# study_Department class attributes and methods
study_Department_name: Property = Property(name="name", type=StringType)
study_Department.attributes={study_Department_name}

# study_Course class attributes and methods
study_Course_credits: Property = Property(name="credits", type=FloatType)
study_Course_code: Property = Property(name="code", type=StringType)
study_Course_name: Property = Property(name="name", type=StringType)
study_Course_level: Property = Property(name="level", type=IntegerType)
study_Course.attributes={study_Course_code, study_Course_credits, study_Course_level, study_Course_name}

# Relationships
courses4: BinaryAssociation = BinaryAssociation(
    name="courses4",
    ends={
        Property(name="SemesterCourse", type=study_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=study_SemesterCourse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters0: BinaryAssociation = BinaryAssociation(
    name="semesters0",
    ends={
        Property(name="Semester", type=study_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programme", type=study_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializations1: BinaryAssociation = BinaryAssociation(
    name="specializations1",
    ends={
        Property(name="Specialization", type=study_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programme2", type=study_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department3: BinaryAssociation = BinaryAssociation(
    name="department3",
    ends={
        Property(name="Department", type=study_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programs", type=study_Department, multiplicity=Multiplicity(0, 1))
    }
)
programme5: BinaryAssociation = BinaryAssociation(
    name="programme5",
    ends={
        Property(name="Programme", type=study_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semesters", type=study_Programme, multiplicity=Multiplicity(0, 1))
    }
)
specialization6: BinaryAssociation = BinaryAssociation(
    name="specialization6",
    ends={
        Property(name="Specialization8", type=study_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semesters7", type=study_Specialization, multiplicity=Multiplicity(0, 1))
    }
)
semesters9: BinaryAssociation = BinaryAssociation(
    name="semesters9",
    ends={
        Property(name="Semester10", type=study_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization", type=study_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programme11: BinaryAssociation = BinaryAssociation(
    name="programme11",
    ends={
        Property(name="Programme12", type=study_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="specializations", type=study_Programme, multiplicity=Multiplicity(0, 1))
    }
)
course13: BinaryAssociation = BinaryAssociation(
    name="course13",
    ends={
        Property(name="study_Course", type=study_SemesterCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="study_SemesterCourse", type=study_Course, multiplicity=Multiplicity(0, 1))
    }
)
semester14: BinaryAssociation = BinaryAssociation(
    name="semester14",
    ends={
        Property(name="Semester15", type=study_SemesterCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=study_Semester, multiplicity=Multiplicity(0, 1))
    }
)
department16: BinaryAssociation = BinaryAssociation(
    name="department16",
    ends={
        Property(name="Department18", type=study_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses17", type=study_Department, multiplicity=Multiplicity(0, 1))
    }
)
courses19: BinaryAssociation = BinaryAssociation(
    name="courses19",
    ends={
        Property(name="Course", type=study_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=study_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programs20: BinaryAssociation = BinaryAssociation(
    name="programs20",
    ends={
        Property(name="Programme22", type=study_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department21", type=study_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="study",
    types={study_SemesterCourse, study_Programme, study_Semester, study_Specialization, study_Department, study_Course, Season, IsMandatory},
    associations={courses4, semesters0, specializations1, department3, programme5, specialization6, semesters9, programme11, course13, semester14, department16, courses19, programs20},
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