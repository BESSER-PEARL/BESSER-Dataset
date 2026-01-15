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
PetriNet_LocatedElement = Class(name="PetriNet::LocatedElement", is_abstract=True)
PetriNet_NamedElement = Class(name="PetriNet::NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
NamedElement = Class(name="NamedElement")
Element = Class(name="Element")
Arc = Class(name="Arc")
PetriNet_Arc = Class(name="PetriNet::Arc", is_abstract=True)
PetriNet_PlaceToTransition = Class(name="PetriNet::PlaceToTransition")
Place = Class(name="Place")
Transition = Class(name="Transition")
PetriNet_TransitionToPlace = Class(name="PetriNet::TransitionToPlace")
PetriNet_Execution = Class(name="PetriNet::Execution")
Marking = Class(name="Marking")
Movement = Class(name="Movement")
Execution = Class(name="Execution")
PetriNet_Element = Class(name="PetriNet::Element", is_abstract=True)
PetriNet = Class(name="PetriNet")
PetriNet_Place = Class(name="PetriNet::Place")
TransitionToPlace = Class(name="TransitionToPlace")
PlaceToTransition = Class(name="PlaceToTransition")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Token = Class(name="PetriNet::Token")
PetriNet_Marking = Class(name="PetriNet::Marking")
Token = Class(name="Token")
PetriNet_Movement = Class(name="PetriNet::Movement")

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

# Execution class attributes and methods

# PetriNet_Element class attributes and methods

# PetriNet class attributes and methods

# PetriNet_Place class attributes and methods

# TransitionToPlace class attributes and methods

# PlaceToTransition class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Token class attributes and methods

# PetriNet_Marking class attributes and methods

# Token class attributes and methods

# PetriNet_Movement class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="#", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="#3", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingArc19: BinaryAssociation = BinaryAssociation(
    name="outgoingArc19",
    ends={
        Property(name="#21", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="020", type=TransitionToPlace, multiplicity=Multiplicity(1, 9999))
    }
)
net22: BinaryAssociation = BinaryAssociation(
    name="net22",
    ends={
        Property(name="#24", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="023", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
from25: BinaryAssociation = BinaryAssociation(
    name="from25",
    ends={
        Property(name="#27", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="026", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
to28: BinaryAssociation = BinaryAssociation(
    name="to28",
    ends={
        Property(name="#30", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="029", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
from31: BinaryAssociation = BinaryAssociation(
    name="from31",
    ends={
        Property(name="#33", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="032", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
to34: BinaryAssociation = BinaryAssociation(
    name="to34",
    ends={
        Property(name="#36", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="035", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
net37: BinaryAssociation = BinaryAssociation(
    name="net37",
    ends={
        Property(name="#39", type=PetriNet_Execution, multiplicity=Multiplicity(1, 1)),
        Property(name="038", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
markings40: BinaryAssociation = BinaryAssociation(
    name="markings40",
    ends={
        Property(name="#42", type=PetriNet_Execution, multiplicity=Multiplicity(1, 1)),
        Property(name="041", type=Marking, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
movements43: BinaryAssociation = BinaryAssociation(
    name="movements43",
    ends={
        Property(name="#45", type=PetriNet_Execution, multiplicity=Multiplicity(1, 1)),
        Property(name="044", type=Movement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
execs4: BinaryAssociation = BinaryAssociation(
    name="execs4",
    ends={
        Property(name="#6", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="05", type=Execution, multiplicity=Multiplicity(0, 9999))
    }
)
net7: BinaryAssociation = BinaryAssociation(
    name="net7",
    ends={
        Property(name="#9", type=PetriNet_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="08", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
incomingArc10: BinaryAssociation = BinaryAssociation(
    name="incomingArc10",
    ends={
        Property(name="#12", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="011", type=TransitionToPlace, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingArc13: BinaryAssociation = BinaryAssociation(
    name="outgoingArc13",
    ends={
        Property(name="#15", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="014", type=PlaceToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingArc16: BinaryAssociation = BinaryAssociation(
    name="incomingArc16",
    ends={
        Property(name="#18", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="017", type=PlaceToTransition, multiplicity=Multiplicity(1, 9999))
    }
)
source60: BinaryAssociation = BinaryAssociation(
    name="source60",
    ends={
        Property(name="Marking", type=PetriNet_Movement, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Movement61", type=Marking, multiplicity=Multiplicity(1, 1))
    }
)
target62: BinaryAssociation = BinaryAssociation(
    name="target62",
    ends={
        Property(name="Marking64", type=PetriNet_Movement, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Movement63", type=Marking, multiplicity=Multiplicity(1, 1))
    }
)
placedAt46: BinaryAssociation = BinaryAssociation(
    name="placedAt46",
    ends={
        Property(name="Place", type=PetriNet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Token", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
marking47: BinaryAssociation = BinaryAssociation(
    name="marking47",
    ends={
        Property(name="#49", type=PetriNet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="048", type=Marking, multiplicity=Multiplicity(1, 1))
    }
)
exec50: BinaryAssociation = BinaryAssociation(
    name="exec50",
    ends={
        Property(name="#52", type=PetriNet_Marking, multiplicity=Multiplicity(1, 1)),
        Property(name="051", type=Execution, multiplicity=Multiplicity(1, 1))
    }
)
tokens53: BinaryAssociation = BinaryAssociation(
    name="tokens53",
    ends={
        Property(name="#55", type=PetriNet_Marking, multiplicity=Multiplicity(1, 1)),
        Property(name="054", type=Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exec56: BinaryAssociation = BinaryAssociation(
    name="exec56",
    ends={
        Property(name="#58", type=PetriNet_Movement, multiplicity=Multiplicity(1, 1)),
        Property(name="057", type=Execution, multiplicity=Multiplicity(1, 1))
    }
)
fire59: BinaryAssociation = BinaryAssociation(
    name="fire59",
    ends={
        Property(name="Transition", type=PetriNet_Movement, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Movement", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=PetriNet_NamedElement)
gen_PetriNet_PetriNet_NamedElement = Generalization(general=NamedElement, specific=PetriNet_PetriNet)
gen_PetriNet_Arc_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Arc)
gen_PetriNet_PlaceToTransition_Arc = Generalization(general=Arc, specific=PetriNet_PlaceToTransition)
gen_PetriNet_TransitionToPlace_Arc = Generalization(general=Arc, specific=PetriNet_TransitionToPlace)
gen_PetriNet_Element_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Element)
gen_PetriNet_Place_Element = Generalization(general=Element, specific=PetriNet_Place)
gen_PetriNet_Transition_Element = Generalization(general=Element, specific=PetriNet_Transition)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PetriNet_LocatedElement, PetriNet_NamedElement, LocatedElement, PetriNet_PetriNet, NamedElement, Element, Arc, PetriNet_Arc, PetriNet_PlaceToTransition, Place, Transition, PetriNet_TransitionToPlace, PetriNet_Execution, Marking, Movement, Execution, PetriNet_Element, PetriNet, PetriNet_Place, TransitionToPlace, PlaceToTransition, PetriNet_Transition, PetriNet_Token, PetriNet_Marking, Token, PetriNet_Movement},
    associations={elements0, arcs1, outgoingArc19, net22, from25, to28, from31, to34, net37, markings40, movements43, execs4, net7, incomingArc10, outgoingArc13, incomingArc16, source60, target62, placedAt46, marking47, exec50, tokens53, exec56, fire59},
    generalizations={gen_PetriNet_NamedElement_LocatedElement, gen_PetriNet_PetriNet_NamedElement, gen_PetriNet_Arc_NamedElement, gen_PetriNet_PlaceToTransition_Arc, gen_PetriNet_TransitionToPlace_Arc, gen_PetriNet_Element_NamedElement, gen_PetriNet_Place_Element, gen_PetriNet_Transition_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)