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
RefNodes = Class(name="RefNodes")
petrinet_Arc = Class(name="petrinet::Arc")
RefArcs = Class(name="RefArcs")
petrinet_PetriNet = Class(name="petrinet::PetriNet")
RefPetriNets = Class(name="RefPetriNets")
petrinet_RefNodes = Class(name="petrinet::RefNodes", is_abstract=True)
petrinet_RefArcs = Class(name="petrinet::RefArcs", is_abstract=True)
petrinet_RefPetriNets = Class(name="petrinet::RefPetriNets", is_abstract=True)
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
petrinet_Transition = Class(name="petrinet::Transition")
Node = Class(name="Node")
petrinet_Place = Class(name="petrinet::Place")
petrinet_RefTokens = Class(name="petrinet::RefTokens", is_abstract=True)
petrinet_Token = Class(name="petrinet::Token")
RefTokens = Class(name="RefTokens")

# RefNodes class attributes and methods

# petrinet_Arc class attributes and methods
petrinet_Arc_name: Property = Property(name="name", type=StringType)
petrinet_Arc.attributes={petrinet_Arc_name}

# RefArcs class attributes and methods

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# RefPetriNets class attributes and methods

# petrinet_RefNodes class attributes and methods

# petrinet_RefArcs class attributes and methods

# petrinet_RefPetriNets class attributes and methods

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# petrinet_Transition class attributes and methods

# Node class attributes and methods

# petrinet_Place class attributes and methods

# petrinet_RefTokens class attributes and methods

# petrinet_Token class attributes and methods
petrinet_Token_name: Property = Property(name="name", type=StringType)
petrinet_Token.attributes={petrinet_Token_name}

# RefTokens class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="petrinet_RefNodes", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_RefNodes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="petrinet_RefArcs", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet2", type=petrinet_RefArcs, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="petrinet_RefNodes4", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc", type=petrinet_RefNodes, multiplicity=Multiplicity(1, 1))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="petrinet_RefNodes7", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc6", type=petrinet_RefNodes, multiplicity=Multiplicity(1, 1))
    }
)
marking8: BinaryAssociation = BinaryAssociation(
    name="marking8",
    ends={
        Property(name="petrinet_RefTokens", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place", type=petrinet_RefTokens, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_petrinet_Node_RefNodes = Generalization(general=RefNodes, specific=petrinet_Node)
gen_petrinet_Arc_RefArcs = Generalization(general=RefArcs, specific=petrinet_Arc)
gen_petrinet_PetriNet_RefPetriNets = Generalization(general=RefPetriNets, specific=petrinet_PetriNet)
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)
gen_petrinet_Token_RefTokens = Generalization(general=RefTokens, specific=petrinet_Token)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={RefNodes, petrinet_Arc, RefArcs, petrinet_PetriNet, RefPetriNets, petrinet_RefNodes, petrinet_RefArcs, petrinet_RefPetriNets, petrinet_Node, petrinet_Transition, Node, petrinet_Place, petrinet_RefTokens, petrinet_Token, RefTokens},
    associations={nodes0, arcs1, target3, source5, marking8},
    generalizations={gen_petrinet_Node_RefNodes, gen_petrinet_Arc_RefArcs, gen_petrinet_PetriNet_RefPetriNets, gen_petrinet_Transition_Node, gen_petrinet_Place_Node, gen_petrinet_Token_RefTokens},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)