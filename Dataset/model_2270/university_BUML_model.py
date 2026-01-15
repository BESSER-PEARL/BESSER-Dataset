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
university_University = Class(name="university::University")
university_Course = Class(name="university::Course")
university_Student = Class(name="university::Student")

# university_University class attributes and methods
university_University_name: Property = Property(name="name", type=StringType)
university_University.attributes={university_University_name}

# university_Course class attributes and methods
university_Course_name: Property = Property(name="name", type=StringType)
university_Course.attributes={university_Course_name}

# university_Student class attributes and methods
university_Student_id: Property = Property(name="id", type=StringType)
university_Student.attributes={university_Student_id}

# Relationships
courses1: BinaryAssociation = BinaryAssociation(
    name="courses1",
    ends={
        Property(name="Course", type=university_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=university_Course, multiplicity=Multiplicity(1, 9999))
    }
)
students2: BinaryAssociation = BinaryAssociation(
    name="students2",
    ends={
        Property(name="university_Student", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University", type=university_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses3: BinaryAssociation = BinaryAssociation(
    name="courses3",
    ends={
        Property(name="university_Course", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University4", type=university_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students0: BinaryAssociation = BinaryAssociation(
    name="students0",
    ends={
        Property(name="Student", type=university_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=university_Student, multiplicity=Multiplicity(1, 10))
    }
)

# Domain Model
domain_model = DomainModel(
    name="university",
    types={university_University, university_Course, university_Student},
    associations={courses1, students2, courses3, students0},
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