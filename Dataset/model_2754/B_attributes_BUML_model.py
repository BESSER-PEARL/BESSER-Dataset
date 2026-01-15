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
BAttributes_B = Class(name="BAttributes::B")
BAttributes_RootB = Class(name="BAttributes::RootB")
BAttributes_Y = Class(name="BAttributes::Y")

# BAttributes_B class attributes and methods

# BAttributes_RootB class attributes and methods

# BAttributes_Y class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="RootB", type=BAttributes_B, multiplicity=Multiplicity(1, 1)),
        Property(name="bs", type=BAttributes_RootB, multiplicity=Multiplicity(1, 1))
    }
)
y1: BinaryAssociation = BinaryAssociation(
    name="y1",
    ends={
        Property(name="BAttributes_Y", type=BAttributes_B, multiplicity=Multiplicity(1, 1)),
        Property(name="BAttributes_B", type=BAttributes_Y, multiplicity=Multiplicity(1, 1))
    }
)
bs2: BinaryAssociation = BinaryAssociation(
    name="bs2",
    ends={
        Property(name="B", type=BAttributes_RootB, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=BAttributes_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ys3: BinaryAssociation = BinaryAssociation(
    name="ys3",
    ends={
        Property(name="BAttributes_Y4", type=BAttributes_RootB, multiplicity=Multiplicity(1, 1)),
        Property(name="BAttributes_RootB", type=BAttributes_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="BAttributes",
    types={BAttributes_B, BAttributes_RootB, BAttributes_Y},
    associations={root0, y1, bs2, ys3},
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