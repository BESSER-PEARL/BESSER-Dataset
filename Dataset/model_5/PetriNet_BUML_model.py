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
PetriNet_Place = Class(name="PetriNet::Place")
Element = Class(name="Element")
PetriNet_TransitionToPlace = Class(name="PetriNet::TransitionToPlace")
PetriNet_PlaceToTransition = Class(name="PetriNet::PlaceToTransition")
PetriNet_Transition = Class(name="PetriNet::Transition")
Arc = Class(name="Arc")
PetriNet_NamedElement = Class(name="PetriNet::NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
NamedElement = Class(name="NamedElement")
PetriNet_Element = Class(name="PetriNet::Element", is_abstract=True)
PetriNet_Arc = Class(name="PetriNet::Arc", is_abstract=True)

# PetriNet_LocatedElement class attributes and methods
PetriNet_LocatedElement_location: Property = Property(name="location", type=StringType)
PetriNet_LocatedElement.attributes={PetriNet_LocatedElement_location}

# PetriNet_Place class attributes and methods

# Element class attributes and methods

# PetriNet_TransitionToPlace class attributes and methods

# PetriNet_PlaceToTransition class attributes and methods

# PetriNet_Transition class attributes and methods

# Arc class attributes and methods

# PetriNet_NamedElement class attributes and methods
PetriNet_NamedElement_name: Property = Property(name="name", type=StringType)
PetriNet_NamedElement.attributes={PetriNet_NamedElement_name}

# LocatedElement class attributes and methods

# PetriNet_PetriNet class attributes and methods

# NamedElement class attributes and methods

# PetriNet_Element class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNet_Arc.attributes={PetriNet_Arc_weight}

# Relationships
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="net2", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="PetriNet", type=PetriNet_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
incomingArc4: BinaryAssociation = BinaryAssociation(
    name="incomingArc4",
    ends={
        Property(name="TransitionToPlace", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingArc5: BinaryAssociation = BinaryAssociation(
    name="outgoingArc5",
    ends={
        Property(name="PlaceToTransition", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingArc6: BinaryAssociation = BinaryAssociation(
    name="incomingArc6",
    ends={
        Property(name="PlaceToTransition8", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="to7", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingArc9: BinaryAssociation = BinaryAssociation(
    name="outgoingArc9",
    ends={
        Property(name="TransitionToPlace11", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="from10", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 9999))
    }
)
net12: BinaryAssociation = BinaryAssociation(
    name="net12",
    ends={
        Property(name="PetriNet13", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="Element", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=PetriNet_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from16: BinaryAssociation = BinaryAssociation(
    name="from16",
    ends={
        Property(name="Transition18", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc17", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
to19: BinaryAssociation = BinaryAssociation(
    name="to19",
    ends={
        Property(name="Place21", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc20", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
from14: BinaryAssociation = BinaryAssociation(
    name="from14",
    ends={
        Property(name="Place", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
to15: BinaryAssociation = BinaryAssociation(
    name="to15",
    ends={
        Property(name="Transition", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_Element_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Element)
gen_PetriNet_Place_Element = Generalization(general=Element, specific=PetriNet_Place)
gen_PetriNet_Transition_Element = Generalization(general=Element, specific=PetriNet_Transition)
gen_PetriNet_Arc_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Arc)
gen_PetriNet_PlaceToTransition_Arc = Generalization(general=Arc, specific=PetriNet_PlaceToTransition)
gen_PetriNet_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=PetriNet_NamedElement)
gen_PetriNet_PetriNet_NamedElement = Generalization(general=NamedElement, specific=PetriNet_PetriNet)
gen_PetriNet_TransitionToPlace_Arc = Generalization(general=Arc, specific=PetriNet_TransitionToPlace)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_LocatedElement, PetriNet_Place, Element, PetriNet_TransitionToPlace, PetriNet_PlaceToTransition, PetriNet_Transition, Arc, PetriNet_NamedElement, LocatedElement, PetriNet_PetriNet, NamedElement, PetriNet_Element, PetriNet_Arc},
    associations={arcs1, net3, incomingArc4, outgoingArc5, incomingArc6, outgoingArc9, net12, elements0, from16, to19, from14, to15},
    generalizations={gen_PetriNet_Element_NamedElement, gen_PetriNet_Place_Element, gen_PetriNet_Transition_Element, gen_PetriNet_Arc_NamedElement, gen_PetriNet_PlaceToTransition_Arc, gen_PetriNet_NamedElement_LocatedElement, gen_PetriNet_PetriNet_NamedElement, gen_PetriNet_TransitionToPlace_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)