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
BKeys_B = Class(name="BKeys::B")
BKeys_RootB = Class(name="BKeys::RootB")
BKeys_Y = Class(name="BKeys::Y")

# BKeys_B class attributes and methods

# BKeys_RootB class attributes and methods

# BKeys_Y class attributes and methods

# Relationships
ys3: BinaryAssociation = BinaryAssociation(
    name="ys3",
    ends={
        Property(name="BKeys_Y", type=BKeys_RootB, multiplicity=Multiplicity(1, 1)),
        Property(name="BKeys_RootB", type=BKeys_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b4: BinaryAssociation = BinaryAssociation(
    name="b4",
    ends={
        Property(name="B5", type=BKeys_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="y", type=BKeys_B, multiplicity=Multiplicity(0, 1))
    }
)
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="RootB", type=BKeys_B, multiplicity=Multiplicity(1, 1)),
        Property(name="bs", type=BKeys_RootB, multiplicity=Multiplicity(1, 1))
    }
)
y1: BinaryAssociation = BinaryAssociation(
    name="y1",
    ends={
        Property(name="Y", type=BKeys_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b", type=BKeys_Y, multiplicity=Multiplicity(1, 1))
    }
)
bs2: BinaryAssociation = BinaryAssociation(
    name="bs2",
    ends={
        Property(name="B", type=BKeys_RootB, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=BKeys_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="BKeys",
    types={BKeys_B, BKeys_RootB, BKeys_Y},
    associations={ys3, b4, root0, y1, bs2},
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