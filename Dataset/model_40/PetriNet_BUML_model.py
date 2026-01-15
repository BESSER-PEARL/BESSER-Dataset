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
			EnumerationLiteral(name="read_arc")
    }
)

# Classes
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_Transition = Class(name="petrinet::Transition")
Node = Class(name="Node")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
petrinet_Arc = Class(name="petrinet::Arc")

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# petrinet_Transition class attributes and methods
petrinet_Transition_min_time: Property = Property(name="min_time", type=IntegerType)
petrinet_Transition_max_time: Property = Property(name="max_time", type=IntegerType)
petrinet_Transition.attributes={petrinet_Transition_max_time, petrinet_Transition_min_time}

# Node class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_marking: Property = Property(name="marking", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_marking}

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# petrinet_Arc class attributes and methods
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc_kind: Property = Property(name="kind", type=StringType)
petrinet_Arc.attributes={petrinet_Arc_weight, petrinet_Arc_kind}

# Relationships
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="PetriNet", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
outgoings4: BinaryAssociation = BinaryAssociation(
    name="outgoings4",
    ends={
        Property(name="Arc5", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
incomings6: BinaryAssociation = BinaryAssociation(
    name="incomings6",
    ends={
        Property(name="Arc7", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="Arc", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net12: BinaryAssociation = BinaryAssociation(
    name="net12",
    ends={
        Property(name="PetriNet13", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="Node9", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="incomings", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="Node11", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_PetriNet, petrinet_Transition, Node, petrinet_Place, petrinet_Node, petrinet_Arc, ArcKind},
    associations={net3, outgoings4, incomings6, nodes0, arcs1, net12, target8, source10},
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