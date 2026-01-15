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
TypeB_A = Class(name="TypeB::A")
TypeB_B = Class(name="TypeB::B")
TypeB_C = Class(name="TypeB::C")
TypeB_BDescription1 = Class(name="TypeB::BDescription1")
TypeB_BDescription2 = Class(name="TypeB::BDescription2")
TypeB_BDescription3 = Class(name="TypeB::BDescription3")
TypeB_CDescription = Class(name="TypeB::CDescription")

# TypeB_A class attributes and methods
TypeB_A_name: Property = Property(name="name", type=StringType)
TypeB_A.attributes={TypeB_A_name}

# TypeB_B class attributes and methods
TypeB_B_name: Property = Property(name="name", type=StringType)
TypeB_B.attributes={TypeB_B_name}

# TypeB_C class attributes and methods
TypeB_C_name: Property = Property(name="name", type=StringType)
TypeB_C.attributes={TypeB_C_name}

# TypeB_BDescription1 class attributes and methods
TypeB_BDescription1_description: Property = Property(name="description", type=StringType)
TypeB_BDescription1.attributes={TypeB_BDescription1_description}

# TypeB_BDescription2 class attributes and methods
TypeB_BDescription2_description: Property = Property(name="description", type=StringType)
TypeB_BDescription2.attributes={TypeB_BDescription2_description}

# TypeB_BDescription3 class attributes and methods
TypeB_BDescription3_description: Property = Property(name="description", type=StringType)
TypeB_BDescription3.attributes={TypeB_BDescription3_description}

# TypeB_CDescription class attributes and methods
TypeB_CDescription_description: Property = Property(name="description", type=StringType)
TypeB_CDescription.attributes={TypeB_CDescription_description}

# Relationships
bElements0: BinaryAssociation = BinaryAssociation(
    name="bElements0",
    ends={
        Property(name="TypeB_B", type=TypeB_A, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_A", type=TypeB_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cElements1: BinaryAssociation = BinaryAssociation(
    name="cElements1",
    ends={
        Property(name="TypeB_C", type=TypeB_A, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_A2", type=TypeB_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description13: BinaryAssociation = BinaryAssociation(
    name="description13",
    ends={
        Property(name="TypeB_BDescription1", type=TypeB_B, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_B4", type=TypeB_BDescription1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description25: BinaryAssociation = BinaryAssociation(
    name="description25",
    ends={
        Property(name="TypeB_BDescription2", type=TypeB_B, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_B6", type=TypeB_BDescription2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description37: BinaryAssociation = BinaryAssociation(
    name="description37",
    ends={
        Property(name="TypeB_BDescription3", type=TypeB_B, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_B8", type=TypeB_BDescription3, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description9: BinaryAssociation = BinaryAssociation(
    name="description9",
    ends={
        Property(name="TypeB_CDescription", type=TypeB_C, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeB_C10", type=TypeB_CDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="TypeB",
    types={TypeB_A, TypeB_B, TypeB_C, TypeB_BDescription1, TypeB_BDescription2, TypeB_BDescription3, TypeB_CDescription},
    associations={bElements0, cElements1, description13, description25, description37, description9},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)