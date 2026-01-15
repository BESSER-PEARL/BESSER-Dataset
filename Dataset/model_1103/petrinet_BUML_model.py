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
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Transition = Class(name="petrinet::Transition")
Node = Class(name="Node")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Token = Class(name="petrinet::Token")

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# petrinet_Node class attributes and methods

# petrinet_Arc class attributes and methods
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc_m_isEnabled: Method = Method(name="isEnabled", parameters={}, type=BooleanType)
petrinet_Arc.attributes={petrinet_Arc_weight}
petrinet_Arc.methods={petrinet_Arc_m_isEnabled}

# petrinet_Transition class attributes and methods
petrinet_Transition_m_fire: Method = Method(name="fire", parameters={})
petrinet_Transition_m_isEnabled: Method = Method(name="isEnabled", parameters={}, type=BooleanType)
petrinet_Transition.methods={petrinet_Transition_m_fire, petrinet_Transition_m_isEnabled}

# Node class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_capacity: Property = Property(name="capacity", type=IntegerType)
petrinet_Place_m_hasCapacity: Method = Method(name="hasCapacity", parameters={Parameter(name='amount')}, type=BooleanType)
petrinet_Place.attributes={petrinet_Place_capacity}
petrinet_Place.methods={petrinet_Place_m_hasCapacity}

# petrinet_Token class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="petrinet_Node", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="petrinet_Arc", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet2", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out3: BinaryAssociation = BinaryAssociation(
    name="out3",
    ends={
        Property(name="Arc", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
in4: BinaryAssociation = BinaryAssociation(
    name="in4",
    ends={
        Property(name="Arc5", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
tokens6: BinaryAssociation = BinaryAssociation(
    name="tokens6",
    ends={
        Property(name="petrinet_Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="Node", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="Node9", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_PetriNet, petrinet_Node, petrinet_Arc, petrinet_Transition, Node, petrinet_Place, petrinet_Token},
    associations={nodes0, arcs1, out3, in4, tokens6, source7, target8},
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