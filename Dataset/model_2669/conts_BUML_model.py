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
conts_A = Class(name="conts::A")
Named = Class(name="Named")
conts_B = Class(name="conts::B")
conts_C = Class(name="conts::C")
conts_G = Class(name="conts::G")
conts_Named = Class(name="conts::Named")
conts_E = Class(name="conts::E")
B = Class(name="B")
conts_F = Class(name="conts::F")
conts_H = Class(name="conts::H")

# conts_A class attributes and methods

# Named class attributes and methods

# conts_B class attributes and methods

# conts_C class attributes and methods

# conts_G class attributes and methods

# conts_Named class attributes and methods
conts_Named_name: Property = Property(name="name", type=StringType)
conts_Named.attributes={conts_Named_name}

# conts_E class attributes and methods

# B class attributes and methods

# conts_F class attributes and methods

# conts_H class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="conts_B", type=conts_A, multiplicity=Multiplicity(1, 1)),
        Property(name="conts_A", type=conts_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs1: BinaryAssociation = BinaryAssociation(
    name="cs1",
    ends={
        Property(name="conts_C", type=conts_B, multiplicity=Multiplicity(1, 1)),
        Property(name="conts_B2", type=conts_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gs3: BinaryAssociation = BinaryAssociation(
    name="gs3",
    ends={
        Property(name="conts_G", type=conts_B, multiplicity=Multiplicity(1, 1)),
        Property(name="conts_B4", type=conts_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs5: BinaryAssociation = BinaryAssociation(
    name="fs5",
    ends={
        Property(name="conts_F", type=conts_E, multiplicity=Multiplicity(1, 1)),
        Property(name="conts_E", type=conts_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hs6: BinaryAssociation = BinaryAssociation(
    name="hs6",
    ends={
        Property(name="conts_H", type=conts_G, multiplicity=Multiplicity(1, 1)),
        Property(name="conts_G7", type=conts_H, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_conts_A_Named = Generalization(general=Named, specific=conts_A)
gen_conts_C_Named = Generalization(general=Named, specific=conts_C)
gen_conts_E_Named = Generalization(general=Named, specific=conts_E)
gen_conts_E_B = Generalization(general=B, specific=conts_E)
gen_conts_B_Named = Generalization(general=Named, specific=conts_B)
gen_conts_F_Named = Generalization(general=Named, specific=conts_F)
gen_conts_G_Named = Generalization(general=Named, specific=conts_G)
gen_conts_H_Named = Generalization(general=Named, specific=conts_H)

# Domain Model
domain_model = DomainModel(
    name="conts",
    types={conts_A, Named, conts_B, conts_C, conts_G, conts_Named, conts_E, B, conts_F, conts_H},
    associations={bs0, cs1, gs3, fs5, hs6},
    generalizations={gen_conts_A_Named, gen_conts_C_Named, gen_conts_E_Named, gen_conts_E_B, gen_conts_B_Named, gen_conts_F_Named, gen_conts_G_Named, gen_conts_H_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)