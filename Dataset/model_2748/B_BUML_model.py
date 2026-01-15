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
B_B = Class(name="B::B")
B_RootB = Class(name="B::RootB")

# B_B class attributes and methods
B_B_b: Property = Property(name="b", type=IntegerType)
B_B.attributes={B_B_b}

# B_RootB class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="RootB", type=B_B, multiplicity=Multiplicity(1, 1)),
        Property(name="bs", type=B_RootB, multiplicity=Multiplicity(1, 1))
    }
)
bs1: BinaryAssociation = BinaryAssociation(
    name="bs1",
    ends={
        Property(name="B", type=B_RootB, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=B_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="B",
    types={B_B, B_RootB},
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