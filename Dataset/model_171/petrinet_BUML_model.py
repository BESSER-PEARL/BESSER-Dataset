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
petrinet_Place = Class(name="petrinet::Place")
Node = Class(name="Node")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_PlaceTransitionArc = Class(name="petrinet::PlaceTransitionArc")
Arc = Class(name="Arc")
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_Arc = Class(name="petrinet::Arc", is_abstract=True)
petrinet_TransitionPlaceArc = Class(name="petrinet::TransitionPlaceArc")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)

# petrinet_Place class attributes and methods
petrinet_Place_tokens: Property = Property(name="tokens", type=IntegerType)
petrinet_Place_capacity: Property = Property(name="capacity", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_capacity, petrinet_Place_tokens}

# Node class attributes and methods

# petrinet_Transition class attributes and methods

# petrinet_PlaceTransitionArc class attributes and methods

# Arc class attributes and methods

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# petrinet_Arc class attributes and methods
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc.attributes={petrinet_Arc_weight}

# petrinet_TransitionPlaceArc class attributes and methods

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# Relationships
ptFromPlace0: BinaryAssociation = BinaryAssociation(
    name="ptFromPlace0",
    ends={
        Property(name="petrinet_Place", type=petrinet_PlaceTransitionArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PlaceTransitionArc", type=petrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)
ptToTransition1: BinaryAssociation = BinaryAssociation(
    name="ptToTransition1",
    ends={
        Property(name="petrinet_Transition", type=petrinet_PlaceTransitionArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PlaceTransitionArc2", type=petrinet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
tpFromTransition3: BinaryAssociation = BinaryAssociation(
    name="tpFromTransition3",
    ends={
        Property(name="petrinet_Transition4", type=petrinet_TransitionPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_TransitionPlaceArc", type=petrinet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
tpToPlace5: BinaryAssociation = BinaryAssociation(
    name="tpToPlace5",
    ends={
        Property(name="petrinet_Place7", type=petrinet_TransitionPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_TransitionPlaceArc6", type=petrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)
places8: BinaryAssociation = BinaryAssociation(
    name="places8",
    ends={
        Property(name="petrinet_Place9", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions10: BinaryAssociation = BinaryAssociation(
    name="transitions10",
    ends={
        Property(name="petrinet_Transition12", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet11", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputArcs13: BinaryAssociation = BinaryAssociation(
    name="inputArcs13",
    ends={
        Property(name="petrinet_PlaceTransitionArc15", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet14", type=petrinet_PlaceTransitionArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputArcs16: BinaryAssociation = BinaryAssociation(
    name="outputArcs16",
    ends={
        Property(name="petrinet_TransitionPlaceArc18", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet17", type=petrinet_TransitionPlaceArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes21: BinaryAssociation = BinaryAssociation(
    name="nodes21",
    ends={
        Property(name="petrinet_Node", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet22", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs19: BinaryAssociation = BinaryAssociation(
    name="arcs19",
    ends={
        Property(name="petrinet_Arc", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet20", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_PlaceTransitionArc_Arc = Generalization(general=Arc, specific=petrinet_PlaceTransitionArc)
gen_petrinet_TransitionPlaceArc_Arc = Generalization(general=Arc, specific=petrinet_TransitionPlaceArc)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Place, Node, petrinet_Transition, petrinet_PlaceTransitionArc, Arc, petrinet_PetriNet, petrinet_Arc, petrinet_TransitionPlaceArc, petrinet_Node},
    associations={ptFromPlace0, ptToTransition1, tpFromTransition3, tpToPlace5, places8, transitions10, inputArcs13, outputArcs16, nodes21, arcs19},
    generalizations={gen_petrinet_Place_Node, gen_petrinet_Transition_Node, gen_petrinet_PlaceTransitionArc_Arc, gen_petrinet_TransitionPlaceArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)