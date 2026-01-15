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
petrinet_Petrinet = Class(name="petrinet::Petrinet")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Place = Class(name="petrinet::Place")
Node = Class(name="Node")
petrinet_Token = Class(name="petrinet::Token")

# petrinet_Petrinet class attributes and methods
petrinet_Petrinet_name: Property = Property(name="name", type=StringType)
petrinet_Petrinet.attributes={petrinet_Petrinet_name}

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# petrinet_Transition class attributes and methods

# petrinet_Arc class attributes and methods

# petrinet_Place class attributes and methods

# Node class attributes and methods

# petrinet_Token class attributes and methods

# Relationships
petrinet4: BinaryAssociation = BinaryAssociation(
    name="petrinet4",
    ends={
        Property(name="Petrinet", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=petrinet_Petrinet, multiplicity=Multiplicity(0, 1))
    }
)
in5: BinaryAssociation = BinaryAssociation(
    name="in5",
    ends={
        Property(name="Arc6", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
out7: BinaryAssociation = BinaryAssociation(
    name="out7",
    ends={
        Property(name="Arc8", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
place9: BinaryAssociation = BinaryAssociation(
    name="place9",
    ends={
        Property(name="Place", type=petrinet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="tokens", type=petrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="Node11", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="Node13", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
petrinet14: BinaryAssociation = BinaryAssociation(
    name="petrinet14",
    ends={
        Property(name="Petrinet15", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=petrinet_Petrinet, multiplicity=Multiplicity(0, 1))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="Arc", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens3: BinaryAssociation = BinaryAssociation(
    name="tokens3",
    ends={
        Property(name="Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Petrinet, petrinet_Node, petrinet_Transition, petrinet_Arc, petrinet_Place, Node, petrinet_Token},
    associations={petrinet4, in5, out7, place9, source10, target12, petrinet14, nodes0, arcs1, tokens3},
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