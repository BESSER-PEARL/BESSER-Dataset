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
            EnumerationLiteral(name="read_arc"),
			EnumerationLiteral(name="normal")
    }
)

# Classes
petriNet_Node = Class(name="petriNet::Node", is_abstract=True)
petriNet_Arc = Class(name="petriNet::Arc")
petriNet_Transition = Class(name="petriNet::Transition")
Node = Class(name="Node")
petriNet_PetriNet = Class(name="petriNet::PetriNet")
petriNet_Place = Class(name="petriNet::Place")

# petriNet_Node class attributes and methods
petriNet_Node_name: Property = Property(name="name", type=StringType)
petriNet_Node.attributes={petriNet_Node_name}

# petriNet_Arc class attributes and methods
petriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petriNet_Arc_kind: Property = Property(name="kind", type=StringType)
petriNet_Arc.attributes={petriNet_Arc_kind, petriNet_Arc_weight}

# petriNet_Transition class attributes and methods
petriNet_Transition_min_time: Property = Property(name="min_time", type=IntegerType)
petriNet_Transition_max_time: Property = Property(name="max_time", type=IntegerType)
petriNet_Transition.attributes={petriNet_Transition_max_time, petriNet_Transition_min_time}

# Node class attributes and methods

# petriNet_PetriNet class attributes and methods
petriNet_PetriNet_name: Property = Property(name="name", type=StringType)
petriNet_PetriNet.attributes={petriNet_PetriNet_name}

# petriNet_Place class attributes and methods
petriNet_Place_marking: Property = Property(name="marking", type=IntegerType)
petriNet_Place.attributes={petriNet_Place_marking}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=petriNet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="Arc", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=petriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="PetriNet", type=petriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
outgoings4: BinaryAssociation = BinaryAssociation(
    name="outgoings4",
    ends={
        Property(name="Arc5", type=petriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petriNet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
incomings6: BinaryAssociation = BinaryAssociation(
    name="incomings6",
    ends={
        Property(name="Arc7", type=petriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petriNet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="Node9", type=petriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="incomings", type=petriNet_Node, multiplicity=Multiplicity(1, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="Node11", type=petriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=petriNet_Node, multiplicity=Multiplicity(1, 1))
    }
)
net12: BinaryAssociation = BinaryAssociation(
    name="net12",
    ends={
        Property(name="PetriNet13", type=petriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petriNet_Transition_Node = Generalization(general=Node, specific=petriNet_Transition)
gen_petriNet_Place_Node = Generalization(general=Node, specific=petriNet_Place)

# Domain Model
domain_model = DomainModel(
    name="petriNet",
    types={petriNet_Node, petriNet_Arc, petriNet_Transition, Node, petriNet_PetriNet, petriNet_Place, ArcKind},
    associations={nodes0, arcs1, net3, outgoings4, incomings6, target8, source10, net12},
    generalizations={gen_petriNet_Transition_Node, gen_petriNet_Place_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)