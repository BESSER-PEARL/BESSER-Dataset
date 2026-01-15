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
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Network = Class(name="petrinet::Network")
petrinet_Transition = Class(name="petrinet::Transition")
Node = Class(name="Node")
petrinet_Place = Class(name="petrinet::Place")

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# petrinet_Arc class attributes and methods
petrinet_Arc_readOnly: Property = Property(name="readOnly", type=BooleanType)
petrinet_Arc_kind: Property = Property(name="kind", type=StringType)
petrinet_Arc_tokensCount: Property = Property(name="tokensCount", type=IntegerType)
petrinet_Arc.attributes={petrinet_Arc_tokensCount, petrinet_Arc_readOnly, petrinet_Arc_kind}

# petrinet_Network class attributes and methods
petrinet_Network_name: Property = Property(name="name", type=StringType)
petrinet_Network.attributes={petrinet_Network_name}

# petrinet_Transition class attributes and methods

# Node class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_tokensCount: Property = Property(name="tokensCount", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_tokensCount}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=petrinet_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="reseau", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="Arc", type=petrinet_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="reseau2", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reseau3: BinaryAssociation = BinaryAssociation(
    name="reseau3",
    ends={
        Property(name="Network", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=petrinet_Network, multiplicity=Multiplicity(1, 1))
    }
)
predecessors4: BinaryAssociation = BinaryAssociation(
    name="predecessors4",
    ends={
        Property(name="Arc5", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
successors6: BinaryAssociation = BinaryAssociation(
    name="successors6",
    ends={
        Property(name="Arc7", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
reseau8: BinaryAssociation = BinaryAssociation(
    name="reseau8",
    ends={
        Property(name="Network9", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=petrinet_Network, multiplicity=Multiplicity(1, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="Node11", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="successors", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="Node13", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessors", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Node, petrinet_Arc, petrinet_Network, petrinet_Transition, Node, petrinet_Place, ArcKind},
    associations={nodes0, arcs1, reseau3, predecessors4, successors6, reseau8, source10, target12},
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