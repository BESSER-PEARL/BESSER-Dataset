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
petrinetsemantics_DDMMPetriNet_PetriNet = Class(name="petrinetsemantics_DDMMPetriNet_PetriNet")
Node = Class(name="Node")
petrinetsemantics_SDMMPetriNet_Node_dynamic = Class(name="petrinetsemantics_SDMMPetriNet_Node_dynamic", is_abstract=True)
petrinetsemantics_SDMMPetriNet_Place_dynamic = Class(name="petrinetsemantics_SDMMPetriNet_Place_dynamic")
Node_dynamic = Class(name="Node_dynamic")
Place = Class(name="Place")
petrinetsemantics_SDMMPetriNet_PetriNet_dynamic = Class(name="petrinetsemantics_SDMMPetriNet_PetriNet_dynamic")
Arc = Class(name="Arc")
petrinetsemantics_DDMMPetriNet_Transition = Class(name="petrinetsemantics_DDMMPetriNet_Transition")
petrinetsemantics_DDMMPetriNet_Node = Class(name="petrinetsemantics_DDMMPetriNet_Node", is_abstract=True)
PetriNet = Class(name="PetriNet")
petrinetsemantics_DDMMPetriNet_Place = Class(name="petrinetsemantics_DDMMPetriNet_Place")
petrinetsemantics_DDMMPetriNet_Arc = Class(name="petrinetsemantics_DDMMPetriNet_Arc")
petrinetsemantics_EDMMPetriNet_PetriNetEvent = Class(name="petrinetsemantics_EDMMPetriNet_PetriNetEvent", is_abstract=True)
PNSimEvent = Class(name="PNSimEvent")
petrinetsemantics_EDMMPetriNet_FireTransitionEvent = Class(name="petrinetsemantics_EDMMPetriNet_FireTransitionEvent")
PetriNetEvent = Class(name="PetriNetEvent")
Transition = Class(name="Transition")
petrinetsemantics_TM3PetriNet_PNScenario = Class(name="petrinetsemantics_TM3PetriNet_PNScenario")
PNTrace = Class(name="PNTrace")
petrinetsemantics_TM3PetriNet_PNTrace = Class(name="petrinetsemantics_TM3PetriNet_PNTrace")
PNScenario = Class(name="PNScenario")
petrinetsemantics_TM3PetriNet_PNSimEvent = Class(name="petrinetsemantics_TM3PetriNet_PNSimEvent")

# petrinetsemantics_DDMMPetriNet_PetriNet class attributes and methods
petrinetsemantics_DDMMPetriNet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinetsemantics_DDMMPetriNet_PetriNet.attributes={petrinetsemantics_DDMMPetriNet_PetriNet_name}

# Node class attributes and methods

# petrinetsemantics_SDMMPetriNet_Node_dynamic class attributes and methods

# petrinetsemantics_SDMMPetriNet_Place_dynamic class attributes and methods
petrinetsemantics_SDMMPetriNet_Place_dynamic_marking: Property = Property(name="marking", type=IntegerType)
petrinetsemantics_SDMMPetriNet_Place_dynamic.attributes={petrinetsemantics_SDMMPetriNet_Place_dynamic_marking}

# Node_dynamic class attributes and methods

# Place class attributes and methods

