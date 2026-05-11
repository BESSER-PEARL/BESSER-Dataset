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
refs_A = Class(name="refs_A")
Named = Class(name="Named")
refs_B = Class(name="refs_B")
refs_E = Class(name="refs_E")
refs_C = Class(name="refs_C")
refs_G = Class(name="refs_G")
refs_H = Class(name="refs_H")
refs_F = Class(name="refs_F")
refs_Named = Class(name="refs_Named")

# refs_A class attributes and methods

# Named class attributes and methods

# refs_B class attributes and methods

# refs_E class attributes and methods

# refs_C class attributes and methods

# refs_G class attributes and methods

# refs_H class attributes and methods

# refs_F class attributes and methods

# refs_Named class attributes and methods
refs_Named_name: Property = Property(name="name", type=StringType)
refs_Named.attributes={refs_Named_name}

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="refs_B", type=refs_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refs_A", type=refs_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="refs_E", type=refs_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refs_A2", type=refs_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acs3: BinaryAssociation = BinaryAssociation(
    name="acs3",
    ends={
        Property(name="refs_C", type=refs_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refs_A4", type=refs_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ags5: BinaryAssociation = BinaryAssociation(
    name="ags5",
    ends={
        Property(name="refs_G", type=refs_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refs_A6", type=refs_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ahs7: BinaryAssociation = BinaryAssociation(
    name="ahs7",
    ends={
        Property(name="refs_H", type=refs_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refs_A8", type=refs_H, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs15: BinaryAssociation = BinaryAssociation(
    name="fs15",
    ends={
        Property(name="refs_F", type=refs_E, multiplicity=Multiplicity(1, 1)),
        Property(name="refs_E16", type=refs_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hs17: BinaryAssociation = BinaryAssociation(
    name="hs17",
    ends={
        Property(name="refs_H19", type=refs_G, multiplicity=Multiplicity(1, 1)),
        Property(name="refs_G18", type=refs_H, multiplicity=Multiplicity(0, 9999))
    }
)
cs9: BinaryAssociation = BinaryAssociation(
    name="cs9",
    ends={
        Property(name="refs_C11", type=refs_B, multiplicity=Multiplicity(1, 1)),
        Property(name="refs_B10", type=refs_C, multiplicity=Multiplicity(0, 9999))
    }
)
gs12: BinaryAssociation = BinaryAssociation(
    name="gs12",
    ends={
        Property(name="refs_G14", type=refs_B, multiplicity=Multiplicity(1, 1)),
        Property(name="refs_B13", type=refs_G, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_refs_A_Named = Generalization(general=Named, specific=refs_A)
gen_refs_B_Named = Generalization(general=Named, specific=refs_B)
gen_refs_E_Named = Generalization(general=Named, specific=refs_E)
gen_refs_F_Named = Generalization(general=Named, specific=refs_F)
gen_refs_G_Named = Generalization(general=Named, specific=refs_G)
gen_refs_H_Named = Generalization(general=Named, specific=refs_H)
gen_refs_C_Named = Generalization(general=Named, specific=refs_C)

# Domain Model
domain_model = DomainModel(
    name="refs",
    types={refs_A, Named, refs_B, refs_E, refs_C, refs_G, refs_H, refs_F, refs_Named},
    associations={bs0, es1, acs3, ags5, ahs7, fs15, hs17, cs9, gs12},
    generalizations={gen_refs_A_Named, gen_refs_B_Named, gen_refs_E_Named, gen_refs_F_Named, gen_refs_G_Named, gen_refs_H_Named, gen_refs_C_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)