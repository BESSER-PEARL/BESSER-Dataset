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
link_A = Class(name="link::A")
Named = Class(name="Named")
link_M = Class(name="link::M")
link_N99 = Class(name="link::N99")
link_B = Class(name="link::B")
link_C = Class(name="link::C")
link_W = Class(name="link::W")
link_X = Class(name="link::X")
link_K = Class(name="link::K")
link_D = Class(name="link::D")
link_Named = Class(name="link::Named", is_abstract=True)

# link_A class attributes and methods

# Named class attributes and methods

# link_M class attributes and methods

# link_N99 class attributes and methods

# link_B class attributes and methods

# link_C class attributes and methods

# link_W class attributes and methods

# link_X class attributes and methods

# link_K class attributes and methods

# link_D class attributes and methods

# link_Named class attributes and methods
link_Named_name: Property = Property(name="name", type=StringType)
link_Named.attributes={link_Named_name}

# Relationships
ws3: BinaryAssociation = BinaryAssociation(
    name="ws3",
    ends={
        Property(name="link_A4", type=link_W, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="link_W", type=link_A, multiplicity=Multiplicity(1, 1))
    }
)
ms5: BinaryAssociation = BinaryAssociation(
    name="ms5",
    ends={
        Property(name="link_M", type=link_A, multiplicity=Multiplicity(1, 1)),
        Property(name="link_A6", type=link_M, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ns9997: BinaryAssociation = BinaryAssociation(
    name="ns9997",
    ends={
        Property(name="link_N99", type=link_A, multiplicity=Multiplicity(1, 1)),
        Property(name="link_A8", type=link_N99, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="link_B", type=link_A, multiplicity=Multiplicity(1, 1)),
        Property(name="link_A", type=link_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs1: BinaryAssociation = BinaryAssociation(
    name="cs1",
    ends={
        Property(name="link_C", type=link_A, multiplicity=Multiplicity(1, 1)),
        Property(name="link_A2", type=link_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
as14: BinaryAssociation = BinaryAssociation(
    name="as14",
    ends={
        Property(name="link_A15", type=link_X, multiplicity=Multiplicity(1, 1)),
        Property(name="link_X", type=link_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b9: BinaryAssociation = BinaryAssociation(
    name="b9",
    ends={
        Property(name="link_B11", type=link_C, multiplicity=Multiplicity(1, 1)),
        Property(name="link_C10", type=link_B, multiplicity=Multiplicity(0, 1))
    }
)
ds12: BinaryAssociation = BinaryAssociation(
    name="ds12",
    ends={
        Property(name="link_D", type=link_C, multiplicity=Multiplicity(1, 1)),
        Property(name="link_C13", type=link_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ks16: BinaryAssociation = BinaryAssociation(
    name="ks16",
    ends={
        Property(name="link_K", type=link_X, multiplicity=Multiplicity(1, 1)),
        Property(name="link_X17", type=link_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wc18: BinaryAssociation = BinaryAssociation(
    name="wc18",
    ends={
        Property(name="link_C20", type=link_W, multiplicity=Multiplicity(1, 1)),
        Property(name="link_W19", type=link_C, multiplicity=Multiplicity(0, 1))
    }
)
mk21: BinaryAssociation = BinaryAssociation(
    name="mk21",
    ends={
        Property(name="link_K23", type=link_M, multiplicity=Multiplicity(1, 1)),
        Property(name="link_M22", type=link_K, multiplicity=Multiplicity(0, 1))
    }
)
ma24: BinaryAssociation = BinaryAssociation(
    name="ma24",
    ends={
        Property(name="link_A26", type=link_M, multiplicity=Multiplicity(1, 1)),
        Property(name="link_M25", type=link_A, multiplicity=Multiplicity(0, 1))
    }
)
nk27: BinaryAssociation = BinaryAssociation(
    name="nk27",
    ends={
        Property(name="link_K29", type=link_N99, multiplicity=Multiplicity(1, 1)),
        Property(name="link_N9928", type=link_K, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_link_A_Named = Generalization(general=Named, specific=link_A)
gen_link_B_Named = Generalization(general=Named, specific=link_B)
gen_link_X_Named = Generalization(general=Named, specific=link_X)
gen_link_C_Named = Generalization(general=Named, specific=link_C)
gen_link_K_Named = Generalization(general=Named, specific=link_K)
gen_link_M_Named = Generalization(general=Named, specific=link_M)
gen_link_W_Named = Generalization(general=Named, specific=link_W)
gen_link_D_Named = Generalization(general=Named, specific=link_D)
gen_link_N99_Named = Generalization(general=Named, specific=link_N99)

# Domain Model
domain_model = DomainModel(
    name="link",
    types={link_A, Named, link_M, link_N99, link_B, link_C, link_W, link_X, link_K, link_D, link_Named},
    associations={ws3, ms5, ns9997, bs0, cs1, as14, b9, ds12, ks16, wc18, mk21, ma24, nk27},
    generalizations={gen_link_A_Named, gen_link_B_Named, gen_link_X_Named, gen_link_C_Named, gen_link_K_Named, gen_link_M_Named, gen_link_W_Named, gen_link_D_Named, gen_link_N99_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)