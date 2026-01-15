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
reference_A = Class(name="reference::A")
Named = Class(name="Named")
reference_B = Class(name="reference::B")
reference_E = Class(name="reference::E")
reference_C = Class(name="reference::C")
reference_G = Class(name="reference::G")
reference_H = Class(name="reference::H")
reference_Named = Class(name="reference::Named")
reference_F = Class(name="reference::F")

# reference_A class attributes and methods

# Named class attributes and methods

# reference_B class attributes and methods

# reference_E class attributes and methods

# reference_C class attributes and methods

# reference_G class attributes and methods

# reference_H class attributes and methods

# reference_Named class attributes and methods
reference_Named_name: Property = Property(name="name", type=StringType)
reference_Named.attributes={reference_Named_name}

# reference_F class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="reference_B", type=reference_A, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_A", type=reference_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
acs3: BinaryAssociation = BinaryAssociation(
    name="acs3",
    ends={
        Property(name="reference_C", type=reference_A, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_A4", type=reference_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ags5: BinaryAssociation = BinaryAssociation(
    name="ags5",
    ends={
        Property(name="reference_G", type=reference_A, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_A6", type=reference_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ahs7: BinaryAssociation = BinaryAssociation(
    name="ahs7",
    ends={
        Property(name="reference_H", type=reference_A, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_A8", type=reference_H, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs9: BinaryAssociation = BinaryAssociation(
    name="cs9",
    ends={
        Property(name="reference_C11", type=reference_B, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_B10", type=reference_C, multiplicity=Multiplicity(0, 9999))
    }
)
gs12: BinaryAssociation = BinaryAssociation(
    name="gs12",
    ends={
        Property(name="reference_G14", type=reference_B, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_B13", type=reference_G, multiplicity=Multiplicity(0, 9999))
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="reference_E", type=reference_A, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_A2", type=reference_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs15: BinaryAssociation = BinaryAssociation(
    name="fs15",
    ends={
        Property(name="reference_F", type=reference_E, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_E16", type=reference_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hs17: BinaryAssociation = BinaryAssociation(
    name="hs17",
    ends={
        Property(name="reference_H19", type=reference_G, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_G18", type=reference_H, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_reference_A_Named = Generalization(general=Named, specific=reference_A)
gen_reference_B_Named = Generalization(general=Named, specific=reference_B)
gen_reference_E_Named = Generalization(general=Named, specific=reference_E)
gen_reference_F_Named = Generalization(general=Named, specific=reference_F)
gen_reference_G_Named = Generalization(general=Named, specific=reference_G)
gen_reference_C_Named = Generalization(general=Named, specific=reference_C)
gen_reference_H_Named = Generalization(general=Named, specific=reference_H)

# Domain Model
domain_model = DomainModel(
    name="reference",
    types={reference_A, Named, reference_B, reference_E, reference_C, reference_G, reference_H, reference_Named, reference_F},
    associations={bs0, acs3, ags5, ahs7, cs9, gs12, es1, fs15, hs17},
    generalizations={gen_reference_A_Named, gen_reference_B_Named, gen_reference_E_Named, gen_reference_F_Named, gen_reference_G_Named, gen_reference_C_Named, gen_reference_H_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)