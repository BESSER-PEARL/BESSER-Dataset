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
BBase_B = Class(name="BBase::B")
BBase_RootB = Class(name="BBase::RootB")

# BBase_B class attributes and methods

# BBase_RootB class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="RootB", type=BBase_B, multiplicity=Multiplicity(1, 1)),
        Property(name="bs", type=BBase_RootB, multiplicity=Multiplicity(1, 1))
    }
)
bs1: BinaryAssociation = BinaryAssociation(
    name="bs1",
    ends={
        Property(name="B", type=BBase_RootB, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=BBase_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="BBase",
    types={BBase_B, BBase_RootB},
    associations={root0, bs1},
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