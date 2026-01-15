from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class stateMachine_Branch(ABC):

    pass
class Branch:

    pass
class stateMachine_Otherwise(Branch):

    pass
class stateMachine_Key(Branch):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class stateMachine_SMS:

    def __init__(self, from: str, to: str, text: str, stateMachine_SMS: "stateMachine_SendSms" = None, stateMachine_SMS19: "stateMachine_SMSReceived" = None):
        self.from = from
        self.to = to
        self.text = text
        self.stateMachine_SMS = stateMachine_SMS
        self.stateMachine_SMS19 = stateMachine_SMS19
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def stateMachine_SMS(self):
        return self.__stateMachine_SMS

    @stateMachine_SMS.setter
    def stateMachine_SMS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_SMS__stateMachine_SMS", None)
        self.__stateMachine_SMS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_SendSms"):
                opp_val = getattr(old_value, "stateMachine_SendSms", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_SendSms", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_SendSms"):
                opp_val = getattr(value, "stateMachine_SendSms", None)
                setattr(value, "stateMachine_SendSms", self)

    @property
    def stateMachine_SMS19(self):
        return self.__stateMachine_SMS19

    @stateMachine_SMS19.setter
    def stateMachine_SMS19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_SMS__stateMachine_SMS19", None)
        self.__stateMachine_SMS19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_SMSReceived"):
                opp_val = getattr(old_value, "stateMachine_SMSReceived", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_SMSReceived", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_SMSReceived"):
                opp_val = getattr(value, "stateMachine_SMSReceived", None)
                setattr(value, "stateMachine_SMSReceived", self)

class IvrAction:

    pass
class stateMachine_Terminate(IvrAction):

    pass
class stateMachine_Play(IvrAction):

    def __init__(self, baseURL: str, mediaURI: str):
        self.baseURL = baseURL
        self.mediaURI = mediaURI
        
    @property
    def mediaURI(self) -> str:
        return self.__mediaURI

    @mediaURI.setter
    def mediaURI(self, mediaURI: str):
        self.__mediaURI = mediaURI

    @property
    def baseURL(self) -> str:
        return self.__baseURL

    @baseURL.setter
    def baseURL(self, baseURL: str):
        self.__baseURL = baseURL

class Action:

    pass
class stateMachine_SendSms(Action):

    pass
class stateMachine_SetTimer(Action):

    def __init__(self, millis: float):
        self.millis = millis
        
    @property
    def millis(self) -> float:
        return self.__millis

    @millis.setter
    def millis(self, millis: float):
        self.__millis = millis

class stateMachine_IvrAction(Action):

    pass
class stateMachine_Action(ABC):

    pass
class IVREvent:

    pass
class stateMachine_Cancel(IVREvent):

    pass
class stateMachine_Init(IVREvent):

    pass
class stateMachine_Played(IVREvent):

    pass
class stateMachine_Terminated(IVREvent):

    pass
class stateMachine_Recorderd(IVREvent):

    def __init__(self, recordId: str):
        self.recordId = recordId
        
    @property
    def recordId(self) -> str:
        return self.__recordId

    @recordId.setter
    def recordId(self, recordId: str):
        self.__recordId = recordId

class stateMachine_PickUp(IVREvent):

    pass
class stateMachine_Call(IVREvent):

    def __init__(self, from: str, to: str):
        self.from = from
        self.to = to
        
    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

class stateMachine_Collected(IVREvent):

    pass
class stateMachine_CollectTimeout(IVREvent):

    pass
class stateMachine_Managed(IVREvent):

    def __init__(self, success: bool, code: int):
        self.success = success
        self.code = code
        
    @property
    def code(self) -> int:
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def success(self) -> bool:
        return self.__success

    @success.setter
    def success(self, success: bool):
        self.__success = success

class stateMachine_Bye(IVREvent):

    pass
class Transition:

    pass
class stateMachine_NoneEvent(Transition):

    pass
class stateMachine_SMSReceived(Transition):

    pass
class stateMachine_Timer(Transition):

    pass
class stateMachine_IVREvent(Transition):

    pass
