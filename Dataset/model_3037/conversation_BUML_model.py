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
ConnectionType: Enumeration = Enumeration(
    name="ConnectionType",
    literals={
            EnumerationLiteral(name="independent"),
			EnumerationLiteral(name="dependent")
    }
)

StateMachineType: Enumeration = Enumeration(
    name="StateMachineType",
    literals={
            EnumerationLiteral(name="infinite"),
			EnumerationLiteral(name="stateless"),
			EnumerationLiteral(name="finite")
    }
)

# Classes
conversation_Projection = Class(name="conversation::Projection")
conversation_RestService = Class(name="conversation::RestService")
conversation_Conversation = Class(name="conversation::Conversation")
conversation_Agent = Class(name="conversation::Agent")
conversation_Service = Class(name="conversation::Service")
conversation_TypeImport = Class(name="conversation::TypeImport")
conversation_AgentImport = Class(name="conversation::AgentImport")
conversation_View = Class(name="conversation::View")
conversation_State = Class(name="conversation::State")
conversation_StateMachine = Class(name="conversation::StateMachine")
conversation_PubliclySubscribable = Class(name="conversation::PubliclySubscribable")
conversation_Transition = Class(name="conversation::Transition")
conversation_Event = Class(name="conversation::Event", is_abstract=True)
Event = Class(name="Event")
conversation_Decision = Class(name="conversation::Decision")
State = Class(name="State")
conversation_SubscribableByOthers = Class(name="conversation::SubscribableByOthers", is_abstract=True)
conversation_PrivatePubSub = Class(name="conversation::PrivatePubSub")
conversation_PublishableByOthers = Class(name="conversation::PublishableByOthers", is_abstract=True)
conversation_PublishableByMe = Class(name="conversation::PublishableByMe", is_abstract=True)
conversation_ProjectionField = Class(name="conversation::ProjectionField")
conversation_SubscribableByMe = Class(name="conversation::SubscribableByMe", is_abstract=True)
conversation_PublicEvent = Class(name="conversation::PublicEvent", is_abstract=True)
conversation_PubliclyPublishable = Class(name="conversation::PubliclyPublishable")
SubscribableByMe = Class(name="SubscribableByMe")
PublishableByOthers = Class(name="PublishableByOthers")
PublicEvent = Class(name="PublicEvent")
PublishableByMe = Class(name="PublishableByMe")
SubscribableByOthers = Class(name="SubscribableByOthers")
conversation_PublicPubSub = Class(name="conversation::PublicPubSub")
PubliclyPublishable = Class(name="PubliclyPublishable")
PubliclySubscribable = Class(name="PubliclySubscribable")
Import = Class(name="Import")
conversation_Import = Class(name="conversation::Import")
conversation_Join = Class(name="conversation::Join")
conversation_Junction = Class(name="conversation::Junction")

# conversation_Projection class attributes and methods

# conversation_RestService class attributes and methods

# conversation_Conversation class attributes and methods
conversation_Conversation_name: Property = Property(name="name", type=StringType)
conversation_Conversation.attributes={conversation_Conversation_name}

# conversation_Agent class attributes and methods
conversation_Agent_name: Property = Property(name="name", type=StringType)
conversation_Agent_stateMachineType: Property = Property(name="stateMachineType", type=StringType)
conversation_Agent_connectionType: Property = Property(name="connectionType", type=StringType)
conversation_Agent_accessRequirement: Property = Property(name="accessRequirement", type=StringType)
conversation_Agent.attributes={conversation_Agent_stateMachineType, conversation_Agent_name, conversation_Agent_accessRequirement, conversation_Agent_connectionType}

# conversation_Service class attributes and methods

# conversation_TypeImport class attributes and methods

# conversation_AgentImport class attributes and methods

# conversation_View class attributes and methods

# conversation_State class attributes and methods
conversation_State_requiresExecution: Property = Property(name="requiresExecution", type=BooleanType)
conversation_State_join: Property = Property(name="join", type=BooleanType)
conversation_State_name: Property = Property(name="name", type=StringType)
conversation_State.attributes={conversation_State_requiresExecution, conversation_State_name, conversation_State_join}

# conversation_StateMachine class attributes and methods

# conversation_PubliclySubscribable class attributes and methods

# conversation_Transition class attributes and methods
conversation_Transition_requiresExecution: Property = Property(name="requiresExecution", type=BooleanType)
conversation_Transition.attributes={conversation_Transition_requiresExecution}

