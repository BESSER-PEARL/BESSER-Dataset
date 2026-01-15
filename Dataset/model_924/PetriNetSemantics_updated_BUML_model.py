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
			EnumerationLiteral(name="read_arc")
    }
)

# Classes
Arc = Class(name="Arc")
petrinetsemantics_DDMMPetriNet_Transition = Class(name="petrinetsemantics::DDMMPetriNet::Transition")
petrinetsemantics_DDMMPetriNet_Node = Class(name="petrinetsemantics::DDMMPetriNet::Node", is_abstract=True)
PetriNet = Class(name="PetriNet")
petrinetsemantics_DDMMPetriNet_Place = Class(name="petrinetsemantics::DDMMPetriNet::Place")
petrinetsemantics_DDMMPetriNet_Arc = Class(name="petrinetsemantics::DDMMPetriNet::Arc")
petrinetsemantics_DDMMPetriNet_PetriNet = Class(name="petrinetsemantics::DDMMPetriNet::PetriNet")
Node = Class(name="Node")
petrinetsemantics_SDMMPetriNet_PetriNet_dynamic = Class(name="petrinetsemantics::SDMMPetriNet::PetriNet::dynamic")
petrinetsemantics_EDMMPetriNet_PetriNetEvent = Class(name="petrinetsemantics::EDMMPetriNet::PetriNetEvent", is_abstract=True)
PNSimEvent = Class(name="PNSimEvent")
petrinetsemantics_EDMMPetriNet_FireTransitionEvent = Class(name="petrinetsemantics::EDMMPetriNet::FireTransitionEvent")
PetriNetEvent = Class(name="PetriNetEvent")
Transition = Class(name="Transition")
petrinetsemantics_TM3PetriNet_PNScenario = Class(name="petrinetsemantics::TM3PetriNet::PNScenario")
PNTrace = Class(name="PNTrace")
petrinetsemantics_TM3PetriNet_PNTrace = Class(name="petrinetsemantics::TM3PetriNet::PNTrace")
PNScenario = Class(name="PNScenario")
petrinetsemantics_TM3PetriNet_PNSimEvent = Class(name="petrinetsemantics::TM3PetriNet::PNSimEvent")
petrinetsemantics_SDMMPetriNet_Node_dynamic = Class(name="petrinetsemantics::SDMMPetriNet::Node::dynamic", is_abstract=True)
petrinetsemantics_SDMMPetriNet_Place_dynamic = Class(name="petrinetsemantics::SDMMPetriNet::Place::dynamic")
Node_dynamic = Class(name="Node::dynamic")
Place = Class(name="Place")

# Arc class attributes and methods

# petrinetsemantics_DDMMPetriNet_Transition class attributes and methods
petrinetsemantics_DDMMPetriNet_Transition_min_time: Property = Property(name="min_time", type=IntegerType)
petrinetsemantics_DDMMPetriNet_Transition_max_time: Property = Property(name="max_time", type=IntegerType)
petrinetsemantics_DDMMPetriNet_Transition.attributes={petrinetsemantics_DDMMPetriNet_Transition_min_time, petrinetsemantics_DDMMPetriNet_Transition_max_time}

# petrinetsemantics_DDMMPetriNet_Node class attributes and methods
petrinetsemantics_DDMMPetriNet_Node_name: Property = Property(name="name", type=StringType)
petrinetsemantics_DDMMPetriNet_Node.attributes={petrinetsemantics_DDMMPetriNet_Node_name}

# PetriNet class attributes and methods

# petrinetsemantics_DDMMPetriNet_Place class attributes and methods
petrinetsemantics_DDMMPetriNet_Place_initialMarking: Property = Property(name="initialMarking", type=IntegerType)
petrinetsemantics_DDMMPetriNet_Place.attributes={petrinetsemantics_DDMMPetriNet_Place_initialMarking}

# petrinetsemantics_DDMMPetriNet_Arc class attributes and methods
petrinetsemantics_DDMMPetriNet_Arc_kind: Property = Property(name="kind", type=StringType)
petrinetsemantics_DDMMPetriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinetsemantics_DDMMPetriNet_Arc.attributes={petrinetsemantics_DDMMPetriNet_Arc_weight, petrinetsemantics_DDMMPetriNet_Arc_kind}

