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
ale2_B = Class(name="ale2::B")
ale2_RB = Class(name="ale2::RB", is_abstract=True)

# ale2_B class attributes and methods

# ale2_RB class attributes and methods

# Relationships
rb0: BinaryAssociation = BinaryAssociation(
    name="rb0",
    ends={
        Property(name="ale2_RB", type=ale2_B, multiplicity=Multiplicity(1, 1)),
        Property(name="ale2_B", type=ale2_RB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ale2",
    types={ale2_B, ale2_RB},
    associations={rb0},
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