# conversation_Event class attributes and methods
conversation_Event_name: Property = Property(name="name", type=StringType)
conversation_Event.attributes={conversation_Event_name}

# Event class attributes and methods

# conversation_Decision class attributes and methods

# State class attributes and methods

# conversation_SubscribableByOthers class attributes and methods

# conversation_PrivatePubSub class attributes and methods

# conversation_PublishableByOthers class attributes and methods

# conversation_PublishableByMe class attributes and methods

# conversation_ProjectionField class attributes and methods

# conversation_SubscribableByMe class attributes and methods

# conversation_PublicEvent class attributes and methods

# conversation_PubliclyPublishable class attributes and methods

# SubscribableByMe class attributes and methods

# PublishableByOthers class attributes and methods

# PublicEvent class attributes and methods

# PublishableByMe class attributes and methods

# SubscribableByOthers class attributes and methods

# conversation_PublicPubSub class attributes and methods

# PubliclyPublishable class attributes and methods

# PubliclySubscribable class attributes and methods

# Import class attributes and methods

# conversation_Import class attributes and methods
conversation_Import_alias: Property = Property(name="alias", type=StringType)
conversation_Import.attributes={conversation_Import_alias}

# conversation_Join class attributes and methods

# conversation_Junction class attributes and methods

# Relationships
definedTypes1: BinaryAssociation = BinaryAssociation(
    name="definedTypes1",
    ends={
        Property(name="conversation_Projection", type=conversation_Conversation, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Conversation", type=conversation_Projection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
agents0: BinaryAssociation = BinaryAssociation(
    name="agents0",
    ends={
        Property(name="Agent", type=conversation_Conversation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=conversation_Agent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definedTypes12: BinaryAssociation = BinaryAssociation(
    name="definedTypes12",
    ends={
        Property(name="conversation_Projection13", type=conversation_Agent, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Agent", type=conversation_Projection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
restServices2: BinaryAssociation = BinaryAssociation(
    name="restServices2",
    ends={
        Property(name="conversation_RestService", type=conversation_Conversation, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Conversation3", type=conversation_RestService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services4: BinaryAssociation = BinaryAssociation(
    name="services4",
    ends={
        Property(name="conversation_Service", type=conversation_Conversation, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Conversation5", type=conversation_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedTypes6: BinaryAssociation = BinaryAssociation(
    name="importedTypes6",
    ends={
        Property(name="conversation_TypeImport", type=conversation_Conversation, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Conversation7", type=conversation_TypeImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedAgents8: BinaryAssociation = BinaryAssociation(
    name="importedAgents8",
    ends={
        Property(name="conversation_AgentImport", type=conversation_Conversation, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Conversation9", type=conversation_AgentImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views10: BinaryAssociation = BinaryAssociation(
    name="views10",
    ends={
        Property(name="conversation_View", type=conversation_Conversation, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Conversation11", type=conversation_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState22: BinaryAssociation = BinaryAssociation(
    name="initialState22",
    ends={
        Property(name="conversation_State", type=conversation_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_StateMachine", type=conversation_State, multiplicity=Multiplicity(0, 1))
    }
)
states23: BinaryAssociation = BinaryAssociation(
    name="states23",
    ends={
        Property(name="State", type=conversation_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="parent24", type=conversation_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
stateMachine14: BinaryAssociation = BinaryAssociation(
    name="stateMachine14",
    ends={
        Property(name="StateMachine", type=conversation_Agent, multiplicity=Multiplicity(1, 1)),
        Property(name="parent15", type=conversation_StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sendables16: BinaryAssociation = BinaryAssociation(
    name="sendables16",
    ends={
        Property(name="PubliclySubscribable", type=conversation_Agent, multiplicity=Multiplicity(1, 1)),
        Property(name="parent17", type=conversation_PubliclySubscribable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent18: BinaryAssociation = BinaryAssociation(
    name="parent18",
    ends={
        Property(name="Conversation", type=conversation_Agent, multiplicity=Multiplicity(1, 1)),
        Property(name="agents", type=conversation_Conversation, multiplicity=Multiplicity(0, 1))
    }
)
projection19: BinaryAssociation = BinaryAssociation(
    name="projection19",
    ends={
        Property(name="conversation_Projection21", type=conversation_Agent, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Agent20", type=conversation_Projection, multiplicity=Multiplicity(0, 1))
    }
)
parent25: BinaryAssociation = BinaryAssociation(
    name="parent25",
    ends={
        Property(name="Agent26", type=conversation_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=conversation_Agent, multiplicity=Multiplicity(0, 1))
    }
)
initialTransition27: BinaryAssociation = BinaryAssociation(
    name="initialTransition27",
    ends={
        Property(name="conversation_Transition", type=conversation_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_StateMachine28", type=conversation_Transition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent34: BinaryAssociation = BinaryAssociation(
    name="parent34",
    ends={
        Property(name="StateMachine35", type=conversation_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=conversation_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
refType29: BinaryAssociation = BinaryAssociation(
    name="refType29",
    ends={
        Property(name="conversation_Projection30", type=conversation_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Event", type=conversation_Projection, multiplicity=Multiplicity(0, 1))
    }
)
transitions31: BinaryAssociation = BinaryAssociation(
    name="transitions31",
    ends={
        Property(name="conversation_Transition33", type=conversation_State, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_State32", type=conversation_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toState36: BinaryAssociation = BinaryAssociation(
    name="toState36",
    ends={
        Property(name="conversation_State38", type=conversation_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Transition37", type=conversation_State, multiplicity=Multiplicity(1, 1))
    }
)
exCausedBy39: BinaryAssociation = BinaryAssociation(
    name="exCausedBy39",
    ends={
        Property(name="conversation_SubscribableByOthers", type=conversation_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Transition40", type=conversation_SubscribableByOthers, multiplicity=Multiplicity(0, 1))
    }
)
causedBy41: BinaryAssociation = BinaryAssociation(
    name="causedBy41",
    ends={
        Property(name="PrivatePubSub", type=conversation_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=conversation_PrivatePubSub, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exTriggers42: BinaryAssociation = BinaryAssociation(
    name="exTriggers42",
    ends={
        Property(name="conversation_PublishableByOthers", type=conversation_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Transition43", type=conversation_PublishableByOthers, multiplicity=Multiplicity(0, 1))
    }
)
triggers44: BinaryAssociation = BinaryAssociation(
    name="triggers44",
    ends={
        Property(name="conversation_PublishableByMe", type=conversation_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Transition45", type=conversation_PublishableByMe, multiplicity=Multiplicity(0, 1))
    }
)
fieldMapping46: BinaryAssociation = BinaryAssociation(
    name="fieldMapping46",
    ends={
        Property(name="conversation_ProjectionField", type=conversation_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Transition47", type=conversation_ProjectionField, multiplicity=Multiplicity(0, 1))
    }
)
transition50: BinaryAssociation = BinaryAssociation(
    name="transition50",
    ends={
        Property(name="Transition", type=conversation_PrivatePubSub, multiplicity=Multiplicity(1, 1)),
        Property(name="causedBy", type=conversation_Transition, multiplicity=Multiplicity(0, 1))
    }
)
parent48: BinaryAssociation = BinaryAssociation(
    name="parent48",
    ends={
        Property(name="Agent49", type=conversation_PubliclySubscribable, multiplicity=Multiplicity(1, 1)),
        Property(name="sendables", type=conversation_Agent, multiplicity=Multiplicity(0, 1))
    }
)
agent51: BinaryAssociation = BinaryAssociation(
    name="agent51",
    ends={
        Property(name="conversation_Agent53", type=conversation_AgentImport, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_AgentImport52", type=conversation_Agent, multiplicity=Multiplicity(0, 1))
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="conversation_Projection56", type=conversation_TypeImport, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_TypeImport55", type=conversation_Projection, multiplicity=Multiplicity(0, 1))
    }
)
joins57: BinaryAssociation = BinaryAssociation(
    name="joins57",
    ends={
        Property(name="conversation_Junction", type=conversation_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Join", type=conversation_Junction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
message58: BinaryAssociation = BinaryAssociation(
    name="message58",
    ends={
        Property(name="conversation_SubscribableByOthers60", type=conversation_Junction, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Junction59", type=conversation_SubscribableByOthers, multiplicity=Multiplicity(1, 1))
    }
)
fieldMapping61: BinaryAssociation = BinaryAssociation(
    name="fieldMapping61",
    ends={
        Property(name="conversation_ProjectionField63", type=conversation_Junction, multiplicity=Multiplicity(1, 1)),
        Property(name="conversation_Junction62", type=conversation_ProjectionField, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_conversation_SubscribableByOthers_Event = Generalization(general=Event, specific=conversation_SubscribableByOthers)
gen_conversation_PublishableByOthers_Event = Generalization(general=Event, specific=conversation_PublishableByOthers)
gen_conversation_Decision_State = Generalization(general=State, specific=conversation_Decision)
gen_conversation_SubscribableByMe_Event = Generalization(general=Event, specific=conversation_SubscribableByMe)
gen_conversation_PublishableByMe_Event = Generalization(general=Event, specific=conversation_PublishableByMe)
gen_conversation_PublicEvent_Event = Generalization(general=Event, specific=conversation_PublicEvent)
gen_conversation_PubliclyPublishable_SubscribableByMe = Generalization(general=SubscribableByMe, specific=conversation_PubliclyPublishable)
gen_conversation_PubliclyPublishable_PublishableByOthers = Generalization(general=PublishableByOthers, specific=conversation_PubliclyPublishable)
gen_conversation_PubliclyPublishable_PublicEvent = Generalization(general=PublicEvent, specific=conversation_PubliclyPublishable)
gen_conversation_PubliclySubscribable_PublishableByMe = Generalization(general=PublishableByMe, specific=conversation_PubliclySubscribable)
gen_conversation_PubliclySubscribable_SubscribableByOthers = Generalization(general=SubscribableByOthers, specific=conversation_PubliclySubscribable)
gen_conversation_PubliclySubscribable_PublicEvent = Generalization(general=PublicEvent, specific=conversation_PubliclySubscribable)
gen_conversation_PrivatePubSub_PublishableByMe = Generalization(general=PublishableByMe, specific=conversation_PrivatePubSub)
gen_conversation_PrivatePubSub_SubscribableByMe = Generalization(general=SubscribableByMe, specific=conversation_PrivatePubSub)
gen_conversation_PublicPubSub_PubliclyPublishable = Generalization(general=PubliclyPublishable, specific=conversation_PublicPubSub)
gen_conversation_PublicPubSub_PubliclySubscribable = Generalization(general=PubliclySubscribable, specific=conversation_PublicPubSub)
gen_conversation_AgentImport_Import = Generalization(general=Import, specific=conversation_AgentImport)
gen_conversation_TypeImport_Import = Generalization(general=Import, specific=conversation_TypeImport)
gen_conversation_Join_State = Generalization(general=State, specific=conversation_Join)

# Domain Model
domain_model = DomainModel(
    name="conversation",
    types={conversation_Projection, conversation_RestService, conversation_Conversation, conversation_Agent, conversation_Service, conversation_TypeImport, conversation_AgentImport, conversation_View, conversation_State, conversation_StateMachine, conversation_PubliclySubscribable, conversation_Transition, conversation_Event, Event, conversation_Decision, State, conversation_SubscribableByOthers, conversation_PrivatePubSub, conversation_PublishableByOthers, conversation_PublishableByMe, conversation_ProjectionField, conversation_SubscribableByMe, conversation_PublicEvent, conversation_PubliclyPublishable, SubscribableByMe, PublishableByOthers, PublicEvent, PublishableByMe, SubscribableByOthers, conversation_PublicPubSub, PubliclyPublishable, PubliclySubscribable, Import, conversation_Import, conversation_Join, conversation_Junction, ConnectionType, StateMachineType},
    associations={definedTypes1, agents0, definedTypes12, restServices2, services4, importedTypes6, importedAgents8, views10, initialState22, states23, stateMachine14, sendables16, parent18, projection19, parent25, initialTransition27, parent34, refType29, transitions31, toState36, exCausedBy39, causedBy41, exTriggers42, triggers44, fieldMapping46, transition50, parent48, agent51, type54, joins57, message58, fieldMapping61},
    generalizations={gen_conversation_SubscribableByOthers_Event, gen_conversation_PublishableByOthers_Event, gen_conversation_Decision_State, gen_conversation_SubscribableByMe_Event, gen_conversation_PublishableByMe_Event, gen_conversation_PublicEvent_Event, gen_conversation_PubliclyPublishable_SubscribableByMe, gen_conversation_PubliclyPublishable_PublishableByOthers, gen_conversation_PubliclyPublishable_PublicEvent, gen_conversation_PubliclySubscribable_PublishableByMe, gen_conversation_PubliclySubscribable_SubscribableByOthers, gen_conversation_PubliclySubscribable_PublicEvent, gen_conversation_PrivatePubSub_PublishableByMe, gen_conversation_PrivatePubSub_SubscribableByMe, gen_conversation_PublicPubSub_PubliclyPublishable, gen_conversation_PublicPubSub_PubliclySubscribable, gen_conversation_AgentImport_Import, gen_conversation_TypeImport_Import, gen_conversation_Join_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)