# petrinetsemantics_DDMMPetriNet_PetriNet class attributes and methods
petrinetsemantics_DDMMPetriNet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinetsemantics_DDMMPetriNet_PetriNet.attributes={petrinetsemantics_DDMMPetriNet_PetriNet_name}

# Node class attributes and methods

# petrinetsemantics_SDMMPetriNet_PetriNet_dynamic class attributes and methods

# petrinetsemantics_EDMMPetriNet_PetriNetEvent class attributes and methods

# PNSimEvent class attributes and methods

# petrinetsemantics_EDMMPetriNet_FireTransitionEvent class attributes and methods
petrinetsemantics_EDMMPetriNet_FireTransitionEvent_time: Property = Property(name="time", type=FloatType)
petrinetsemantics_EDMMPetriNet_FireTransitionEvent.attributes={petrinetsemantics_EDMMPetriNet_FireTransitionEvent_time}

# PetriNetEvent class attributes and methods

# Transition class attributes and methods

# petrinetsemantics_TM3PetriNet_PNScenario class attributes and methods

# PNTrace class attributes and methods

# petrinetsemantics_TM3PetriNet_PNTrace class attributes and methods

# PNScenario class attributes and methods

# petrinetsemantics_TM3PetriNet_PNSimEvent class attributes and methods
petrinetsemantics_TM3PetriNet_PNSimEvent_internal: Property = Property(name="internal", type=BooleanType)
petrinetsemantics_TM3PetriNet_PNSimEvent_date: Property = Property(name="date", type=IntegerType)
petrinetsemantics_TM3PetriNet_PNSimEvent_name: Property = Property(name="name", type=StringType)
petrinetsemantics_TM3PetriNet_PNSimEvent.attributes={petrinetsemantics_TM3PetriNet_PNSimEvent_name, petrinetsemantics_TM3PetriNet_PNSimEvent_date, petrinetsemantics_TM3PetriNet_PNSimEvent_internal}

# petrinetsemantics_SDMMPetriNet_Node_dynamic class attributes and methods

# petrinetsemantics_SDMMPetriNet_Place_dynamic class attributes and methods
petrinetsemantics_SDMMPetriNet_Place_dynamic_marking: Property = Property(name="marking", type=IntegerType)
petrinetsemantics_SDMMPetriNet_Place_dynamic.attributes={petrinetsemantics_SDMMPetriNet_Place_dynamic_marking}

# Node_dynamic class attributes and methods

# Place class attributes and methods

