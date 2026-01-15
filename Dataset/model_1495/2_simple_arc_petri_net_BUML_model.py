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
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
PetriNet_Node = Class(name="PetriNet::Node", is_abstract=True)
PetriNet_Place = Class(name="PetriNet::Place")
Node = Class(name="Node")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Arc = Class(name="PetriNet::Arc")

# PetriNet_PetriNet class attributes and methods

# PetriNet_Node class attributes and methods
PetriNet_Node_name: Property = Property(name="name", type=StringType)
PetriNet_Node.attributes={PetriNet_Node_name}

# PetriNet_Place class attributes and methods
PetriNet_Place_marking: Property = Property(name="marking", type=IntegerType)
PetriNet_Place.attributes={PetriNet_Place_marking}

# Node class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_name: Property = Property(name="name", type=StringType)
PetriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNet_Arc.attributes={PetriNet_Arc_weight, PetriNet_Arc_name}

# Relationships
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="PetriNet_Node5", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Arc4", type=PetriNet_Node, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="PetriNet_Node8", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Arc7", type=PetriNet_Node, multiplicity=Multiplicity(1, 1))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="PetriNet_Node", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=PetriNet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="PetriNet_Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet2", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PetriNet_Place_Node = Generalization(general=Node, specific=PetriNet_Place)
gen_PetriNet_Transition_Node = Generalization(general=Node, specific=PetriNet_Transition)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_PetriNet, PetriNet_Node, PetriNet_Place, Node, PetriNet_Transition, PetriNet_Arc},
    associations={source3, target6, nodes0, arcs1},
    generalizations={gen_PetriNet_Place_Node, gen_PetriNet_Transition_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)