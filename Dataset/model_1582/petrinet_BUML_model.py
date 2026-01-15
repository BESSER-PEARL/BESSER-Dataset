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
petrinet_Element = Class(name="petrinet::Element", is_abstract=True)
petrinet_OutputArc = Class(name="petrinet::OutputArc")
Arc = Class(name="Arc")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_Place = Class(name="petrinet::Place")
petrinet_InputArc = Class(name="petrinet::InputArc")
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
Element = Class(name="Element")
petrinet_Arc = Class(name="petrinet::Arc", is_abstract=True)
Node = Class(name="Node")

# petrinet_Element class attributes and methods
petrinet_Element_name: Property = Property(name="name", type=StringType)
petrinet_Element.attributes={petrinet_Element_name}

# petrinet_OutputArc class attributes and methods

# Arc class attributes and methods

# petrinet_Transition class attributes and methods
petrinet_Transition_maxDelay: Property = Property(name="maxDelay", type=FloatType)
petrinet_Transition_minDelay: Property = Property(name="minDelay", type=FloatType)
petrinet_Transition.attributes={petrinet_Transition_minDelay, petrinet_Transition_maxDelay}

# petrinet_Place class attributes and methods

# petrinet_InputArc class attributes and methods

# petrinet_PetriNet class attributes and methods

# petrinet_Node class attributes and methods

# Element class attributes and methods

# petrinet_Arc class attributes and methods

# Node class attributes and methods

# Relationships
from1: BinaryAssociation = BinaryAssociation(
    name="from1",
    ends={
        Property(name="petrinet_Transition", type=petrinet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_OutputArc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
to2: BinaryAssociation = BinaryAssociation(
    name="to2",
    ends={
        Property(name="petrinet_Place", type=petrinet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_OutputArc3", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
to4: BinaryAssociation = BinaryAssociation(
    name="to4",
    ends={
        Property(name="petrinet_Transition5", type=petrinet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_InputArc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
from6: BinaryAssociation = BinaryAssociation(
    name="from6",
    ends={
        Property(name="petrinet_Place8", type=petrinet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_InputArc7", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="petrinet_Element", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_petrinet_Arc_Element = Generalization(general=Element, specific=petrinet_Arc)
gen_petrinet_OutputArc_Arc = Generalization(general=Arc, specific=petrinet_OutputArc)
gen_petrinet_InputArc_Arc = Generalization(general=Arc, specific=petrinet_InputArc)
gen_petrinet_Node_Element = Generalization(general=Element, specific=petrinet_Node)
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Element, petrinet_OutputArc, Arc, petrinet_Transition, petrinet_Place, petrinet_InputArc, petrinet_PetriNet, petrinet_Node, Element, petrinet_Arc, Node},
    associations={from1, to2, to4, from6, elements0},
    generalizations={gen_petrinet_Arc_Element, gen_petrinet_OutputArc_Arc, gen_petrinet_InputArc_Arc, gen_petrinet_Node_Element, gen_petrinet_Transition_Node, gen_petrinet_Place_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)