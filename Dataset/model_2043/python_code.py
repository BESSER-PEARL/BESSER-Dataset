from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveType(Enum):
    void = "void"
    int8 = "int8"
    int16 = "int16"
    int32 = "int32"
    uint8 = "uint8"
    uint16 = "uint16"
    uint32 = "uint32"
    float32 = "float32"
    float64 = "float64"
    boolean = "boolean"
    string = "string"
    char = "char"


############################################
# Definition of Classes
############################################

class TransitionTerminal:

    pass
class room_SubStateTrPointTerminal(TransitionTerminal):

    pass
class room_TrPointTerminal(TransitionTerminal):

    pass
class room_StateTerminal(TransitionTerminal):

    pass
class room_Trigger:

    pass
class room_Guard:

    pass
class room_MessageFromIf:

    pass
class room_ChoicepointTerminal(TransitionTerminal):

    pass
class room_TransitionTerminal:

    pass
class TrPoint:

    pass
class room_ExitPoint(TrPoint):

    pass
class room_EntryPoint(TrPoint):

    pass
class room_TransitionPoint(TrPoint):

    def __init__(self, handler: bool):
        self.handler = handler
        
    @property
    def handler(self) -> bool:
        return self.__handler

    @handler.setter
    def handler(self, handler: bool):
        self.__handler = handler

class State:

    pass
class room_RefinedState(State):

    pass
class room_BaseState(State):

    def __init__(self, name: str, room_BaseState: "room_RefinedState" = None, room_BaseState196: "room_StateTerminal" = None, room_BaseState203: "room_SubStateTrPointTerminal" = None):
        self.name = name
        self.room_BaseState = room_BaseState
        self.room_BaseState196 = room_BaseState196
        self.room_BaseState203 = room_BaseState203
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_BaseState203(self):
        return self.__room_BaseState203

    @room_BaseState203.setter
    def room_BaseState203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_BaseState__room_BaseState203", None)
        self.__room_BaseState203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SubStateTrPointTerminal202"):
                opp_val = getattr(old_value, "room_SubStateTrPointTerminal202", None)
                if opp_val == self:
                    setattr(old_value, "room_SubStateTrPointTerminal202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SubStateTrPointTerminal202"):
                opp_val = getattr(value, "room_SubStateTrPointTerminal202", None)
                setattr(value, "room_SubStateTrPointTerminal202", self)

    @property
    def room_BaseState(self):
        return self.__room_BaseState

    @room_BaseState.setter
    def room_BaseState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_BaseState__room_BaseState", None)
        self.__room_BaseState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RefinedState"):
                opp_val = getattr(old_value, "room_RefinedState", None)
                if opp_val == self:
                    setattr(old_value, "room_RefinedState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RefinedState"):
                opp_val = getattr(value, "room_RefinedState", None)
                setattr(value, "room_RefinedState", self)

    @property
    def room_BaseState196(self):
        return self.__room_BaseState196

    @room_BaseState196.setter
    def room_BaseState196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_BaseState__room_BaseState196", None)
        self.__room_BaseState196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateTerminal"):
                opp_val = getattr(old_value, "room_StateTerminal", None)
                if opp_val == self:
                    setattr(old_value, "room_StateTerminal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateTerminal"):
                opp_val = getattr(value, "room_StateTerminal", None)
                setattr(value, "room_StateTerminal", self)

class NonInitialTransition:

    pass
class room_TriggeredTransition(NonInitialTransition):

    pass
class room_CPBranchTransition(NonInitialTransition):

    pass
class room_ContinuationTransition(NonInitialTransition):

    pass
class Transition:

    pass
class room_InitialTransition(Transition):

    pass
class room_NonInitialTransition(Transition):

    pass
class StateGraphNode:

    pass