class stateMachine_Properties:

    def __init__(self, applicationServerHost: str, applicationServerPort: int, mediaHost: str, mediaPort: int, mediaProtocol: str, setupConference: bool, applicationAddress: str, mediaFromAddr: str, mediaToAddr: str, mediaURI: str, recordPath: str, scscfUser: str, scscfHost: str, scscfPort: int, scscfProtocol: str, applicationServerProtocol: str, stateMachine_Properties: "stateMachine_StateMachine" = None):
        self.applicationServerHost = applicationServerHost
        self.applicationServerPort = applicationServerPort
        self.mediaHost = mediaHost
        self.mediaPort = mediaPort
        self.mediaProtocol = mediaProtocol
        self.setupConference = setupConference
        self.applicationAddress = applicationAddress
        self.mediaFromAddr = mediaFromAddr
        self.mediaToAddr = mediaToAddr
        self.mediaURI = mediaURI
        self.recordPath = recordPath
        self.scscfUser = scscfUser
        self.scscfHost = scscfHost
        self.scscfPort = scscfPort
        self.scscfProtocol = scscfProtocol
        self.applicationServerProtocol = applicationServerProtocol
        self.stateMachine_Properties = stateMachine_Properties
        
    @property
    def scscfProtocol(self) -> str:
        return self.__scscfProtocol

    @scscfProtocol.setter
    def scscfProtocol(self, scscfProtocol: str):
        self.__scscfProtocol = scscfProtocol

    @property
    def applicationAddress(self) -> str:
        return self.__applicationAddress

    @applicationAddress.setter
    def applicationAddress(self, applicationAddress: str):
        self.__applicationAddress = applicationAddress

    @property
    def mediaHost(self) -> str:
        return self.__mediaHost

    @mediaHost.setter
    def mediaHost(self, mediaHost: str):
        self.__mediaHost = mediaHost

    @property
    def setupConference(self) -> bool:
        return self.__setupConference

    @setupConference.setter
    def setupConference(self, setupConference: bool):
        self.__setupConference = setupConference

    @property
    def mediaToAddr(self) -> str:
        return self.__mediaToAddr

    @mediaToAddr.setter
    def mediaToAddr(self, mediaToAddr: str):
        self.__mediaToAddr = mediaToAddr

    @property
    def applicationServerHost(self) -> str:
        return self.__applicationServerHost

    @applicationServerHost.setter
    def applicationServerHost(self, applicationServerHost: str):
        self.__applicationServerHost = applicationServerHost

    @property
    def recordPath(self) -> str:
        return self.__recordPath

    @recordPath.setter
    def recordPath(self, recordPath: str):
        self.__recordPath = recordPath

    @property
    def applicationServerPort(self) -> int:
        return self.__applicationServerPort

    @applicationServerPort.setter
    def applicationServerPort(self, applicationServerPort: int):
        self.__applicationServerPort = applicationServerPort

    @property
    def applicationServerProtocol(self) -> str:
        return self.__applicationServerProtocol

    @applicationServerProtocol.setter
    def applicationServerProtocol(self, applicationServerProtocol: str):
        self.__applicationServerProtocol = applicationServerProtocol

    @property
    def scscfHost(self) -> str:
        return self.__scscfHost

    @scscfHost.setter
    def scscfHost(self, scscfHost: str):
        self.__scscfHost = scscfHost

    @property
    def mediaPort(self) -> int:
        return self.__mediaPort

    @mediaPort.setter
    def mediaPort(self, mediaPort: int):
        self.__mediaPort = mediaPort

    @property
    def scscfUser(self) -> str:
        return self.__scscfUser

    @scscfUser.setter
    def scscfUser(self, scscfUser: str):
        self.__scscfUser = scscfUser

    @property
    def mediaProtocol(self) -> str:
        return self.__mediaProtocol

    @mediaProtocol.setter
    def mediaProtocol(self, mediaProtocol: str):
        self.__mediaProtocol = mediaProtocol

    @property
    def mediaFromAddr(self) -> str:
        return self.__mediaFromAddr

    @mediaFromAddr.setter
    def mediaFromAddr(self, mediaFromAddr: str):
        self.__mediaFromAddr = mediaFromAddr

    @property
    def mediaURI(self) -> str:
        return self.__mediaURI

    @mediaURI.setter
    def mediaURI(self, mediaURI: str):
        self.__mediaURI = mediaURI

    @property
    def scscfPort(self) -> int:
        return self.__scscfPort

    @scscfPort.setter
    def scscfPort(self, scscfPort: int):
        self.__scscfPort = scscfPort

    @property
    def stateMachine_Properties(self):
        return self.__stateMachine_Properties

    @stateMachine_Properties.setter
    def stateMachine_Properties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Properties__stateMachine_Properties", None)
        self.__stateMachine_Properties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine2"):
                opp_val = getattr(old_value, "stateMachine_StateMachine2", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_StateMachine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine2"):
                opp_val = getattr(value, "stateMachine_StateMachine2", None)
                setattr(value, "stateMachine_StateMachine2", self)

class stateMachine_State:

    def __init__(self, nombre: str, src: set["stateMachine_Transition"] = None, State: "stateMachine_State" = None, parent: set["stateMachine_State"] = None, State8: "stateMachine_State" = None, children: "stateMachine_State" = None, stateMachine_State: "stateMachine_StateMachine" = None, State14: "stateMachine_Transition" = None, stateMachine_State17: "stateMachine_Transition" = None, stateMachine_State23: "stateMachine_Branch" = None):
        self.nombre = nombre
        self.src = src if src is not None else set()
        self.State = State
        self.parent = parent if parent is not None else set()
        self.State8 = State8
        self.children = children
        self.stateMachine_State = stateMachine_State
        self.State14 = State14
        self.stateMachine_State17 = stateMachine_State17
        self.stateMachine_State23 = stateMachine_State23
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State14(self):
        return self.__State14

    @State14.setter
    def State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__State14", None)
        self.__State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outs"):
                opp_val = getattr(old_value, "outs", None)
                if opp_val == self:
                    setattr(old_value, "outs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outs"):
                opp_val = getattr(value, "outs", None)
                setattr(value, "outs", self)

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__src", None)
        self.__src = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def stateMachine_State(self):
        return self.__stateMachine_State

    @stateMachine_State.setter
    def stateMachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State", None)
        self.__stateMachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine"):
                opp_val = getattr(old_value, "stateMachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine"):
                opp_val = getattr(value, "stateMachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_State23(self):
        return self.__stateMachine_State23

    @stateMachine_State23.setter
    def stateMachine_State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State23", None)
        self.__stateMachine_State23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Branch22"):
                opp_val = getattr(old_value, "stateMachine_Branch22", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Branch22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Branch22"):
                opp_val = getattr(value, "stateMachine_Branch22", None)
                setattr(value, "stateMachine_Branch22", self)

    @property
    def stateMachine_State17(self):
        return self.__stateMachine_State17

    @stateMachine_State17.setter
    def stateMachine_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State17", None)
        self.__stateMachine_State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Transition16"):
                opp_val = getattr(old_value, "stateMachine_Transition16", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Transition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Transition16"):
                opp_val = getattr(value, "stateMachine_Transition16", None)
                setattr(value, "stateMachine_Transition16", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State8"):
                opp_val = getattr(old_value, "State8", None)
                if opp_val == self:
                    setattr(old_value, "State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State8"):
                opp_val = getattr(value, "State8", None)
                setattr(value, "State8", self)

    @property
    def State8(self):
        return self.__State8

    @State8.setter
    def State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__State8", None)
        self.__State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

class stateMachine_StateMachine:

    def __init__(self, nombre: str, stateMachine_StateMachine: set["stateMachine_State"] = None, stateMachine_StateMachine2: "stateMachine_Properties" = None, stateMachine_StateMachine10: "stateMachine_CompositeState" = None):
        self.nombre = nombre
        self.stateMachine_StateMachine = stateMachine_StateMachine if stateMachine_StateMachine is not None else set()
        self.stateMachine_StateMachine2 = stateMachine_StateMachine2
        self.stateMachine_StateMachine10 = stateMachine_StateMachine10
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def stateMachine_StateMachine10(self):
        return self.__stateMachine_StateMachine10

    @stateMachine_StateMachine10.setter
    def stateMachine_StateMachine10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine10", None)
        self.__stateMachine_StateMachine10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_CompositeState"):
                opp_val = getattr(old_value, "stateMachine_CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_CompositeState"):
                opp_val = getattr(value, "stateMachine_CompositeState", None)
                setattr(value, "stateMachine_CompositeState", self)

    @property
    def stateMachine_StateMachine(self):
        return self.__stateMachine_StateMachine

    @stateMachine_StateMachine.setter
    def stateMachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine", None)
        self.__stateMachine_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_State"):
                    opp_val = getattr(item, "stateMachine_State", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_State"):
                    opp_val = getattr(item, "stateMachine_State", None)
                    
                    setattr(item, "stateMachine_State", self)
                    

    @property
    def stateMachine_StateMachine2(self):
        return self.__stateMachine_StateMachine2

    @stateMachine_StateMachine2.setter
    def stateMachine_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine2", None)
        self.__stateMachine_StateMachine2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Properties"):
                opp_val = getattr(old_value, "stateMachine_Properties", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Properties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Properties"):
                opp_val = getattr(value, "stateMachine_Properties", None)
                setattr(value, "stateMachine_Properties", self)

class State:

    pass
class stateMachine_CompositeState(State):

    pass
class stateMachine_FinalState(State):

    pass
class stateMachine_InitialState(State):

    pass
class stateMachine_Transition(ABC):

    pass