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
petrinet_System = Class(name="petrinet::System")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
Element = Class(name="Element")
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_PetriNetRelationship = Class(name="petrinet::PetriNetRelationship")
petrinet_Element = Class(name="petrinet::Element", is_abstract=True)
petrinet_InputArc = Class(name="petrinet::InputArc")
petrinet_Arc = Class(name="petrinet::Arc", is_abstract=True)
petrinet_Place = Class(name="petrinet::Place")
Node = Class(name="Node")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_OutputArc = Class(name="petrinet::OutputArc")
Arc = Class(name="Arc")

# petrinet_System class attributes and methods

# petrinet_Node class attributes and methods
petrinet_Node_minDelay: Property = Property(name="minDelay", type=FloatType)
petrinet_Node_maxDelay: Property = Property(name="maxDelay", type=FloatType)
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name, petrinet_Node_minDelay, petrinet_Node_maxDelay}

# Element class attributes and methods

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# petrinet_PetriNetRelationship class attributes and methods

# petrinet_Element class attributes and methods

# petrinet_InputArc class attributes and methods

# petrinet_Arc class attributes and methods

# petrinet_Place class attributes and methods

# Node class attributes and methods

# petrinet_Transition class attributes and methods

# petrinet_OutputArc class attributes and methods

# Arc class attributes and methods

# Relationships
from5: BinaryAssociation = BinaryAssociation(
    name="from5",
    ends={
        Property(name="petrinet_PetriNet7", type=petrinet_PetriNetRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNetRelationship6", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
to8: BinaryAssociation = BinaryAssociation(
    name="to8",
    ends={
        Property(name="petrinet_PetriNet10", type=petrinet_PetriNetRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNetRelationship9", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
petrinets0: BinaryAssociation = BinaryAssociation(
    name="petrinets0",
    ends={
        Property(name="petrinet_PetriNet", type=petrinet_System, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_System", type=petrinet_PetriNet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
petrinetrelationships1: BinaryAssociation = BinaryAssociation(
    name="petrinetrelationships1",
    ends={
        Property(name="petrinet_PetriNetRelationship", type=petrinet_System, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_System2", type=petrinet_PetriNetRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="petrinet_Element", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet4", type=petrinet_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to14: BinaryAssociation = BinaryAssociation(
    name="to14",
    ends={
        Property(name="petrinet_Transition15", type=petrinet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_InputArc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
from16: BinaryAssociation = BinaryAssociation(
    name="from16",
    ends={
        Property(name="petrinet_Place18", type=petrinet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_InputArc17", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
to11: BinaryAssociation = BinaryAssociation(
    name="to11",
    ends={
        Property(name="petrinet_Place", type=petrinet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_OutputArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
from12: BinaryAssociation = BinaryAssociation(
    name="from12",
    ends={
        Property(name="petrinet_Transition", type=petrinet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_OutputArc13", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Node_Element = Generalization(general=Element, specific=petrinet_Node)
gen_petrinet_InputArc_Arc = Generalization(general=Arc, specific=petrinet_InputArc)
gen_petrinet_Arc_Element = Generalization(general=Element, specific=petrinet_Arc)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_OutputArc_Arc = Generalization(general=Arc, specific=petrinet_OutputArc)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_System, petrinet_Node, Element, petrinet_PetriNet, petrinet_PetriNetRelationship, petrinet_Element, petrinet_InputArc, petrinet_Arc, petrinet_Place, Node, petrinet_Transition, petrinet_OutputArc, Arc},
    associations={from5, to8, petrinets0, petrinetrelationships1, elements3, to14, from16, to11, from12},
    generalizations={gen_petrinet_Node_Element, gen_petrinet_InputArc_Arc, gen_petrinet_Arc_Element, gen_petrinet_Place_Node, gen_petrinet_Transition_Node, gen_petrinet_OutputArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)