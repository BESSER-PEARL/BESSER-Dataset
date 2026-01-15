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
dmm_Person = Class(name="dmm::Person", is_abstract=True)
dmm_Student = Class(name="dmm::Student")
Person = Class(name="Person")
dmm_Course = Class(name="dmm::Course")
dmm_Professor = Class(name="dmm::Professor")
dmm_Exam = Class(name="dmm::Exam")
dmm_UniversityManagementSystem = Class(name="dmm::UniversityManagementSystem")

# dmm_Person class attributes and methods
dmm_Person_name: Property = Property(name="name", type=StringType)
dmm_Person_email: Property = Property(name="email", type=StringType)
dmm_Person.attributes={dmm_Person_email, dmm_Person_name}

# dmm_Student class attributes and methods
dmm_Student_matriculationNumber: Property = Property(name="matriculationNumber", type=IntegerType)
dmm_Student.attributes={dmm_Student_matriculationNumber}

# Person class attributes and methods

# dmm_Course class attributes and methods
dmm_Course_courseType: Property = Property(name="courseType", type=StringType)
dmm_Course_name: Property = Property(name="name", type=StringType)
dmm_Course_courseNumber: Property = Property(name="courseNumber", type=IntegerType)
dmm_Course.attributes={dmm_Course_name, dmm_Course_courseNumber, dmm_Course_courseType}

# dmm_Professor class attributes and methods
dmm_Professor_employeeNumber: Property = Property(name="employeeNumber", type=IntegerType)
dmm_Professor.attributes={dmm_Professor_employeeNumber}

# dmm_Exam class attributes and methods
dmm_Exam_examID: Property = Property(name="examID", type=StringType)
dmm_Exam.attributes={dmm_Exam_examID}

# dmm_UniversityManagementSystem class attributes and methods

# Relationships
attends0: BinaryAssociation = BinaryAssociation(
    name="attends0",
    ends={
        Property(name="dmm_Course", type=dmm_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="dmm_Student", type=dmm_Course, multiplicity=Multiplicity(0, 9999))
    }
)
mandatoryFor4: BinaryAssociation = BinaryAssociation(
    name="mandatoryFor4",
    ends={
        Property(name="dmm_Course5", type=dmm_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="dmm_Course3", type=dmm_Course, multiplicity=Multiplicity(0, 9999))
    }
)
exam6: BinaryAssociation = BinaryAssociation(
    name="exam6",
    ends={
        Property(name="dmm_Exam", type=dmm_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="dmm_Course7", type=dmm_Exam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course8: BinaryAssociation = BinaryAssociation(
    name="course8",
    ends={
        Property(name="dmm_Course9", type=dmm_UniversityManagementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="dmm_UniversityManagementSystem", type=dmm_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person10: BinaryAssociation = BinaryAssociation(
    name="person10",
    ends={
        Property(name="dmm_Person", type=dmm_UniversityManagementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="dmm_UniversityManagementSystem11", type=dmm_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lectures1: BinaryAssociation = BinaryAssociation(
    name="lectures1",
    ends={
        Property(name="dmm_Course2", type=dmm_Professor, multiplicity=Multiplicity(1, 1)),
        Property(name="dmm_Professor", type=dmm_Course, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_dmm_Student_Person = Generalization(general=Person, specific=dmm_Student)
gen_dmm_Professor_Person = Generalization(general=Person, specific=dmm_Professor)

# Domain Model
domain_model = DomainModel(
    name="dmm",
    types={dmm_Person, dmm_Student, Person, dmm_Course, dmm_Professor, dmm_Exam, dmm_UniversityManagementSystem, CourseType},
    associations={attends0, mandatoryFor4, exam6, course8, person10, lectures1},
    generalizations={gen_dmm_Student_Person, gen_dmm_Professor_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)