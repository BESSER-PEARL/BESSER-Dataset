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
petrinet_Identifyable = Class(name="petrinet_Identifyable", is_abstract=True)
petrinet_Node = Class(name="petrinet_Node")
Identifyable = Class(name="Identifyable")
petrinet_Arc = Class(name="petrinet_Arc")
petrinet_PetriNet = Class(name="petrinet_PetriNet")
petrinet_Transition = Class(name="petrinet_Transition")
petrinet_Place = Class(name="petrinet_Place")
Node = Class(name="Node")

# petrinet_Identifyable class attributes and methods
petrinet_Identifyable_id: Property = Property(name="id", type=StringType)
petrinet_Identifyable.attributes={petrinet_Identifyable_id}

# petrinet_Node class attributes and methods

# Identifyable class attributes and methods

# petrinet_Arc class attributes and methods

# petrinet_PetriNet class attributes and methods

# petrinet_Transition class attributes and methods

# petrinet_Place class attributes and methods

# Node class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="petrinet_Node", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="petrinet_Node3", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc2", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
places4: BinaryAssociation = BinaryAssociation(
    name="places4",
    ends={
        Property(name="petrinet_Node5", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs6: BinaryAssociation = BinaryAssociation(
    name="arcs6",
    ends={
        Property(name="petrinet_Arc8", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet7", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions9: BinaryAssociation = BinaryAssociation(
    name="transitions9",
    ends={
        Property(name="petrinet_Transition", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet10", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)
gen_petrinet_Node_Identifyable = Generalization(general=Identifyable, specific=petrinet_Node)
gen_petrinet_Arc_Identifyable = Generalization(general=Identifyable, specific=petrinet_Arc)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Identifyable, petrinet_Node, Identifyable, petrinet_Arc, petrinet_PetriNet, petrinet_Transition, petrinet_Place, Node},
    associations={source0, target1, places4, arcs6, transitions9},
    generalizations={gen_petrinet_Transition_Node, gen_petrinet_Node_Identifyable, gen_petrinet_Arc_Identifyable, gen_petrinet_Place_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)