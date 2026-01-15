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
refac_A = Class(name="refac::A")
refac_B = Class(name="refac::B")
refac_C = Class(name="refac::C")
refac_W = Class(name="refac::W")
refac_M = Class(name="refac::M")
refac_N99 = Class(name="refac::N99")
refac_X = Class(name="refac::X")
refac_K = Class(name="refac::K")

# refac_A class attributes and methods

# refac_B class attributes and methods

# refac_C class attributes and methods

# refac_W class attributes and methods
refac_W_name: Property = Property(name="name", type=StringType)
refac_W.attributes={refac_W_name}

# refac_M class attributes and methods

# refac_N99 class attributes and methods

# refac_X class attributes and methods

# refac_K class attributes and methods

# Relationships
cs1: BinaryAssociation = BinaryAssociation(
    name="cs1",
    ends={
        Property(name="refac_C", type=refac_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_A2", type=refac_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws3: BinaryAssociation = BinaryAssociation(
    name="ws3",
    ends={
        Property(name="refac_W", type=refac_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_A4", type=refac_W, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ms5: BinaryAssociation = BinaryAssociation(
    name="ms5",
    ends={
        Property(name="refac_M", type=refac_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_A6", type=refac_M, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ns9997: BinaryAssociation = BinaryAssociation(
    name="ns9997",
    ends={
        Property(name="refac_N99", type=refac_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_A8", type=refac_N99, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="refac_B", type=refac_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_A", type=refac_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b9: BinaryAssociation = BinaryAssociation(
    name="b9",
    ends={
        Property(name="refac_B11", type=refac_C, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_C10", type=refac_B, multiplicity=Multiplicity(0, 9999))
    }
)
as12: BinaryAssociation = BinaryAssociation(
    name="as12",
    ends={
        Property(name="refac_A13", type=refac_X, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_X", type=refac_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ks14: BinaryAssociation = BinaryAssociation(
    name="ks14",
    ends={
        Property(name="refac_K", type=refac_X, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_X15", type=refac_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wc16: BinaryAssociation = BinaryAssociation(
    name="wc16",
    ends={
        Property(name="refac_C18", type=refac_W, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_W17", type=refac_C, multiplicity=Multiplicity(0, 1))
    }
)
k19: BinaryAssociation = BinaryAssociation(
    name="k19",
    ends={
        Property(name="refac_K21", type=refac_M, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_M20", type=refac_K, multiplicity=Multiplicity(0, 1))
    }
)
k22: BinaryAssociation = BinaryAssociation(
    name="k22",
    ends={
        Property(name="refac_K24", type=refac_N99, multiplicity=Multiplicity(1, 1)),
        Property(name="refac_N9923", type=refac_K, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="refac",
    types={refac_A, refac_B, refac_C, refac_W, refac_M, refac_N99, refac_X, refac_K},
    associations={cs1, ws3, ms5, ns9997, bs0, b9, as12, ks14, wc16, k19, k22},
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