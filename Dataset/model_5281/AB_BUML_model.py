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
AB_B = Class(name="AB_B")
AB_A = Class(name="AB_A")

# AB_B class attributes and methods
AB_B_name: Property = Property(name="name", type=StringType)
AB_B.attributes={AB_B_name}

# AB_A class attributes and methods
AB_A_i: Property = Property(name="i", type=IntegerType)
AB_A.attributes={AB_A_i}

# Relationships
a0: BinaryAssociation = BinaryAssociation(
    name="a0",
    ends={
        Property(name="AB_A", type=AB_B, multiplicity=Multiplicity(1, 1)),
        Property(name="AB_B", type=AB_A, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="AB",
    types={AB_B, AB_A},
    associations={a0},
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