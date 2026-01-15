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
b_B = Class(name="b::B")
ASub = Class(name="ASub")

# b_B class attributes and methods

# ASub class attributes and methods

# Relationships
ref0: BinaryAssociation = BinaryAssociation(
    name="ref0",
    ends={
        Property(name="ASub", type=b_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b_B", type=ASub, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b",
    types={b_B, ASub},
    associations={ref0},
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