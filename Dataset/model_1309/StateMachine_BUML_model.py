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
stateMachine_Transition = Class(name="stateMachine::Transition", is_abstract=True)
stateMachine_InitialState = Class(name="stateMachine::InitialState")
State = Class(name="State")
stateMachine_StateMachine = Class(name="stateMachine::StateMachine")
stateMachine_State = Class(name="stateMachine::State")
stateMachine_Properties = Class(name="stateMachine::Properties")
stateMachine_IVREvent = Class(name="stateMachine::IVREvent", is_abstract=True)
Transition = Class(name="Transition")
stateMachine_Bye = Class(name="stateMachine::Bye")
IVREvent = Class(name="IVREvent")
stateMachine_Call = Class(name="stateMachine::Call")
stateMachine_PickUp = Class(name="stateMachine::PickUp")
stateMachine_Played = Class(name="stateMachine::Played")
stateMachine_Recorderd = Class(name="stateMachine::Recorderd")
stateMachine_Terminated = Class(name="stateMachine::Terminated")
stateMachine_FinalState = Class(name="stateMachine::FinalState")
stateMachine_CompositeState = Class(name="stateMachine::CompositeState")
stateMachine_Action = Class(name="stateMachine::Action", is_abstract=True)
stateMachine_IvrAction = Class(name="stateMachine::IvrAction", is_abstract=True)
Action = Class(name="Action")
stateMachine_Play = Class(name="stateMachine::Play")
IvrAction = Class(name="IvrAction")
stateMachine_Terminate = Class(name="stateMachine::Terminate")
stateMachine_SendSms = Class(name="stateMachine::SendSms")
stateMachine_SMS = Class(name="stateMachine::SMS")
stateMachine_SetTimer = Class(name="stateMachine::SetTimer")
stateMachine_Key = Class(name="stateMachine::Key")
Branch = Class(name="Branch")
stateMachine_Otherwise = Class(name="stateMachine::Otherwise")
stateMachine_Init = Class(name="stateMachine::Init")
stateMachine_Cancel = Class(name="stateMachine::Cancel")
stateMachine_CollectTimeout = Class(name="stateMachine::CollectTimeout")
stateMachine_Managed = Class(name="stateMachine::Managed")
stateMachine_NoneEvent = Class(name="stateMachine::NoneEvent")
stateMachine_SMSReceived = Class(name="stateMachine::SMSReceived")
stateMachine_Timer = Class(name="stateMachine::Timer")
stateMachine_Collected = Class(name="stateMachine::Collected")
stateMachine_Branch = Class(name="stateMachine::Branch", is_abstract=True)

# stateMachine_Transition class attributes and methods

# stateMachine_InitialState class attributes and methods

# State class attributes and methods

# stateMachine_StateMachine class attributes and methods
stateMachine_StateMachine_nombre: Property = Property(name="nombre", type=StringType)
stateMachine_StateMachine.attributes={stateMachine_StateMachine_nombre}

# stateMachine_State class attributes and methods
stateMachine_State_nombre: Property = Property(name="nombre", type=StringType)
stateMachine_State.attributes={stateMachine_State_nombre}

