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
petri_net_PetriNet = Class(name="petri_net_PetriNet")
petri_net_Node = Class(name="petri_net_Node", is_abstract=True)
petri_net_Arc = Class(name="petri_net_Arc")
petri_net_Transition = Class(name="petri_net_Transition")
Node = Class(name="Node")
petri_net_Place = Class(name="petri_net_Place")

# petri_net_PetriNet class attributes and methods
petri_net_PetriNet_name: Property = Property(name="name", type=StringType)
petri_net_PetriNet.attributes={petri_net_PetriNet_name}

# petri_net_Node class attributes and methods
petri_net_Node_name: Property = Property(name="name", type=StringType)
petri_net_Node.attributes={petri_net_Node_name}

# petri_net_Arc class attributes and methods
petri_net_Arc_name: Property = Property(name="name", type=StringType)
petri_net_Arc.attributes={petri_net_Arc_name}

# petri_net_Transition class attributes and methods

# Node class attributes and methods

# petri_net_Place class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="petri_net_Node", type=petri_net_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_net_PetriNet", type=petri_net_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="petri_net_Arc", type=petri_net_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_net_PetriNet2", type=petri_net_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="petri_net_Node5", type=petri_net_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_net_Arc4", type=petri_net_Node, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="petri_net_Node8", type=petri_net_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_net_Arc7", type=petri_net_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petri_net_Transition_Node = Generalization(general=Node, specific=petri_net_Transition)
gen_petri_net_Place_Node = Generalization(general=Node, specific=petri_net_Place)

# Domain Model
domain_model = DomainModel(
    name="petri_net",
    types={petri_net_PetriNet, petri_net_Node, petri_net_Arc, petri_net_Transition, Node, petri_net_Place},
    associations={nodes0, arcs1, source3, target6},
    generalizations={gen_petri_net_Transition_Node, gen_petri_net_Place_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)