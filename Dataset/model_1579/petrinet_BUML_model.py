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
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
Element = Class(name="Element")
petrinet_Arc = Class(name="petrinet::Arc", is_abstract=True)
petrinet_Element = Class(name="petrinet::Element", is_abstract=True)
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_OutputArc = Class(name="petrinet::OutputArc")
Arc = Class(name="Arc")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_Place = Class(name="petrinet::Place")
petrinet_InputArc = Class(name="petrinet::InputArc")
Node = Class(name="Node")
petrinet_NetworkSystem = Class(name="petrinet::NetworkSystem")

# petrinet_Node class attributes and methods

# Element class attributes and methods

# petrinet_Arc class attributes and methods

# petrinet_Element class attributes and methods
petrinet_Element_name: Property = Property(name="name", type=StringType)
petrinet_Element.attributes={petrinet_Element_name}

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# petrinet_OutputArc class attributes and methods

# Arc class attributes and methods

# petrinet_Transition class attributes and methods
petrinet_Transition_maxDelay: Property = Property(name="maxDelay", type=FloatType)
petrinet_Transition_minDelay: Property = Property(name="minDelay", type=FloatType)
petrinet_Transition.attributes={petrinet_Transition_minDelay, petrinet_Transition_maxDelay}

# petrinet_Place class attributes and methods

# petrinet_InputArc class attributes and methods

# Node class attributes and methods

# petrinet_NetworkSystem class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="petrinet_Element", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromNet1: BinaryAssociation = BinaryAssociation(
    name="fromNet1",
    ends={
        Property(name="petrinet_PetriNet2", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
toNet3: BinaryAssociation = BinaryAssociation(
    name="toNet3",
    ends={
        Property(name="petrinet_PetriNet5", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc4", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
from6: BinaryAssociation = BinaryAssociation(
    name="from6",
    ends={
        Property(name="petrinet_Transition", type=petrinet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_OutputArc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
to7: BinaryAssociation = BinaryAssociation(
    name="to7",
    ends={
        Property(name="petrinet_Place", type=petrinet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_OutputArc8", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
to9: BinaryAssociation = BinaryAssociation(
    name="to9",
    ends={
        Property(name="petrinet_Transition10", type=petrinet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_InputArc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
from11: BinaryAssociation = BinaryAssociation(
    name="from11",
    ends={
        Property(name="petrinet_Place13", type=petrinet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_InputArc12", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
petrinets14: BinaryAssociation = BinaryAssociation(
    name="petrinets14",
    ends={
        Property(name="petrinet_PetriNet15", type=petrinet_NetworkSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_NetworkSystem", type=petrinet_PetriNet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_petrinet_Node_Element = Generalization(general=Element, specific=petrinet_Node)
gen_petrinet_Arc_Element = Generalization(general=Element, specific=petrinet_Arc)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)
gen_petrinet_OutputArc_Arc = Generalization(general=Arc, specific=petrinet_OutputArc)
gen_petrinet_InputArc_Arc = Generalization(general=Arc, specific=petrinet_InputArc)
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Node, Element, petrinet_Arc, petrinet_Element, petrinet_PetriNet, petrinet_OutputArc, Arc, petrinet_Transition, petrinet_Place, petrinet_InputArc, Node, petrinet_NetworkSystem},
    associations={elements0, fromNet1, toNet3, from6, to7, to9, from11, petrinets14},
    generalizations={gen_petrinet_Node_Element, gen_petrinet_Arc_Element, gen_petrinet_Place_Node, gen_petrinet_OutputArc_Arc, gen_petrinet_InputArc_Arc, gen_petrinet_Transition_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)