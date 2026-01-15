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
LHS_A = Class(name="LHS::A")
LHS_B = Class(name="LHS::B")

# LHS_A class attributes and methods
LHS_A_name: Property = Property(name="name", type=StringType)
LHS_A.attributes={LHS_A_name}

# LHS_B class attributes and methods
LHS_B_name: Property = Property(name="name", type=StringType)
LHS_B.attributes={LHS_B_name}

# Relationships
refB0: BinaryAssociation = BinaryAssociation(
    name="refB0",
    ends={
        Property(name="LHS_B", type=LHS_A, multiplicity=Multiplicity(1, 1)),
        Property(name="LHS_A", type=LHS_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="LHS",
    types={LHS_A, LHS_B},
    associations={refB0},
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