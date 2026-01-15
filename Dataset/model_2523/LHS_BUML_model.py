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
LHS_C = Class(name="LHS::C")
LHS_D = Class(name="LHS::D")

# LHS_A class attributes and methods
LHS_A_name: Property = Property(name="name", type=StringType)
LHS_A.attributes={LHS_A_name}

# LHS_B class attributes and methods
LHS_B_name: Property = Property(name="name", type=StringType)
LHS_B.attributes={LHS_B_name}

# LHS_C class attributes and methods
LHS_C_name: Property = Property(name="name", type=StringType)
LHS_C.attributes={LHS_C_name}

# LHS_D class attributes and methods
LHS_D_name: Property = Property(name="name", type=StringType)
LHS_D.attributes={LHS_D_name}

# Relationships
refB0: BinaryAssociation = BinaryAssociation(
    name="refB0",
    ends={
        Property(name="LHS_B", type=LHS_A, multiplicity=Multiplicity(1, 1)),
        Property(name="LHS_A", type=LHS_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refC1: BinaryAssociation = BinaryAssociation(
    name="refC1",
    ends={
        Property(name="LHS_C", type=LHS_A, multiplicity=Multiplicity(1, 1)),
        Property(name="LHS_A2", type=LHS_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refD3: BinaryAssociation = BinaryAssociation(
    name="refD3",
    ends={
        Property(name="LHS_D", type=LHS_B, multiplicity=Multiplicity(1, 1)),
        Property(name="LHS_B4", type=LHS_D, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="LHS",
    types={LHS_A, LHS_B, LHS_C, LHS_D},
    associations={refB0, refC1, refD3},
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