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
TypeOfChannel: Enumeration = Enumeration(
    name="TypeOfChannel",
    literals={
            EnumerationLiteral(name="Synchronous"),
			EnumerationLiteral(name="Asynchronous")
    }
)

Event: Enumeration = Enumeration(
    name="Event",
    literals={
            EnumerationLiteral(name="SEND"),
			EnumerationLiteral(name="RECEIVE")
    }
)

# Classes
amf_Network = Class(name="amf::Network")
amf_Channel = Class(name="amf::Channel")
amf_Statemachine = Class(name="amf::Statemachine")
amf_State = Class(name="amf::State")
amf_Transition = Class(name="amf::Transition")

# amf_Network class attributes and methods
amf_Network_name: Property = Property(name="name", type=StringType)
amf_Network.attributes={amf_Network_name}

# amf_Channel class attributes and methods
amf_Channel_Type: Property = Property(name="Type", type=StringType)
amf_Channel_name: Property = Property(name="name", type=StringType)
amf_Channel.attributes={amf_Channel_name, amf_Channel_Type}

# amf_Statemachine class attributes and methods
amf_Statemachine_name: Property = Property(name="name", type=StringType)
amf_Statemachine.attributes={amf_Statemachine_name}

# amf_State class attributes and methods
amf_State_name: Property = Property(name="name", type=StringType)
amf_State.attributes={amf_State_name}

# amf_Transition class attributes and methods
amf_Transition_event: Property = Property(name="event", type=StringType)
amf_Transition.attributes={amf_Transition_event}

# Relationships
channel0: BinaryAssociation = BinaryAssociation(
    name="channel0",
    ends={
        Property(name="amf_Channel", type=amf_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="amf_Network", type=amf_Channel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statemachine1: BinaryAssociation = BinaryAssociation(
    name="statemachine1",
    ends={
        Property(name="amf_Statemachine", type=amf_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="amf_Network2", type=amf_Statemachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="amf_State12", type=amf_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="amf_Transition11", type=amf_State, multiplicity=Multiplicity(0, 1))
    }
)
channel13: BinaryAssociation = BinaryAssociation(
    name="channel13",
    ends={
        Property(name="amf_Channel15", type=amf_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="amf_Transition14", type=amf_Channel, multiplicity=Multiplicity(0, 1))
    }
)
initialstate3: BinaryAssociation = BinaryAssociation(
    name="initialstate3",
    ends={
        Property(name="amf_State", type=amf_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="amf_Statemachine4", type=amf_State, multiplicity=Multiplicity(0, 1))
    }
)
state5: BinaryAssociation = BinaryAssociation(
    name="state5",
    ends={
        Property(name="amf_State7", type=amf_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="amf_Statemachine6", type=amf_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="amf_Transition", type=amf_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="amf_Statemachine9", type=amf_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="amf_State18", type=amf_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="amf_Transition17", type=amf_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="amf",
    types={amf_Network, amf_Channel, amf_Statemachine, amf_State, amf_Transition, TypeOfChannel, Event},
    associations={channel0, statemachine1, source10, channel13, initialstate3, state5, transition8, target16},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)