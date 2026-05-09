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
petrinet_Petrinet = Class(name="petrinet_Petrinet")
petrinet_Arc = Class(name="petrinet_Arc")
petrinet_Token = Class(name="petrinet_Token")
petrinet_Place = Class(name="petrinet_Place")
petrinet_Node = Class(name="petrinet_Node", is_abstract=True)
petrinet_Transition = Class(name="petrinet_Transition")
Node = Class(name="Node")

# petrinet_Petrinet class attributes and methods
petrinet_Petrinet_name: Property = Property(name="name", type=StringType)
petrinet_Petrinet.attributes={petrinet_Petrinet_name}

# petrinet_Arc class attributes and methods

# petrinet_Token class attributes and methods

# petrinet_Place class attributes and methods

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# petrinet_Transition class attributes and methods

# Node class attributes and methods

# Relationships
arcs0: BinaryAssociation = BinaryAssociation(
    name="arcs0",
    ends={
        Property(name="Arc", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="out", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="Node7", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
petrinet8: BinaryAssociation = BinaryAssociation(
    name="petrinet8",
    ends={
        Property(name="Petrinet", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=petrinet_Petrinet, multiplicity=Multiplicity(0, 1))
    }
)
out9: BinaryAssociation = BinaryAssociation(
    name="out9",
    ends={
        Property(name="Arc10", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
in_11: BinaryAssociation = BinaryAssociation(
    name="in_11",
    ends={
        Property(name="Arc12", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
petrinet13: BinaryAssociation = BinaryAssociation(
    name="petrinet13",
    ends={
        Property(name="Petrinet14", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=petrinet_Petrinet, multiplicity=Multiplicity(0, 1))
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="Node", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens15: BinaryAssociation = BinaryAssociation(
    name="tokens15",
    ends={
        Property(name="Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Petrinet, petrinet_Arc, petrinet_Token, petrinet_Place, petrinet_Node, petrinet_Transition, Node},
    associations={arcs0, place3, source4, target6, petrinet8, out9, in_11, petrinet13, nodes1, tokens15},
    generalizations={gen_petrinet_Place_Node, gen_petrinet_Transition_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)