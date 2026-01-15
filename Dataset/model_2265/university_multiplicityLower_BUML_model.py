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
TUWien_University = Class(name="TUWien::University")
TUWien_Course = Class(name="TUWien::Course")
TUWien_Student = Class(name="TUWien::Student")

# TUWien_University class attributes and methods
TUWien_University_name: Property = Property(name="name", type=StringType)
TUWien_University.attributes={TUWien_University_name}

# TUWien_Course class attributes and methods
TUWien_Course_id: Property = Property(name="id", type=StringType)
TUWien_Course_name: Property = Property(name="name", type=StringType)
TUWien_Course.attributes={TUWien_Course_id, TUWien_Course_name}

# TUWien_Student class attributes and methods
TUWien_Student_name: Property = Property(name="name", type=StringType)
TUWien_Student_id: Property = Property(name="id", type=IntegerType)
TUWien_Student.attributes={TUWien_Student_name, TUWien_Student_id}

# Relationships
course3: BinaryAssociation = BinaryAssociation(
    name="course3",
    ends={
        Property(name="Course", type=TUWien_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=TUWien_Course, multiplicity=Multiplicity(1, 9999))
    }
)
student4: BinaryAssociation = BinaryAssociation(
    name="student4",
    ends={
        Property(name="Student", type=TUWien_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=TUWien_Student, multiplicity=Multiplicity(5, 9999))
    }
)
courses0: BinaryAssociation = BinaryAssociation(
    name="courses0",
    ends={
        Property(name="TUWien_Course", type=TUWien_University, multiplicity=Multiplicity(1, 1)),
        Property(name="TUWien_University", type=TUWien_Course, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
students1: BinaryAssociation = BinaryAssociation(
    name="students1",
    ends={
        Property(name="TUWien_Student", type=TUWien_University, multiplicity=Multiplicity(1, 1)),
        Property(name="TUWien_University2", type=TUWien_Student, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="TUWien",
    types={TUWien_University, TUWien_Course, TUWien_Student},
    associations={course3, student4, courses0, students1},
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