# Relationships
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="DDMMPetriNet2", type=petrinetsemantics_DDMMPetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="Arc", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="DDMMPetriNet4", type=petrinetsemantics_DDMMPetriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
outgoings5: BinaryAssociation = BinaryAssociation(
    name="outgoings5",
    ends={
        Property(name="DDMMPetriNet7", type=petrinetsemantics_DDMMPetriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Arc6", type=Arc, multiplicity=Multiplicity(0, 9999))
    }
)
incomings8: BinaryAssociation = BinaryAssociation(
    name="incomings8",
    ends={
        Property(name="DDMMPetriNet10", type=petrinetsemantics_DDMMPetriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Arc9", type=Arc, multiplicity=Multiplicity(0, 9999))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="DDMMPetriNet13", type=petrinetsemantics_DDMMPetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="Node12", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="DDMMPetriNet16", type=petrinetsemantics_DDMMPetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="Node15", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
net17: BinaryAssociation = BinaryAssociation(
    name="net17",
    ends={
        Property(name="DDMMPetriNet19", type=petrinetsemantics_DDMMPetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet18", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="DDMMPetriNet", type=petrinetsemantics_DDMMPetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="Node", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes23: BinaryAssociation = BinaryAssociation(
    name="nodes23",
    ends={
        Property(name="Node_dynamic", type=petrinetsemantics_SDMMPetriNet_PetriNet_dynamic, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_SDMMPetriNet_PetriNet_dynamic", type=Node_dynamic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PetriNet_static24: BinaryAssociation = BinaryAssociation(
    name="PetriNet_static24",
    ends={
        Property(name="PetriNet26", type=petrinetsemantics_SDMMPetriNet_PetriNet_dynamic, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_SDMMPetriNet_PetriNet_dynamic25", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
firedTransition27: BinaryAssociation = BinaryAssociation(
    name="firedTransition27",
    ends={
        Property(name="Transition", type=petrinetsemantics_EDMMPetriNet_FireTransitionEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_EDMMPetriNet_FireTransitionEvent", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
traces28: BinaryAssociation = BinaryAssociation(
    name="traces28",
    ends={
        Property(name="TM3PetriNet", type=petrinetsemantics_TM3PetriNet_PNScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="PNTrace", type=PNTrace, multiplicity=Multiplicity(0, 9999))
    }
)
simEvents29: BinaryAssociation = BinaryAssociation(
    name="simEvents29",
    ends={
        Property(name="PNSimEvent", type=petrinetsemantics_TM3PetriNet_PNScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_TM3PetriNet_PNScenario", type=PNSimEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario30: BinaryAssociation = BinaryAssociation(
    name="scenario30",
    ends={
        Property(name="TM3PetriNet31", type=petrinetsemantics_TM3PetriNet_PNTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="PNScenario", type=PNScenario, multiplicity=Multiplicity(1, 1))
    }
)
Node_static20: BinaryAssociation = BinaryAssociation(
    name="Node_static20",
    ends={
        Property(name="Node21", type=petrinetsemantics_SDMMPetriNet_Node_dynamic, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_SDMMPetriNet_Node_dynamic", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
Place_static22: BinaryAssociation = BinaryAssociation(
    name="Place_static22",
    ends={
        Property(name="Place", type=petrinetsemantics_SDMMPetriNet_Place_dynamic, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_SDMMPetriNet_Place_dynamic", type=Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinetsemantics_DDMMPetriNet_Transition_Node = Generalization(general=Node, specific=petrinetsemantics_DDMMPetriNet_Transition)
gen_petrinetsemantics_DDMMPetriNet_Place_Node = Generalization(general=Node, specific=petrinetsemantics_DDMMPetriNet_Place)
gen_petrinetsemantics_EDMMPetriNet_PetriNetEvent_PNSimEvent = Generalization(general=PNSimEvent, specific=petrinetsemantics_EDMMPetriNet_PetriNetEvent)
gen_petrinetsemantics_EDMMPetriNet_FireTransitionEvent_PetriNetEvent = Generalization(general=PetriNetEvent, specific=petrinetsemantics_EDMMPetriNet_FireTransitionEvent)
gen_petrinetsemantics_SDMMPetriNet_Place_dynamic_Node_dynamic = Generalization(general=Node_dynamic, specific=petrinetsemantics_SDMMPetriNet_Place_dynamic)

# Domain Model
domain_model = DomainModel(
    name="petrinetsemantics",
    types={Arc, petrinetsemantics_DDMMPetriNet_Transition, petrinetsemantics_DDMMPetriNet_Node, PetriNet, petrinetsemantics_DDMMPetriNet_Place, petrinetsemantics_DDMMPetriNet_Arc, petrinetsemantics_DDMMPetriNet_PetriNet, Node, petrinetsemantics_SDMMPetriNet_PetriNet_dynamic, petrinetsemantics_EDMMPetriNet_PetriNetEvent, PNSimEvent, petrinetsemantics_EDMMPetriNet_FireTransitionEvent, PetriNetEvent, Transition, petrinetsemantics_TM3PetriNet_PNScenario, PNTrace, petrinetsemantics_TM3PetriNet_PNTrace, PNScenario, petrinetsemantics_TM3PetriNet_PNSimEvent, petrinetsemantics_SDMMPetriNet_Node_dynamic, petrinetsemantics_SDMMPetriNet_Place_dynamic, Node_dynamic, Place, ArcKind},
    associations={arcs1, net3, outgoings5, incomings8, target11, source14, net17, nodes0, nodes23, PetriNet_static24, firedTransition27, traces28, simEvents29, scenario30, Node_static20, Place_static22},
    generalizations={gen_petrinetsemantics_DDMMPetriNet_Transition_Node, gen_petrinetsemantics_DDMMPetriNet_Place_Node, gen_petrinetsemantics_EDMMPetriNet_PetriNetEvent_PNSimEvent, gen_petrinetsemantics_EDMMPetriNet_FireTransitionEvent_PetriNetEvent, gen_petrinetsemantics_SDMMPetriNet_Place_dynamic_Node_dynamic},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)