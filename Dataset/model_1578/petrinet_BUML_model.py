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
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Transition = Class(name="petrinet::Transition")
Node = Class(name="Node")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Token = Class(name="petrinet::Token")

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# petrinet_Arc class attributes and methods
petrinet_Arc_name: Property = Property(name="name", type=StringType)
petrinet_Arc.attributes={petrinet_Arc_name}

# petrinet_Transition class attributes and methods

# Node class attributes and methods

# petrinet_Place class attributes and methods

# petrinet_Token class attributes and methods
petrinet_Token_name: Property = Property(name="name", type=StringType)
petrinet_Token.attributes={petrinet_Token_name}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="petrinet_Node", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="petrinet_Arc", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet2", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="petrinet_Node5", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc4", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="petrinet_Node8", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc7", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
marking9: BinaryAssociation = BinaryAssociation(
    name="marking9",
    ends={
        Property(name="petrinet_Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_PetriNet, petrinet_Node, petrinet_Arc, petrinet_Transition, Node, petrinet_Place, petrinet_Token},
    associations={nodes0, arcs1, target3, source6, marking9},
    generalizations={gen_petrinet_Transition_Node, gen_petrinet_Place_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)