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
RHS_Y = Class(name="RHS::Y")

# RHS_X class attributes and methods
RHS_X_name: Property = Property(name="name", type=StringType)
RHS_X.attributes={RHS_X_name}

# RHS_Y class attributes and methods
RHS_Y_name: Property = Property(name="name", type=StringType)
RHS_Y.attributes={RHS_Y_name}

# Relationships
refX0: BinaryAssociation = BinaryAssociation(
    name="refX0",
    ends={
        Property(name="RHS_X", type=RHS_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="RHS_Y", type=RHS_X, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="RHS",
    types={RHS_X, RHS_Y},
    associations={refX0},
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