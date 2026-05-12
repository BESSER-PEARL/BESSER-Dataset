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
PetriNet_Place = Class(name="PetriNet_Place")
Net = Class(name="Net")
PTArc = Class(name="PTArc")
TPArc = Class(name="TPArc")
Token = Class(name="Token")
PetriNet_Transition = Class(name="PetriNet_Transition")
PetriNet_Net = Class(name="PetriNet_Net")
Place = Class(name="Place")
Transition = Class(name="Transition")
PetriNet_Arc = Class(name="PetriNet_Arc", is_abstract=True)
PetriNet_PTArc = Class(name="PetriNet_PTArc")
Arc = Class(name="Arc")
PetriNet_TPArc = Class(name="PetriNet_TPArc")
PetriNet_Token = Class(name="PetriNet_Token")

# PetriNet_Place class attributes and methods

# Net class attributes and methods

# PTArc class attributes and methods

# TPArc class attributes and methods

# Token class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Net class attributes and methods

# Place class attributes and methods

# Transition class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=StringType)
PetriNet_Arc.attributes={PetriNet_Arc_weight}

# PetriNet_PTArc class attributes and methods

# Arc class attributes and methods

# PetriNet_TPArc class attributes and methods

# PetriNet_Token class attributes and methods

# Relationships
net0: BinaryAssociation = BinaryAssociation(
    name="net0",
    ends={
        Property(name="Net", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=Net, multiplicity=Multiplicity(1, 1))
    }
)
out1: BinaryAssociation = BinaryAssociation(
    name="out1",
    ends={
        Property(name="PTArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
in_2: BinaryAssociation = BinaryAssociation(
    name="in_2",
    ends={
        Property(name="TPArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
token3: BinaryAssociation = BinaryAssociation(
    name="token3",
    ends={
        Property(name="Token", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place4", type=Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net5: BinaryAssociation = BinaryAssociation(
    name="net5",
    ends={
        Property(name="Net6", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=Net, multiplicity=Multiplicity(1, 1))
    }
)
in_7: BinaryAssociation = BinaryAssociation(
    name="in_7",
    ends={
        Property(name="PTArc9", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst8", type=PTArc, multiplicity=Multiplicity(1, 9999))
    }
)
out10: BinaryAssociation = BinaryAssociation(
    name="out10",
    ends={
        Property(name="TPArc12", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src11", type=TPArc, multiplicity=Multiplicity(1, 9999))
    }
)
place13: BinaryAssociation = BinaryAssociation(
    name="place13",
    ends={
        Property(name="Place", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transition14: BinaryAssociation = BinaryAssociation(
    name="transition14",
    ends={
        Property(name="Transition", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net15", type=Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dst16: BinaryAssociation = BinaryAssociation(
    name="dst16",
    ends={
        Property(name="Transition17", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
src18: BinaryAssociation = BinaryAssociation(
    name="src18",
    ends={
        Property(name="Place19", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
src20: BinaryAssociation = BinaryAssociation(
    name="src20",
    ends={
        Property(name="Transition22", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out21", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
dst23: BinaryAssociation = BinaryAssociation(
    name="dst23",
    ends={
        Property(name="Place25", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_24", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
place26: BinaryAssociation = BinaryAssociation(
    name="place26",
    ends={
        Property(name="Place27", type=PetriNet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="token", type=Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_PTArc_Arc = Generalization(general=Arc, specific=PetriNet_PTArc)
gen_PetriNet_TPArc_Arc = Generalization(general=Arc, specific=PetriNet_TPArc)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PetriNet_Place, Net, PTArc, TPArc, Token, PetriNet_Transition, PetriNet_Net, Place, Transition, PetriNet_Arc, PetriNet_PTArc, Arc, PetriNet_TPArc, PetriNet_Token},
    associations={net0, out1, in_2, token3, net5, in_7, out10, place13, transition14, dst16, src18, src20, dst23, place26},
    generalizations={gen_PetriNet_PTArc_Arc, gen_PetriNet_TPArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)