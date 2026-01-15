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
containment_A = Class(name="containment::A")
Named = Class(name="Named")
containment_B = Class(name="containment::B")
containment_E = Class(name="containment::E")
containment_Named = Class(name="containment::Named")
containment_C = Class(name="containment::C")
containment_G = Class(name="containment::G")
containment_F = Class(name="containment::F")
containment_H = Class(name="containment::H")

# containment_A class attributes and methods

# Named class attributes and methods

# containment_B class attributes and methods

# containment_E class attributes and methods

# containment_Named class attributes and methods
containment_Named_name: Property = Property(name="name", type=StringType)
containment_Named.attributes={containment_Named_name}

# containment_C class attributes and methods

# containment_G class attributes and methods

# containment_F class attributes and methods

# containment_H class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="containment_B", type=containment_A, multiplicity=Multiplicity(1, 1)),
        Property(name="containment_A", type=containment_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="containment_E", type=containment_A, multiplicity=Multiplicity(1, 1)),
        Property(name="containment_A2", type=containment_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs3: BinaryAssociation = BinaryAssociation(
    name="cs3",
    ends={
        Property(name="containment_C", type=containment_B, multiplicity=Multiplicity(1, 1)),
        Property(name="containment_B4", type=containment_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gs5: BinaryAssociation = BinaryAssociation(
    name="gs5",
    ends={
        Property(name="containment_G", type=containment_B, multiplicity=Multiplicity(1, 1)),
        Property(name="containment_B6", type=containment_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs7: BinaryAssociation = BinaryAssociation(
    name="fs7",
    ends={
        Property(name="containment_F", type=containment_E, multiplicity=Multiplicity(1, 1)),
        Property(name="containment_E8", type=containment_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hs9: BinaryAssociation = BinaryAssociation(
    name="hs9",
    ends={
        Property(name="containment_H", type=containment_G, multiplicity=Multiplicity(1, 1)),
        Property(name="containment_G10", type=containment_H, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_containment_A_Named = Generalization(general=Named, specific=containment_A)
gen_containment_C_Named = Generalization(general=Named, specific=containment_C)
gen_containment_B_Named = Generalization(general=Named, specific=containment_B)
gen_containment_F_Named = Generalization(general=Named, specific=containment_F)
gen_containment_E_Named = Generalization(general=Named, specific=containment_E)
gen_containment_G_Named = Generalization(general=Named, specific=containment_G)
gen_containment_H_Named = Generalization(general=Named, specific=containment_H)

# Domain Model
domain_model = DomainModel(
    name="containment",
    types={containment_A, Named, containment_B, containment_E, containment_Named, containment_C, containment_G, containment_F, containment_H},
    associations={bs0, es1, cs3, gs5, fs7, hs9},
    generalizations={gen_containment_A_Named, gen_containment_C_Named, gen_containment_B_Named, gen_containment_F_Named, gen_containment_E_Named, gen_containment_G_Named, gen_containment_H_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)