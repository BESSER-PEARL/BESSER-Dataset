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
minher_B = Class(name="minher::B")
Named = Class(name="Named")
minher_G = Class(name="minher::G")
minher_Named = Class(name="minher::Named", is_abstract=True)
minher_A = Class(name="minher::A")
minher_C = Class(name="minher::C")
minher_E = Class(name="minher::E")
B = Class(name="B")

# minher_B class attributes and methods
minher_B_value: Property = Property(name="value", type=StringType)
minher_B.attributes={minher_B_value}

# Named class attributes and methods

# minher_G class attributes and methods

# minher_Named class attributes and methods
minher_Named_name: Property = Property(name="name", type=StringType)
minher_Named.attributes={minher_Named_name}

# minher_A class attributes and methods

# minher_C class attributes and methods

# minher_E class attributes and methods

# B class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="minher_B", type=minher_A, multiplicity=Multiplicity(1, 1)),
        Property(name="minher_A", type=minher_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gs1: BinaryAssociation = BinaryAssociation(
    name="gs1",
    ends={
        Property(name="minher_G", type=minher_B, multiplicity=Multiplicity(1, 1)),
        Property(name="minher_B2", type=minher_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs3: BinaryAssociation = BinaryAssociation(
    name="cs3",
    ends={
        Property(name="minher_C", type=minher_B, multiplicity=Multiplicity(1, 1)),
        Property(name="minher_B4", type=minher_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_minher_B_Named = Generalization(general=Named, specific=minher_B)
gen_minher_E_B = Generalization(general=B, specific=minher_E)
gen_minher_G_Named = Generalization(general=Named, specific=minher_G)
gen_minher_C_Named = Generalization(general=Named, specific=minher_C)

# Domain Model
domain_model = DomainModel(
    name="minher",
    types={minher_B, Named, minher_G, minher_Named, minher_A, minher_C, minher_E, B},
    associations={bs0, gs1, cs3},
    generalizations={gen_minher_B_Named, gen_minher_E_B, gen_minher_G_Named, gen_minher_C_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)