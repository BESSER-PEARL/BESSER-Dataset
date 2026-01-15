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
PetriNets_PetriNet = Class(name="PetriNets::PetriNet")
PetriNets_Node = Class(name="PetriNets::Node", is_abstract=True)
PetriNets_Arc = Class(name="PetriNets::Arc", is_abstract=True)
PetriNets_Place = Class(name="PetriNets::Place")
Node = Class(name="Node")
PetriNets_Transition = Class(name="PetriNets::Transition")
PetriNets_TPArc = Class(name="PetriNets::TPArc")
Arc = Class(name="Arc")
PetriNets_PTArc = Class(name="PetriNets::PTArc")
PetriNets_Token = Class(name="PetriNets::Token")

# PetriNets_PetriNet class attributes and methods
PetriNets_PetriNet_bound: Property = Property(name="bound", type=IntegerType)
PetriNets_PetriNet.attributes={PetriNets_PetriNet_bound}

# PetriNets_Node class attributes and methods
PetriNets_Node_name: Property = Property(name="name", type=StringType)
PetriNets_Node.attributes={PetriNets_Node_name}

# PetriNets_Arc class attributes and methods
PetriNets_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNets_Arc.attributes={PetriNets_Arc_weight}

# PetriNets_Place class attributes and methods
PetriNets_Place_tokens: Property = Property(name="tokens", type=IntegerType)
PetriNets_Place.attributes={PetriNets_Place_tokens}

# Node class attributes and methods

# PetriNets_Transition class attributes and methods

# PetriNets_TPArc class attributes and methods

# Arc class attributes and methods

# PetriNets_PTArc class attributes and methods

# PetriNets_Token class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=PetriNets_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="PetriNets_Arc", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_PetriNet", type=PetriNets_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs2: BinaryAssociation = BinaryAssociation(
    name="inputs2",
    ends={
        Property(name="PetriNets_Place", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)
input7: BinaryAssociation = BinaryAssociation(
    name="input7",
    ends={
        Property(name="PetriNets_Transition8", type=PetriNets_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_TPArc", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1))
    }
)
output9: BinaryAssociation = BinaryAssociation(
    name="output9",
    ends={
        Property(name="PetriNets_Place11", type=PetriNets_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_TPArc10", type=PetriNets_Place, multiplicity=Multiplicity(1, 1))
    }
)
output12: BinaryAssociation = BinaryAssociation(
    name="output12",
    ends={
        Property(name="PetriNets_Transition13", type=PetriNets_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_PTArc", type=PetriNets_Transition, multiplicity=Multiplicity(0, 1))
    }
)
input14: BinaryAssociation = BinaryAssociation(
    name="input14",
    ends={
        Property(name="PetriNets_Place16", type=PetriNets_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_PTArc15", type=PetriNets_Place, multiplicity=Multiplicity(0, 1))
    }
)
outputs3: BinaryAssociation = BinaryAssociation(
    name="outputs3",
    ends={
        Property(name="PetriNets_Place5", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition4", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)
net6: BinaryAssociation = BinaryAssociation(
    name="net6",
    ends={
        Property(name="PetriNet", type=PetriNets_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=PetriNets_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_PetriNets_Place_Node = Generalization(general=Node, specific=PetriNets_Place)
gen_PetriNets_Transition_Node = Generalization(general=Node, specific=PetriNets_Transition)
gen_PetriNets_TPArc_Arc = Generalization(general=Arc, specific=PetriNets_TPArc)
gen_PetriNets_PTArc_Arc = Generalization(general=Arc, specific=PetriNets_PTArc)

# Domain Model
domain_model = DomainModel(
    name="PetriNets",
    types={PetriNets_PetriNet, PetriNets_Node, PetriNets_Arc, PetriNets_Place, Node, PetriNets_Transition, PetriNets_TPArc, Arc, PetriNets_PTArc, PetriNets_Token},
    associations={nodes0, arcs1, inputs2, input7, output9, output12, input14, outputs3, net6},
    generalizations={gen_PetriNets_Place_Node, gen_PetriNets_Transition_Node, gen_PetriNets_TPArc_Arc, gen_PetriNets_PTArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)