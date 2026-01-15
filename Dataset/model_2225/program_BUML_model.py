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
SemesterStatus: Enumeration = Enumeration(
    name="SemesterStatus",
    literals={
            EnumerationLiteral(name="FALL"),
			EnumerationLiteral(name="SPRING")
    }
)

CourseStatus: Enumeration = Enumeration(
    name="CourseStatus",
    literals={
            EnumerationLiteral(name="MANDATORY"),
			EnumerationLiteral(name="ELECTIVE")
    }
)

# Classes
Program_Program = Class(name="Program::Program")
Program_Semester = Class(name="Program::Semester")
Program_Specialization = Class(name="Program::Specialization")
Program_Course = Class(name="Program::Course")
Program_SemesterCourse = Class(name="Program::SemesterCourse")
Program_Department = Class(name="Program::Department")

# Program_Program class attributes and methods
Program_Program_name: Property = Property(name="name", type=StringType)
Program_Program_year: Property = Property(name="year", type=FloatType)
Program_Program.attributes={Program_Program_name, Program_Program_year}

# Program_Semester class attributes and methods
Program_Semester_status: Property = Property(name="status", type=StringType)
Program_Semester_name: Property = Property(name="name", type=StringType)
Program_Semester_code: Property = Property(name="code", type=StringType)
Program_Semester.attributes={Program_Semester_status, Program_Semester_code, Program_Semester_name}

# Program_Specialization class attributes and methods
Program_Specialization_name: Property = Property(name="name", type=StringType)
Program_Specialization.attributes={Program_Specialization_name}

# Program_Course class attributes and methods
Program_Course_name: Property = Property(name="name", type=StringType)
Program_Course_code: Property = Property(name="code", type=StringType)
Program_Course_credit: Property = Property(name="credit", type=FloatType)
Program_Course.attributes={Program_Course_code, Program_Course_name, Program_Course_credit}

# Program_SemesterCourse class attributes and methods
Program_SemesterCourse_status: Property = Property(name="status", type=StringType)
Program_SemesterCourse.attributes={Program_SemesterCourse_status}

# Program_Department class attributes and methods
Program_Department_name: Property = Property(name="name", type=StringType)
Program_Department.attributes={Program_Department_name}

# Relationships
semesters0: BinaryAssociation = BinaryAssociation(
    name="semesters0",
    ends={
        Property(name="Program_Semester", type=Program_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="Program_Program", type=Program_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializations1: BinaryAssociation = BinaryAssociation(
    name="specializations1",
    ends={
        Property(name="Program_Specialization", type=Program_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="Program_Program2", type=Program_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters3: BinaryAssociation = BinaryAssociation(
    name="semesters3",
    ends={
        Property(name="Program_Semester5", type=Program_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="Program_Specialization4", type=Program_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializations7: BinaryAssociation = BinaryAssociation(
    name="specializations7",
    ends={
        Property(name="Program_Specialization8", type=Program_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="Program_Specialization6", type=Program_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course10: BinaryAssociation = BinaryAssociation(
    name="course10",
    ends={
        Property(name="Program_Course", type=Program_SemesterCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="Program_SemesterCourse", type=Program_Course, multiplicity=Multiplicity(0, 1))
    }
)
semester11: BinaryAssociation = BinaryAssociation(
    name="semester11",
    ends={
        Property(name="Semester", type=Program_SemesterCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="semesterCourses", type=Program_Semester, multiplicity=Multiplicity(0, 1))
    }
)
semesterCourses9: BinaryAssociation = BinaryAssociation(
    name="semesterCourses9",
    ends={
        Property(name="SemesterCourse", type=Program_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=Program_SemesterCourse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department12: BinaryAssociation = BinaryAssociation(
    name="department12",
    ends={
        Property(name="Department", type=Program_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=Program_Department, multiplicity=Multiplicity(0, 1))
    }
)
programs13: BinaryAssociation = BinaryAssociation(
    name="programs13",
    ends={
        Property(name="Program_Program14", type=Program_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="Program_Department", type=Program_Program, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
courses15: BinaryAssociation = BinaryAssociation(
    name="courses15",
    ends={
        Property(name="Course", type=Program_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=Program_Course, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Program",
    types={Program_Program, Program_Semester, Program_Specialization, Program_Course, Program_SemesterCourse, Program_Department, SemesterStatus, CourseStatus},
    associations={semesters0, specializations1, semesters3, specializations7, course10, semester11, semesterCourses9, department12, programs13, courses15},
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