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

# Enumerations
ArcKind: Enumeration = Enumeration(
    name="ArcKind",
    literals={
            EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="read_arc"),
			EnumerationLiteral(name="inhibitor")
    }
)

# Classes
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
PetriNet_Node = Class(name="PetriNet::Node", is_abstract=True)
PetriNet_Arc = Class(name="PetriNet::Arc")
PetriNet_Transition = Class(name="PetriNet::Transition")
Node = Class(name="Node")
PetriNet_Place = Class(name="PetriNet::Place")

# PetriNet_PetriNet class attributes and methods
PetriNet_PetriNet_name: Property = Property(name="name", type=StringType)
PetriNet_PetriNet.attributes={PetriNet_PetriNet_name}

# PetriNet_Node class attributes and methods
PetriNet_Node_name: Property = Property(name="name", type=StringType)
PetriNet_Node.attributes={PetriNet_Node_name}

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNet_Arc_kind: Property = Property(name="kind", type=StringType)
PetriNet_Arc.attributes={PetriNet_Arc_kind, PetriNet_Arc_weight}

# PetriNet_Transition class attributes and methods
PetriNet_Transition_max_time: Property = Property(name="max_time", type=IntegerType)
PetriNet_Transition_min_time: Property = Property(name="min_time", type=IntegerType)
PetriNet_Transition.attributes={PetriNet_Transition_max_time, PetriNet_Transition_min_time}

# Node class attributes and methods

# PetriNet_Place class attributes and methods
PetriNet_Place_marking: Property = Property(name="marking", type=IntegerType)
PetriNet_Place.attributes={PetriNet_Place_marking}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=PetriNet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoings4: BinaryAssociation = BinaryAssociation(
    name="outgoings4",
    ends={
        Property(name="Arc5", type=PetriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="PetriNet", type=PetriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="Node9", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="incomings", type=PetriNet_Node, multiplicity=Multiplicity(1, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="Node11", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=PetriNet_Node, multiplicity=Multiplicity(1, 1))
    }
)
net12: BinaryAssociation = BinaryAssociation(
    name="net12",
    ends={
        Property(name="PetriNet13", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
incomings6: BinaryAssociation = BinaryAssociation(
    name="incomings6",
    ends={
        Property(name="Arc7", type=PetriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_PetriNet_Transition_Node = Generalization(general=Node, specific=PetriNet_Transition)
gen_PetriNet_Place_Node = Generalization(general=Node, specific=PetriNet_Place)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_PetriNet, PetriNet_Node, PetriNet_Arc, PetriNet_Transition, Node, PetriNet_Place, ArcKind},
    associations={nodes0, arcs1, outgoings4, net3, target8, source10, net12, incomings6},
    generalizations={gen_PetriNet_Transition_Node, gen_PetriNet_Place_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)