# stateMachine_Properties class attributes and methods
stateMachine_Properties_applicationServerHost: Property = Property(name="applicationServerHost", type=StringType)
stateMachine_Properties_applicationServerPort: Property = Property(name="applicationServerPort", type=IntegerType)
stateMachine_Properties_mediaHost: Property = Property(name="mediaHost", type=StringType)
stateMachine_Properties_mediaPort: Property = Property(name="mediaPort", type=IntegerType)
stateMachine_Properties_mediaProtocol: Property = Property(name="mediaProtocol", type=StringType)
stateMachine_Properties_setupConference: Property = Property(name="setupConference", type=BooleanType)
stateMachine_Properties_applicationAddress: Property = Property(name="applicationAddress", type=StringType)
stateMachine_Properties_mediaFromAddr: Property = Property(name="mediaFromAddr", type=StringType)
stateMachine_Properties_mediaToAddr: Property = Property(name="mediaToAddr", type=StringType)
stateMachine_Properties_mediaURI: Property = Property(name="mediaURI", type=StringType)
stateMachine_Properties_recordPath: Property = Property(name="recordPath", type=StringType)
stateMachine_Properties_scscfUser: Property = Property(name="scscfUser", type=StringType)
stateMachine_Properties_scscfHost: Property = Property(name="scscfHost", type=StringType)
stateMachine_Properties_scscfPort: Property = Property(name="scscfPort", type=IntegerType)
stateMachine_Properties_scscfProtocol: Property = Property(name="scscfProtocol", type=StringType)
stateMachine_Properties_applicationServerProtocol: Property = Property(name="applicationServerProtocol", type=StringType)
stateMachine_Properties.attributes={stateMachine_Properties_scscfProtocol, stateMachine_Properties_applicationAddress, stateMachine_Properties_mediaHost, stateMachine_Properties_setupConference, stateMachine_Properties_mediaToAddr, stateMachine_Properties_applicationServerHost, stateMachine_Properties_recordPath, stateMachine_Properties_applicationServerPort, stateMachine_Properties_applicationServerProtocol, stateMachine_Properties_scscfHost, stateMachine_Properties_mediaPort, stateMachine_Properties_scscfUser, stateMachine_Properties_mediaProtocol, stateMachine_Properties_mediaFromAddr, stateMachine_Properties_mediaURI, stateMachine_Properties_scscfPort}

# stateMachine_IVREvent class attributes and methods

# Transition class attributes and methods

# stateMachine_Bye class attributes and methods

# IVREvent class attributes and methods

# stateMachine_Call class attributes and methods
stateMachine_Call_from: Property = Property(name="from", type=StringType)
stateMachine_Call_to: Property = Property(name="to", type=StringType)
stateMachine_Call.attributes={stateMachine_Call_from, stateMachine_Call_to}

# stateMachine_PickUp class attributes and methods

# stateMachine_Played class attributes and methods

# stateMachine_Recorderd class attributes and methods
stateMachine_Recorderd_recordId: Property = Property(name="recordId", type=StringType)
stateMachine_Recorderd.attributes={stateMachine_Recorderd_recordId}

# stateMachine_Terminated class attributes and methods

# stateMachine_FinalState class attributes and methods

# stateMachine_CompositeState class attributes and methods

# stateMachine_Action class attributes and methods

# stateMachine_IvrAction class attributes and methods

# Action class attributes and methods

# stateMachine_Play class attributes and methods
stateMachine_Play_baseURL: Property = Property(name="baseURL", type=StringType)
stateMachine_Play_mediaURI: Property = Property(name="mediaURI", type=StringType)
stateMachine_Play.attributes={stateMachine_Play_mediaURI, stateMachine_Play_baseURL}

# IvrAction class attributes and methods

# stateMachine_Terminate class attributes and methods

# stateMachine_SendSms class attributes and methods

# stateMachine_SMS class attributes and methods
stateMachine_SMS_from: Property = Property(name="from", type=StringType)
stateMachine_SMS_to: Property = Property(name="to", type=StringType)
stateMachine_SMS_text: Property = Property(name="text", type=StringType)
stateMachine_SMS.attributes={stateMachine_SMS_text, stateMachine_SMS_from, stateMachine_SMS_to}

# stateMachine_SetTimer class attributes and methods
stateMachine_SetTimer_millis: Property = Property(name="millis", type=FloatType)
stateMachine_SetTimer.attributes={stateMachine_SetTimer_millis}

# stateMachine_Key class attributes and methods
stateMachine_Key_key: Property = Property(name="key", type=StringType)
stateMachine_Key.attributes={stateMachine_Key_key}

# Branch class attributes and methods

# stateMachine_Otherwise class attributes and methods

# stateMachine_Init class attributes and methods

