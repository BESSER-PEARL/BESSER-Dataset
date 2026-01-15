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
petrinet_Place = Class(name="petrinet::Place")
Node = Class(name="Node")
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
petrinet_Petrinet = Class(name="petrinet::Petrinet")
petrinet_Token = Class(name="petrinet::Token")
petrinet_Transition = Class(name="petrinet::Transition")

# petrinet_Place class attributes and methods

# Node class attributes and methods

# petrinet_Arc class attributes and methods

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# petrinet_Petrinet class attributes and methods
petrinet_Petrinet_name: Property = Property(name="name", type=StringType)
petrinet_Petrinet.attributes={petrinet_Petrinet_name}

# petrinet_Token class attributes and methods

# petrinet_Transition class attributes and methods

# Relationships
petrinet4: BinaryAssociation = BinaryAssociation(
    name="petrinet4",
    ends={
        Property(name="Petrinet5", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=petrinet_Petrinet, multiplicity=Multiplicity(0, 1))
    }
)
in6: BinaryAssociation = BinaryAssociation(
    name="in6",
    ends={
        Property(name="Arc", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
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
nodes9: BinaryAssociation = BinaryAssociation(
    name="nodes9",
    ends={
        Property(name="Node10", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs11: BinaryAssociation = BinaryAssociation(
    name="arcs11",
    ends={
        Property(name="Arc13", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet12", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="Node", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="Node2", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
petrinet3: BinaryAssociation = BinaryAssociation(
    name="petrinet3",
    ends={
        Property(name="Petrinet", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=petrinet_Petrinet, multiplicity=Multiplicity(0, 1))
    }
)
tokens14: BinaryAssociation = BinaryAssociation(
    name="tokens14",
    ends={
        Property(name="Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place15: BinaryAssociation = BinaryAssociation(
    name="place15",
    ends={
        Property(name="Place", type=petrinet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="tokens", type=petrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Place, Node, petrinet_Arc, petrinet_Node, petrinet_Petrinet, petrinet_Token, petrinet_Transition},
    associations={petrinet4, in6, out7, nodes9, arcs11, source0, target1, petrinet3, tokens14, place15},
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