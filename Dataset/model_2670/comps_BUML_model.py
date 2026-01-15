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
comps_A = Class(name="comps::A")
Named = Class(name="Named")
comps_C = Class(name="comps::C")
comps_G = Class(name="comps::G")
comps_B = Class(name="comps::B")
comps_E = Class(name="comps::E")
B = Class(name="B")
comps_Named = Class(name="comps::Named")
comps_F = Class(name="comps::F")
comps_H = Class(name="comps::H")

# comps_A class attributes and methods

# Named class attributes and methods

# comps_C class attributes and methods

# comps_G class attributes and methods

# comps_B class attributes and methods

# comps_E class attributes and methods

# B class attributes and methods

# comps_Named class attributes and methods
comps_Named_name: Property = Property(name="name", type=StringType)
comps_Named.attributes={comps_Named_name}

# comps_F class attributes and methods

# comps_H class attributes and methods

# Relationships
cs1: BinaryAssociation = BinaryAssociation(
    name="cs1",
    ends={
        Property(name="comps_C", type=comps_B, multiplicity=Multiplicity(1, 1)),
        Property(name="comps_B2", type=comps_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="comps_B", type=comps_A, multiplicity=Multiplicity(1, 1)),
        Property(name="comps_A", type=comps_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gs3: BinaryAssociation = BinaryAssociation(
    name="gs3",
    ends={
        Property(name="comps_G", type=comps_B, multiplicity=Multiplicity(1, 1)),
        Property(name="comps_B4", type=comps_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs5: BinaryAssociation = BinaryAssociation(
    name="fs5",
    ends={
        Property(name="comps_F", type=comps_E, multiplicity=Multiplicity(1, 1)),
        Property(name="comps_E", type=comps_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hs6: BinaryAssociation = BinaryAssociation(
    name="hs6",
    ends={
        Property(name="comps_H", type=comps_G, multiplicity=Multiplicity(1, 1)),
        Property(name="comps_G7", type=comps_H, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_comps_A_Named = Generalization(general=Named, specific=comps_A)
gen_comps_B_Named = Generalization(general=Named, specific=comps_B)
gen_comps_E_Named = Generalization(general=Named, specific=comps_E)
gen_comps_E_B = Generalization(general=B, specific=comps_E)
gen_comps_C_Named = Generalization(general=Named, specific=comps_C)
gen_comps_F_Named = Generalization(general=Named, specific=comps_F)
gen_comps_G_Named = Generalization(general=Named, specific=comps_G)
gen_comps_H_Named = Generalization(general=Named, specific=comps_H)

# Domain Model
domain_model = DomainModel(
    name="comps",
    types={comps_A, Named, comps_C, comps_G, comps_B, comps_E, B, comps_Named, comps_F, comps_H},
    associations={cs1, bs0, gs3, fs5, hs6},
    generalizations={gen_comps_A_Named, gen_comps_B_Named, gen_comps_E_Named, gen_comps_E_B, gen_comps_C_Named, gen_comps_F_Named, gen_comps_G_Named, gen_comps_H_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)