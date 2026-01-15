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
PetriNets_Object = Class(name="PetriNets::Object", is_abstract=True)
PetriNets_PetriNet = Class(name="PetriNets::PetriNet")
PetriNets_Node = Class(name="PetriNets::Node", is_abstract=True)
Object = Class(name="Object")
PetriNets_Arc = Class(name="PetriNets::Arc")
PetriNets_Transition = Class(name="PetriNets::Transition")
Node = Class(name="Node")
PetriNets_Place = Class(name="PetriNets::Place")
PetriNets_Token = Class(name="PetriNets::Token")

# PetriNets_Object class attributes and methods

# PetriNets_PetriNet class attributes and methods

# PetriNets_Node class attributes and methods
PetriNets_Node_name: Property = Property(name="name", type=StringType)
PetriNets_Node.attributes={PetriNets_Node_name}

# Object class attributes and methods

# PetriNets_Arc class attributes and methods

# PetriNets_Transition class attributes and methods

# Node class attributes and methods

# PetriNets_Place class attributes and methods
PetriNets_Place_capacity: Property = Property(name="capacity", type=IntegerType)
PetriNets_Place.attributes={PetriNets_Place_capacity}

# PetriNets_Token class attributes and methods

# Relationships
object0: BinaryAssociation = BinaryAssociation(
    name="object0",
    ends={
        Property(name="PetriNets_Object", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_PetriNet", type=PetriNets_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in1: BinaryAssociation = BinaryAssociation(
    name="in1",
    ends={
        Property(name="Arc", type=PetriNets_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=PetriNets_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
out2: BinaryAssociation = BinaryAssociation(
    name="out2",
    ends={
        Property(name="Arc3", type=PetriNets_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PetriNets_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Node", type=PetriNets_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=PetriNets_Node, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="Node6", type=PetriNets_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=PetriNets_Node, multiplicity=Multiplicity(1, 1))
    }
)
token7: BinaryAssociation = BinaryAssociation(
    name="token7",
    ends={
        Property(name="PetriNets_Token", type=PetriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Place", type=PetriNets_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PetriNets_Node_Object = Generalization(general=Object, specific=PetriNets_Node)
gen_PetriNets_Arc_Object = Generalization(general=Object, specific=PetriNets_Arc)
gen_PetriNets_Transition_Node = Generalization(general=Node, specific=PetriNets_Transition)
gen_PetriNets_Place_Node = Generalization(general=Node, specific=PetriNets_Place)

# Domain Model
domain_model = DomainModel(
    name="PetriNets",
    types={PetriNets_Object, PetriNets_PetriNet, PetriNets_Node, Object, PetriNets_Arc, PetriNets_Transition, Node, PetriNets_Place, PetriNets_Token},
    associations={object0, in1, out2, source4, target5, token7},
    generalizations={gen_PetriNets_Node_Object, gen_PetriNets_Arc_Object, gen_PetriNets_Transition_Node, gen_PetriNets_Place_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)