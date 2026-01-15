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
university_Course = Class(name="university::Course")
university_Professor = Class(name="university::Professor")
university_University = Class(name="university::University")
university_Student = Class(name="university::Student")

# university_Course class attributes and methods
university_Course_name: Property = Property(name="name", type=StringType)
university_Course.attributes={university_Course_name}

# university_Professor class attributes and methods
university_Professor_name: Property = Property(name="name", type=StringType)
university_Professor.attributes={university_Professor_name}

# university_University class attributes and methods
university_University_name: Property = Property(name="name", type=StringType)
university_University.attributes={university_University_name}

# university_Student class attributes and methods
university_Student_MNR: Property = Property(name="MNR", type=StringType)
university_Student.attributes={university_Student_MNR}

# Relationships
professors0: BinaryAssociation = BinaryAssociation(
    name="professors0",
    ends={
        Property(name="Professor", type=university_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=university_Professor, multiplicity=Multiplicity(1, 9999))
    }
)
courses1: BinaryAssociation = BinaryAssociation(
    name="courses1",
    ends={
        Property(name="Course", type=university_Professor, multiplicity=Multiplicity(1, 1)),
        Property(name="professors", type=university_Course, multiplicity=Multiplicity(1, 9999))
    }
)
professors2: BinaryAssociation = BinaryAssociation(
    name="professors2",
    ends={
        Property(name="university_Professor", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University", type=university_Professor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses3: BinaryAssociation = BinaryAssociation(
    name="courses3",
    ends={
        Property(name="university_Course", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University4", type=university_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students5: BinaryAssociation = BinaryAssociation(
    name="students5",
    ends={
        Property(name="university_Student", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University6", type=university_Student, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
uni7: BinaryAssociation = BinaryAssociation(
    name="uni7",
    ends={
        Property(name="university_University9", type=university_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Student8", type=university_University, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="university",
    types={university_Course, university_Professor, university_University, university_Student},
    associations={professors0, courses1, professors2, courses3, students5, uni7},
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