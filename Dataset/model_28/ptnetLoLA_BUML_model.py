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

# Enumerations
NodeType: Enumeration = Enumeration(
    name="NodeType",
    literals={
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output"),
			EnumerationLiteral(name="inout")
    }
)

# Classes
ptnetLoLA_Place = Class(name="ptnetLoLA::Place")
Node = Class(name="Node")
ptnetLoLA_PtNet = Class(name="ptnetLoLA::PtNet")
ptnetLoLA_Transition = Class(name="ptnetLoLA::Transition")
ptnetLoLA_Marking = Class(name="ptnetLoLA::Marking")
ptnetLoLA_Annotation = Class(name="ptnetLoLA::Annotation")
ptnetLoLA_Node = Class(name="ptnetLoLA::Node")
ptnetLoLA_RefMarkedPlace = Class(name="ptnetLoLA::RefMarkedPlace")
ptnetLoLA_PlaceReference = Class(name="ptnetLoLA::PlaceReference")
ptnetLoLA_Arc = Class(name="ptnetLoLA::Arc")
ptnetLoLA_ArcToPlace = Class(name="ptnetLoLA::ArcToPlace")
Arc = Class(name="Arc")
ptnetLoLA_ArcToTransition = Class(name="ptnetLoLA::ArcToTransition")
ptnetLoLA_TransitionExt = Class(name="ptnetLoLA::TransitionExt")
Transition = Class(name="Transition")
PlaceReference = Class(name="PlaceReference")
ptnetLoLA_ArcToPlaceExt = Class(name="ptnetLoLA::ArcToPlaceExt")
ArcToPlace = Class(name="ArcToPlace")
ptnetLoLA_ArcToTransitionExt = Class(name="ptnetLoLA::ArcToTransitionExt")
ArcToTransition = Class(name="ArcToTransition")
ptnetLoLA_PlaceExt = Class(name="ptnetLoLA::PlaceExt")
Place = Class(name="Place")

# ptnetLoLA_Place class attributes and methods
ptnetLoLA_Place_token: Property = Property(name="token", type=IntegerType)
ptnetLoLA_Place_finalMarking: Property = Property(name="finalMarking", type=IntegerType)
ptnetLoLA_Place.attributes={ptnetLoLA_Place_finalMarking, ptnetLoLA_Place_token}

# Node class attributes and methods

# ptnetLoLA_PtNet class attributes and methods

# ptnetLoLA_Transition class attributes and methods

# ptnetLoLA_Marking class attributes and methods

# ptnetLoLA_Annotation class attributes and methods
ptnetLoLA_Annotation_text: Property = Property(name="text", type=StringType)
ptnetLoLA_Annotation.attributes={ptnetLoLA_Annotation_text}

# ptnetLoLA_Node class attributes and methods
ptnetLoLA_Node_name: Property = Property(name="name", type=StringType)
ptnetLoLA_Node_type: Property = Property(name="type", type=StringType)
ptnetLoLA_Node.attributes={ptnetLoLA_Node_type, ptnetLoLA_Node_name}

# ptnetLoLA_RefMarkedPlace class attributes and methods
ptnetLoLA_RefMarkedPlace_token: Property = Property(name="token", type=IntegerType)
ptnetLoLA_RefMarkedPlace.attributes={ptnetLoLA_RefMarkedPlace_token}

# ptnetLoLA_PlaceReference class attributes and methods

# ptnetLoLA_Arc class attributes and methods
ptnetLoLA_Arc_weight: Property = Property(name="weight", type=IntegerType)
ptnetLoLA_Arc.attributes={ptnetLoLA_Arc_weight}

# ptnetLoLA_ArcToPlace class attributes and methods

# Arc class attributes and methods

# ptnetLoLA_ArcToTransition class attributes and methods

# ptnetLoLA_TransitionExt class attributes and methods
ptnetLoLA_TransitionExt_probability: Property = Property(name="probability", type=FloatType)
ptnetLoLA_TransitionExt_minTime: Property = Property(name="minTime", type=IntegerType)
ptnetLoLA_TransitionExt_cost: Property = Property(name="cost", type=FloatType)
ptnetLoLA_TransitionExt_maxTime: Property = Property(name="maxTime", type=IntegerType)
ptnetLoLA_TransitionExt.attributes={ptnetLoLA_TransitionExt_maxTime, ptnetLoLA_TransitionExt_minTime, ptnetLoLA_TransitionExt_cost, ptnetLoLA_TransitionExt_probability}

# Transition class attributes and methods

# PlaceReference class attributes and methods

# ptnetLoLA_ArcToPlaceExt class attributes and methods
ptnetLoLA_ArcToPlaceExt_probability: Property = Property(name="probability", type=FloatType)
ptnetLoLA_ArcToPlaceExt.attributes={ptnetLoLA_ArcToPlaceExt_probability}

# ArcToPlace class attributes and methods

# ptnetLoLA_ArcToTransitionExt class attributes and methods
ptnetLoLA_ArcToTransitionExt_probability: Property = Property(name="probability", type=FloatType)
ptnetLoLA_ArcToTransitionExt.attributes={ptnetLoLA_ArcToTransitionExt_probability}

# ArcToTransition class attributes and methods

# ptnetLoLA_PlaceExt class attributes and methods
ptnetLoLA_PlaceExt_probability: Property = Property(name="probability", type=FloatType)
ptnetLoLA_PlaceExt_isStart: Property = Property(name="isStart", type=BooleanType)
ptnetLoLA_PlaceExt.attributes={ptnetLoLA_PlaceExt_isStart, ptnetLoLA_PlaceExt_probability}

