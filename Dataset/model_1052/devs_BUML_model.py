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
devs_AtomicModel = Class(name="devs::AtomicModel")
devs_State = Class(name="devs::State")
devs_InputEvent = Class(name="devs::InputEvent")
Event = Class(name="Event")
devs_ExternalTransition = Class(name="devs::ExternalTransition")
devs_OutputEvent = Class(name="devs::OutputEvent")
devs_Event = Class(name="devs::Event")
devs_Transition = Class(name="devs::Transition")
devs_OutputFunction = Class(name="devs::OutputFunction")
devs_InternalTransition = Class(name="devs::InternalTransition")
Transition = Class(name="Transition")

# devs_AtomicModel class attributes and methods
devs_AtomicModel_name: Property = Property(name="name", type=StringType)
devs_AtomicModel.attributes={devs_AtomicModel_name}

# devs_State class attributes and methods
devs_State_lifeTime: Property = Property(name="lifeTime", type=FloatType)
devs_State_name: Property = Property(name="name", type=StringType)
devs_State.attributes={devs_State_lifeTime, devs_State_name}

# devs_InputEvent class attributes and methods

# Event class attributes and methods

# devs_ExternalTransition class attributes and methods

# devs_OutputEvent class attributes and methods

# devs_Event class attributes and methods
devs_Event_name: Property = Property(name="name", type=StringType)
devs_Event.attributes={devs_Event_name}

# devs_Transition class attributes and methods
devs_Transition_name: Property = Property(name="name", type=StringType)
devs_Transition.attributes={devs_Transition_name}

# devs_OutputFunction class attributes and methods
devs_OutputFunction_name: Property = Property(name="name", type=StringType)
devs_OutputFunction.attributes={devs_OutputFunction_name}

# devs_InternalTransition class attributes and methods

# Transition class attributes and methods

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="State", type=devs_AtomicModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atomicModel", type=devs_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
out9: BinaryAssociation = BinaryAssociation(
    name="out9",
    ends={
        Property(name="Transition10", type=devs_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=devs_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outF11: BinaryAssociation = BinaryAssociation(
    name="outF11",
    ends={
        Property(name="OutputFunction13", type=devs_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source12", type=devs_OutputFunction, multiplicity=Multiplicity(1, 1))
    }
)
atomicModel14: BinaryAssociation = BinaryAssociation(
    name="atomicModel14",
    ends={
        Property(name="AtomicModel", type=devs_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=devs_AtomicModel, multiplicity=Multiplicity(1, 1))
    }
)
atomicModel15: BinaryAssociation = BinaryAssociation(
    name="atomicModel15",
    ends={
        Property(name="AtomicModel16", type=devs_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="event", type=devs_AtomicModel, multiplicity=Multiplicity(1, 1))
    }
)
externalTransition17: BinaryAssociation = BinaryAssociation(
    name="externalTransition17",
    ends={
        Property(name="ExternalTransition", type=devs_InputEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="inputEvent", type=devs_ExternalTransition, multiplicity=Multiplicity(0, 9999))
    }
)
outputFunction18: BinaryAssociation = BinaryAssociation(
    name="outputFunction18",
    ends={
        Property(name="OutputFunction19", type=devs_OutputEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="outputEvent", type=devs_OutputFunction, multiplicity=Multiplicity(0, 9999))
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="State21", type=devs_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=devs_State, multiplicity=Multiplicity(1, 1))
    }
)
event1: BinaryAssociation = BinaryAssociation(
    name="event1",
    ends={
        Property(name="Event", type=devs_AtomicModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atomicModel2", type=devs_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition3: BinaryAssociation = BinaryAssociation(
    name="transition3",
    ends={
        Property(name="Transition", type=devs_AtomicModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atomicModel4", type=devs_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputFunction5: BinaryAssociation = BinaryAssociation(
    name="outputFunction5",
    ends={
        Property(name="OutputFunction", type=devs_AtomicModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atomicModel6", type=devs_OutputFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in7: BinaryAssociation = BinaryAssociation(
    name="in7",
    ends={
        Property(name="Transition8", type=devs_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=devs_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outputEvent29: BinaryAssociation = BinaryAssociation(
    name="outputEvent29",
    ends={
        Property(name="OutputEvent", type=devs_OutputFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="outputFunction", type=devs_OutputEvent, multiplicity=Multiplicity(1, 1))
    }
)
atomicModel30: BinaryAssociation = BinaryAssociation(
    name="atomicModel30",
    ends={
        Property(name="AtomicModel32", type=devs_OutputFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="outputFunction31", type=devs_AtomicModel, multiplicity=Multiplicity(1, 1))
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="State23", type=devs_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=devs_State, multiplicity=Multiplicity(1, 1))
    }
)
atomicModel24: BinaryAssociation = BinaryAssociation(
    name="atomicModel24",
    ends={
        Property(name="AtomicModel25", type=devs_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=devs_AtomicModel, multiplicity=Multiplicity(1, 1))
    }
)
inputEvent26: BinaryAssociation = BinaryAssociation(
    name="inputEvent26",
    ends={
        Property(name="InputEvent", type=devs_ExternalTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="externalTransition", type=devs_InputEvent, multiplicity=Multiplicity(1, 1))
    }
)
source27: BinaryAssociation = BinaryAssociation(
    name="source27",
    ends={
        Property(name="State28", type=devs_OutputFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="outF", type=devs_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_devs_InputEvent_Event = Generalization(general=Event, specific=devs_InputEvent)
gen_devs_OutputEvent_Event = Generalization(general=Event, specific=devs_OutputEvent)
gen_devs_InternalTransition_Transition = Generalization(general=Transition, specific=devs_InternalTransition)
gen_devs_ExternalTransition_Transition = Generalization(general=Transition, specific=devs_ExternalTransition)

# Domain Model
domain_model = DomainModel(
    name="devs",
    types={devs_AtomicModel, devs_State, devs_InputEvent, Event, devs_ExternalTransition, devs_OutputEvent, devs_Event, devs_Transition, devs_OutputFunction, devs_InternalTransition, Transition},
    associations={state0, out9, outF11, atomicModel14, atomicModel15, externalTransition17, outputFunction18, source20, event1, transition3, outputFunction5, in7, outputEvent29, atomicModel30, target22, atomicModel24, inputEvent26, source27},
    generalizations={gen_devs_InputEvent_Event, gen_devs_OutputEvent_Event, gen_devs_InternalTransition_Transition, gen_devs_ExternalTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)