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
petrinet_Transition = Class(name="petrinet::Transition")
Node = Class(name="Node")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Petrinet = Class(name="petrinet::Petrinet")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
petrinet_Arc = Class(name="petrinet::Arc")

# petrinet_Transition class attributes and methods

# Node class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_tokenNb: Property = Property(name="tokenNb", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_tokenNb}

# petrinet_Petrinet class attributes and methods

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# petrinet_Arc class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="petrinet_Node", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Petrinet", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="petrinet_Arc", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Petrinet2", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomming3: BinaryAssociation = BinaryAssociation(
    name="incomming3",
    ends={
        Property(name="Arc", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Arc5", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="Node", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="incomming", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="Node8", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Transition, Node, petrinet_Place, petrinet_Petrinet, petrinet_Node, petrinet_Arc},
    associations={nodes0, arcs1, incomming3, outgoing4, target6, source7},
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