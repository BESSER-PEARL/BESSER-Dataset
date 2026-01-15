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
CourseStatus: Enumeration = Enumeration(
    name="CourseStatus",
    literals={
            EnumerationLiteral(name="MANDATORY"),
			EnumerationLiteral(name="ELECTIVE")
    }
)

Season: Enumeration = Enumeration(
    name="Season",
    literals={
            EnumerationLiteral(name="SPRING"),
			EnumerationLiteral(name="FALL")
    }
)

# Classes
studyplan_Program = Class(name="studyplan::Program")
studyplan_Semester = Class(name="studyplan::Semester")
studyplan_Specialization = Class(name="studyplan::Specialization")
studyplan_SemesterCourse = Class(name="studyplan::SemesterCourse")
studyplan_Department = Class(name="studyplan::Department")
studyplan_Course = Class(name="studyplan::Course")

# studyplan_Program class attributes and methods
studyplan_Program_code: Property = Property(name="code", type=StringType)
studyplan_Program_name: Property = Property(name="name", type=StringType)
studyplan_Program.attributes={studyplan_Program_name, studyplan_Program_code}

# studyplan_Semester class attributes and methods
studyplan_Semester_name: Property = Property(name="name", type=StringType)
studyplan_Semester_season: Property = Property(name="season", type=StringType)
studyplan_Semester_year: Property = Property(name="year", type=IntegerType)
studyplan_Semester.attributes={studyplan_Semester_name, studyplan_Semester_year, studyplan_Semester_season}

# studyplan_Specialization class attributes and methods
studyplan_Specialization_name: Property = Property(name="name", type=StringType)
studyplan_Specialization.attributes={studyplan_Specialization_name}

# studyplan_SemesterCourse class attributes and methods
studyplan_SemesterCourse_status: Property = Property(name="status", type=StringType)
studyplan_SemesterCourse.attributes={studyplan_SemesterCourse_status}

# studyplan_Department class attributes and methods
studyplan_Department_name: Property = Property(name="name", type=StringType)
studyplan_Department.attributes={studyplan_Department_name}

# studyplan_Course class attributes and methods
studyplan_Course_code: Property = Property(name="code", type=StringType)
studyplan_Course_name: Property = Property(name="name", type=StringType)
studyplan_Course_credits: Property = Property(name="credits", type=FloatType)
studyplan_Course.attributes={studyplan_Course_code, studyplan_Course_credits, studyplan_Course_name}

# Relationships
semesters0: BinaryAssociation = BinaryAssociation(
    name="semesters0",
    ends={
        Property(name="studyplan_Semester", type=studyplan_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_Program", type=studyplan_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializations1: BinaryAssociation = BinaryAssociation(
    name="specializations1",
    ends={
        Property(name="studyplan_Specialization", type=studyplan_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_Program2", type=studyplan_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department3: BinaryAssociation = BinaryAssociation(
    name="department3",
    ends={
        Property(name="programs", type=studyplan_Department, multiplicity=Multiplicity(0, 1)),
        Property(name="Department", type=studyplan_Program, multiplicity=Multiplicity(1, 1))
    }
)
courses4: BinaryAssociation = BinaryAssociation(
    name="courses4",
    ends={
        Property(name="studyplan_SemesterCourse", type=studyplan_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_Semester5", type=studyplan_SemesterCourse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters6: BinaryAssociation = BinaryAssociation(
    name="semesters6",
    ends={
        Property(name="studyplan_Semester8", type=studyplan_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_Specialization7", type=studyplan_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department12: BinaryAssociation = BinaryAssociation(
    name="department12",
    ends={
        Property(name="Department13", type=studyplan_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=studyplan_Department, multiplicity=Multiplicity(0, 1))
    }
)
specializations10: BinaryAssociation = BinaryAssociation(
    name="specializations10",
    ends={
        Property(name="studyplan_Specialization11", type=studyplan_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_Specialization9", type=studyplan_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course14: BinaryAssociation = BinaryAssociation(
    name="course14",
    ends={
        Property(name="studyplan_Course", type=studyplan_SemesterCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="studyplan_SemesterCourse15", type=studyplan_Course, multiplicity=Multiplicity(0, 1))
    }
)
courses16: BinaryAssociation = BinaryAssociation(
    name="courses16",
    ends={
        Property(name="Course", type=studyplan_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=studyplan_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programs17: BinaryAssociation = BinaryAssociation(
    name="programs17",
    ends={
        Property(name="Program", type=studyplan_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department18", type=studyplan_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="studyplan",
    types={studyplan_Program, studyplan_Semester, studyplan_Specialization, studyplan_SemesterCourse, studyplan_Department, studyplan_Course, CourseStatus, Season},
    associations={semesters0, specializations1, department3, courses4, semesters6, department12, specializations10, course14, courses16, programs17},
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