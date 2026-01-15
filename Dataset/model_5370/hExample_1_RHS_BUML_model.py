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
hExample_1_RHS_X = Class(name="hExample::1::RHS::X")
hExample_1_RHS_Y = Class(name="hExample::1::RHS::Y")

# hExample_1_RHS_X class attributes and methods

# hExample_1_RHS_Y class attributes and methods
hExample_1_RHS_Y_label: Property = Property(name="label", type=StringType)
hExample_1_RHS_Y.attributes={hExample_1_RHS_Y_label}

# Relationships
link0: BinaryAssociation = BinaryAssociation(
    name="link0",
    ends={
        Property(name="hExample_1_RHS_Y", type=hExample_1_RHS_X, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_1_RHS_X", type=hExample_1_RHS_Y, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="hExample_1_RHS",
    types={hExample_1_RHS_X, hExample_1_RHS_Y},
    associations={link0},
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