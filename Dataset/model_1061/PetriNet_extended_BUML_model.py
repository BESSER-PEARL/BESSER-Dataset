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
TransitionToPlace = Class(name="TransitionToPlace")
PlaceToTransition = Class(name="PlaceToTransition")
PetriNet_LocatedElement = Class(name="PetriNet_LocatedElement", is_abstract=True)
PetriNet_NamedElement = Class(name="PetriNet_NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
PetriNet_PetriNet = Class(name="PetriNet_PetriNet")
NamedElement = Class(name="NamedElement")
Element = Class(name="Element")
Arc = Class(name="Arc")
Execution = Class(name="Execution")
PetriNet_Element = Class(name="PetriNet_Element", is_abstract=True)
PetriNet = Class(name="PetriNet")
PetriNet_Place = Class(name="PetriNet_Place")
PetriNet_Transition = Class(name="PetriNet_Transition")
PetriNet_Arc = Class(name="PetriNet_Arc", is_abstract=True)
PetriNet_PlaceToTransition = Class(name="PetriNet_PlaceToTransition")
Place = Class(name="Place")
Transition = Class(name="Transition")
PetriNet_TransitionToPlace = Class(name="PetriNet_TransitionToPlace")
PetriNet_Execution = Class(name="PetriNet_Execution")
Marking = Class(name="Marking")
Movement = Class(name="Movement")
PetriNet_Token = Class(name="PetriNet_Token")
PetriNet_Marking = Class(name="PetriNet_Marking")
Token = Class(name="Token")
PetriNet_Movement = Class(name="PetriNet_Movement")

# TransitionToPlace class attributes and methods

# PlaceToTransition class attributes and methods

# PetriNet_LocatedElement class attributes and methods
PetriNet_LocatedElement_location: Property = Property(name="location", type=StringType)
PetriNet_LocatedElement.attributes={PetriNet_LocatedElement_location}

# PetriNet_NamedElement class attributes and methods
PetriNet_NamedElement_name: Property = Property(name="name", type=StringType)
PetriNet_NamedElement.attributes={PetriNet_NamedElement_name}

# LocatedElement class attributes and methods

# PetriNet_PetriNet class attributes and methods

# NamedElement class attributes and methods

# Element class attributes and methods

# Arc class attributes and methods

# Execution class attributes and methods

# PetriNet_Element class attributes and methods

# PetriNet class attributes and methods

# PetriNet_Place class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=StringType)
PetriNet_Arc.attributes={PetriNet_Arc_weight}

# PetriNet_PlaceToTransition class attributes and methods

# Place class attributes and methods

# Transition class attributes and methods

# PetriNet_TransitionToPlace class attributes and methods

# PetriNet_Execution class attributes and methods

# Marking class attributes and methods

# Movement class attributes and methods

# PetriNet_Token class attributes and methods

# PetriNet_Marking class attributes and methods

# Token class attributes and methods

# PetriNet_Movement class attributes and methods

# Relationships
incomingArc6: BinaryAssociation = BinaryAssociation(
    name="incomingArc6",
    ends={
        Property(name="TransitionToPlace", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=TransitionToPlace, multiplicity=Multiplicity(0, 9999))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="Element", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
execs3: BinaryAssociation = BinaryAssociation(
    name="execs3",
    ends={
        Property(name="Execution", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net4", type=Execution, multiplicity=Multiplicity(0, 9999))
    }
)
net5: BinaryAssociation = BinaryAssociation(
    name="net5",
    ends={
        Property(name="PetriNet", type=PetriNet_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
exec33: BinaryAssociation = BinaryAssociation(
    name="exec33",
    ends={
        Property(name="Execution34", type=PetriNet_Marking, multiplicity=Multiplicity(1, 1)),
        Property(name="markings", type=Execution, multiplicity=Multiplicity(1, 1))
    }
)
outgoingArc7: BinaryAssociation = BinaryAssociation(
    name="outgoingArc7",
    ends={
        Property(name="PlaceToTransition", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=PlaceToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingArc8: BinaryAssociation = BinaryAssociation(
    name="incomingArc8",
    ends={
        Property(name="PlaceToTransition10", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="to9", type=PlaceToTransition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingArc11: BinaryAssociation = BinaryAssociation(
    name="outgoingArc11",
    ends={
        Property(name="TransitionToPlace13", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="from_12", type=TransitionToPlace, multiplicity=Multiplicity(1, 9999))
    }
)
net14: BinaryAssociation = BinaryAssociation(
    name="net14",
    ends={
        Property(name="PetriNet15", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
from_16: BinaryAssociation = BinaryAssociation(
    name="from_16",
    ends={
        Property(name="Place", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
to17: BinaryAssociation = BinaryAssociation(
    name="to17",
    ends={
        Property(name="Transition", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
from_18: BinaryAssociation = BinaryAssociation(
    name="from_18",
    ends={
        Property(name="Transition20", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc19", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
to21: BinaryAssociation = BinaryAssociation(
    name="to21",
    ends={
        Property(name="Place23", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc22", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
net24: BinaryAssociation = BinaryAssociation(
    name="net24",
    ends={
        Property(name="PetriNet25", type=PetriNet_Execution, multiplicity=Multiplicity(1, 1)),
        Property(name="execs", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
markings26: BinaryAssociation = BinaryAssociation(
    name="markings26",
    ends={
        Property(name="Marking", type=PetriNet_Execution, multiplicity=Multiplicity(1, 1)),
        Property(name="exec", type=Marking, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
movements27: BinaryAssociation = BinaryAssociation(
    name="movements27",
    ends={
        Property(name="Movement", type=PetriNet_Execution, multiplicity=Multiplicity(1, 1)),
        Property(name="exec28", type=Movement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
placedAt29: BinaryAssociation = BinaryAssociation(
    name="placedAt29",
    ends={
        Property(name="Place30", type=PetriNet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Token", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
marking31: BinaryAssociation = BinaryAssociation(
    name="marking31",
    ends={
        Property(name="Marking32", type=PetriNet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="tokens", type=Marking, multiplicity=Multiplicity(1, 1))
    }
)
tokens35: BinaryAssociation = BinaryAssociation(
    name="tokens35",
    ends={
        Property(name="Token", type=PetriNet_Marking, multiplicity=Multiplicity(1, 1)),
        Property(name="marking", type=Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exec36: BinaryAssociation = BinaryAssociation(
    name="exec36",
    ends={
        Property(name="Execution37", type=PetriNet_Movement, multiplicity=Multiplicity(1, 1)),
        Property(name="movements", type=Execution, multiplicity=Multiplicity(1, 1))
    }
)
fire38: BinaryAssociation = BinaryAssociation(
    name="fire38",
    ends={
        Property(name="Transition39", type=PetriNet_Movement, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Movement", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
source40: BinaryAssociation = BinaryAssociation(
    name="source40",
    ends={
        Property(name="Marking42", type=PetriNet_Movement, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Movement41", type=Marking, multiplicity=Multiplicity(1, 1))
    }
)
target43: BinaryAssociation = BinaryAssociation(
    name="target43",
    ends={
        Property(name="Marking45", type=PetriNet_Movement, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Movement44", type=Marking, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=PetriNet_NamedElement)
gen_PetriNet_PetriNet_NamedElement = Generalization(general=NamedElement, specific=PetriNet_PetriNet)
gen_PetriNet_Element_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Element)
gen_PetriNet_Place_Element = Generalization(general=Element, specific=PetriNet_Place)
gen_PetriNet_Transition_Element = Generalization(general=Element, specific=PetriNet_Transition)
gen_PetriNet_Arc_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Arc)
gen_PetriNet_PlaceToTransition_Arc = Generalization(general=Arc, specific=PetriNet_PlaceToTransition)
gen_PetriNet_TransitionToPlace_Arc = Generalization(general=Arc, specific=PetriNet_TransitionToPlace)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={TransitionToPlace, PlaceToTransition, PetriNet_LocatedElement, PetriNet_NamedElement, LocatedElement, PetriNet_PetriNet, NamedElement, Element, Arc, Execution, PetriNet_Element, PetriNet, PetriNet_Place, PetriNet_Transition, PetriNet_Arc, PetriNet_PlaceToTransition, Place, Transition, PetriNet_TransitionToPlace, PetriNet_Execution, Marking, Movement, PetriNet_Token, PetriNet_Marking, Token, PetriNet_Movement},
    associations={incomingArc6, elements0, arcs1, execs3, net5, exec33, outgoingArc7, incomingArc8, outgoingArc11, net14, from_16, to17, from_18, to21, net24, markings26, movements27, placedAt29, marking31, tokens35, exec36, fire38, source40, target43},
    generalizations={gen_PetriNet_NamedElement_LocatedElement, gen_PetriNet_PetriNet_NamedElement, gen_PetriNet_Element_NamedElement, gen_PetriNet_Place_Element, gen_PetriNet_Transition_Element, gen_PetriNet_Arc_NamedElement, gen_PetriNet_PlaceToTransition_Arc, gen_PetriNet_TransitionToPlace_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)