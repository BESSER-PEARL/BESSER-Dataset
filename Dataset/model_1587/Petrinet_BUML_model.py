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
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
petrinet_Token = Class(name="petrinet::Token")
petrinet_Place = Class(name="petrinet::Place")
petrinet_petrinet = Class(name="petrinet::petrinet")
petrinet_Transition = Class(name="petrinet::Transition")
Node = Class(name="Node")

# petrinet_Arc class attributes and methods

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# petrinet_Token class attributes and methods

# petrinet_Place class attributes and methods

# petrinet_petrinet class attributes and methods
petrinet_petrinet_nume: Property = Property(name="nume", type=StringType)
petrinet_petrinet.attributes={petrinet_petrinet_nume}

# petrinet_Transition class attributes and methods

# Node class attributes and methods

# Relationships
arcs0: BinaryAssociation = BinaryAssociation(
    name="arcs0",
    ends={
        Property(name="Arc", type=petrinet_petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="Node", type=petrinet_petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place3: BinaryAssociation = BinaryAssociation(
    name="place3",
    ends={
        Property(name="Place", type=petrinet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="tokens", type=petrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Node5", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=petrinet_Node, multiplicity=Multiplicity(0, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="Node7", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=petrinet_Node, multiplicity=Multiplicity(0, 1))
    }
)
petrinet8: BinaryAssociation = BinaryAssociation(
    name="petrinet8",
    ends={
        Property(name="petrinet9", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=petrinet_petrinet, multiplicity=Multiplicity(0, 1))
    }
)
in10: BinaryAssociation = BinaryAssociation(
    name="in10",
    ends={
        Property(name="Arc11", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
petrinet14: BinaryAssociation = BinaryAssociation(
    name="petrinet14",
    ends={
        Property(name="petrinet15", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=petrinet_petrinet, multiplicity=Multiplicity(0, 1))
    }
)
tokens16: BinaryAssociation = BinaryAssociation(
    name="tokens16",
    ends={
        Property(name="Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out12: BinaryAssociation = BinaryAssociation(
    name="out12",
    ends={
        Property(name="Arc13", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Arc, petrinet_Node, petrinet_Token, petrinet_Place, petrinet_petrinet, petrinet_Transition, Node},
    associations={arcs0, nodes1, place3, source4, target6, petrinet8, in10, petrinet14, tokens16, out12},
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