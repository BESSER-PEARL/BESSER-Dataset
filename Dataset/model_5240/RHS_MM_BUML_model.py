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
rhs_X = Class(name="rhs::X")
rhs_Y = Class(name="rhs::Y")

# rhs_X class attributes and methods
rhs_X_x: Property = Property(name="x", type=StringType)
rhs_X.attributes={rhs_X_x}

# rhs_Y class attributes and methods
rhs_Y_y: Property = Property(name="y", type=StringType)
rhs_Y.attributes={rhs_Y_y}

# Relationships
y0: BinaryAssociation = BinaryAssociation(
    name="y0",
    ends={
        Property(name="rhs_Y", type=rhs_X, multiplicity=Multiplicity(1, 1)),
        Property(name="rhs_X", type=rhs_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="rhs",
    types={rhs_X, rhs_Y},
    associations={y0},
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