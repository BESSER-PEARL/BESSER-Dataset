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
Courses_Assignment = Class(name="Courses::Assignment")
Courses_Course = Class(name="Courses::Course")
Courses_Person = Class(name="Courses::Person")
Courses_Answer = Class(name="Courses::Answer")

# Courses_Assignment class attributes and methods
Courses_Assignment_description: Property = Property(name="description", type=StringType)
Courses_Assignment_mandatory: Property = Property(name="mandatory", type=BooleanType)
Courses_Assignment_name: Property = Property(name="name", type=StringType)
Courses_Assignment.attributes={Courses_Assignment_name, Courses_Assignment_mandatory, Courses_Assignment_description}

# Courses_Course class attributes and methods
Courses_Course_name: Property = Property(name="name", type=StringType)
Courses_Course_id: Property = Property(name="id", type=StringType)
Courses_Course_credit: Property = Property(name="credit", type=FloatType)
Courses_Course.attributes={Courses_Course_credit, Courses_Course_id, Courses_Course_name}

# Courses_Person class attributes and methods
Courses_Person_name: Property = Property(name="name", type=StringType)
Courses_Person_id: Property = Property(name="id", type=IntegerType)
Courses_Person_role: Property = Property(name="role", type=StringType)
Courses_Person.attributes={Courses_Person_name, Courses_Person_role, Courses_Person_id}

# Courses_Answer class attributes and methods
Courses_Answer_id: Property = Property(name="id", type=IntegerType)
Courses_Answer_text: Property = Property(name="text", type=StringType)
Courses_Answer_pass: Property = Property(name="pass", type=BooleanType)
Courses_Answer.attributes={Courses_Answer_text, Courses_Answer_id, Courses_Answer_pass}

# Relationships
assignments1: BinaryAssociation = BinaryAssociation(
    name="assignments1",
    ends={
        Property(name="Courses_Assignment", type=Courses_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="Courses_Course2", type=Courses_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="Courses_Person", type=Courses_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="Courses_Course", type=Courses_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignmentDelivery3: BinaryAssociation = BinaryAssociation(
    name="assignmentDelivery3",
    ends={
        Property(name="Courses_Answer", type=Courses_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Courses_Person4", type=Courses_Answer, multiplicity=Multiplicity(0, 9999))
    }
)
answer5: BinaryAssociation = BinaryAssociation(
    name="answer5",
    ends={
        Property(name="Courses_Answer7", type=Courses_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="Courses_Assignment6", type=Courses_Answer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Courses",
    types={Courses_Assignment, Courses_Course, Courses_Person, Courses_Answer},
    associations={assignments1, members0, assignmentDelivery3, answer5},
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