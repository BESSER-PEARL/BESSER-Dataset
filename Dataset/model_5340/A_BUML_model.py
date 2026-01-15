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
A_A1 = Class(name="A::A1")
A_A2 = Class(name="A::A2")
A_A = Class(name="A::A")

# A_A1 class attributes and methods
A_A1_description: Property = Property(name="description", type=StringType)
A_A1.attributes={A_A1_description}

# A_A2 class attributes and methods
A_A2_description: Property = Property(name="description", type=StringType)
A_A2.attributes={A_A2_description}

# A_A class attributes and methods
A_A_name: Property = Property(name="name", type=StringType)
A_A.attributes={A_A_name}

# Relationships
elementA10: BinaryAssociation = BinaryAssociation(
    name="elementA10",
    ends={
        Property(name="A_A1", type=A_A, multiplicity=Multiplicity(1, 1)),
        Property(name="A_A", type=A_A1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementA21: BinaryAssociation = BinaryAssociation(
    name="elementA21",
    ends={
        Property(name="A_A2", type=A_A1, multiplicity=Multiplicity(1, 1)),
        Property(name="A_A12", type=A_A2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="A",
    types={A_A1, A_A2, A_A},
    associations={elementA10, elementA21},
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