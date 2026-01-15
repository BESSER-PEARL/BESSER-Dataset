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
PN_PetriNet = Class(name="PN::PetriNet")
PN_NamedElement = Class(name="PN::NamedElement", is_abstract=True)
PN_Node = Class(name="PN::Node", is_abstract=True)
NamedElement = Class(name="NamedElement")
PN_Transition = Class(name="PN::Transition")
Node = Class(name="Node")
PN_Place = Class(name="PN::Place")
PN_Arc = Class(name="PN::Arc", is_abstract=True)
PN_OutputArc = Class(name="PN::OutputArc")
Arc = Class(name="Arc")
PN_InputArc = Class(name="PN::InputArc")

# PN_PetriNet class attributes and methods
PN_PetriNet_name: Property = Property(name="name", type=StringType)
PN_PetriNet.attributes={PN_PetriNet_name}

# PN_NamedElement class attributes and methods
PN_NamedElement_name: Property = Property(name="name", type=StringType)
PN_NamedElement.attributes={PN_NamedElement_name}

# PN_Node class attributes and methods

# NamedElement class attributes and methods

# PN_Transition class attributes and methods
PN_Transition_maxDelay: Property = Property(name="maxDelay", type=FloatType)
PN_Transition_minDelay: Property = Property(name="minDelay", type=FloatType)
PN_Transition.attributes={PN_Transition_maxDelay, PN_Transition_minDelay}

# Node class attributes and methods

# PN_Place class attributes and methods

# PN_Arc class attributes and methods

# PN_OutputArc class attributes and methods

# Arc class attributes and methods

# PN_InputArc class attributes and methods

# Relationships
from1: BinaryAssociation = BinaryAssociation(
    name="from1",
    ends={
        Property(name="PN_Transition", type=PN_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PN_OutputArc", type=PN_Transition, multiplicity=Multiplicity(1, 1))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="PN_NamedElement", type=PN_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PN_PetriNet", type=PN_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to2: BinaryAssociation = BinaryAssociation(
    name="to2",
    ends={
        Property(name="PN_Place", type=PN_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PN_OutputArc3", type=PN_Place, multiplicity=Multiplicity(1, 1))
    }
)
from4: BinaryAssociation = BinaryAssociation(
    name="from4",
    ends={
        Property(name="PN_Place5", type=PN_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PN_InputArc", type=PN_Place, multiplicity=Multiplicity(1, 1))
    }
)
to6: BinaryAssociation = BinaryAssociation(
    name="to6",
    ends={
        Property(name="PN_Transition8", type=PN_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PN_InputArc7", type=PN_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PN_Node_NamedElement = Generalization(general=NamedElement, specific=PN_Node)
gen_PN_Transition_Node = Generalization(general=Node, specific=PN_Transition)
gen_PN_Place_Node = Generalization(general=Node, specific=PN_Place)
gen_PN_Arc_NamedElement = Generalization(general=NamedElement, specific=PN_Arc)
gen_PN_OutputArc_Arc = Generalization(general=Arc, specific=PN_OutputArc)
gen_PN_InputArc_Arc = Generalization(general=Arc, specific=PN_InputArc)

# Domain Model
domain_model = DomainModel(
    name="PN",
    types={PN_PetriNet, PN_NamedElement, PN_Node, NamedElement, PN_Transition, Node, PN_Place, PN_Arc, PN_OutputArc, Arc, PN_InputArc},
    associations={from1, elements0, to2, from4, to6},
    generalizations={gen_PN_Node_NamedElement, gen_PN_Transition_Node, gen_PN_Place_Node, gen_PN_Arc_NamedElement, gen_PN_OutputArc_Arc, gen_PN_InputArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)