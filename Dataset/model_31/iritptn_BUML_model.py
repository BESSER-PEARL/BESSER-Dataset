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
			EnumerationLiteral(name="readArc")
    }
)

# Classes
iritptn_PetriNet = Class(name="iritptn::PetriNet")
iritptn_Node = Class(name="iritptn::Node")
iritptn_Arc = Class(name="iritptn::Arc")
iritptn_Place = Class(name="iritptn::Place")
iritptn_Transition = Class(name="iritptn::Transition")
Node = Class(name="Node")

# iritptn_PetriNet class attributes and methods
iritptn_PetriNet_name: Property = Property(name="name", type=StringType)
iritptn_PetriNet.attributes={iritptn_PetriNet_name}

# iritptn_Node class attributes and methods
iritptn_Node_name: Property = Property(name="name", type=StringType)
iritptn_Node.attributes={iritptn_Node_name}

# iritptn_Arc class attributes and methods
iritptn_Arc_weight: Property = Property(name="weight", type=IntegerType)
iritptn_Arc_kind: Property = Property(name="kind", type=StringType)
iritptn_Arc.attributes={iritptn_Arc_kind, iritptn_Arc_weight}

# iritptn_Place class attributes and methods
iritptn_Place_marking: Property = Property(name="marking", type=IntegerType)
iritptn_Place.attributes={iritptn_Place_marking}

# iritptn_Transition class attributes and methods
iritptn_Transition_tMax: Property = Property(name="tMax", type=IntegerType)
iritptn_Transition_tMin: Property = Property(name="tMin", type=IntegerType)
iritptn_Transition.attributes={iritptn_Transition_tMax, iritptn_Transition_tMin}

# Node class attributes and methods

# Relationships
outgoings5: BinaryAssociation = BinaryAssociation(
    name="outgoings5",
    ends={
        Property(name="Arc6", type=iritptn_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=iritptn_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
net7: BinaryAssociation = BinaryAssociation(
    name="net7",
    ends={
        Property(name="PetriNet", type=iritptn_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=iritptn_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="Node9", type=iritptn_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="ingoings", type=iritptn_Node, multiplicity=Multiplicity(1, 1))
    }
)
net10: BinaryAssociation = BinaryAssociation(
    name="net10",
    ends={
        Property(name="PetriNet11", type=iritptn_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arc", type=iritptn_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=iritptn_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=iritptn_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arc1: BinaryAssociation = BinaryAssociation(
    name="arc1",
    ends={
        Property(name="Arc", type=iritptn_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=iritptn_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ingoings3: BinaryAssociation = BinaryAssociation(
    name="ingoings3",
    ends={
        Property(name="Arc4", type=iritptn_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=iritptn_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="Node13", type=iritptn_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=iritptn_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_iritptn_Place_Node = Generalization(general=Node, specific=iritptn_Place)
gen_iritptn_Transition_Node = Generalization(general=Node, specific=iritptn_Transition)

# Domain Model
domain_model = DomainModel(
    name="iritptn",
    types={iritptn_PetriNet, iritptn_Node, iritptn_Arc, iritptn_Place, iritptn_Transition, Node, ArcKind},
    associations={outgoings5, net7, target8, net10, nodes0, arc1, ingoings3, source12},
    generalizations={gen_iritptn_Place_Node, gen_iritptn_Transition_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)