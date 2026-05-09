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
evoPetrinet_PetriNet = Class(name="evoPetrinet_PetriNet")
NamedElement = Class(name="NamedElement")
evoPetrinet_PetriNetModel = Class(name="evoPetrinet_PetriNetModel")
PetriNet = Class(name="PetriNet")
evoPetrinet_LocatedElement = Class(name="evoPetrinet_LocatedElement", is_abstract=True)
evoPetrinet_NamedElement = Class(name="evoPetrinet_NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
Place = Class(name="Place")
Transition = Class(name="Transition")
Element = Class(name="Element")
evoPetrinet_Element = Class(name="evoPetrinet_Element", is_abstract=True)
evoPetrinet_Place = Class(name="evoPetrinet_Place")
TransitionToPlace = Class(name="TransitionToPlace")
PlaceToTransition = Class(name="PlaceToTransition")
evoPetrinet_Transition = Class(name="evoPetrinet_Transition")
evoPetrinet_Arc = Class(name="evoPetrinet_Arc", is_abstract=True)
evoPetrinet_PlaceToTransition = Class(name="evoPetrinet_PlaceToTransition")
Arc = Class(name="Arc")
evoPetrinet_TransitionToPlace = Class(name="evoPetrinet_TransitionToPlace")

# evoPetrinet_PetriNet class attributes and methods

# NamedElement class attributes and methods

# evoPetrinet_PetriNetModel class attributes and methods

# PetriNet class attributes and methods

# evoPetrinet_LocatedElement class attributes and methods
evoPetrinet_LocatedElement_location: Property = Property(name="location", type=StringType)
evoPetrinet_LocatedElement.attributes={evoPetrinet_LocatedElement_location}

# evoPetrinet_NamedElement class attributes and methods
evoPetrinet_NamedElement_name: Property = Property(name="name", type=StringType)
evoPetrinet_NamedElement.attributes={evoPetrinet_NamedElement_name}

# LocatedElement class attributes and methods

# Place class attributes and methods

# Transition class attributes and methods

# Element class attributes and methods

# evoPetrinet_Element class attributes and methods

# evoPetrinet_Place class attributes and methods

# TransitionToPlace class attributes and methods

# PlaceToTransition class attributes and methods

# evoPetrinet_Transition class attributes and methods

# evoPetrinet_Arc class attributes and methods
evoPetrinet_Arc_weight: Property = Property(name="weight", type=StringType)
evoPetrinet_Arc.attributes={evoPetrinet_Arc_weight}

# evoPetrinet_PlaceToTransition class attributes and methods

# Arc class attributes and methods

# evoPetrinet_TransitionToPlace class attributes and methods

# Relationships
nets0: BinaryAssociation = BinaryAssociation(
    name="nets0",
    ends={
        Property(name="PetriNet", type=evoPetrinet_PetriNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="evoPetrinet_PetriNetModel", type=PetriNet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src12: BinaryAssociation = BinaryAssociation(
    name="src12",
    ends={
        Property(name="Place", type=evoPetrinet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="Element", type=evoPetrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net2: BinaryAssociation = BinaryAssociation(
    name="net2",
    ends={
        Property(name="PetriNet3", type=evoPetrinet_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
incomingArc4: BinaryAssociation = BinaryAssociation(
    name="incomingArc4",
    ends={
        Property(name="TransitionToPlace", type=evoPetrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=TransitionToPlace, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingArc5: BinaryAssociation = BinaryAssociation(
    name="outgoingArc5",
    ends={
        Property(name="PlaceToTransition", type=evoPetrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=PlaceToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingArc6: BinaryAssociation = BinaryAssociation(
    name="incomingArc6",
    ends={
        Property(name="PlaceToTransition8", type=evoPetrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst7", type=PlaceToTransition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingArc9: BinaryAssociation = BinaryAssociation(
    name="outgoingArc9",
    ends={
        Property(name="TransitionToPlace11", type=evoPetrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src10", type=TransitionToPlace, multiplicity=Multiplicity(1, 9999))
    }
)
dst13: BinaryAssociation = BinaryAssociation(
    name="dst13",
    ends={
        Property(name="Transition", type=evoPetrinet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
src14: BinaryAssociation = BinaryAssociation(
    name="src14",
    ends={
        Property(name="Transition16", type=evoPetrinet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc15", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
dst17: BinaryAssociation = BinaryAssociation(
    name="dst17",
    ends={
        Property(name="Place19", type=evoPetrinet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc18", type=Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_evoPetrinet_PetriNet_NamedElement = Generalization(general=NamedElement, specific=evoPetrinet_PetriNet)
gen_evoPetrinet_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=evoPetrinet_NamedElement)
gen_evoPetrinet_Element_NamedElement = Generalization(general=NamedElement, specific=evoPetrinet_Element)
gen_evoPetrinet_Place_Element = Generalization(general=Element, specific=evoPetrinet_Place)
gen_evoPetrinet_Transition_Element = Generalization(general=Element, specific=evoPetrinet_Transition)
gen_evoPetrinet_Arc_Element = Generalization(general=Element, specific=evoPetrinet_Arc)
gen_evoPetrinet_PlaceToTransition_Arc = Generalization(general=Arc, specific=evoPetrinet_PlaceToTransition)
gen_evoPetrinet_TransitionToPlace_Arc = Generalization(general=Arc, specific=evoPetrinet_TransitionToPlace)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={evoPetrinet_PetriNet, NamedElement, evoPetrinet_PetriNetModel, PetriNet, evoPetrinet_LocatedElement, evoPetrinet_NamedElement, LocatedElement, Place, Transition, Element, evoPetrinet_Element, evoPetrinet_Place, TransitionToPlace, PlaceToTransition, evoPetrinet_Transition, evoPetrinet_Arc, evoPetrinet_PlaceToTransition, Arc, evoPetrinet_TransitionToPlace},
    associations={nets0, src12, elements1, net2, incomingArc4, outgoingArc5, incomingArc6, outgoingArc9, dst13, src14, dst17},
    generalizations={gen_evoPetrinet_PetriNet_NamedElement, gen_evoPetrinet_NamedElement_LocatedElement, gen_evoPetrinet_Element_NamedElement, gen_evoPetrinet_Place_Element, gen_evoPetrinet_Transition_Element, gen_evoPetrinet_Arc_Element, gen_evoPetrinet_PlaceToTransition_Arc, gen_evoPetrinet_TransitionToPlace_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)