# Place class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="ptnetLoLA_Place", type=ptnetLoLA_PtNet, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnetLoLA_PtNet", type=ptnetLoLA_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="ptnetLoLA_Transition", type=ptnetLoLA_PtNet, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnetLoLA_PtNet2", type=ptnetLoLA_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialMarking3: BinaryAssociation = BinaryAssociation(
    name="initialMarking3",
    ends={
        Property(name="ptnetLoLA_Marking", type=ptnetLoLA_PtNet, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnetLoLA_PtNet4", type=ptnetLoLA_Marking, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotation5: BinaryAssociation = BinaryAssociation(
    name="annotation5",
    ends={
        Property(name="ptnetLoLA_Annotation", type=ptnetLoLA_PtNet, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnetLoLA_PtNet6", type=ptnetLoLA_Annotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation12: BinaryAssociation = BinaryAssociation(
    name="annotation12",
    ends={
        Property(name="ptnetLoLA_Annotation13", type=ptnetLoLA_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnetLoLA_Node", type=ptnetLoLA_Annotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incoming14: BinaryAssociation = BinaryAssociation(
    name="incoming14",
    ends={
        Property(name="Arc", type=ptnetLoLA_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=ptnetLoLA_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing15: BinaryAssociation = BinaryAssociation(
    name="outgoing15",
    ends={
        Property(name="Arc16", type=ptnetLoLA_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ptnetLoLA_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
places17: BinaryAssociation = BinaryAssociation(
    name="places17",
    ends={
        Property(name="ptnetLoLA_RefMarkedPlace", type=ptnetLoLA_Marking, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnetLoLA_Marking18", type=ptnetLoLA_RefMarkedPlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs7: BinaryAssociation = BinaryAssociation(
    name="arcs7",
    ends={
        Property(name="ptnetLoLA_Arc", type=ptnetLoLA_PtNet, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnetLoLA_PtNet8", type=ptnetLoLA_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalMarking9: BinaryAssociation = BinaryAssociation(
    name="finalMarking9",
    ends={
        Property(name="ptnetLoLA_Marking11", type=ptnetLoLA_PtNet, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnetLoLA_PtNet10", type=ptnetLoLA_Marking, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="Node", type=ptnetLoLA_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=ptnetLoLA_Node, multiplicity=Multiplicity(1, 1))
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="Node23", type=ptnetLoLA_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=ptnetLoLA_Node, multiplicity=Multiplicity(1, 1))
    }
)
place19: BinaryAssociation = BinaryAssociation(
    name="place19",
    ends={
        Property(name="ptnetLoLA_Place20", type=ptnetLoLA_PlaceReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ptnetLoLA_PlaceReference", type=ptnetLoLA_Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ptnetLoLA_Place_Node = Generalization(general=Node, specific=ptnetLoLA_Place)
gen_ptnetLoLA_Transition_Node = Generalization(general=Node, specific=ptnetLoLA_Transition)
gen_ptnetLoLA_ArcToPlace_Arc = Generalization(general=Arc, specific=ptnetLoLA_ArcToPlace)
gen_ptnetLoLA_ArcToTransition_Arc = Generalization(general=Arc, specific=ptnetLoLA_ArcToTransition)
gen_ptnetLoLA_TransitionExt_Transition = Generalization(general=Transition, specific=ptnetLoLA_TransitionExt)
gen_ptnetLoLA_RefMarkedPlace_PlaceReference = Generalization(general=PlaceReference, specific=ptnetLoLA_RefMarkedPlace)
gen_ptnetLoLA_ArcToPlaceExt_ArcToPlace = Generalization(general=ArcToPlace, specific=ptnetLoLA_ArcToPlaceExt)
gen_ptnetLoLA_ArcToTransitionExt_ArcToTransition = Generalization(general=ArcToTransition, specific=ptnetLoLA_ArcToTransitionExt)
gen_ptnetLoLA_PlaceExt_Place = Generalization(general=Place, specific=ptnetLoLA_PlaceExt)

# Domain Model
domain_model = DomainModel(
    name="ptnetLoLA",
    types={ptnetLoLA_Place, Node, ptnetLoLA_PtNet, ptnetLoLA_Transition, ptnetLoLA_Marking, ptnetLoLA_Annotation, ptnetLoLA_Node, ptnetLoLA_RefMarkedPlace, ptnetLoLA_PlaceReference, ptnetLoLA_Arc, ptnetLoLA_ArcToPlace, Arc, ptnetLoLA_ArcToTransition, ptnetLoLA_TransitionExt, Transition, PlaceReference, ptnetLoLA_ArcToPlaceExt, ArcToPlace, ptnetLoLA_ArcToTransitionExt, ArcToTransition, ptnetLoLA_PlaceExt, Place, NodeType},
    associations={places0, transitions1, initialMarking3, annotation5, annotation12, incoming14, outgoing15, places17, arcs7, finalMarking9, source21, target22, place19},
    generalizations={gen_ptnetLoLA_Place_Node, gen_ptnetLoLA_Transition_Node, gen_ptnetLoLA_ArcToPlace_Arc, gen_ptnetLoLA_ArcToTransition_Arc, gen_ptnetLoLA_TransitionExt_Transition, gen_ptnetLoLA_RefMarkedPlace_PlaceReference, gen_ptnetLoLA_ArcToPlaceExt_ArcToPlace, gen_ptnetLoLA_ArcToTransitionExt_ArcToTransition, gen_ptnetLoLA_PlaceExt_Place},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)