# petrinetsemantics_SDMMPetriNet_PetriNet_dynamic class attributes and methods

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
petrinetsemantics_DDMMPetriNet_Arc.attributes={petrinetsemantics_DDMMPetriNet_Arc_kind, petrinetsemantics_DDMMPetriNet_Arc_weight}

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
petrinetsemantics_TM3PetriNet_PNSimEvent.attributes={petrinetsemantics_TM3PetriNet_PNSimEvent_internal, petrinetsemantics_TM3PetriNet_PNSimEvent_date, petrinetsemantics_TM3PetriNet_PNSimEvent_name}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=petrinetsemantics_DDMMPetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="Node11", type=petrinetsemantics_DDMMPetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
net12: BinaryAssociation = BinaryAssociation(
    name="net12",
    ends={
        Property(name="PetriNet13", type=petrinetsemantics_DDMMPetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
Node_static14: BinaryAssociation = BinaryAssociation(
    name="Node_static14",
    ends={
        Property(name="Node15", type=petrinetsemantics_SDMMPetriNet_Node_dynamic, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_SDMMPetriNet_Node_dynamic", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
Place_static16: BinaryAssociation = BinaryAssociation(
    name="Place_static16",
    ends={
        Property(name="Place", type=petrinetsemantics_SDMMPetriNet_Place_dynamic, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_SDMMPetriNet_Place_dynamic", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
nodes17: BinaryAssociation = BinaryAssociation(
    name="nodes17",
    ends={
        Property(name="Node_dynamic", type=petrinetsemantics_SDMMPetriNet_PetriNet_dynamic, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_SDMMPetriNet_PetriNet_dynamic", type=Node_dynamic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PetriNet_static18: BinaryAssociation = BinaryAssociation(
    name="PetriNet_static18",
    ends={
        Property(name="PetriNet20", type=petrinetsemantics_SDMMPetriNet_PetriNet_dynamic, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_SDMMPetriNet_PetriNet_dynamic19", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="Arc", type=petrinetsemantics_DDMMPetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="PetriNet", type=petrinetsemantics_DDMMPetriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
outgoings4: BinaryAssociation = BinaryAssociation(
    name="outgoings4",
    ends={
        Property(name="Arc5", type=petrinetsemantics_DDMMPetriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Arc, multiplicity=Multiplicity(0, 9999))
    }
)
incomings6: BinaryAssociation = BinaryAssociation(
    name="incomings6",
    ends={
        Property(name="Arc7", type=petrinetsemantics_DDMMPetriNet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Arc, multiplicity=Multiplicity(0, 9999))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="Node9", type=petrinetsemantics_DDMMPetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="incomings", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
firedTransition21: BinaryAssociation = BinaryAssociation(
    name="firedTransition21",
    ends={
        Property(name="Transition", type=petrinetsemantics_EDMMPetriNet_FireTransitionEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_EDMMPetriNet_FireTransitionEvent", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
traces22: BinaryAssociation = BinaryAssociation(
    name="traces22",
    ends={
        Property(name="PNTrace", type=petrinetsemantics_TM3PetriNet_PNScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="scenario", type=PNTrace, multiplicity=Multiplicity(0, 9999))
    }
)
simEvents23: BinaryAssociation = BinaryAssociation(
    name="simEvents23",
    ends={
        Property(name="PNSimEvent", type=petrinetsemantics_TM3PetriNet_PNScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetsemantics_TM3PetriNet_PNScenario", type=PNSimEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenario24: BinaryAssociation = BinaryAssociation(
    name="scenario24",
    ends={
        Property(name="PNScenario", type=petrinetsemantics_TM3PetriNet_PNTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces", type=PNScenario, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinetsemantics_SDMMPetriNet_Place_dynamic_Node_dynamic = Generalization(general=Node_dynamic, specific=petrinetsemantics_SDMMPetriNet_Place_dynamic)
gen_petrinetsemantics_DDMMPetriNet_Transition_Node = Generalization(general=Node, specific=petrinetsemantics_DDMMPetriNet_Transition)
gen_petrinetsemantics_DDMMPetriNet_Place_Node = Generalization(general=Node, specific=petrinetsemantics_DDMMPetriNet_Place)
gen_petrinetsemantics_EDMMPetriNet_PetriNetEvent_PNSimEvent = Generalization(general=PNSimEvent, specific=petrinetsemantics_EDMMPetriNet_PetriNetEvent)
gen_petrinetsemantics_EDMMPetriNet_FireTransitionEvent_PetriNetEvent = Generalization(general=PetriNetEvent, specific=petrinetsemantics_EDMMPetriNet_FireTransitionEvent)

# Domain Model
domain_model = DomainModel(
    name="petrinetsemantics",
    types={petrinetsemantics_DDMMPetriNet_PetriNet, Node, petrinetsemantics_SDMMPetriNet_Node_dynamic, petrinetsemantics_SDMMPetriNet_Place_dynamic, Node_dynamic, Place, petrinetsemantics_SDMMPetriNet_PetriNet_dynamic, Arc, petrinetsemantics_DDMMPetriNet_Transition, petrinetsemantics_DDMMPetriNet_Node, PetriNet, petrinetsemantics_DDMMPetriNet_Place, petrinetsemantics_DDMMPetriNet_Arc, petrinetsemantics_EDMMPetriNet_PetriNetEvent, PNSimEvent, petrinetsemantics_EDMMPetriNet_FireTransitionEvent, PetriNetEvent, Transition, petrinetsemantics_TM3PetriNet_PNScenario, PNTrace, petrinetsemantics_TM3PetriNet_PNTrace, PNScenario, petrinetsemantics_TM3PetriNet_PNSimEvent, ArcKind},
    associations={nodes0, source10, net12, Node_static14, Place_static16, nodes17, PetriNet_static18, arcs1, net3, outgoings4, incomings6, target8, firedTransition21, traces22, simEvents23, scenario24},
    generalizations={gen_petrinetsemantics_SDMMPetriNet_Place_dynamic_Node_dynamic, gen_petrinetsemantics_DDMMPetriNet_Transition_Node, gen_petrinetsemantics_DDMMPetriNet_Place_Node, gen_petrinetsemantics_EDMMPetriNet_PetriNetEvent_PNSimEvent, gen_petrinetsemantics_EDMMPetriNet_FireTransitionEvent_PetriNetEvent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)