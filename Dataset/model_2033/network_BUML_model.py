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
Event: Enumeration = Enumeration(
    name="Event",
    literals={
            EnumerationLiteral(name="SEND"),
			EnumerationLiteral(name="RECEIVE")
    }
)

TypeOfChannel: Enumeration = Enumeration(
    name="TypeOfChannel",
    literals={
            EnumerationLiteral(name="Asynchronous"),
			EnumerationLiteral(name="Synchronous")
    }
)

# Classes
network_Network = Class(name="network_Network")
AbstractElement = Class(name="AbstractElement")
network_Statemachine = Class(name="network_Statemachine")
network_Channel = Class(name="network_Channel")
network_AbstractElement = Class(name="network_AbstractElement", is_abstract=True)
network_State = Class(name="network_State")
network_Transition = Class(name="network_Transition")

# network_Network class attributes and methods

# AbstractElement class attributes and methods

# network_Statemachine class attributes and methods

# network_Channel class attributes and methods
network_Channel_Type: Property = Property(name="Type", type=StringType)
network_Channel.attributes={network_Channel_Type}

# network_AbstractElement class attributes and methods
network_AbstractElement_name: Property = Property(name="name", type=StringType)
network_AbstractElement.attributes={network_AbstractElement_name}

# network_State class attributes and methods

# network_Transition class attributes and methods
network_Transition_Event: Property = Property(name="Event", type=StringType)
network_Transition.attributes={network_Transition_Event}

# Relationships
statemachine0: BinaryAssociation = BinaryAssociation(
    name="statemachine0",
    ends={
        Property(name="network_Statemachine", type=network_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="network_Network", type=network_Statemachine, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
channel1: BinaryAssociation = BinaryAssociation(
    name="channel1",
    ends={
        Property(name="network_Channel", type=network_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="network_Network2", type=network_Channel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
state3: BinaryAssociation = BinaryAssociation(
    name="state3",
    ends={
        Property(name="network_State", type=network_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="network_Statemachine4", type=network_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initState5: BinaryAssociation = BinaryAssociation(
    name="initState5",
    ends={
        Property(name="network_State7", type=network_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="network_Statemachine6", type=network_State, multiplicity=Multiplicity(1, 1))
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="network_Transition", type=network_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="network_Statemachine9", type=network_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="network_State12", type=network_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="network_Transition11", type=network_State, multiplicity=Multiplicity(1, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="network_State15", type=network_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="network_Transition14", type=network_State, multiplicity=Multiplicity(1, 1))
    }
)
channel16: BinaryAssociation = BinaryAssociation(
    name="channel16",
    ends={
        Property(name="network_Channel18", type=network_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="network_Transition17", type=network_Channel, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_network_Network_AbstractElement = Generalization(general=AbstractElement, specific=network_Network)
gen_network_Statemachine_AbstractElement = Generalization(general=AbstractElement, specific=network_Statemachine)
gen_network_State_AbstractElement = Generalization(general=AbstractElement, specific=network_State)
gen_network_Channel_AbstractElement = Generalization(general=AbstractElement, specific=network_Channel)

# Domain Model
domain_model = DomainModel(
    name="network",
    types={network_Network, AbstractElement, network_Statemachine, network_Channel, network_AbstractElement, network_State, network_Transition, Event, TypeOfChannel},
    associations={statemachine0, channel1, state3, initState5, transition8, source10, target13, channel16},
    generalizations={gen_network_Network_AbstractElement, gen_network_Statemachine_AbstractElement, gen_network_State_AbstractElement, gen_network_Channel_AbstractElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)