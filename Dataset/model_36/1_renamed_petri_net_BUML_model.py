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
PetriNet_Place = Class(name="PetriNet::Place")
Node = Class(name="Node")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
PetriNet_Node = Class(name="PetriNet::Node", is_abstract=True)
PetriNet_Arc = Class(name="PetriNet::Arc", is_abstract=True)
PetriNet_PTArc = Class(name="PetriNet::PTArc")
Arc = Class(name="Arc")
PetriNet_TPArc = Class(name="PetriNet::TPArc")

# PetriNet_Place class attributes and methods
PetriNet_Place_marking: Property = Property(name="marking", type=IntegerType)
PetriNet_Place.attributes={PetriNet_Place_marking}

# Node class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_PetriNet class attributes and methods

# PetriNet_Node class attributes and methods
PetriNet_Node_name: Property = Property(name="name", type=StringType)
PetriNet_Node.attributes={PetriNet_Node_name}

# PetriNet_Arc class attributes and methods
PetriNet_Arc_name: Property = Property(name="name", type=StringType)
PetriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNet_Arc.attributes={PetriNet_Arc_weight, PetriNet_Arc_name}

# PetriNet_PTArc class attributes and methods

# Arc class attributes and methods

# PetriNet_TPArc class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="PetriNet_Node", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=PetriNet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="PetriNet_Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet2", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="PetriNet_Place", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PTArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="PetriNet_Transition", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PTArc5", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="PetriNet_Transition7", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_TPArc", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="PetriNet_Place10", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_TPArc9", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_Place_Node = Generalization(general=Node, specific=PetriNet_Place)
gen_PetriNet_Transition_Node = Generalization(general=Node, specific=PetriNet_Transition)
gen_PetriNet_PTArc_Arc = Generalization(general=Arc, specific=PetriNet_PTArc)
gen_PetriNet_TPArc_Arc = Generalization(general=Arc, specific=PetriNet_TPArc)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Place, Node, PetriNet_Transition, PetriNet_PetriNet, PetriNet_Node, PetriNet_Arc, PetriNet_PTArc, Arc, PetriNet_TPArc},
    associations={nodes0, arcs1, source3, target4, source6, target8},
    generalizations={gen_PetriNet_Place_Node, gen_PetriNet_Transition_Node, gen_PetriNet_PTArc_Arc, gen_PetriNet_TPArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)