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
multiview_B = Class(name="multiview::B")
multiview_E = Class(name="multiview::E")
multiview_C = Class(name="multiview::C")
multiview_Named = Class(name="multiview::Named")
multiview_A = Class(name="multiview::A")
Named = Class(name="Named")
multiview_F = Class(name="multiview::F")

# multiview_B class attributes and methods

# multiview_E class attributes and methods

# multiview_C class attributes and methods

# multiview_Named class attributes and methods
multiview_Named_name: Property = Property(name="name", type=StringType)
multiview_Named.attributes={multiview_Named_name}

# multiview_A class attributes and methods

# Named class attributes and methods

# multiview_F class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="multiview_B", type=multiview_A, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview_A", type=multiview_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="multiview_E", type=multiview_A, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview_A2", type=multiview_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs3: BinaryAssociation = BinaryAssociation(
    name="cs3",
    ends={
        Property(name="multiview_C", type=multiview_B, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview_B4", type=multiview_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs5: BinaryAssociation = BinaryAssociation(
    name="fs5",
    ends={
        Property(name="multiview_F", type=multiview_E, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview_E6", type=multiview_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_multiview_B_Named = Generalization(general=Named, specific=multiview_B)
gen_multiview_C_Named = Generalization(general=Named, specific=multiview_C)
gen_multiview_A_Named = Generalization(general=Named, specific=multiview_A)
gen_multiview_F_Named = Generalization(general=Named, specific=multiview_F)
gen_multiview_E_Named = Generalization(general=Named, specific=multiview_E)

# Domain Model
domain_model = DomainModel(
    name="multiview",
    types={multiview_B, multiview_E, multiview_C, multiview_Named, multiview_A, Named, multiview_F},
    associations={bs0, es1, cs3, fs5},
    generalizations={gen_multiview_B_Named, gen_multiview_C_Named, gen_multiview_A_Named, gen_multiview_F_Named, gen_multiview_E_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)