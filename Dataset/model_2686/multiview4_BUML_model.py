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
multiview4_A = Class(name="multiview4::A")
Named = Class(name="Named")
multiview4_C = Class(name="multiview4::C")
multiview4_B = Class(name="multiview4::B")
multiview4_E = Class(name="multiview4::E")
multiview4_F = Class(name="multiview4::F")
multiview4_Named = Class(name="multiview4::Named")

# multiview4_A class attributes and methods

# Named class attributes and methods

# multiview4_C class attributes and methods

# multiview4_B class attributes and methods

# multiview4_E class attributes and methods

# multiview4_F class attributes and methods

# multiview4_Named class attributes and methods
multiview4_Named_name: Property = Property(name="name", type=StringType)
multiview4_Named.attributes={multiview4_Named_name}

# Relationships
cs3: BinaryAssociation = BinaryAssociation(
    name="cs3",
    ends={
        Property(name="multiview4_C", type=multiview4_B, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview4_B4", type=multiview4_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="multiview4_B", type=multiview4_A, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview4_A", type=multiview4_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="multiview4_E", type=multiview4_A, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview4_A2", type=multiview4_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs5: BinaryAssociation = BinaryAssociation(
    name="fs5",
    ends={
        Property(name="multiview4_F", type=multiview4_E, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview4_E6", type=multiview4_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_multiview4_A_Named = Generalization(general=Named, specific=multiview4_A)
gen_multiview4_B_Named = Generalization(general=Named, specific=multiview4_B)
gen_multiview4_E_Named = Generalization(general=Named, specific=multiview4_E)
gen_multiview4_C_Named = Generalization(general=Named, specific=multiview4_C)
gen_multiview4_F_Named = Generalization(general=Named, specific=multiview4_F)

# Domain Model
domain_model = DomainModel(
    name="multiview4",
    types={multiview4_A, Named, multiview4_C, multiview4_B, multiview4_E, multiview4_F, multiview4_Named},
    associations={cs3, bs0, es1, fs5},
    generalizations={gen_multiview4_A_Named, gen_multiview4_B_Named, gen_multiview4_E_Named, gen_multiview4_C_Named, gen_multiview4_F_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)