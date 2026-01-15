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
RHS_X = Class(name="RHS::X")
RHS_V = Class(name="RHS::V")
RHS_Y = Class(name="RHS::Y")
RHS_W = Class(name="RHS::W")

# RHS_X class attributes and methods
RHS_X_name: Property = Property(name="name", type=StringType)
RHS_X.attributes={RHS_X_name}

# RHS_V class attributes and methods
RHS_V_name: Property = Property(name="name", type=StringType)
RHS_V.attributes={RHS_V_name}

# RHS_Y class attributes and methods
RHS_Y_name: Property = Property(name="name", type=StringType)
RHS_Y.attributes={RHS_Y_name}

# RHS_W class attributes and methods
RHS_W_name: Property = Property(name="name", type=StringType)
RHS_W.attributes={RHS_W_name}

# Relationships
refV0: BinaryAssociation = BinaryAssociation(
    name="refV0",
    ends={
        Property(name="RHS_V", type=RHS_X, multiplicity=Multiplicity(1, 1)),
        Property(name="RHS_X", type=RHS_V, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refX1: BinaryAssociation = BinaryAssociation(
    name="refX1",
    ends={
        Property(name="RHS_X2", type=RHS_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="RHS_Y", type=RHS_X, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refW3: BinaryAssociation = BinaryAssociation(
    name="refW3",
    ends={
        Property(name="RHS_W", type=RHS_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="RHS_Y4", type=RHS_W, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="RHS",
    types={RHS_X, RHS_V, RHS_Y, RHS_W},
    associations={refV0, refX1, refW3},
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