class room_ChoicePoint(StateGraphNode):

    def __init__(self, name: str, room_ChoicePoint: "room_StateGraph" = None, room_ChoicePoint205: "room_ChoicepointTerminal" = None):
        self.name = name
        self.room_ChoicePoint = room_ChoicePoint
        self.room_ChoicePoint205 = room_ChoicePoint205
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_ChoicePoint(self):
        return self.__room_ChoicePoint

    @room_ChoicePoint.setter
    def room_ChoicePoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ChoicePoint__room_ChoicePoint", None)
        self.__room_ChoicePoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph181"):
                opp_val = getattr(old_value, "room_StateGraph181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph181"):
                opp_val = getattr(value, "room_StateGraph181", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_ChoicePoint205(self):
        return self.__room_ChoicePoint205

    @room_ChoicePoint205.setter
    def room_ChoicePoint205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ChoicePoint__room_ChoicePoint205", None)
        self.__room_ChoicePoint205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ChoicepointTerminal"):
                opp_val = getattr(old_value, "room_ChoicepointTerminal", None)
                if opp_val == self:
                    setattr(old_value, "room_ChoicepointTerminal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ChoicepointTerminal"):
                opp_val = getattr(value, "room_ChoicepointTerminal", None)
                setattr(value, "room_ChoicepointTerminal", self)

class room_TrPoint(StateGraphNode):

    def __init__(self, name: str, room_TrPoint: "room_StateGraph" = None, room_TrPoint198: "room_TrPointTerminal" = None, room_TrPoint200: "room_SubStateTrPointTerminal" = None):
        self.name = name
        self.room_TrPoint = room_TrPoint
        self.room_TrPoint198 = room_TrPoint198
        self.room_TrPoint200 = room_TrPoint200
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_TrPoint(self):
        return self.__room_TrPoint

    @room_TrPoint.setter
    def room_TrPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_TrPoint__room_TrPoint", None)
        self.__room_TrPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph179"):
                opp_val = getattr(old_value, "room_StateGraph179", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph179"):
                opp_val = getattr(value, "room_StateGraph179", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph179", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_TrPoint200(self):
        return self.__room_TrPoint200

    @room_TrPoint200.setter
    def room_TrPoint200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_TrPoint__room_TrPoint200", None)
        self.__room_TrPoint200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SubStateTrPointTerminal"):
                opp_val = getattr(old_value, "room_SubStateTrPointTerminal", None)
                if opp_val == self:
                    setattr(old_value, "room_SubStateTrPointTerminal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SubStateTrPointTerminal"):
                opp_val = getattr(value, "room_SubStateTrPointTerminal", None)
                setattr(value, "room_SubStateTrPointTerminal", self)

    @property
    def room_TrPoint198(self):
        return self.__room_TrPoint198

    @room_TrPoint198.setter
    def room_TrPoint198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_TrPoint__room_TrPoint198", None)
        self.__room_TrPoint198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_TrPointTerminal"):
                opp_val = getattr(old_value, "room_TrPointTerminal", None)
                if opp_val == self:
                    setattr(old_value, "room_TrPointTerminal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_TrPointTerminal"):
                opp_val = getattr(value, "room_TrPointTerminal", None)
                setattr(value, "room_TrPointTerminal", self)

class room_State(StateGraphNode):

    def __init__(self, room_State: "room_DetailCode" = None, room_State170: "room_DetailCode" = None, room_State173: "room_StateGraph" = None, room_State177: "room_StateGraph" = None):
        self.room_State = room_State
        self.room_State170 = room_State170
        self.room_State173 = room_State173
        self.room_State177 = room_State177
        
    @property
    def room_State173(self):
        return self.__room_State173

    @room_State173.setter
    def room_State173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State173", None)
        self.__room_State173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph174"):
                opp_val = getattr(old_value, "room_StateGraph174", None)
                if opp_val == self:
                    setattr(old_value, "room_StateGraph174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph174"):
                opp_val = getattr(value, "room_StateGraph174", None)
                setattr(value, "room_StateGraph174", self)

    @property
    def room_State170(self):
        return self.__room_State170

    @room_State170.setter
    def room_State170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State170", None)
        self.__room_State170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode171"):
                opp_val = getattr(old_value, "room_DetailCode171", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode171"):
                opp_val = getattr(value, "room_DetailCode171", None)
                setattr(value, "room_DetailCode171", self)

    @property
    def room_State177(self):
        return self.__room_State177

    @room_State177.setter
    def room_State177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State177", None)
        self.__room_State177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph176"):
                opp_val = getattr(old_value, "room_StateGraph176", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph176"):
                opp_val = getattr(value, "room_StateGraph176", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph176", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_State(self):
        return self.__room_State

    @room_State.setter
    def room_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State", None)
        self.__room_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode168"):
                opp_val = getattr(old_value, "room_DetailCode168", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode168"):
                opp_val = getattr(value, "room_DetailCode168", None)
                setattr(value, "room_DetailCode168", self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class room_StateGraphItem:

    pass
class StateGraphItem:

    pass
class room_Transition(StateGraphItem):

    def __init__(self, name: str, room_Transition188: "room_DetailCode" = None, room_Transition: "room_StateGraph" = None, room_Transition186: "room_TransitionTerminal" = None):
        self.name = name
        self.room_Transition188 = room_Transition188
        self.room_Transition = room_Transition
        self.room_Transition186 = room_Transition186
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_Transition188(self):
        return self.__room_Transition188

    @room_Transition188.setter
    def room_Transition188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Transition__room_Transition188", None)
        self.__room_Transition188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode189"):
                opp_val = getattr(old_value, "room_DetailCode189", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode189"):
                opp_val = getattr(value, "room_DetailCode189", None)
                setattr(value, "room_DetailCode189", self)

    @property
    def room_Transition(self):
        return self.__room_Transition

    @room_Transition.setter
    def room_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Transition__room_Transition", None)
        self.__room_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph183"):
                opp_val = getattr(old_value, "room_StateGraph183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph183"):
                opp_val = getattr(value, "room_StateGraph183", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Transition186(self):
        return self.__room_Transition186

    @room_Transition186.setter
    def room_Transition186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Transition__room_Transition186", None)
        self.__room_Transition186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_TransitionTerminal"):
                opp_val = getattr(old_value, "room_TransitionTerminal", None)
                if opp_val == self:
                    setattr(old_value, "room_TransitionTerminal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_TransitionTerminal"):
                opp_val = getattr(value, "room_TransitionTerminal", None)
                setattr(value, "room_TransitionTerminal", self)

class room_StateGraphNode(StateGraphItem):

    pass
class SAPoint:

    pass
class room_RelaySAPoint(SAPoint):

    pass
class room_RefSAPoint(SAPoint):

    pass
class room_SPPoint:

    pass
class room_SAPoint:

    pass
class room_LogicalThread:

    def __init__(self, name: str, room_LogicalThread139: set["room_ActorInstancePath"] = None, room_LogicalThread: "room_SubSystemClass" = None):
        self.name = name
        self.room_LogicalThread139 = room_LogicalThread139 if room_LogicalThread139 is not None else set()
        self.room_LogicalThread = room_LogicalThread
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_LogicalThread(self):
        return self.__room_LogicalThread

    @room_LogicalThread.setter
    def room_LogicalThread(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_LogicalThread__room_LogicalThread", None)
        self.__room_LogicalThread = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SubSystemClass137"):
                opp_val = getattr(old_value, "room_SubSystemClass137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SubSystemClass137"):
                opp_val = getattr(value, "room_SubSystemClass137", None)
                if opp_val is None:
                    setattr(value, "room_SubSystemClass137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_LogicalThread139(self):
        return self.__room_LogicalThread139

    @room_LogicalThread139.setter
    def room_LogicalThread139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_LogicalThread__room_LogicalThread139", None)
        self.__room_LogicalThread139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_ActorInstancePath"):
                    opp_val = getattr(item, "room_ActorInstancePath", None)
                    
                    if opp_val == self:
                        setattr(item, "room_ActorInstancePath", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_ActorInstancePath"):
                    opp_val = getattr(item, "room_ActorInstancePath", None)
                    
                    setattr(item, "room_ActorInstancePath", self)
                    

class ActorContainerRef:

    pass
class room_ActorContainerRef:

    def __init__(self, name: str, room_ActorContainerRef: "room_BindingEndPoint" = None, room_ActorContainerRef155: "room_RefSAPoint" = None, room_ActorContainerRef160: "room_SPPoint" = None):
        self.name = name
        self.room_ActorContainerRef = room_ActorContainerRef
        self.room_ActorContainerRef155 = room_ActorContainerRef155
        self.room_ActorContainerRef160 = room_ActorContainerRef160
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_ActorContainerRef(self):
        return self.__room_ActorContainerRef

    @room_ActorContainerRef.setter
    def room_ActorContainerRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorContainerRef__room_ActorContainerRef", None)
        self.__room_ActorContainerRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_BindingEndPoint146"):
                opp_val = getattr(old_value, "room_BindingEndPoint146", None)
                if opp_val == self:
                    setattr(old_value, "room_BindingEndPoint146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_BindingEndPoint146"):
                opp_val = getattr(value, "room_BindingEndPoint146", None)
                setattr(value, "room_BindingEndPoint146", self)

    @property
    def room_ActorContainerRef155(self):
        return self.__room_ActorContainerRef155

    @room_ActorContainerRef155.setter
    def room_ActorContainerRef155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorContainerRef__room_ActorContainerRef155", None)
        self.__room_ActorContainerRef155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RefSAPoint"):
                opp_val = getattr(old_value, "room_RefSAPoint", None)
                if opp_val == self:
                    setattr(old_value, "room_RefSAPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RefSAPoint"):
                opp_val = getattr(value, "room_RefSAPoint", None)
                setattr(value, "room_RefSAPoint", self)

    @property
    def room_ActorContainerRef160(self):
        return self.__room_ActorContainerRef160

    @room_ActorContainerRef160.setter
    def room_ActorContainerRef160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorContainerRef__room_ActorContainerRef160", None)
        self.__room_ActorContainerRef160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SPPoint159"):
                opp_val = getattr(old_value, "room_SPPoint159", None)
                if opp_val == self:
                    setattr(old_value, "room_SPPoint159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SPPoint159"):
                opp_val = getattr(value, "room_SPPoint159", None)
                setattr(value, "room_SPPoint159", self)

class room_SubSystemRef(ActorContainerRef):

    pass
class room_BindingEndPoint:

    pass
class room_ActorInstancePath:

    def __init__(self, segments: str, room_ActorInstancePath: "room_LogicalThread" = None):
        self.segments = segments
        self.room_ActorInstancePath = room_ActorInstancePath
        
    @property
    def segments(self) -> str:
        return self.__segments

    @segments.setter
    def segments(self, segments: str):
        self.__segments = segments

    @property
    def room_ActorInstancePath(self):
        return self.__room_ActorInstancePath

    @room_ActorInstancePath.setter
    def room_ActorInstancePath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorInstancePath__room_ActorInstancePath", None)
        self.__room_ActorInstancePath = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_LogicalThread139"):
                opp_val = getattr(old_value, "room_LogicalThread139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_LogicalThread139"):
                opp_val = getattr(value, "room_LogicalThread139", None)
                if opp_val is None:
                    setattr(value, "room_LogicalThread139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class InterfaceItem:

    pass
class room_InterfaceItem:

    def __init__(self, name: str, room_InterfaceItem: "room_ProtocolClass" = None, room_InterfaceItem215: "room_MessageFromIf" = None):
        self.name = name
        self.room_InterfaceItem = room_InterfaceItem
        self.room_InterfaceItem215 = room_InterfaceItem215
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_InterfaceItem(self):
        return self.__room_InterfaceItem

    @room_InterfaceItem.setter
    def room_InterfaceItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_InterfaceItem__room_InterfaceItem", None)
        self.__room_InterfaceItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass121"):
                opp_val = getattr(old_value, "room_ProtocolClass121", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass121"):
                opp_val = getattr(value, "room_ProtocolClass121", None)
                setattr(value, "room_ProtocolClass121", self)

    @property
    def room_InterfaceItem215(self):
        return self.__room_InterfaceItem215

    @room_InterfaceItem215.setter
    def room_InterfaceItem215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_InterfaceItem__room_InterfaceItem215", None)
        self.__room_InterfaceItem215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageFromIf214"):
                opp_val = getattr(old_value, "room_MessageFromIf214", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageFromIf214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageFromIf214"):
                opp_val = getattr(value, "room_MessageFromIf214", None)
                setattr(value, "room_MessageFromIf214", self)

class room_StateGraph:

    pass
class room_SAPRef(InterfaceItem):

    pass
class room_Port(InterfaceItem):

    def __init__(self, conjugated: bool, multiplicity: int, room_Port105: "room_ActorClass" = None, room_Port: "room_ActorClass" = None, room_Port124: "room_ExternalPort" = None, room_Port135: "room_SubSystemClass" = None, room_Port149: "room_BindingEndPoint" = None):
        self.conjugated = conjugated
        self.multiplicity = multiplicity
        self.room_Port105 = room_Port105
        self.room_Port = room_Port
        self.room_Port124 = room_Port124
        self.room_Port135 = room_Port135
        self.room_Port149 = room_Port149
        
    @property
    def multiplicity(self) -> int:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: int):
        self.__multiplicity = multiplicity

    @property
    def conjugated(self) -> bool:
        return self.__conjugated

    @conjugated.setter
    def conjugated(self, conjugated: bool):
        self.__conjugated = conjugated

    @property
    def room_Port124(self):
        return self.__room_Port124

    @room_Port124.setter
    def room_Port124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port124", None)
        self.__room_Port124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ExternalPort123"):
                opp_val = getattr(old_value, "room_ExternalPort123", None)
                if opp_val == self:
                    setattr(old_value, "room_ExternalPort123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ExternalPort123"):
                opp_val = getattr(value, "room_ExternalPort123", None)
                setattr(value, "room_ExternalPort123", self)

    @property
    def room_Port105(self):
        return self.__room_Port105

    @room_Port105.setter
    def room_Port105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port105", None)
        self.__room_Port105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass104"):
                opp_val = getattr(old_value, "room_ActorClass104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass104"):
                opp_val = getattr(value, "room_ActorClass104", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Port135(self):
        return self.__room_Port135

    @room_Port135.setter
    def room_Port135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port135", None)
        self.__room_Port135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SubSystemClass134"):
                opp_val = getattr(old_value, "room_SubSystemClass134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SubSystemClass134"):
                opp_val = getattr(value, "room_SubSystemClass134", None)
                if opp_val is None:
                    setattr(value, "room_SubSystemClass134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Port(self):
        return self.__room_Port

    @room_Port.setter
    def room_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port", None)
        self.__room_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass96"):
                opp_val = getattr(old_value, "room_ActorClass96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass96"):
                opp_val = getattr(value, "room_ActorClass96", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Port149(self):
        return self.__room_Port149

    @room_Port149.setter
    def room_Port149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port149", None)
        self.__room_Port149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_BindingEndPoint148"):
                opp_val = getattr(old_value, "room_BindingEndPoint148", None)
                if opp_val == self:
                    setattr(old_value, "room_BindingEndPoint148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_BindingEndPoint148"):
                opp_val = getattr(value, "room_BindingEndPoint148", None)
                setattr(value, "room_BindingEndPoint148", self)

class ActorContainerClass:

    pass
class SemanticsRule:

    pass
class room_SemanticsOutRule(SemanticsRule):

    pass
class room_SemanticsInRule(SemanticsRule):

    pass
class room_SemanticsRule:

    pass
class room_ServiceImplementation:

    pass
class room_ExternalPort:

    pass
class room_ProtocolSemantics:

    pass
class room_PortClass:

    pass
class room_Message:

    def __init__(self, name: str, room_Message65: set["room_TypedID"] = None, room_Message: "room_ProtocolClass" = None, room_Message56: "room_ProtocolClass" = None, room_Message80: "room_MessageHandler" = None, room_Message88: "room_SemanticsRule" = None, room_Message212: "room_MessageFromIf" = None):
        self.name = name
        self.room_Message65 = room_Message65 if room_Message65 is not None else set()
        self.room_Message = room_Message
        self.room_Message56 = room_Message56
        self.room_Message80 = room_Message80
        self.room_Message88 = room_Message88
        self.room_Message212 = room_Message212
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_Message65(self):
        return self.__room_Message65

    @room_Message65.setter
    def room_Message65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message65", None)
        self.__room_Message65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_TypedID66"):
                    opp_val = getattr(item, "room_TypedID66", None)
                    
                    if opp_val == self:
                        setattr(item, "room_TypedID66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_TypedID66"):
                    opp_val = getattr(item, "room_TypedID66", None)
                    
                    setattr(item, "room_TypedID66", self)
                    

    @property
    def room_Message212(self):
        return self.__room_Message212

    @room_Message212.setter
    def room_Message212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message212", None)
        self.__room_Message212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageFromIf211"):
                opp_val = getattr(old_value, "room_MessageFromIf211", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageFromIf211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageFromIf211"):
                opp_val = getattr(value, "room_MessageFromIf211", None)
                setattr(value, "room_MessageFromIf211", self)

    @property
    def room_Message56(self):
        return self.__room_Message56

    @room_Message56.setter
    def room_Message56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message56", None)
        self.__room_Message56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass55"):
                opp_val = getattr(old_value, "room_ProtocolClass55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass55"):
                opp_val = getattr(value, "room_ProtocolClass55", None)
                if opp_val is None:
                    setattr(value, "room_ProtocolClass55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Message(self):
        return self.__room_Message

    @room_Message.setter
    def room_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message", None)
        self.__room_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass53"):
                opp_val = getattr(old_value, "room_ProtocolClass53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass53"):
                opp_val = getattr(value, "room_ProtocolClass53", None)
                if opp_val is None:
                    setattr(value, "room_ProtocolClass53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Message80(self):
        return self.__room_Message80

    @room_Message80.setter
    def room_Message80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message80", None)
        self.__room_Message80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageHandler79"):
                opp_val = getattr(old_value, "room_MessageHandler79", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageHandler79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageHandler79"):
                opp_val = getattr(value, "room_MessageHandler79", None)
                setattr(value, "room_MessageHandler79", self)

    @property
    def room_Message88(self):
        return self.__room_Message88

    @room_Message88.setter
    def room_Message88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message88", None)
        self.__room_Message88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SemanticsRule87"):
                opp_val = getattr(old_value, "room_SemanticsRule87", None)
                if opp_val == self:
                    setattr(old_value, "room_SemanticsRule87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SemanticsRule87"):
                opp_val = getattr(value, "room_SemanticsRule87", None)
                setattr(value, "room_SemanticsRule87", self)

class room_DetailCode:

    def __init__(self, commands: str, room_DetailCode69: "room_PortClass" = None, room_DetailCode: "room_Operation" = None, room_DetailCode48: "room_ProtocolClass" = None, room_DetailCode51: "room_ProtocolClass" = None, room_DetailCode83: "room_MessageHandler" = None, room_DetailCode99: "room_ActorClass" = None, room_DetailCode102: "room_ActorClass" = None, room_DetailCode171: "room_State" = None, room_DetailCode168: "room_State" = None, room_DetailCode189: "room_Transition" = None, room_DetailCode218: "room_Guard" = None, room_DetailCode194: "room_CPBranchTransition" = None):
        self.commands = commands
        self.room_DetailCode69 = room_DetailCode69
        self.room_DetailCode = room_DetailCode
        self.room_DetailCode48 = room_DetailCode48
        self.room_DetailCode51 = room_DetailCode51
        self.room_DetailCode83 = room_DetailCode83
        self.room_DetailCode99 = room_DetailCode99
        self.room_DetailCode102 = room_DetailCode102
        self.room_DetailCode171 = room_DetailCode171
        self.room_DetailCode168 = room_DetailCode168
        self.room_DetailCode189 = room_DetailCode189
        self.room_DetailCode218 = room_DetailCode218
        self.room_DetailCode194 = room_DetailCode194
        
    @property
    def commands(self) -> str:
        return self.__commands

    @commands.setter
    def commands(self, commands: str):
        self.__commands = commands

    @property
    def room_DetailCode99(self):
        return self.__room_DetailCode99

    @room_DetailCode99.setter
    def room_DetailCode99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode99", None)
        self.__room_DetailCode99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass98"):
                opp_val = getattr(old_value, "room_ActorClass98", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass98"):
                opp_val = getattr(value, "room_ActorClass98", None)
                setattr(value, "room_ActorClass98", self)

    @property
    def room_DetailCode194(self):
        return self.__room_DetailCode194

    @room_DetailCode194.setter
    def room_DetailCode194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode194", None)
        self.__room_DetailCode194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_CPBranchTransition"):
                opp_val = getattr(old_value, "room_CPBranchTransition", None)
                if opp_val == self:
                    setattr(old_value, "room_CPBranchTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_CPBranchTransition"):
                opp_val = getattr(value, "room_CPBranchTransition", None)
                setattr(value, "room_CPBranchTransition", self)

    @property
    def room_DetailCode69(self):
        return self.__room_DetailCode69

    @room_DetailCode69.setter
    def room_DetailCode69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode69", None)
        self.__room_DetailCode69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_PortClass68"):
                opp_val = getattr(old_value, "room_PortClass68", None)
                if opp_val == self:
                    setattr(old_value, "room_PortClass68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortClass68"):
                opp_val = getattr(value, "room_PortClass68", None)
                setattr(value, "room_PortClass68", self)

    @property
    def room_DetailCode218(self):
        return self.__room_DetailCode218

    @room_DetailCode218.setter
    def room_DetailCode218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode218", None)
        self.__room_DetailCode218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Guard217"):
                opp_val = getattr(old_value, "room_Guard217", None)
                if opp_val == self:
                    setattr(old_value, "room_Guard217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Guard217"):
                opp_val = getattr(value, "room_Guard217", None)
                setattr(value, "room_Guard217", self)

    @property
    def room_DetailCode189(self):
        return self.__room_DetailCode189

    @room_DetailCode189.setter
    def room_DetailCode189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode189", None)
        self.__room_DetailCode189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Transition188"):
                opp_val = getattr(old_value, "room_Transition188", None)
                if opp_val == self:
                    setattr(old_value, "room_Transition188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Transition188"):
                opp_val = getattr(value, "room_Transition188", None)
                setattr(value, "room_Transition188", self)

    @property
    def room_DetailCode48(self):
        return self.__room_DetailCode48

    @room_DetailCode48.setter
    def room_DetailCode48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode48", None)
        self.__room_DetailCode48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass47"):
                opp_val = getattr(old_value, "room_ProtocolClass47", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass47"):
                opp_val = getattr(value, "room_ProtocolClass47", None)
                setattr(value, "room_ProtocolClass47", self)

    @property
    def room_DetailCode83(self):
        return self.__room_DetailCode83

    @room_DetailCode83.setter
    def room_DetailCode83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode83", None)
        self.__room_DetailCode83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageHandler82"):
                opp_val = getattr(old_value, "room_MessageHandler82", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageHandler82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageHandler82"):
                opp_val = getattr(value, "room_MessageHandler82", None)
                setattr(value, "room_MessageHandler82", self)

    @property
    def room_DetailCode102(self):
        return self.__room_DetailCode102

    @room_DetailCode102.setter
    def room_DetailCode102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode102", None)
        self.__room_DetailCode102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass101"):
                opp_val = getattr(old_value, "room_ActorClass101", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass101"):
                opp_val = getattr(value, "room_ActorClass101", None)
                setattr(value, "room_ActorClass101", self)

    @property
    def room_DetailCode51(self):
        return self.__room_DetailCode51

    @room_DetailCode51.setter
    def room_DetailCode51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode51", None)
        self.__room_DetailCode51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass50"):
                opp_val = getattr(old_value, "room_ProtocolClass50", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass50"):
                opp_val = getattr(value, "room_ProtocolClass50", None)
                setattr(value, "room_ProtocolClass50", self)

    @property
    def room_DetailCode171(self):
        return self.__room_DetailCode171

    @room_DetailCode171.setter
    def room_DetailCode171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode171", None)
        self.__room_DetailCode171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_State170"):
                opp_val = getattr(old_value, "room_State170", None)
                if opp_val == self:
                    setattr(old_value, "room_State170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_State170"):
                opp_val = getattr(value, "room_State170", None)
                setattr(value, "room_State170", self)

    @property
    def room_DetailCode(self):
        return self.__room_DetailCode

    @room_DetailCode.setter
    def room_DetailCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode", None)
        self.__room_DetailCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Operation42"):
                opp_val = getattr(old_value, "room_Operation42", None)
                if opp_val == self:
                    setattr(old_value, "room_Operation42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Operation42"):
                opp_val = getattr(value, "room_Operation42", None)
                setattr(value, "room_Operation42", self)

    @property
    def room_DetailCode168(self):
        return self.__room_DetailCode168

    @room_DetailCode168.setter
    def room_DetailCode168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode168", None)
        self.__room_DetailCode168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_State"):
                opp_val = getattr(old_value, "room_State", None)
                if opp_val == self:
                    setattr(old_value, "room_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_State"):
                opp_val = getattr(value, "room_State", None)
                setattr(value, "room_State", self)

class room_MessageHandler:

    pass
class room_FreeType:

    def __init__(self, prim: str, type: str, room_FreeType: "room_FreeTypedID" = None, room_FreeType40: "room_Operation" = None):
        self.prim = prim
        self.type = type
        self.room_FreeType = room_FreeType
        self.room_FreeType40 = room_FreeType40
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def prim(self) -> str:
        return self.__prim

    @prim.setter
    def prim(self, prim: str):
        self.__prim = prim

    @property
    def room_FreeType40(self):
        return self.__room_FreeType40

    @room_FreeType40.setter
    def room_FreeType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_FreeType__room_FreeType40", None)
        self.__room_FreeType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Operation39"):
                opp_val = getattr(old_value, "room_Operation39", None)
                if opp_val == self:
                    setattr(old_value, "room_Operation39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Operation39"):
                opp_val = getattr(value, "room_Operation39", None)
                setattr(value, "room_Operation39", self)

    @property
    def room_FreeType(self):
        return self.__room_FreeType

    @room_FreeType.setter
    def room_FreeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_FreeType__room_FreeType", None)
        self.__room_FreeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_FreeTypedID"):
                opp_val = getattr(old_value, "room_FreeTypedID", None)
                if opp_val == self:
                    setattr(old_value, "room_FreeTypedID", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_FreeTypedID"):
                opp_val = getattr(value, "room_FreeTypedID", None)
                setattr(value, "room_FreeTypedID", self)

class room_FreeTypedID:

    def __init__(self, name: str, room_FreeTypedID: "room_FreeType" = None, room_FreeTypedID37: "room_Operation" = None):
        self.name = name
        self.room_FreeTypedID = room_FreeTypedID
        self.room_FreeTypedID37 = room_FreeTypedID37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_FreeTypedID37(self):
        return self.__room_FreeTypedID37

    @room_FreeTypedID37.setter
    def room_FreeTypedID37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_FreeTypedID__room_FreeTypedID37", None)
        self.__room_FreeTypedID37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Operation36"):
                opp_val = getattr(old_value, "room_Operation36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Operation36"):
                opp_val = getattr(value, "room_Operation36", None)
                if opp_val is None:
                    setattr(value, "room_Operation36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_FreeTypedID(self):
        return self.__room_FreeTypedID

    @room_FreeTypedID.setter
    def room_FreeTypedID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_FreeTypedID__room_FreeTypedID", None)
        self.__room_FreeTypedID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_FreeType"):
                opp_val = getattr(old_value, "room_FreeType", None)
                if opp_val == self:
                    setattr(old_value, "room_FreeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_FreeType"):
                opp_val = getattr(value, "room_FreeType", None)
                setattr(value, "room_FreeType", self)

class room_Type:

    def __init__(self, prim: str, room_Type: "room_TypedID" = None, room_Type20: "room_DataClass" = None, room_Type34: "room_Attribute" = None):
        self.prim = prim
        self.room_Type = room_Type
        self.room_Type20 = room_Type20
        self.room_Type34 = room_Type34
        
    @property
    def prim(self) -> str:
        return self.__prim

    @prim.setter
    def prim(self, prim: str):
        self.__prim = prim

    @property
    def room_Type34(self):
        return self.__room_Type34

    @room_Type34.setter
    def room_Type34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Type__room_Type34", None)
        self.__room_Type34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Attribute33"):
                opp_val = getattr(old_value, "room_Attribute33", None)
                if opp_val == self:
                    setattr(old_value, "room_Attribute33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Attribute33"):
                opp_val = getattr(value, "room_Attribute33", None)
                setattr(value, "room_Attribute33", self)

    @property
    def room_Type20(self):
        return self.__room_Type20

    @room_Type20.setter
    def room_Type20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Type__room_Type20", None)
        self.__room_Type20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass21"):
                opp_val = getattr(old_value, "room_DataClass21", None)
                if opp_val == self:
                    setattr(old_value, "room_DataClass21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass21"):
                opp_val = getattr(value, "room_DataClass21", None)
                setattr(value, "room_DataClass21", self)

    @property
    def room_Type(self):
        return self.__room_Type

    @room_Type.setter
    def room_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Type__room_Type", None)
        self.__room_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_TypedID"):
                opp_val = getattr(old_value, "room_TypedID", None)
                if opp_val == self:
                    setattr(old_value, "room_TypedID", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_TypedID"):
                opp_val = getattr(value, "room_TypedID", None)
                setattr(value, "room_TypedID", self)

class room_TypedID:

    def __init__(self, name: str, room_TypedID: "room_Type" = None, room_TypedID66: "room_Message" = None):
        self.name = name
        self.room_TypedID = room_TypedID
        self.room_TypedID66 = room_TypedID66
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_TypedID(self):
        return self.__room_TypedID

    @room_TypedID.setter
    def room_TypedID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_TypedID__room_TypedID", None)
        self.__room_TypedID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Type"):
                opp_val = getattr(old_value, "room_Type", None)
                if opp_val == self:
                    setattr(old_value, "room_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Type"):
                opp_val = getattr(value, "room_Type", None)
                setattr(value, "room_Type", self)

    @property
    def room_TypedID66(self):
        return self.__room_TypedID66

    @room_TypedID66.setter
    def room_TypedID66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_TypedID__room_TypedID66", None)
        self.__room_TypedID66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Message65"):
                opp_val = getattr(old_value, "room_Message65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Message65"):
                opp_val = getattr(value, "room_Message65", None)
                if opp_val is None:
                    setattr(value, "room_Message65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_ActorRef(ActorContainerRef):

    pass
class room_SPPRef(InterfaceItem):

    pass
class StructureClass:

    pass
class room_ActorContainerClass(StructureClass):

    pass
class room_LayerConnection:

    pass
class room_Binding:

    pass
class room_Operation:

    def __init__(self, name: str, room_Operation: "room_DataClass" = None, room_Operation75: "room_PortClass" = None, room_Operation36: set["room_FreeTypedID"] = None, room_Operation39: "room_FreeType" = None, room_Operation42: "room_DetailCode" = None, room_Operation117: "room_ActorClass" = None):
        self.name = name
        self.room_Operation = room_Operation
        self.room_Operation75 = room_Operation75
        self.room_Operation36 = room_Operation36 if room_Operation36 is not None else set()
        self.room_Operation39 = room_Operation39
        self.room_Operation42 = room_Operation42
        self.room_Operation117 = room_Operation117
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_Operation36(self):
        return self.__room_Operation36

    @room_Operation36.setter
    def room_Operation36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation36", None)
        self.__room_Operation36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_FreeTypedID37"):
                    opp_val = getattr(item, "room_FreeTypedID37", None)
                    
                    if opp_val == self:
                        setattr(item, "room_FreeTypedID37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_FreeTypedID37"):
                    opp_val = getattr(item, "room_FreeTypedID37", None)
                    
                    setattr(item, "room_FreeTypedID37", self)
                    

    @property
    def room_Operation42(self):
        return self.__room_Operation42

    @room_Operation42.setter
    def room_Operation42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation42", None)
        self.__room_Operation42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode"):
                opp_val = getattr(old_value, "room_DetailCode", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode"):
                opp_val = getattr(value, "room_DetailCode", None)
                setattr(value, "room_DetailCode", self)

    @property
    def room_Operation75(self):
        return self.__room_Operation75

    @room_Operation75.setter
    def room_Operation75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation75", None)
        self.__room_Operation75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_PortClass74"):
                opp_val = getattr(old_value, "room_PortClass74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortClass74"):
                opp_val = getattr(value, "room_PortClass74", None)
                if opp_val is None:
                    setattr(value, "room_PortClass74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Operation39(self):
        return self.__room_Operation39

    @room_Operation39.setter
    def room_Operation39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation39", None)
        self.__room_Operation39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_FreeType40"):
                opp_val = getattr(old_value, "room_FreeType40", None)
                if opp_val == self:
                    setattr(old_value, "room_FreeType40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_FreeType40"):
                opp_val = getattr(value, "room_FreeType40", None)
                setattr(value, "room_FreeType40", self)

    @property
    def room_Operation(self):
        return self.__room_Operation

    @room_Operation.setter
    def room_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation", None)
        self.__room_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass31"):
                opp_val = getattr(old_value, "room_DataClass31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass31"):
                opp_val = getattr(value, "room_DataClass31", None)
                if opp_val is None:
                    setattr(value, "room_DataClass31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Operation117(self):
        return self.__room_Operation117

    @room_Operation117.setter
    def room_Operation117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation117", None)
        self.__room_Operation117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass116"):
                opp_val = getattr(old_value, "room_ActorClass116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass116"):
                opp_val = getattr(value, "room_ActorClass116", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_Attribute:

    def __init__(self, name: str, size: int, room_Attribute: "room_DataClass" = None, room_Attribute72: "room_PortClass" = None, room_Attribute33: "room_Type" = None, room_Attribute114: "room_ActorClass" = None):
        self.name = name
        self.size = size
        self.room_Attribute = room_Attribute
        self.room_Attribute72 = room_Attribute72
        self.room_Attribute33 = room_Attribute33
        self.room_Attribute114 = room_Attribute114
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def room_Attribute33(self):
        return self.__room_Attribute33

    @room_Attribute33.setter
    def room_Attribute33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute33", None)
        self.__room_Attribute33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Type34"):
                opp_val = getattr(old_value, "room_Type34", None)
                if opp_val == self:
                    setattr(old_value, "room_Type34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Type34"):
                opp_val = getattr(value, "room_Type34", None)
                setattr(value, "room_Type34", self)

    @property
    def room_Attribute114(self):
        return self.__room_Attribute114

    @room_Attribute114.setter
    def room_Attribute114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute114", None)
        self.__room_Attribute114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass113"):
                opp_val = getattr(old_value, "room_ActorClass113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass113"):
                opp_val = getattr(value, "room_ActorClass113", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Attribute(self):
        return self.__room_Attribute

    @room_Attribute.setter
    def room_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute", None)
        self.__room_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass29"):
                opp_val = getattr(old_value, "room_DataClass29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass29"):
                opp_val = getattr(value, "room_DataClass29", None)
                if opp_val is None:
                    setattr(value, "room_DataClass29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Attribute72(self):
        return self.__room_Attribute72

    @room_Attribute72.setter
    def room_Attribute72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute72", None)
        self.__room_Attribute72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_PortClass71"):
                opp_val = getattr(old_value, "room_PortClass71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortClass71"):
                opp_val = getattr(value, "room_PortClass71", None)
                if opp_val is None:
                    setattr(value, "room_PortClass71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_SubSystemClass(ActorContainerClass):

    pass
class room_ActorClass(ActorContainerClass):

    def __init__(self, abstract: bool, room_ActorClass: "room_RoomModel" = None, room_ActorClass104: set["room_Port"] = None, room_ActorClass107: set["room_ExternalPort"] = None, room_ActorClass109: set["room_ServiceImplementation"] = None, room_ActorClass94: "room_ActorClass" = None, room_ActorClass92: "room_ActorClass" = None, room_ActorClass96: set["room_Port"] = None, room_ActorClass98: "room_DetailCode" = None, room_ActorClass101: "room_DetailCode" = None, room_ActorClass111: set["room_SAPRef"] = None, room_ActorClass113: set["room_Attribute"] = None, room_ActorClass116: set["room_Operation"] = None, room_ActorClass119: "room_StateGraph" = None, room_ActorClass166: "room_ActorRef" = None):
        self.abstract = abstract
        self.room_ActorClass = room_ActorClass
        self.room_ActorClass104 = room_ActorClass104 if room_ActorClass104 is not None else set()
        self.room_ActorClass107 = room_ActorClass107 if room_ActorClass107 is not None else set()
        self.room_ActorClass109 = room_ActorClass109 if room_ActorClass109 is not None else set()
        self.room_ActorClass94 = room_ActorClass94
        self.room_ActorClass92 = room_ActorClass92
        self.room_ActorClass96 = room_ActorClass96 if room_ActorClass96 is not None else set()
        self.room_ActorClass98 = room_ActorClass98
        self.room_ActorClass101 = room_ActorClass101
        self.room_ActorClass111 = room_ActorClass111 if room_ActorClass111 is not None else set()
        self.room_ActorClass113 = room_ActorClass113 if room_ActorClass113 is not None else set()
        self.room_ActorClass116 = room_ActorClass116 if room_ActorClass116 is not None else set()
        self.room_ActorClass119 = room_ActorClass119
        self.room_ActorClass166 = room_ActorClass166
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def room_ActorClass98(self):
        return self.__room_ActorClass98

    @room_ActorClass98.setter
    def room_ActorClass98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass98", None)
        self.__room_ActorClass98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode99"):
                opp_val = getattr(old_value, "room_DetailCode99", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode99"):
                opp_val = getattr(value, "room_DetailCode99", None)
                setattr(value, "room_DetailCode99", self)

    @property
    def room_ActorClass(self):
        return self.__room_ActorClass

    @room_ActorClass.setter
    def room_ActorClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass", None)
        self.__room_ActorClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RoomModel6"):
                opp_val = getattr(old_value, "room_RoomModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RoomModel6"):
                opp_val = getattr(value, "room_RoomModel6", None)
                if opp_val is None:
                    setattr(value, "room_RoomModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_ActorClass109(self):
        return self.__room_ActorClass109

    @room_ActorClass109.setter
    def room_ActorClass109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass109", None)
        self.__room_ActorClass109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_ServiceImplementation"):
                    opp_val = getattr(item, "room_ServiceImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "room_ServiceImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_ServiceImplementation"):
                    opp_val = getattr(item, "room_ServiceImplementation", None)
                    
                    setattr(item, "room_ServiceImplementation", self)
                    

    @property
    def room_ActorClass92(self):
        return self.__room_ActorClass92

    @room_ActorClass92.setter
    def room_ActorClass92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass92", None)
        self.__room_ActorClass92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass94"):
                opp_val = getattr(old_value, "room_ActorClass94", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass94"):
                opp_val = getattr(value, "room_ActorClass94", None)
                setattr(value, "room_ActorClass94", self)

    @property
    def room_ActorClass101(self):
        return self.__room_ActorClass101

    @room_ActorClass101.setter
    def room_ActorClass101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass101", None)
        self.__room_ActorClass101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode102"):
                opp_val = getattr(old_value, "room_DetailCode102", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode102"):
                opp_val = getattr(value, "room_DetailCode102", None)
                setattr(value, "room_DetailCode102", self)

    @property
    def room_ActorClass96(self):
        return self.__room_ActorClass96

    @room_ActorClass96.setter
    def room_ActorClass96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass96", None)
        self.__room_ActorClass96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Port"):
                    opp_val = getattr(item, "room_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Port"):
                    opp_val = getattr(item, "room_Port", None)
                    
                    setattr(item, "room_Port", self)
                    

    @property
    def room_ActorClass119(self):
        return self.__room_ActorClass119

    @room_ActorClass119.setter
    def room_ActorClass119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass119", None)
        self.__room_ActorClass119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph"):
                opp_val = getattr(old_value, "room_StateGraph", None)
                if opp_val == self:
                    setattr(old_value, "room_StateGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph"):
                opp_val = getattr(value, "room_StateGraph", None)
                setattr(value, "room_StateGraph", self)

    @property
    def room_ActorClass113(self):
        return self.__room_ActorClass113

    @room_ActorClass113.setter
    def room_ActorClass113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass113", None)
        self.__room_ActorClass113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Attribute114"):
                    opp_val = getattr(item, "room_Attribute114", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Attribute114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Attribute114"):
                    opp_val = getattr(item, "room_Attribute114", None)
                    
                    setattr(item, "room_Attribute114", self)
                    

    @property
    def room_ActorClass166(self):
        return self.__room_ActorClass166

    @room_ActorClass166.setter
    def room_ActorClass166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass166", None)
        self.__room_ActorClass166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorRef165"):
                opp_val = getattr(old_value, "room_ActorRef165", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorRef165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorRef165"):
                opp_val = getattr(value, "room_ActorRef165", None)
                setattr(value, "room_ActorRef165", self)

    @property
    def room_ActorClass116(self):
        return self.__room_ActorClass116

    @room_ActorClass116.setter
    def room_ActorClass116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass116", None)
        self.__room_ActorClass116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Operation117"):
                    opp_val = getattr(item, "room_Operation117", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Operation117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Operation117"):
                    opp_val = getattr(item, "room_Operation117", None)
                    
                    setattr(item, "room_Operation117", self)
                    

    @property
    def room_ActorClass111(self):
        return self.__room_ActorClass111

    @room_ActorClass111.setter
    def room_ActorClass111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass111", None)
        self.__room_ActorClass111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_SAPRef"):
                    opp_val = getattr(item, "room_SAPRef", None)
                    
                    if opp_val == self:
                        setattr(item, "room_SAPRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_SAPRef"):
                    opp_val = getattr(item, "room_SAPRef", None)
                    
                    setattr(item, "room_SAPRef", self)
                    

    @property
    def room_ActorClass104(self):
        return self.__room_ActorClass104

    @room_ActorClass104.setter
    def room_ActorClass104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass104", None)
        self.__room_ActorClass104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Port105"):
                    opp_val = getattr(item, "room_Port105", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Port105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Port105"):
                    opp_val = getattr(item, "room_Port105", None)
                    
                    setattr(item, "room_Port105", self)
                    

    @property
    def room_ActorClass94(self):
        return self.__room_ActorClass94

    @room_ActorClass94.setter
    def room_ActorClass94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass94", None)
        self.__room_ActorClass94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass92"):
                opp_val = getattr(old_value, "room_ActorClass92", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass92"):
                opp_val = getattr(value, "room_ActorClass92", None)
                setattr(value, "room_ActorClass92", self)

    @property
    def room_ActorClass107(self):
        return self.__room_ActorClass107

    @room_ActorClass107.setter
    def room_ActorClass107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass107", None)
        self.__room_ActorClass107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_ExternalPort"):
                    opp_val = getattr(item, "room_ExternalPort", None)
                    
                    if opp_val == self:
                        setattr(item, "room_ExternalPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_ExternalPort"):
                    opp_val = getattr(item, "room_ExternalPort", None)
                    
                    setattr(item, "room_ExternalPort", self)
                    

class room_Import:

    def __init__(self, importedNamespace: str, room_Import: "room_RoomModel" = None, room_Import27: "room_DataClass" = None):
        self.importedNamespace = importedNamespace
        self.room_Import = room_Import
        self.room_Import27 = room_Import27
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def room_Import(self):
        return self.__room_Import

    @room_Import.setter
    def room_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Import__room_Import", None)
        self.__room_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RoomModel"):
                opp_val = getattr(old_value, "room_RoomModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RoomModel"):
                opp_val = getattr(value, "room_RoomModel", None)
                if opp_val is None:
                    setattr(value, "room_RoomModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Import27(self):
        return self.__room_Import27

    @room_Import27.setter
    def room_Import27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Import__room_Import27", None)
        self.__room_Import27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass26"):
                opp_val = getattr(old_value, "room_DataClass26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass26"):
                opp_val = getattr(value, "room_DataClass26", None)
                if opp_val is None:
                    setattr(value, "room_DataClass26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_RoomModel:

    def __init__(self, name: str, room_RoomModel10: set["room_LogicalSystem"] = None, room_RoomModel: set["room_Import"] = None, room_RoomModel2: set["room_DataClass"] = None, room_RoomModel4: set["room_ProtocolClass"] = None, room_RoomModel6: set["room_ActorClass"] = None, room_RoomModel8: set["room_SubSystemClass"] = None):
        self.name = name
        self.room_RoomModel10 = room_RoomModel10 if room_RoomModel10 is not None else set()
        self.room_RoomModel = room_RoomModel if room_RoomModel is not None else set()
        self.room_RoomModel2 = room_RoomModel2 if room_RoomModel2 is not None else set()
        self.room_RoomModel4 = room_RoomModel4 if room_RoomModel4 is not None else set()
        self.room_RoomModel6 = room_RoomModel6 if room_RoomModel6 is not None else set()
        self.room_RoomModel8 = room_RoomModel8 if room_RoomModel8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_RoomModel10(self):
        return self.__room_RoomModel10

    @room_RoomModel10.setter
    def room_RoomModel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomModel__room_RoomModel10", None)
        self.__room_RoomModel10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_LogicalSystem"):
                    opp_val = getattr(item, "room_LogicalSystem", None)
                    
                    if opp_val == self:
                        setattr(item, "room_LogicalSystem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_LogicalSystem"):
                    opp_val = getattr(item, "room_LogicalSystem", None)
                    
                    setattr(item, "room_LogicalSystem", self)
                    

    @property
    def room_RoomModel2(self):
        return self.__room_RoomModel2

    @room_RoomModel2.setter
    def room_RoomModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomModel__room_RoomModel2", None)
        self.__room_RoomModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_DataClass"):
                    opp_val = getattr(item, "room_DataClass", None)
                    
                    if opp_val == self:
                        setattr(item, "room_DataClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_DataClass"):
                    opp_val = getattr(item, "room_DataClass", None)
                    
                    setattr(item, "room_DataClass", self)
                    

    @property
    def room_RoomModel8(self):
        return self.__room_RoomModel8

    @room_RoomModel8.setter
    def room_RoomModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomModel__room_RoomModel8", None)
        self.__room_RoomModel8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_SubSystemClass"):
                    opp_val = getattr(item, "room_SubSystemClass", None)
                    
                    if opp_val == self:
                        setattr(item, "room_SubSystemClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_SubSystemClass"):
                    opp_val = getattr(item, "room_SubSystemClass", None)
                    
                    setattr(item, "room_SubSystemClass", self)
                    

    @property
    def room_RoomModel6(self):
        return self.__room_RoomModel6

    @room_RoomModel6.setter
    def room_RoomModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomModel__room_RoomModel6", None)
        self.__room_RoomModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_ActorClass"):
                    opp_val = getattr(item, "room_ActorClass", None)
                    
                    if opp_val == self:
                        setattr(item, "room_ActorClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_ActorClass"):
                    opp_val = getattr(item, "room_ActorClass", None)
                    
                    setattr(item, "room_ActorClass", self)
                    

    @property
    def room_RoomModel(self):
        return self.__room_RoomModel

    @room_RoomModel.setter
    def room_RoomModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomModel__room_RoomModel", None)
        self.__room_RoomModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Import"):
                    opp_val = getattr(item, "room_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Import"):
                    opp_val = getattr(item, "room_Import", None)
                    
                    setattr(item, "room_Import", self)
                    

    @property
    def room_RoomModel4(self):
        return self.__room_RoomModel4

    @room_RoomModel4.setter
    def room_RoomModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomModel__room_RoomModel4", None)
        self.__room_RoomModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_ProtocolClass"):
                    opp_val = getattr(item, "room_ProtocolClass", None)
                    
                    if opp_val == self:
                        setattr(item, "room_ProtocolClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_ProtocolClass"):
                    opp_val = getattr(item, "room_ProtocolClass", None)
                    
                    setattr(item, "room_ProtocolClass", self)
                    

class RoomClass:

    pass
class room_DataClass(RoomClass):

    pass
class room_ProtocolClass(RoomClass):

    pass
class room_StructureClass(RoomClass):

    pass
class room_RoomClass:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class room_LogicalSystem(StructureClass):

    pass