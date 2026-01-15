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
petriNet_LocatedElement = Class(name="petriNet::LocatedElement", is_abstract=True)
petriNet_NamedElement = Class(name="petriNet::NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
petriNet_PetriNet = Class(name="petriNet::PetriNet")
NamedElement = Class(name="NamedElement")
petriNet_Element = Class(name="petriNet::Element", is_abstract=True)
petriNet_Place = Class(name="petriNet::Place")
Element = Class(name="Element")
petriNet_TransitionToPlace = Class(name="petriNet::TransitionToPlace")
petriNet_Arc = Class(name="petriNet::Arc", is_abstract=True)
petriNet_PlaceToTransition = Class(name="petriNet::PlaceToTransition")
petriNet_Transition = Class(name="petriNet::Transition")
Arc = Class(name="Arc")

# petriNet_LocatedElement class attributes and methods
petriNet_LocatedElement_location: Property = Property(name="location", type=StringType)
petriNet_LocatedElement.attributes={petriNet_LocatedElement_location}

# petriNet_NamedElement class attributes and methods
petriNet_NamedElement_name: Property = Property(name="name", type=StringType)
petriNet_NamedElement.attributes={petriNet_NamedElement_name}

# LocatedElement class attributes and methods

# petriNet_PetriNet class attributes and methods

# NamedElement class attributes and methods

# petriNet_Element class attributes and methods

# petriNet_Place class attributes and methods

# Element class attributes and methods

# petriNet_TransitionToPlace class attributes and methods

# petriNet_Arc class attributes and methods
petriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petriNet_Arc.attributes={petriNet_Arc_weight}

# petriNet_PlaceToTransition class attributes and methods

# petriNet_Transition class attributes and methods

# Arc class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="Element", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=petriNet_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="PetriNet", type=petriNet_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
incomingArc4: BinaryAssociation = BinaryAssociation(
    name="incomingArc4",
    ends={
        Property(name="TransitionToPlace", type=petriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=petriNet_TransitionToPlace, multiplicity=Multiplicity(0, 9999))
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="Arc", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=petriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingArc5: BinaryAssociation = BinaryAssociation(
    name="outgoingArc5",
    ends={
        Property(name="PlaceToTransition", type=petriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=petriNet_PlaceToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingArc6: BinaryAssociation = BinaryAssociation(
    name="incomingArc6",
    ends={
        Property(name="PlaceToTransition8", type=petriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="to7", type=petriNet_PlaceToTransition, multiplicity=Multiplicity(1, 9999))
    }
)
net12: BinaryAssociation = BinaryAssociation(
    name="net12",
    ends={
        Property(name="PetriNet13", type=petriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
from14: BinaryAssociation = BinaryAssociation(
    name="from14",
    ends={
        Property(name="Place", type=petriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc", type=petriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
outgoingArc9: BinaryAssociation = BinaryAssociation(
    name="outgoingArc9",
    ends={
        Property(name="TransitionToPlace11", type=petriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="from10", type=petriNet_TransitionToPlace, multiplicity=Multiplicity(1, 9999))
    }
)
from16: BinaryAssociation = BinaryAssociation(
    name="from16",
    ends={
        Property(name="Transition18", type=petriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc17", type=petriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
to19: BinaryAssociation = BinaryAssociation(
    name="to19",
    ends={
        Property(name="Place21", type=petriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc20", type=petriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
to15: BinaryAssociation = BinaryAssociation(
    name="to15",
    ends={
        Property(name="Transition", type=petriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc", type=petriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petriNet_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=petriNet_NamedElement)
gen_petriNet_PetriNet_NamedElement = Generalization(general=NamedElement, specific=petriNet_PetriNet)
gen_petriNet_Element_NamedElement = Generalization(general=NamedElement, specific=petriNet_Element)
gen_petriNet_Place_Element = Generalization(general=Element, specific=petriNet_Place)
gen_petriNet_Transition_Element = Generalization(general=Element, specific=petriNet_Transition)
gen_petriNet_PlaceToTransition_Arc = Generalization(general=Arc, specific=petriNet_PlaceToTransition)
gen_petriNet_Arc_NamedElement = Generalization(general=NamedElement, specific=petriNet_Arc)
gen_petriNet_TransitionToPlace_Arc = Generalization(general=Arc, specific=petriNet_TransitionToPlace)

# Domain Model
domain_model = DomainModel(
    name="petriNet",
    types={petriNet_LocatedElement, petriNet_NamedElement, LocatedElement, petriNet_PetriNet, NamedElement, petriNet_Element, petriNet_Place, Element, petriNet_TransitionToPlace, petriNet_Arc, petriNet_PlaceToTransition, petriNet_Transition, Arc},
    associations={elements0, net3, incomingArc4, arcs1, outgoingArc5, incomingArc6, net12, from14, outgoingArc9, from16, to19, to15},
    generalizations={gen_petriNet_NamedElement_LocatedElement, gen_petriNet_PetriNet_NamedElement, gen_petriNet_Element_NamedElement, gen_petriNet_Place_Element, gen_petriNet_Transition_Element, gen_petriNet_PlaceToTransition_Arc, gen_petriNet_Arc_NamedElement, gen_petriNet_TransitionToPlace_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)