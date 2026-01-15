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
multiview2_A = Class(name="multiview2::A")
Named = Class(name="Named")
multiview2_B = Class(name="multiview2::B")
multiview2_E = Class(name="multiview2::E")
multiview2_C = Class(name="multiview2::C")
multiview2_Named = Class(name="multiview2::Named")
multiview2_F = Class(name="multiview2::F")

# multiview2_A class attributes and methods

# Named class attributes and methods

# multiview2_B class attributes and methods

# multiview2_E class attributes and methods

# multiview2_C class attributes and methods

# multiview2_Named class attributes and methods
multiview2_Named_name: Property = Property(name="name", type=StringType)
multiview2_Named.attributes={multiview2_Named_name}

# multiview2_F class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="multiview2_B", type=multiview2_A, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview2_A", type=multiview2_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="multiview2_E", type=multiview2_A, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview2_A2", type=multiview2_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs3: BinaryAssociation = BinaryAssociation(
    name="cs3",
    ends={
        Property(name="multiview2_C", type=multiview2_B, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview2_B4", type=multiview2_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs5: BinaryAssociation = BinaryAssociation(
    name="fs5",
    ends={
        Property(name="multiview2_F", type=multiview2_E, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview2_E6", type=multiview2_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_multiview2_A_Named = Generalization(general=Named, specific=multiview2_A)
gen_multiview2_B_Named = Generalization(general=Named, specific=multiview2_B)
gen_multiview2_E_Named = Generalization(general=Named, specific=multiview2_E)
gen_multiview2_F_Named = Generalization(general=Named, specific=multiview2_F)
gen_multiview2_C_Named = Generalization(general=Named, specific=multiview2_C)

# Domain Model
domain_model = DomainModel(
    name="multiview2",
    types={multiview2_A, Named, multiview2_B, multiview2_E, multiview2_C, multiview2_Named, multiview2_F},
    associations={bs0, es1, cs3, fs5},
    generalizations={gen_multiview2_A_Named, gen_multiview2_B_Named, gen_multiview2_E_Named, gen_multiview2_F_Named, gen_multiview2_C_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)