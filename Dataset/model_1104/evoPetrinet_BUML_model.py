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
PetriNet = Class(name="PetriNet")
evoPetrinet_LocatedElement = Class(name="evoPetrinet::LocatedElement", is_abstract=True)
evoPetrinet_NamedElement = Class(name="evoPetrinet::NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
evoPetrinet_PetriNet = Class(name="evoPetrinet::PetriNet")
NamedElement = Class(name="NamedElement")
Element = Class(name="Element")
evoPetrinet_PetriNetModel = Class(name="evoPetrinet::PetriNetModel")
evoPetrinet_Transition = Class(name="evoPetrinet::Transition")
evoPetrinet_Arc = Class(name="evoPetrinet::Arc", is_abstract=True)
evoPetrinet_PlaceToTransition = Class(name="evoPetrinet::PlaceToTransition")
Arc = Class(name="Arc")
Place = Class(name="Place")
evoPetrinet_Element = Class(name="evoPetrinet::Element", is_abstract=True)
evoPetrinet_Place = Class(name="evoPetrinet::Place")
TransitionToPlace = Class(name="TransitionToPlace")
PlaceToTransition = Class(name="PlaceToTransition")
Transition = Class(name="Transition")
evoPetrinet_TransitionToPlace = Class(name="evoPetrinet::TransitionToPlace")

# PetriNet class attributes and methods

# evoPetrinet_LocatedElement class attributes and methods
evoPetrinet_LocatedElement_location: Property = Property(name="location", type=StringType)
evoPetrinet_LocatedElement.attributes={evoPetrinet_LocatedElement_location}

# evoPetrinet_NamedElement class attributes and methods
evoPetrinet_NamedElement_name: Property = Property(name="name", type=StringType)
evoPetrinet_NamedElement.attributes={evoPetrinet_NamedElement_name}

# LocatedElement class attributes and methods

# evoPetrinet_PetriNet class attributes and methods

# NamedElement class attributes and methods

# Element class attributes and methods

# evoPetrinet_PetriNetModel class attributes and methods

# evoPetrinet_Transition class attributes and methods

# evoPetrinet_Arc class attributes and methods
evoPetrinet_Arc_weight: Property = Property(name="weight", type=StringType)
evoPetrinet_Arc.attributes={evoPetrinet_Arc_weight}

# evoPetrinet_PlaceToTransition class attributes and methods

# Arc class attributes and methods

# Place class attributes and methods

# evoPetrinet_Element class attributes and methods

# evoPetrinet_Place class attributes and methods

# TransitionToPlace class attributes and methods

# PlaceToTransition class attributes and methods

# Transition class attributes and methods

# evoPetrinet_TransitionToPlace class attributes and methods

# Relationships
nets0: BinaryAssociation = BinaryAssociation(
    name="nets0",
    ends={
        Property(name="PetriNet", type=evoPetrinet_PetriNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="evoPetrinet_PetriNetModel", type=PetriNet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="#", type=evoPetrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingArc8: BinaryAssociation = BinaryAssociation(
    name="outgoingArc8",
    ends={
        Property(name="09", type=PlaceToTransition, multiplicity=Multiplicity(0, 9999)),
        Property(name="#10", type=evoPetrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
incomingArc11: BinaryAssociation = BinaryAssociation(
    name="incomingArc11",
    ends={
        Property(name="#13", type=evoPetrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="012", type=PlaceToTransition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingArc14: BinaryAssociation = BinaryAssociation(
    name="outgoingArc14",
    ends={
        Property(name="#16", type=evoPetrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="015", type=TransitionToPlace, multiplicity=Multiplicity(1, 9999))
    }
)
net2: BinaryAssociation = BinaryAssociation(
    name="net2",
    ends={
        Property(name="#4", type=evoPetrinet_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="03", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
incomingArc5: BinaryAssociation = BinaryAssociation(
    name="incomingArc5",
    ends={
        Property(name="#7", type=evoPetrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="06", type=TransitionToPlace, multiplicity=Multiplicity(0, 9999))
    }
)
src17: BinaryAssociation = BinaryAssociation(
    name="src17",
    ends={
        Property(name="#19", type=evoPetrinet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="018", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
dst20: BinaryAssociation = BinaryAssociation(
    name="dst20",
    ends={
        Property(name="#22", type=evoPetrinet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="021", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
src23: BinaryAssociation = BinaryAssociation(
    name="src23",
    ends={
        Property(name="#25", type=evoPetrinet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="024", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
dst26: BinaryAssociation = BinaryAssociation(
    name="dst26",
    ends={
        Property(name="#28", type=evoPetrinet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="027", type=Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_evoPetrinet_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=evoPetrinet_NamedElement)
gen_evoPetrinet_PetriNet_NamedElement = Generalization(general=NamedElement, specific=evoPetrinet_PetriNet)
gen_evoPetrinet_Transition_Element = Generalization(general=Element, specific=evoPetrinet_Transition)
gen_evoPetrinet_Arc_Element = Generalization(general=Element, specific=evoPetrinet_Arc)
gen_evoPetrinet_PlaceToTransition_Arc = Generalization(general=Arc, specific=evoPetrinet_PlaceToTransition)
gen_evoPetrinet_Element_NamedElement = Generalization(general=NamedElement, specific=evoPetrinet_Element)
gen_evoPetrinet_Place_Element = Generalization(general=Element, specific=evoPetrinet_Place)
gen_evoPetrinet_TransitionToPlace_Arc = Generalization(general=Arc, specific=evoPetrinet_TransitionToPlace)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PetriNet, evoPetrinet_LocatedElement, evoPetrinet_NamedElement, LocatedElement, evoPetrinet_PetriNet, NamedElement, Element, evoPetrinet_PetriNetModel, evoPetrinet_Transition, evoPetrinet_Arc, evoPetrinet_PlaceToTransition, Arc, Place, evoPetrinet_Element, evoPetrinet_Place, TransitionToPlace, PlaceToTransition, Transition, evoPetrinet_TransitionToPlace},
    associations={nets0, elements1, outgoingArc8, incomingArc11, outgoingArc14, net2, incomingArc5, src17, dst20, src23, dst26},
    generalizations={gen_evoPetrinet_NamedElement_LocatedElement, gen_evoPetrinet_PetriNet_NamedElement, gen_evoPetrinet_Transition_Element, gen_evoPetrinet_Arc_Element, gen_evoPetrinet_PlaceToTransition_Arc, gen_evoPetrinet_Element_NamedElement, gen_evoPetrinet_Place_Element, gen_evoPetrinet_TransitionToPlace_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)