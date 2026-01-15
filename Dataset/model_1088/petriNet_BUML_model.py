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
petriNet_PetriNet = Class(name="petriNet::PetriNet")
petriNet_Element = Class(name="petriNet::Element", is_abstract=True)
petriNet_Place = Class(name="petriNet::Place")
Node = Class(name="Node")
petriNet_Transition = Class(name="petriNet::Transition")
petriNet_Arc = Class(name="petriNet::Arc")
Element = Class(name="Element")
petriNet_Node = Class(name="petriNet::Node", is_abstract=True)

# petriNet_PetriNet class attributes and methods
petriNet_PetriNet_diagramName: Property = Property(name="diagramName", type=StringType)
petriNet_PetriNet.attributes={petriNet_PetriNet_diagramName}

# petriNet_Element class attributes and methods

# petriNet_Place class attributes and methods
petriNet_Place_noTokens: Property = Property(name="noTokens", type=IntegerType)
petriNet_Place.attributes={petriNet_Place_noTokens}

# Node class attributes and methods

# petriNet_Transition class attributes and methods

# petriNet_Arc class attributes and methods

# Element class attributes and methods

# petriNet_Node class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="Element", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram", type=petriNet_Element, multiplicity=Multiplicity(10, 9999), is_composite=True)
    }
)
diagram1: BinaryAssociation = BinaryAssociation(
    name="diagram1",
    ends={
        Property(name="PetriNet", type=petriNet_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
hiddenOpposite2: BinaryAssociation = BinaryAssociation(
    name="hiddenOpposite2",
    ends={
        Property(name="petriNet_Transition", type=petriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_Place", type=petriNet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="Node", type=petriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArcs", type=petriNet_Node, multiplicity=Multiplicity(1, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="Node5", type=petriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArcs", type=petriNet_Node, multiplicity=Multiplicity(1, 1))
    }
)
outgoingArcs6: BinaryAssociation = BinaryAssociation(
    name="outgoingArcs6",
    ends={
        Property(name="Arc", type=petriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petriNet_Arc, multiplicity=Multiplicity(0, 1))
    }
)
incomingArcs7: BinaryAssociation = BinaryAssociation(
    name="incomingArcs7",
    ends={
        Property(name="Arc8", type=petriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petriNet_Arc, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_petriNet_Place_Node = Generalization(general=Node, specific=petriNet_Place)
gen_petriNet_Transition_Node = Generalization(general=Node, specific=petriNet_Transition)
gen_petriNet_Arc_Element = Generalization(general=Element, specific=petriNet_Arc)
gen_petriNet_Node_Element = Generalization(general=Element, specific=petriNet_Node)

# Domain Model
domain_model = DomainModel(
    name="petriNet",
    types={petriNet_PetriNet, petriNet_Element, petriNet_Place, Node, petriNet_Transition, petriNet_Arc, Element, petriNet_Node},
    associations={elements0, diagram1, hiddenOpposite2, source3, target4, outgoingArcs6, incomingArcs7},
    generalizations={gen_petriNet_Place_Node, gen_petriNet_Transition_Node, gen_petriNet_Arc_Element, gen_petriNet_Node_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)