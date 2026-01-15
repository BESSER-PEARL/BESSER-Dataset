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
CourseType: Enumeration = Enumeration(
    name="CourseType",
    literals={
            EnumerationLiteral(name="VO"),
			EnumerationLiteral(name="UE"),
			EnumerationLiteral(name="SEM"),
			EnumerationLiteral(name="PR")
    }
)

# Classes
University_Person = Class(name="University::Person", is_abstract=True)
University_Student = Class(name="University::Student")
Person = Class(name="Person")
University_Professor = Class(name="University::Professor")
University_Course = Class(name="University::Course")
University_Exam = Class(name="University::Exam")
University_UniversityManagementSystem = Class(name="University::UniversityManagementSystem")

# University_Person class attributes and methods
University_Person_name: Property = Property(name="name", type=StringType)
University_Person_email: Property = Property(name="email", type=StringType)
University_Person.attributes={University_Person_name, University_Person_email}

# University_Student class attributes and methods
University_Student_matriculationNumber: Property = Property(name="matriculationNumber", type=IntegerType)
University_Student.attributes={University_Student_matriculationNumber}

# Person class attributes and methods

# University_Professor class attributes and methods
University_Professor_employeeNumber: Property = Property(name="employeeNumber", type=IntegerType)
University_Professor.attributes={University_Professor_employeeNumber}

# University_Course class attributes and methods
University_Course_name: Property = Property(name="name", type=StringType)
University_Course_courseNumber: Property = Property(name="courseNumber", type=IntegerType)
University_Course_courseType: Property = Property(name="courseType", type=StringType)
University_Course.attributes={University_Course_name, University_Course_courseType, University_Course_courseNumber}

# University_Exam class attributes and methods
University_Exam_examID: Property = Property(name="examID", type=StringType)
University_Exam.attributes={University_Exam_examID}

# University_UniversityManagementSystem class attributes and methods

# Relationships
attends0: BinaryAssociation = BinaryAssociation(
    name="attends0",
    ends={
        Property(name="University_Course", type=University_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="University_Student", type=University_Course, multiplicity=Multiplicity(0, 9999))
    }
)
lectures1: BinaryAssociation = BinaryAssociation(
    name="lectures1",
    ends={
        Property(name="University_Course2", type=University_Professor, multiplicity=Multiplicity(1, 1)),
        Property(name="University_Professor", type=University_Course, multiplicity=Multiplicity(0, 9999))
    }
)
exam6: BinaryAssociation = BinaryAssociation(
    name="exam6",
    ends={
        Property(name="University_Exam", type=University_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="University_Course7", type=University_Exam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mandatoryFor4: BinaryAssociation = BinaryAssociation(
    name="mandatoryFor4",
    ends={
        Property(name="University_Course5", type=University_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="University_Course3", type=University_Course, multiplicity=Multiplicity(0, 9999))
    }
)
course8: BinaryAssociation = BinaryAssociation(
    name="course8",
    ends={
        Property(name="University_Course9", type=University_UniversityManagementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="University_UniversityManagementSystem", type=University_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person10: BinaryAssociation = BinaryAssociation(
    name="person10",
    ends={
        Property(name="University_Person", type=University_UniversityManagementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="University_UniversityManagementSystem11", type=University_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_University_Student_Person = Generalization(general=Person, specific=University_Student)
gen_University_Professor_Person = Generalization(general=Person, specific=University_Professor)

# Domain Model
domain_model = DomainModel(
    name="University",
    types={University_Person, University_Student, Person, University_Professor, University_Course, University_Exam, University_UniversityManagementSystem, CourseType},
    associations={attends0, lectures1, exam6, mandatoryFor4, course8, person10},
    generalizations={gen_University_Student_Person, gen_University_Professor_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)