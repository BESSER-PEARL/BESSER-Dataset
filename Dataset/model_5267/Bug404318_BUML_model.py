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
bug404318_A = Class(name="bug404318::A")
bug404318_B = Class(name="bug404318::B")

# bug404318_A class attributes and methods

# bug404318_B class attributes and methods

# Relationships
a0: BinaryAssociation = BinaryAssociation(
    name="a0",
    ends={
        Property(name="bug404318_A", type=bug404318_B, multiplicity=Multiplicity(1, 1)),
        Property(name="bug404318_B", type=bug404318_A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="bug404318",
    types={bug404318_A, bug404318_B},
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