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
l1_A = Class(name="l1::A")
l1_B = Class(name="l1::B", is_abstract=True)

# l1_A class attributes and methods

# l1_B class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="l1_B", type=l1_A, multiplicity=Multiplicity(1, 1)),
        Property(name="l1_A", type=l1_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="l1",
    types={l1_A, l1_B},
    associations={b0},
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