# stateMachine_Cancel class attributes and methods

# stateMachine_CollectTimeout class attributes and methods

# stateMachine_Managed class attributes and methods
stateMachine_Managed_success: Property = Property(name="success", type=BooleanType)
stateMachine_Managed_code: Property = Property(name="code", type=IntegerType)
stateMachine_Managed.attributes={stateMachine_Managed_code, stateMachine_Managed_success}

# stateMachine_NoneEvent class attributes and methods

# stateMachine_SMSReceived class attributes and methods

# stateMachine_Timer class attributes and methods

# stateMachine_Collected class attributes and methods

# stateMachine_Branch class attributes and methods

# Relationships
outs3: BinaryAssociation = BinaryAssociation(
    name="outs3",
    ends={
        Property(name="Transition", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=stateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="State", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=stateMachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="State8", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="stateMachine_State", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine", type=stateMachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties1: BinaryAssociation = BinaryAssociation(
    name="properties1",
    ends={
        Property(name="stateMachine_Properties", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine2", type=stateMachine_Properties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action12: BinaryAssociation = BinaryAssociation(
    name="action12",
    ends={
        Property(name="stateMachine_Action", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition", type=stateMachine_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src13: BinaryAssociation = BinaryAssociation(
    name="src13",
    ends={
        Property(name="State14", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outs", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
defaultTar15: BinaryAssociation = BinaryAssociation(
    name="defaultTar15",
    ends={
        Property(name="stateMachine_State17", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition16", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
sm9: BinaryAssociation = BinaryAssociation(
    name="sm9",
    ends={
        Property(name="stateMachine_StateMachine10", type=stateMachine_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_CompositeState", type=stateMachine_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
sms11: BinaryAssociation = BinaryAssociation(
    name="sms11",
    ends={
        Property(name="stateMachine_SMS", type=stateMachine_SendSms, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_SendSms", type=stateMachine_SMS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sms18: BinaryAssociation = BinaryAssociation(
    name="sms18",
    ends={
        Property(name="stateMachine_SMS19", type=stateMachine_SMSReceived, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_SMSReceived", type=stateMachine_SMS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branches20: BinaryAssociation = BinaryAssociation(
    name="branches20",
    ends={
        Property(name="stateMachine_Branch", type=stateMachine_Collected, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Collected", type=stateMachine_Branch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out21: BinaryAssociation = BinaryAssociation(
    name="out21",
    ends={
        Property(name="stateMachine_State23", type=stateMachine_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Branch22", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
action24: BinaryAssociation = BinaryAssociation(
    name="action24",
    ends={
        Property(name="stateMachine_Action26", type=stateMachine_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Branch25", type=stateMachine_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_stateMachine_InitialState_State = Generalization(general=State, specific=stateMachine_InitialState)
gen_stateMachine_IVREvent_Transition = Generalization(general=Transition, specific=stateMachine_IVREvent)
gen_stateMachine_Bye_IVREvent = Generalization(general=IVREvent, specific=stateMachine_Bye)
gen_stateMachine_Call_IVREvent = Generalization(general=IVREvent, specific=stateMachine_Call)
gen_stateMachine_PickUp_IVREvent = Generalization(general=IVREvent, specific=stateMachine_PickUp)
gen_stateMachine_Played_IVREvent = Generalization(general=IVREvent, specific=stateMachine_Played)
gen_stateMachine_Recorderd_IVREvent = Generalization(general=IVREvent, specific=stateMachine_Recorderd)
gen_stateMachine_Terminated_IVREvent = Generalization(general=IVREvent, specific=stateMachine_Terminated)
gen_stateMachine_FinalState_State = Generalization(general=State, specific=stateMachine_FinalState)
gen_stateMachine_CompositeState_State = Generalization(general=State, specific=stateMachine_CompositeState)
gen_stateMachine_IvrAction_Action = Generalization(general=Action, specific=stateMachine_IvrAction)
gen_stateMachine_Play_IvrAction = Generalization(general=IvrAction, specific=stateMachine_Play)
gen_stateMachine_Terminate_IvrAction = Generalization(general=IvrAction, specific=stateMachine_Terminate)
gen_stateMachine_SendSms_Action = Generalization(general=Action, specific=stateMachine_SendSms)
gen_stateMachine_SetTimer_Action = Generalization(general=Action, specific=stateMachine_SetTimer)
gen_stateMachine_Key_Branch = Generalization(general=Branch, specific=stateMachine_Key)
gen_stateMachine_Otherwise_Branch = Generalization(general=Branch, specific=stateMachine_Otherwise)
gen_stateMachine_Init_IVREvent = Generalization(general=IVREvent, specific=stateMachine_Init)
gen_stateMachine_Cancel_IVREvent = Generalization(general=IVREvent, specific=stateMachine_Cancel)
gen_stateMachine_CollectTimeout_IVREvent = Generalization(general=IVREvent, specific=stateMachine_CollectTimeout)
gen_stateMachine_Managed_IVREvent = Generalization(general=IVREvent, specific=stateMachine_Managed)
gen_stateMachine_NoneEvent_Transition = Generalization(general=Transition, specific=stateMachine_NoneEvent)
gen_stateMachine_SMSReceived_Transition = Generalization(general=Transition, specific=stateMachine_SMSReceived)
gen_stateMachine_Timer_Transition = Generalization(general=Transition, specific=stateMachine_Timer)
gen_stateMachine_Collected_IVREvent = Generalization(general=IVREvent, specific=stateMachine_Collected)

# Domain Model
domain_model = DomainModel(
    name="stateMachine",
    types={stateMachine_Transition, stateMachine_InitialState, State, stateMachine_StateMachine, stateMachine_State, stateMachine_Properties, stateMachine_IVREvent, Transition, stateMachine_Bye, IVREvent, stateMachine_Call, stateMachine_PickUp, stateMachine_Played, stateMachine_Recorderd, stateMachine_Terminated, stateMachine_FinalState, stateMachine_CompositeState, stateMachine_Action, stateMachine_IvrAction, Action, stateMachine_Play, IvrAction, stateMachine_Terminate, stateMachine_SendSms, stateMachine_SMS, stateMachine_SetTimer, stateMachine_Key, Branch, stateMachine_Otherwise, stateMachine_Init, stateMachine_Cancel, stateMachine_CollectTimeout, stateMachine_Managed, stateMachine_NoneEvent, stateMachine_SMSReceived, stateMachine_Timer, stateMachine_Collected, stateMachine_Branch},
    associations={outs3, children5, parent7, states0, properties1, action12, src13, defaultTar15, sm9, sms11, sms18, branches20, out21, action24},
    generalizations={gen_stateMachine_InitialState_State, gen_stateMachine_IVREvent_Transition, gen_stateMachine_Bye_IVREvent, gen_stateMachine_Call_IVREvent, gen_stateMachine_PickUp_IVREvent, gen_stateMachine_Played_IVREvent, gen_stateMachine_Recorderd_IVREvent, gen_stateMachine_Terminated_IVREvent, gen_stateMachine_FinalState_State, gen_stateMachine_CompositeState_State, gen_stateMachine_IvrAction_Action, gen_stateMachine_Play_IvrAction, gen_stateMachine_Terminate_IvrAction, gen_stateMachine_SendSms_Action, gen_stateMachine_SetTimer_Action, gen_stateMachine_Key_Branch, gen_stateMachine_Otherwise_Branch, gen_stateMachine_Init_IVREvent, gen_stateMachine_Cancel_IVREvent, gen_stateMachine_CollectTimeout_IVREvent, gen_stateMachine_Managed_IVREvent, gen_stateMachine_NoneEvent_Transition, gen_stateMachine_SMSReceived_Transition, gen_stateMachine_Timer_Transition, gen_stateMachine_Collected_IVREvent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)