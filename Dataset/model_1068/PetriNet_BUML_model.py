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
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Arc = Class(name="PetriNet::Arc", is_abstract=True)
PetriNet_PlaceToTransition = Class(name="PetriNet::PlaceToTransition")
Place = Class(name="Place")
Arc = Class(name="Arc")
PetriNet_Element = Class(name="PetriNet::Element", is_abstract=True)
PetriNet = Class(name="PetriNet")
PetriNet_Place = Class(name="PetriNet::Place")
TransitionToPlace = Class(name="TransitionToPlace")
PlaceToTransition = Class(name="PlaceToTransition")
Transition = Class(name="Transition")
PetriNet_TransitionToPlace = Class(name="PetriNet::TransitionToPlace")

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

# PetriNet_Transition class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNet_Arc.attributes={PetriNet_Arc_weight}

# PetriNet_PlaceToTransition class attributes and methods

# Place class attributes and methods

# Arc class attributes and methods

# PetriNet_Element class attributes and methods

# PetriNet class attributes and methods

# PetriNet_Place class attributes and methods

# TransitionToPlace class attributes and methods

# PlaceToTransition class attributes and methods

# Transition class attributes and methods

# PetriNet_TransitionToPlace class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingArc13: BinaryAssociation = BinaryAssociation(
    name="incomingArc13",
    ends={
        Property(name="15", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="014", type=PlaceToTransition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingArc16: BinaryAssociation = BinaryAssociation(
    name="outgoingArc16",
    ends={
        Property(name="18", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="017", type=TransitionToPlace, multiplicity=Multiplicity(1, 9999))
    }
)
net19: BinaryAssociation = BinaryAssociation(
    name="net19",
    ends={
        Property(name="21", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="020", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
from22: BinaryAssociation = BinaryAssociation(
    name="from22",
    ends={
        Property(name="24", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="023", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="3", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net4: BinaryAssociation = BinaryAssociation(
    name="net4",
    ends={
        Property(name="6", type=PetriNet_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="05", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
incomingArc7: BinaryAssociation = BinaryAssociation(
    name="incomingArc7",
    ends={
        Property(name="9", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="08", type=TransitionToPlace, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingArc10: BinaryAssociation = BinaryAssociation(
    name="outgoingArc10",
    ends={
        Property(name="12", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="011", type=PlaceToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
to25: BinaryAssociation = BinaryAssociation(
    name="to25",
    ends={
        Property(name="27", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="026", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
from28: BinaryAssociation = BinaryAssociation(
    name="from28",
    ends={
        Property(name="30", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="029", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
to31: BinaryAssociation = BinaryAssociation(
    name="to31",
    ends={
        Property(name="33", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="032", type=Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=PetriNet_NamedElement)
gen_PetriNet_PetriNet_NamedElement = Generalization(general=NamedElement, specific=PetriNet_PetriNet)
gen_PetriNet_Transition_Element = Generalization(general=Element, specific=PetriNet_Transition)
gen_PetriNet_Arc_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Arc)
gen_PetriNet_PlaceToTransition_Arc = Generalization(general=Arc, specific=PetriNet_PlaceToTransition)
gen_PetriNet_Element_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Element)
gen_PetriNet_Place_Element = Generalization(general=Element, specific=PetriNet_Place)
gen_PetriNet_TransitionToPlace_Arc = Generalization(general=Arc, specific=PetriNet_TransitionToPlace)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_LocatedElement, PetriNet_NamedElement, LocatedElement, PetriNet_PetriNet, NamedElement, Element, PetriNet_Transition, PetriNet_Arc, PetriNet_PlaceToTransition, Place, Arc, PetriNet_Element, PetriNet, PetriNet_Place, TransitionToPlace, PlaceToTransition, Transition, PetriNet_TransitionToPlace},
    associations={elements0, incomingArc13, outgoingArc16, net19, from22, arcs1, net4, incomingArc7, outgoingArc10, to25, from28, to31},
    generalizations={gen_PetriNet_NamedElement_LocatedElement, gen_PetriNet_PetriNet_NamedElement, gen_PetriNet_Transition_Element, gen_PetriNet_Arc_NamedElement, gen_PetriNet_PlaceToTransition_Arc, gen_PetriNet_Element_NamedElement, gen_PetriNet_Place_Element, gen_PetriNet_TransitionToPlace_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)