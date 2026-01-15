from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActorCommunicationType(Enum):
    EVENT_DRIVEN = "EVENT_DRIVEN"
    DATA_DRIVEN = "DATA_DRIVEN"
    ASYNCHRONOUS = "ASYNCHRONOUS"
    SYNCHRONOUS = "SYNCHRONOUS"
class CommunicationType(Enum):
    EVENT_DRIVEN = "EVENT_DRIVEN"
    DATA_DRIVEN = "DATA_DRIVEN"
    SYNCHRONOUS = "SYNCHRONOUS"
class LiteralType(Enum):
    BOOL = "BOOL"
    INT = "INT"
    REAL = "REAL"
    CHAR = "CHAR"


############################################
# Definition of Classes
############################################

class TransitionTerminal:

    pass
class room_TrPointTerminal(TransitionTerminal):

    pass
class room_StateTerminal(TransitionTerminal):

    pass
class room_KeyValue:

    def __init__(self, key: str, value: str, room_KeyValue: "room_Annotation" = None):
        self.key = key
        self.value = value
        self.room_KeyValue = room_KeyValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def room_KeyValue(self):
        return self.__room_KeyValue

    @room_KeyValue.setter
    def room_KeyValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_KeyValue__room_KeyValue", None)
        self.__room_KeyValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Annotation309"):
                opp_val = getattr(old_value, "room_Annotation309", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Annotation309"):
                opp_val = getattr(value, "room_Annotation309", None)
                if opp_val is None:
                    setattr(value, "room_Annotation309", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_Guard:

    pass
class room_MessageFromIf:

    pass
class room_ChoicepointTerminal(TransitionTerminal):

    pass
class room_SubStateTrPointTerminal(TransitionTerminal):

    pass
class room_Trigger:

    pass
class TransitionChainStartTransition:

    pass
class room_GuardedTransition(TransitionChainStartTransition):

    pass
class room_TriggeredTransition(TransitionChainStartTransition):

    pass
class NonInitialTransition:

    pass
class room_CPBranchTransition(NonInitialTransition):

    pass
class room_ContinuationTransition(NonInitialTransition):

    pass
class room_TransitionChainStartTransition(NonInitialTransition):

    pass
class room_RefinedTransition:

    pass
class Transition:

    pass
class room_InitialTransition(Transition):

    pass
class room_NonInitialTransition(Transition):

    pass
class room_TransitionTerminal:

    pass
class TrPoint:

    pass
class room_EntryPoint(TrPoint):

    pass
class room_ExitPoint(TrPoint):

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
class room_SimpleState(State):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class StateGraphNode:

    pass
class room_ChoicePoint(StateGraphNode):

    def __init__(self, name: str, room_ChoicePoint: "room_StateGraph" = None, room_ChoicePoint259: "room_Documentation" = None, room_ChoicePoint295: "room_ChoicepointTerminal" = None):
        self.name = name
        self.room_ChoicePoint = room_ChoicePoint
        self.room_ChoicePoint259 = room_ChoicePoint259
        self.room_ChoicePoint295 = room_ChoicePoint295
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_ChoicePoint295(self):
        return self.__room_ChoicePoint295

    @room_ChoicePoint295.setter
    def room_ChoicePoint295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ChoicePoint__room_ChoicePoint295", None)
        self.__room_ChoicePoint295 = value
        
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
            if hasattr(old_value, "room_StateGraph251"):
                opp_val = getattr(old_value, "room_StateGraph251", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph251"):
                opp_val = getattr(value, "room_StateGraph251", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph251", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_ChoicePoint259(self):
        return self.__room_ChoicePoint259

    @room_ChoicePoint259.setter
    def room_ChoicePoint259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ChoicePoint__room_ChoicePoint259", None)
        self.__room_ChoicePoint259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation260"):
                opp_val = getattr(old_value, "room_Documentation260", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation260"):
                opp_val = getattr(value, "room_Documentation260", None)
                setattr(value, "room_Documentation260", self)

class room_TrPoint(StateGraphNode):

    def __init__(self, name: str, room_TrPoint: "room_StateGraph" = None, room_TrPoint288: "room_TrPointTerminal" = None, room_TrPoint290: "room_SubStateTrPointTerminal" = None):
        self.name = name
        self.room_TrPoint = room_TrPoint
        self.room_TrPoint288 = room_TrPoint288
        self.room_TrPoint290 = room_TrPoint290
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_TrPoint288(self):
        return self.__room_TrPoint288

    @room_TrPoint288.setter
    def room_TrPoint288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_TrPoint__room_TrPoint288", None)
        self.__room_TrPoint288 = value
        
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

    @property
    def room_TrPoint290(self):
        return self.__room_TrPoint290

    @room_TrPoint290.setter
    def room_TrPoint290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_TrPoint__room_TrPoint290", None)
        self.__room_TrPoint290 = value
        
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
    def room_TrPoint(self):
        return self.__room_TrPoint

    @room_TrPoint.setter
    def room_TrPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_TrPoint__room_TrPoint", None)
        self.__room_TrPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph249"):
                opp_val = getattr(old_value, "room_StateGraph249", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph249"):
                opp_val = getattr(value, "room_StateGraph249", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph249", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_State(StateGraphNode):

    def __init__(self, room_State: "room_Documentation" = None, room_State234: "room_DetailCode" = None, room_State237: "room_DetailCode" = None, room_State240: "room_DetailCode" = None, room_State243: "room_StateGraph" = None, room_State247: "room_StateGraph" = None, room_State257: "room_RefinedState" = None, room_State293: "room_SubStateTrPointTerminal" = None, room_State286: "room_StateTerminal" = None):
        self.room_State = room_State
        self.room_State234 = room_State234
        self.room_State237 = room_State237
        self.room_State240 = room_State240
        self.room_State243 = room_State243
        self.room_State247 = room_State247
        self.room_State257 = room_State257
        self.room_State293 = room_State293
        self.room_State286 = room_State286
        
    @property
    def room_State240(self):
        return self.__room_State240

    @room_State240.setter
    def room_State240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State240", None)
        self.__room_State240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode241"):
                opp_val = getattr(old_value, "room_DetailCode241", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode241"):
                opp_val = getattr(value, "room_DetailCode241", None)
                setattr(value, "room_DetailCode241", self)

    @property
    def room_State293(self):
        return self.__room_State293

    @room_State293.setter
    def room_State293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State293", None)
        self.__room_State293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SubStateTrPointTerminal292"):
                opp_val = getattr(old_value, "room_SubStateTrPointTerminal292", None)
                if opp_val == self:
                    setattr(old_value, "room_SubStateTrPointTerminal292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SubStateTrPointTerminal292"):
                opp_val = getattr(value, "room_SubStateTrPointTerminal292", None)
                setattr(value, "room_SubStateTrPointTerminal292", self)

    @property
    def room_State237(self):
        return self.__room_State237

    @room_State237.setter
    def room_State237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State237", None)
        self.__room_State237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode238"):
                opp_val = getattr(old_value, "room_DetailCode238", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode238"):
                opp_val = getattr(value, "room_DetailCode238", None)
                setattr(value, "room_DetailCode238", self)

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
            if hasattr(old_value, "room_Documentation232"):
                opp_val = getattr(old_value, "room_Documentation232", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation232"):
                opp_val = getattr(value, "room_Documentation232", None)
                setattr(value, "room_Documentation232", self)

    @property
    def room_State286(self):
        return self.__room_State286

    @room_State286.setter
    def room_State286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State286", None)
        self.__room_State286 = value
        
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

    @property
    def room_State247(self):
        return self.__room_State247

    @room_State247.setter
    def room_State247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State247", None)
        self.__room_State247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph246"):
                opp_val = getattr(old_value, "room_StateGraph246", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph246"):
                opp_val = getattr(value, "room_StateGraph246", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph246", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_State257(self):
        return self.__room_State257

    @room_State257.setter
    def room_State257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State257", None)
        self.__room_State257 = value
        
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
    def room_State243(self):
        return self.__room_State243

    @room_State243.setter
    def room_State243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State243", None)
        self.__room_State243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph244"):
                opp_val = getattr(old_value, "room_StateGraph244", None)
                if opp_val == self:
                    setattr(old_value, "room_StateGraph244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph244"):
                opp_val = getattr(value, "room_StateGraph244", None)
                setattr(value, "room_StateGraph244", self)

    @property
    def room_State234(self):
        return self.__room_State234

    @room_State234.setter
    def room_State234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State234", None)
        self.__room_State234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode235"):
                opp_val = getattr(old_value, "room_DetailCode235", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode235"):
                opp_val = getattr(value, "room_DetailCode235", None)
                setattr(value, "room_DetailCode235", self)

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class room_StateGraphItem:

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

class StateGraphItem:

    pass
class room_Transition(StateGraphItem):

    def __init__(self, name: str, room_Transition: "room_StateGraph" = None, room_Transition262: "room_TransitionTerminal" = None, room_Transition264: "room_Documentation" = None, room_Transition267: "room_DetailCode" = None, room_Transition278: "room_RefinedTransition" = None):
        self.name = name
        self.room_Transition = room_Transition
        self.room_Transition262 = room_Transition262
        self.room_Transition264 = room_Transition264
        self.room_Transition267 = room_Transition267
        self.room_Transition278 = room_Transition278
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_Transition264(self):
        return self.__room_Transition264

    @room_Transition264.setter
    def room_Transition264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Transition__room_Transition264", None)
        self.__room_Transition264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation265"):
                opp_val = getattr(old_value, "room_Documentation265", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation265"):
                opp_val = getattr(value, "room_Documentation265", None)
                setattr(value, "room_Documentation265", self)

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
            if hasattr(old_value, "room_StateGraph253"):
                opp_val = getattr(old_value, "room_StateGraph253", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph253"):
                opp_val = getattr(value, "room_StateGraph253", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph253", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Transition267(self):
        return self.__room_Transition267

    @room_Transition267.setter
    def room_Transition267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Transition__room_Transition267", None)
        self.__room_Transition267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode268"):
                opp_val = getattr(old_value, "room_DetailCode268", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode268"):
                opp_val = getattr(value, "room_DetailCode268", None)
                setattr(value, "room_DetailCode268", self)

    @property
    def room_Transition278(self):
        return self.__room_Transition278

    @room_Transition278.setter
    def room_Transition278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Transition__room_Transition278", None)
        self.__room_Transition278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RefinedTransition277"):
                opp_val = getattr(old_value, "room_RefinedTransition277", None)
                if opp_val == self:
                    setattr(old_value, "room_RefinedTransition277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RefinedTransition277"):
                opp_val = getattr(value, "room_RefinedTransition277", None)
                setattr(value, "room_RefinedTransition277", self)

    @property
    def room_Transition262(self):
        return self.__room_Transition262

    @room_Transition262.setter
    def room_Transition262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Transition__room_Transition262", None)
        self.__room_Transition262 = value
        
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
            if hasattr(old_value, "room_LogicalThread199"):
                opp_val = getattr(old_value, "room_LogicalThread199", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_LogicalThread199"):
                opp_val = getattr(value, "room_LogicalThread199", None)
                if opp_val is None:
                    setattr(value, "room_LogicalThread199", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
class room_BindingEndPoint:

    pass
class room_LogicalThread:

    def __init__(self, name: str, prio: int, room_LogicalThread: "room_SubSystemClass" = None, room_LogicalThread199: set["room_ActorInstancePath"] = None):
        self.name = name
        self.prio = prio
        self.room_LogicalThread = room_LogicalThread
        self.room_LogicalThread199 = room_LogicalThread199 if room_LogicalThread199 is not None else set()
        
    @property
    def prio(self) -> int:
        return self.__prio

    @prio.setter
    def prio(self, prio: int):
        self.__prio = prio

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_LogicalThread199(self):
        return self.__room_LogicalThread199

    @room_LogicalThread199.setter
    def room_LogicalThread199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_LogicalThread__room_LogicalThread199", None)
        self.__room_LogicalThread199 = value if value is not None else set()
        
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
            if hasattr(old_value, "room_SubSystemClass197"):
                opp_val = getattr(old_value, "room_SubSystemClass197", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SubSystemClass197"):
                opp_val = getattr(value, "room_SubSystemClass197", None)
                if opp_val is None:
                    setattr(value, "room_SubSystemClass197", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ActorContainerRef:

    pass
class room_ActorContainerRef:

    def __init__(self, name: str, room_ActorContainerRef: "room_Documentation" = None, room_ActorContainerRef207: "room_BindingEndPoint" = None, room_ActorContainerRef219: "room_RefSAPoint" = None, room_ActorContainerRef224: "room_SPPoint" = None):
        self.name = name
        self.room_ActorContainerRef = room_ActorContainerRef
        self.room_ActorContainerRef207 = room_ActorContainerRef207
        self.room_ActorContainerRef219 = room_ActorContainerRef219
        self.room_ActorContainerRef224 = room_ActorContainerRef224
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_ActorContainerRef207(self):
        return self.__room_ActorContainerRef207

    @room_ActorContainerRef207.setter
    def room_ActorContainerRef207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorContainerRef__room_ActorContainerRef207", None)
        self.__room_ActorContainerRef207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_BindingEndPoint206"):
                opp_val = getattr(old_value, "room_BindingEndPoint206", None)
                if opp_val == self:
                    setattr(old_value, "room_BindingEndPoint206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_BindingEndPoint206"):
                opp_val = getattr(value, "room_BindingEndPoint206", None)
                setattr(value, "room_BindingEndPoint206", self)

    @property
    def room_ActorContainerRef224(self):
        return self.__room_ActorContainerRef224

    @room_ActorContainerRef224.setter
    def room_ActorContainerRef224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorContainerRef__room_ActorContainerRef224", None)
        self.__room_ActorContainerRef224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SPPoint223"):
                opp_val = getattr(old_value, "room_SPPoint223", None)
                if opp_val == self:
                    setattr(old_value, "room_SPPoint223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SPPoint223"):
                opp_val = getattr(value, "room_SPPoint223", None)
                setattr(value, "room_SPPoint223", self)

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
            if hasattr(old_value, "room_Documentation189"):
                opp_val = getattr(old_value, "room_Documentation189", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation189"):
                opp_val = getattr(value, "room_Documentation189", None)
                setattr(value, "room_Documentation189", self)

    @property
    def room_ActorContainerRef219(self):
        return self.__room_ActorContainerRef219

    @room_ActorContainerRef219.setter
    def room_ActorContainerRef219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorContainerRef__room_ActorContainerRef219", None)
        self.__room_ActorContainerRef219 = value
        
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

class room_SubSystemRef(ActorContainerRef):

    pass
class InterfaceItem:

    pass
class room_InterfaceItem:

    def __init__(self, name: str, room_InterfaceItem: "room_MessageFromIf" = None):
        self.name = name
        self.room_InterfaceItem = room_InterfaceItem
        
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
            if hasattr(old_value, "room_MessageFromIf304"):
                opp_val = getattr(old_value, "room_MessageFromIf304", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageFromIf304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageFromIf304"):
                opp_val = getattr(value, "room_MessageFromIf304", None)
                setattr(value, "room_MessageFromIf304", self)

    def getGeneralProtocol(self) -> GeneralProtocolClass:
        # TODO: Implement getGeneralProtocol method
        pass

class room_StateGraph:

    pass
class room_SAPRef(InterfaceItem):

    pass
class room_ServiceImplementation:

    pass
class room_ExternalPort:

    pass
class room_Port(InterfaceItem):

    def __init__(self, conjugated: bool, multiplicity: int, room_Port: "room_ActorClass" = None, room_Port147: "room_ActorClass" = None, room_Port176: "room_ExternalPort" = None, room_Port195: "room_SubSystemClass" = None, room_Port169: "room_GeneralProtocolClass" = None, room_Port172: "room_Documentation" = None, room_Port210: "room_BindingEndPoint" = None):
        self.conjugated = conjugated
        self.multiplicity = multiplicity
        self.room_Port = room_Port
        self.room_Port147 = room_Port147
        self.room_Port176 = room_Port176
        self.room_Port195 = room_Port195
        self.room_Port169 = room_Port169
        self.room_Port172 = room_Port172
        self.room_Port210 = room_Port210
        
    @property
    def conjugated(self) -> bool:
        return self.__conjugated

    @conjugated.setter
    def conjugated(self, conjugated: bool):
        self.__conjugated = conjugated

    @property
    def multiplicity(self) -> int:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: int):
        self.__multiplicity = multiplicity

    @property
    def room_Port172(self):
        return self.__room_Port172

    @room_Port172.setter
    def room_Port172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port172", None)
        self.__room_Port172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation173"):
                opp_val = getattr(old_value, "room_Documentation173", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation173"):
                opp_val = getattr(value, "room_Documentation173", None)
                setattr(value, "room_Documentation173", self)

    @property
    def room_Port210(self):
        return self.__room_Port210

    @room_Port210.setter
    def room_Port210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port210", None)
        self.__room_Port210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_BindingEndPoint209"):
                opp_val = getattr(old_value, "room_BindingEndPoint209", None)
                if opp_val == self:
                    setattr(old_value, "room_BindingEndPoint209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_BindingEndPoint209"):
                opp_val = getattr(value, "room_BindingEndPoint209", None)
                setattr(value, "room_BindingEndPoint209", self)

    @property
    def room_Port176(self):
        return self.__room_Port176

    @room_Port176.setter
    def room_Port176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port176", None)
        self.__room_Port176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ExternalPort175"):
                opp_val = getattr(old_value, "room_ExternalPort175", None)
                if opp_val == self:
                    setattr(old_value, "room_ExternalPort175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ExternalPort175"):
                opp_val = getattr(value, "room_ExternalPort175", None)
                setattr(value, "room_ExternalPort175", self)

    @property
    def room_Port195(self):
        return self.__room_Port195

    @room_Port195.setter
    def room_Port195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port195", None)
        self.__room_Port195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SubSystemClass194"):
                opp_val = getattr(old_value, "room_SubSystemClass194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SubSystemClass194"):
                opp_val = getattr(value, "room_SubSystemClass194", None)
                if opp_val is None:
                    setattr(value, "room_SubSystemClass194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Port147(self):
        return self.__room_Port147

    @room_Port147.setter
    def room_Port147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port147", None)
        self.__room_Port147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass146"):
                opp_val = getattr(old_value, "room_ActorClass146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass146"):
                opp_val = getattr(value, "room_ActorClass146", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass146", set([self]))
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
            if hasattr(old_value, "room_ActorClass141"):
                opp_val = getattr(old_value, "room_ActorClass141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass141"):
                opp_val = getattr(value, "room_ActorClass141", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Port169(self):
        return self.__room_Port169

    @room_Port169.setter
    def room_Port169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port169", None)
        self.__room_Port169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_GeneralProtocolClass170"):
                opp_val = getattr(old_value, "room_GeneralProtocolClass170", None)
                if opp_val == self:
                    setattr(old_value, "room_GeneralProtocolClass170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_GeneralProtocolClass170"):
                opp_val = getattr(value, "room_GeneralProtocolClass170", None)
                setattr(value, "room_GeneralProtocolClass170", self)

    def isReplicated(self) -> bool:
        # TODO: Implement isReplicated method
        pass

class ActorContainerClass:

    pass
class SemanticsRule:

    pass
class room_OutSemanticsRule(SemanticsRule):

    pass
class room_InSemanticsRule(SemanticsRule):

    pass
class room_SemanticsRule:

    pass
class MessageHandler:

    pass
class room_OutMessageHandler(MessageHandler):

    pass
class room_InMessageHandler(MessageHandler):

    pass
class room_MessageHandler:

    pass
class room_SubProtocol:

    def __init__(self, name: str, room_SubProtocol: "room_CompoundProtocolClass" = None, room_SubProtocol104: "room_GeneralProtocolClass" = None, room_SubProtocol213: "room_BindingEndPoint" = None):
        self.name = name
        self.room_SubProtocol = room_SubProtocol
        self.room_SubProtocol104 = room_SubProtocol104
        self.room_SubProtocol213 = room_SubProtocol213
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_SubProtocol(self):
        return self.__room_SubProtocol

    @room_SubProtocol.setter
    def room_SubProtocol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_SubProtocol__room_SubProtocol", None)
        self.__room_SubProtocol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_CompoundProtocolClass"):
                opp_val = getattr(old_value, "room_CompoundProtocolClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_CompoundProtocolClass"):
                opp_val = getattr(value, "room_CompoundProtocolClass", None)
                if opp_val is None:
                    setattr(value, "room_CompoundProtocolClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_SubProtocol213(self):
        return self.__room_SubProtocol213

    @room_SubProtocol213.setter
    def room_SubProtocol213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_SubProtocol__room_SubProtocol213", None)
        self.__room_SubProtocol213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_BindingEndPoint212"):
                opp_val = getattr(old_value, "room_BindingEndPoint212", None)
                if opp_val == self:
                    setattr(old_value, "room_BindingEndPoint212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_BindingEndPoint212"):
                opp_val = getattr(value, "room_BindingEndPoint212", None)
                setattr(value, "room_BindingEndPoint212", self)

    @property
    def room_SubProtocol104(self):
        return self.__room_SubProtocol104

    @room_SubProtocol104.setter
    def room_SubProtocol104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_SubProtocol__room_SubProtocol104", None)
        self.__room_SubProtocol104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_GeneralProtocolClass105"):
                opp_val = getattr(old_value, "room_GeneralProtocolClass105", None)
                if opp_val == self:
                    setattr(old_value, "room_GeneralProtocolClass105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_GeneralProtocolClass105"):
                opp_val = getattr(value, "room_GeneralProtocolClass105", None)
                setattr(value, "room_GeneralProtocolClass105", self)

class room_ProtocolSemantics:

    pass
class room_PortClass:

    pass
class GeneralProtocolClass:

    pass
class room_CompoundProtocolClass(GeneralProtocolClass):

    pass
class room_ProtocolClass(GeneralProtocolClass):

    def __init__(self, commType: str, room_ProtocolClass: "room_ProtocolClass" = None, room_ProtocolClass78: "room_ProtocolClass" = None, room_ProtocolClass81: "room_DetailCode" = None, room_ProtocolClass84: "room_DetailCode" = None, room_ProtocolClass87: "room_DetailCode" = None, room_ProtocolClass90: set["room_Message"] = None, room_ProtocolClass93: set["room_Message"] = None, room_ProtocolClass96: "room_PortClass" = None, room_ProtocolClass98: "room_PortClass" = None, room_ProtocolClass101: "room_ProtocolSemantics" = None, room_ProtocolClass179: "room_SAPRef" = None, room_ProtocolClass182: "room_SPPRef" = None):
        self.commType = commType
        self.room_ProtocolClass = room_ProtocolClass
        self.room_ProtocolClass78 = room_ProtocolClass78
        self.room_ProtocolClass81 = room_ProtocolClass81
        self.room_ProtocolClass84 = room_ProtocolClass84
        self.room_ProtocolClass87 = room_ProtocolClass87
        self.room_ProtocolClass90 = room_ProtocolClass90 if room_ProtocolClass90 is not None else set()
        self.room_ProtocolClass93 = room_ProtocolClass93 if room_ProtocolClass93 is not None else set()
        self.room_ProtocolClass96 = room_ProtocolClass96
        self.room_ProtocolClass98 = room_ProtocolClass98
        self.room_ProtocolClass101 = room_ProtocolClass101
        self.room_ProtocolClass179 = room_ProtocolClass179
        self.room_ProtocolClass182 = room_ProtocolClass182
        
    @property
    def commType(self) -> str:
        return self.__commType

    @commType.setter
    def commType(self, commType: str):
        self.__commType = commType

    @property
    def room_ProtocolClass81(self):
        return self.__room_ProtocolClass81

    @room_ProtocolClass81.setter
    def room_ProtocolClass81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass81", None)
        self.__room_ProtocolClass81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode82"):
                opp_val = getattr(old_value, "room_DetailCode82", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode82"):
                opp_val = getattr(value, "room_DetailCode82", None)
                setattr(value, "room_DetailCode82", self)

    @property
    def room_ProtocolClass84(self):
        return self.__room_ProtocolClass84

    @room_ProtocolClass84.setter
    def room_ProtocolClass84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass84", None)
        self.__room_ProtocolClass84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode85"):
                opp_val = getattr(old_value, "room_DetailCode85", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode85"):
                opp_val = getattr(value, "room_DetailCode85", None)
                setattr(value, "room_DetailCode85", self)

    @property
    def room_ProtocolClass182(self):
        return self.__room_ProtocolClass182

    @room_ProtocolClass182.setter
    def room_ProtocolClass182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass182", None)
        self.__room_ProtocolClass182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SPPRef181"):
                opp_val = getattr(old_value, "room_SPPRef181", None)
                if opp_val == self:
                    setattr(old_value, "room_SPPRef181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SPPRef181"):
                opp_val = getattr(value, "room_SPPRef181", None)
                setattr(value, "room_SPPRef181", self)

    @property
    def room_ProtocolClass96(self):
        return self.__room_ProtocolClass96

    @room_ProtocolClass96.setter
    def room_ProtocolClass96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass96", None)
        self.__room_ProtocolClass96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_PortClass"):
                opp_val = getattr(old_value, "room_PortClass", None)
                if opp_val == self:
                    setattr(old_value, "room_PortClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortClass"):
                opp_val = getattr(value, "room_PortClass", None)
                setattr(value, "room_PortClass", self)

    @property
    def room_ProtocolClass78(self):
        return self.__room_ProtocolClass78

    @room_ProtocolClass78.setter
    def room_ProtocolClass78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass78", None)
        self.__room_ProtocolClass78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass"):
                opp_val = getattr(old_value, "room_ProtocolClass", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass"):
                opp_val = getattr(value, "room_ProtocolClass", None)
                setattr(value, "room_ProtocolClass", self)

    @property
    def room_ProtocolClass98(self):
        return self.__room_ProtocolClass98

    @room_ProtocolClass98.setter
    def room_ProtocolClass98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass98", None)
        self.__room_ProtocolClass98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_PortClass99"):
                opp_val = getattr(old_value, "room_PortClass99", None)
                if opp_val == self:
                    setattr(old_value, "room_PortClass99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortClass99"):
                opp_val = getattr(value, "room_PortClass99", None)
                setattr(value, "room_PortClass99", self)

    @property
    def room_ProtocolClass87(self):
        return self.__room_ProtocolClass87

    @room_ProtocolClass87.setter
    def room_ProtocolClass87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass87", None)
        self.__room_ProtocolClass87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode88"):
                opp_val = getattr(old_value, "room_DetailCode88", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode88"):
                opp_val = getattr(value, "room_DetailCode88", None)
                setattr(value, "room_DetailCode88", self)

    @property
    def room_ProtocolClass179(self):
        return self.__room_ProtocolClass179

    @room_ProtocolClass179.setter
    def room_ProtocolClass179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass179", None)
        self.__room_ProtocolClass179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SAPRef178"):
                opp_val = getattr(old_value, "room_SAPRef178", None)
                if opp_val == self:
                    setattr(old_value, "room_SAPRef178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SAPRef178"):
                opp_val = getattr(value, "room_SAPRef178", None)
                setattr(value, "room_SAPRef178", self)

    @property
    def room_ProtocolClass90(self):
        return self.__room_ProtocolClass90

    @room_ProtocolClass90.setter
    def room_ProtocolClass90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass90", None)
        self.__room_ProtocolClass90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Message91"):
                    opp_val = getattr(item, "room_Message91", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Message91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Message91"):
                    opp_val = getattr(item, "room_Message91", None)
                    
                    setattr(item, "room_Message91", self)
                    

    @property
    def room_ProtocolClass(self):
        return self.__room_ProtocolClass

    @room_ProtocolClass.setter
    def room_ProtocolClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass", None)
        self.__room_ProtocolClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass78"):
                opp_val = getattr(old_value, "room_ProtocolClass78", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass78"):
                opp_val = getattr(value, "room_ProtocolClass78", None)
                setattr(value, "room_ProtocolClass78", self)

    @property
    def room_ProtocolClass101(self):
        return self.__room_ProtocolClass101

    @room_ProtocolClass101.setter
    def room_ProtocolClass101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass101", None)
        self.__room_ProtocolClass101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolSemantics"):
                opp_val = getattr(old_value, "room_ProtocolSemantics", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolSemantics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolSemantics"):
                opp_val = getattr(value, "room_ProtocolSemantics", None)
                setattr(value, "room_ProtocolSemantics", self)

    @property
    def room_ProtocolClass93(self):
        return self.__room_ProtocolClass93

    @room_ProtocolClass93.setter
    def room_ProtocolClass93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass93", None)
        self.__room_ProtocolClass93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Message94"):
                    opp_val = getattr(item, "room_Message94", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Message94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Message94"):
                    opp_val = getattr(item, "room_Message94", None)
                    
                    setattr(item, "room_Message94", self)
                    

class room_Message:

    def __init__(self, priv: bool, name: str, room_Message: "room_PortOperation" = None, room_Message91: "room_ProtocolClass" = None, room_Message94: "room_ProtocolClass" = None, room_Message107: "room_VarDecl" = None, room_Message110: "room_Documentation" = None, room_Message125: "room_MessageHandler" = None, room_Message133: "room_SemanticsRule" = None, room_Message302: "room_MessageFromIf" = None):
        self.priv = priv
        self.name = name
        self.room_Message = room_Message
        self.room_Message91 = room_Message91
        self.room_Message94 = room_Message94
        self.room_Message107 = room_Message107
        self.room_Message110 = room_Message110
        self.room_Message125 = room_Message125
        self.room_Message133 = room_Message133
        self.room_Message302 = room_Message302
        
    @property
    def priv(self) -> bool:
        return self.__priv

    @priv.setter
    def priv(self, priv: bool):
        self.__priv = priv

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_Message125(self):
        return self.__room_Message125

    @room_Message125.setter
    def room_Message125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message125", None)
        self.__room_Message125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageHandler124"):
                opp_val = getattr(old_value, "room_MessageHandler124", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageHandler124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageHandler124"):
                opp_val = getattr(value, "room_MessageHandler124", None)
                setattr(value, "room_MessageHandler124", self)

    @property
    def room_Message110(self):
        return self.__room_Message110

    @room_Message110.setter
    def room_Message110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message110", None)
        self.__room_Message110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation111"):
                opp_val = getattr(old_value, "room_Documentation111", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation111"):
                opp_val = getattr(value, "room_Documentation111", None)
                setattr(value, "room_Documentation111", self)

    @property
    def room_Message94(self):
        return self.__room_Message94

    @room_Message94.setter
    def room_Message94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message94", None)
        self.__room_Message94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass93"):
                opp_val = getattr(old_value, "room_ProtocolClass93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass93"):
                opp_val = getattr(value, "room_ProtocolClass93", None)
                if opp_val is None:
                    setattr(value, "room_ProtocolClass93", set([self]))
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
            if hasattr(old_value, "room_PortOperation"):
                opp_val = getattr(old_value, "room_PortOperation", None)
                if opp_val == self:
                    setattr(old_value, "room_PortOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortOperation"):
                opp_val = getattr(value, "room_PortOperation", None)
                setattr(value, "room_PortOperation", self)

    @property
    def room_Message133(self):
        return self.__room_Message133

    @room_Message133.setter
    def room_Message133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message133", None)
        self.__room_Message133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SemanticsRule132"):
                opp_val = getattr(old_value, "room_SemanticsRule132", None)
                if opp_val == self:
                    setattr(old_value, "room_SemanticsRule132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SemanticsRule132"):
                opp_val = getattr(value, "room_SemanticsRule132", None)
                setattr(value, "room_SemanticsRule132", self)

    @property
    def room_Message107(self):
        return self.__room_Message107

    @room_Message107.setter
    def room_Message107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message107", None)
        self.__room_Message107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_VarDecl108"):
                opp_val = getattr(old_value, "room_VarDecl108", None)
                if opp_val == self:
                    setattr(old_value, "room_VarDecl108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_VarDecl108"):
                opp_val = getattr(value, "room_VarDecl108", None)
                setattr(value, "room_VarDecl108", self)

    @property
    def room_Message302(self):
        return self.__room_Message302

    @room_Message302.setter
    def room_Message302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message302", None)
        self.__room_Message302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageFromIf301"):
                opp_val = getattr(old_value, "room_MessageFromIf301", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageFromIf301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageFromIf301"):
                opp_val = getattr(value, "room_MessageFromIf301", None)
                setattr(value, "room_MessageFromIf301", self)

    @property
    def room_Message91(self):
        return self.__room_Message91

    @room_Message91.setter
    def room_Message91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message91", None)
        self.__room_Message91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass90"):
                opp_val = getattr(old_value, "room_ProtocolClass90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass90"):
                opp_val = getattr(value, "room_ProtocolClass90", None)
                if opp_val is None:
                    setattr(value, "room_ProtocolClass90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Operation:

    pass
class room_PortOperation(Operation):

    pass
class room_Operation:

    def __init__(self, name: str, room_Operation: set["room_VarDecl"] = None, room_Operation66: "room_RefableType" = None, room_Operation69: "room_Documentation" = None, room_Operation72: "room_DetailCode" = None):
        self.name = name
        self.room_Operation = room_Operation if room_Operation is not None else set()
        self.room_Operation66 = room_Operation66
        self.room_Operation69 = room_Operation69
        self.room_Operation72 = room_Operation72
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_Operation66(self):
        return self.__room_Operation66

    @room_Operation66.setter
    def room_Operation66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation66", None)
        self.__room_Operation66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RefableType67"):
                opp_val = getattr(old_value, "room_RefableType67", None)
                if opp_val == self:
                    setattr(old_value, "room_RefableType67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RefableType67"):
                opp_val = getattr(value, "room_RefableType67", None)
                setattr(value, "room_RefableType67", self)

    @property
    def room_Operation(self):
        return self.__room_Operation

    @room_Operation.setter
    def room_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation", None)
        self.__room_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_VarDecl64"):
                    opp_val = getattr(item, "room_VarDecl64", None)
                    
                    if opp_val == self:
                        setattr(item, "room_VarDecl64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_VarDecl64"):
                    opp_val = getattr(item, "room_VarDecl64", None)
                    
                    setattr(item, "room_VarDecl64", self)
                    

    @property
    def room_Operation69(self):
        return self.__room_Operation69

    @room_Operation69.setter
    def room_Operation69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation69", None)
        self.__room_Operation69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation70"):
                opp_val = getattr(old_value, "room_Documentation70", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation70"):
                opp_val = getattr(value, "room_Documentation70", None)
                setattr(value, "room_Documentation70", self)

    @property
    def room_Operation72(self):
        return self.__room_Operation72

    @room_Operation72.setter
    def room_Operation72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation72", None)
        self.__room_Operation72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode73"):
                opp_val = getattr(old_value, "room_DetailCode73", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode73"):
                opp_val = getattr(value, "room_DetailCode73", None)
                setattr(value, "room_DetailCode73", self)

class room_StandardOperation(Operation):

    def __init__(self, destructor: bool, room_StandardOperation: "room_DataClass" = None, room_StandardOperation165: "room_ActorClass" = None):
        self.destructor = destructor
        self.room_StandardOperation = room_StandardOperation
        self.room_StandardOperation165 = room_StandardOperation165
        
    @property
    def destructor(self) -> bool:
        return self.__destructor

    @destructor.setter
    def destructor(self, destructor: bool):
        self.__destructor = destructor

    @property
    def room_StandardOperation(self):
        return self.__room_StandardOperation

    @room_StandardOperation.setter
    def room_StandardOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_StandardOperation__room_StandardOperation", None)
        self.__room_StandardOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass56"):
                opp_val = getattr(old_value, "room_DataClass56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass56"):
                opp_val = getattr(value, "room_DataClass56", None)
                if opp_val is None:
                    setattr(value, "room_DataClass56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_StandardOperation165(self):
        return self.__room_StandardOperation165

    @room_StandardOperation165.setter
    def room_StandardOperation165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_StandardOperation__room_StandardOperation165", None)
        self.__room_StandardOperation165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass164"):
                opp_val = getattr(old_value, "room_ActorClass164", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass164"):
                opp_val = getattr(value, "room_ActorClass164", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass164", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_Attribute:

    def __init__(self, name: str, size: int, defaultValueLiteral: str, room_Attribute: "room_DataClass" = None, room_Attribute58: "room_RefableType" = None, room_Attribute61: "room_Documentation" = None, room_Attribute117: "room_PortClass" = None, room_Attribute156: "room_ActorClass" = None):
        self.name = name
        self.size = size
        self.defaultValueLiteral = defaultValueLiteral
        self.room_Attribute = room_Attribute
        self.room_Attribute58 = room_Attribute58
        self.room_Attribute61 = room_Attribute61
        self.room_Attribute117 = room_Attribute117
        self.room_Attribute156 = room_Attribute156
        
    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "room_DataClass54"):
                opp_val = getattr(old_value, "room_DataClass54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass54"):
                opp_val = getattr(value, "room_DataClass54", None)
                if opp_val is None:
                    setattr(value, "room_DataClass54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Attribute58(self):
        return self.__room_Attribute58

    @room_Attribute58.setter
    def room_Attribute58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute58", None)
        self.__room_Attribute58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RefableType59"):
                opp_val = getattr(old_value, "room_RefableType59", None)
                if opp_val == self:
                    setattr(old_value, "room_RefableType59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RefableType59"):
                opp_val = getattr(value, "room_RefableType59", None)
                setattr(value, "room_RefableType59", self)

    @property
    def room_Attribute61(self):
        return self.__room_Attribute61

    @room_Attribute61.setter
    def room_Attribute61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute61", None)
        self.__room_Attribute61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation62"):
                opp_val = getattr(old_value, "room_Documentation62", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation62"):
                opp_val = getattr(value, "room_Documentation62", None)
                setattr(value, "room_Documentation62", self)

    @property
    def room_Attribute156(self):
        return self.__room_Attribute156

    @room_Attribute156.setter
    def room_Attribute156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute156", None)
        self.__room_Attribute156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass155"):
                opp_val = getattr(old_value, "room_ActorClass155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass155"):
                opp_val = getattr(value, "room_ActorClass155", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Attribute117(self):
        return self.__room_Attribute117

    @room_Attribute117.setter
    def room_Attribute117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute117", None)
        self.__room_Attribute117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_PortClass116"):
                opp_val = getattr(old_value, "room_PortClass116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortClass116"):
                opp_val = getattr(value, "room_PortClass116", None)
                if opp_val is None:
                    setattr(value, "room_PortClass116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_Binding:

    pass
class room_Annotation:

    def __init__(self, name: str, room_Annotation43: "room_DataClass" = None, room_Annotation: "room_StructureClass" = None, room_Annotation77: "room_GeneralProtocolClass" = None, room_Annotation162: "room_ActorClass" = None, room_Annotation309: set["room_KeyValue"] = None):
        self.name = name
        self.room_Annotation43 = room_Annotation43
        self.room_Annotation = room_Annotation
        self.room_Annotation77 = room_Annotation77
        self.room_Annotation162 = room_Annotation162
        self.room_Annotation309 = room_Annotation309 if room_Annotation309 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_Annotation77(self):
        return self.__room_Annotation77

    @room_Annotation77.setter
    def room_Annotation77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Annotation__room_Annotation77", None)
        self.__room_Annotation77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_GeneralProtocolClass76"):
                opp_val = getattr(old_value, "room_GeneralProtocolClass76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_GeneralProtocolClass76"):
                opp_val = getattr(value, "room_GeneralProtocolClass76", None)
                if opp_val is None:
                    setattr(value, "room_GeneralProtocolClass76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Annotation(self):
        return self.__room_Annotation

    @room_Annotation.setter
    def room_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Annotation__room_Annotation", None)
        self.__room_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StructureClass"):
                opp_val = getattr(old_value, "room_StructureClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StructureClass"):
                opp_val = getattr(value, "room_StructureClass", None)
                if opp_val is None:
                    setattr(value, "room_StructureClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Annotation43(self):
        return self.__room_Annotation43

    @room_Annotation43.setter
    def room_Annotation43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Annotation__room_Annotation43", None)
        self.__room_Annotation43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass42"):
                opp_val = getattr(old_value, "room_DataClass42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass42"):
                opp_val = getattr(value, "room_DataClass42", None)
                if opp_val is None:
                    setattr(value, "room_DataClass42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Annotation309(self):
        return self.__room_Annotation309

    @room_Annotation309.setter
    def room_Annotation309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Annotation__room_Annotation309", None)
        self.__room_Annotation309 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_KeyValue"):
                    opp_val = getattr(item, "room_KeyValue", None)
                    
                    if opp_val == self:
                        setattr(item, "room_KeyValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_KeyValue"):
                    opp_val = getattr(item, "room_KeyValue", None)
                    
                    setattr(item, "room_KeyValue", self)
                    

    @property
    def room_Annotation162(self):
        return self.__room_Annotation162

    @room_Annotation162.setter
    def room_Annotation162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Annotation__room_Annotation162", None)
        self.__room_Annotation162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass161"):
                opp_val = getattr(old_value, "room_ActorClass161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass161"):
                opp_val = getattr(value, "room_ActorClass161", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ComplexType:

    pass
class DataType:

    pass
class room_ComplexType(DataType):

    pass
class room_RefableType:

    def __init__(self, ref: bool, room_RefableType: "room_VarDecl" = None, room_RefableType37: "room_DataType" = None, room_RefableType59: "room_Attribute" = None, room_RefableType67: "room_Operation" = None):
        self.ref = ref
        self.room_RefableType = room_RefableType
        self.room_RefableType37 = room_RefableType37
        self.room_RefableType59 = room_RefableType59
        self.room_RefableType67 = room_RefableType67
        
    @property
    def ref(self) -> bool:
        return self.__ref

    @ref.setter
    def ref(self, ref: bool):
        self.__ref = ref

    @property
    def room_RefableType67(self):
        return self.__room_RefableType67

    @room_RefableType67.setter
    def room_RefableType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RefableType__room_RefableType67", None)
        self.__room_RefableType67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Operation66"):
                opp_val = getattr(old_value, "room_Operation66", None)
                if opp_val == self:
                    setattr(old_value, "room_Operation66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Operation66"):
                opp_val = getattr(value, "room_Operation66", None)
                setattr(value, "room_Operation66", self)

    @property
    def room_RefableType59(self):
        return self.__room_RefableType59

    @room_RefableType59.setter
    def room_RefableType59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RefableType__room_RefableType59", None)
        self.__room_RefableType59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Attribute58"):
                opp_val = getattr(old_value, "room_Attribute58", None)
                if opp_val == self:
                    setattr(old_value, "room_Attribute58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Attribute58"):
                opp_val = getattr(value, "room_Attribute58", None)
                setattr(value, "room_Attribute58", self)

    @property
    def room_RefableType(self):
        return self.__room_RefableType

    @room_RefableType.setter
    def room_RefableType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RefableType__room_RefableType", None)
        self.__room_RefableType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_VarDecl"):
                opp_val = getattr(old_value, "room_VarDecl", None)
                if opp_val == self:
                    setattr(old_value, "room_VarDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_VarDecl"):
                opp_val = getattr(value, "room_VarDecl", None)
                setattr(value, "room_VarDecl", self)

    @property
    def room_RefableType37(self):
        return self.__room_RefableType37

    @room_RefableType37.setter
    def room_RefableType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RefableType__room_RefableType37", None)
        self.__room_RefableType37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataType"):
                opp_val = getattr(old_value, "room_DataType", None)
                if opp_val == self:
                    setattr(old_value, "room_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataType"):
                opp_val = getattr(value, "room_DataType", None)
                setattr(value, "room_DataType", self)

class room_VarDecl:

    def __init__(self, name: str, room_VarDecl: "room_RefableType" = None, room_VarDecl64: "room_Operation" = None, room_VarDecl108: "room_Message" = None):
        self.name = name
        self.room_VarDecl = room_VarDecl
        self.room_VarDecl64 = room_VarDecl64
        self.room_VarDecl108 = room_VarDecl108
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_VarDecl(self):
        return self.__room_VarDecl

    @room_VarDecl.setter
    def room_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_VarDecl__room_VarDecl", None)
        self.__room_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RefableType"):
                opp_val = getattr(old_value, "room_RefableType", None)
                if opp_val == self:
                    setattr(old_value, "room_RefableType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RefableType"):
                opp_val = getattr(value, "room_RefableType", None)
                setattr(value, "room_RefableType", self)

    @property
    def room_VarDecl64(self):
        return self.__room_VarDecl64

    @room_VarDecl64.setter
    def room_VarDecl64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_VarDecl__room_VarDecl64", None)
        self.__room_VarDecl64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Operation"):
                opp_val = getattr(old_value, "room_Operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Operation"):
                opp_val = getattr(value, "room_Operation", None)
                if opp_val is None:
                    setattr(value, "room_Operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_VarDecl108(self):
        return self.__room_VarDecl108

    @room_VarDecl108.setter
    def room_VarDecl108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_VarDecl__room_VarDecl108", None)
        self.__room_VarDecl108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Message107"):
                opp_val = getattr(old_value, "room_Message107", None)
                if opp_val == self:
                    setattr(old_value, "room_Message107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Message107"):
                opp_val = getattr(value, "room_Message107", None)
                setattr(value, "room_Message107", self)

class room_ActorRef(ActorContainerRef):

    def __init__(self, size: int, room_ActorRef: "room_ActorContainerClass" = None, room_ActorRef229: "room_ActorClass" = None):
        self.size = size
        self.room_ActorRef = room_ActorRef
        self.room_ActorRef229 = room_ActorRef229
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def room_ActorRef(self):
        return self.__room_ActorRef

    @room_ActorRef.setter
    def room_ActorRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorRef__room_ActorRef", None)
        self.__room_ActorRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorContainerClass34"):
                opp_val = getattr(old_value, "room_ActorContainerClass34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorContainerClass34"):
                opp_val = getattr(value, "room_ActorContainerClass34", None)
                if opp_val is None:
                    setattr(value, "room_ActorContainerClass34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_ActorRef229(self):
        return self.__room_ActorRef229

    @room_ActorRef229.setter
    def room_ActorRef229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorRef__room_ActorRef229", None)
        self.__room_ActorRef229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass230"):
                opp_val = getattr(old_value, "room_ActorClass230", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass230"):
                opp_val = getattr(value, "room_ActorClass230", None)
                setattr(value, "room_ActorClass230", self)

class room_DetailCode:

    def __init__(self, commands: str, room_DetailCode: "room_ActorContainerClass" = None, room_DetailCode29: "room_ActorContainerClass" = None, room_DetailCode32: "room_ActorContainerClass" = None, room_DetailCode46: "room_DataClass" = None, room_DetailCode49: "room_DataClass" = None, room_DetailCode73: "room_Operation" = None, room_DetailCode52: "room_DataClass" = None, room_DetailCode82: "room_ProtocolClass" = None, room_DetailCode85: "room_ProtocolClass" = None, room_DetailCode88: "room_ProtocolClass" = None, room_DetailCode114: "room_PortClass" = None, room_DetailCode128: "room_MessageHandler" = None, room_DetailCode235: "room_State" = None, room_DetailCode238: "room_State" = None, room_DetailCode241: "room_State" = None, room_DetailCode268: "room_Transition" = None, room_DetailCode273: "room_GuardedTransition" = None, room_DetailCode275: "room_CPBranchTransition" = None, room_DetailCode284: "room_RefinedTransition" = None, room_DetailCode307: "room_Guard" = None):
        self.commands = commands
        self.room_DetailCode = room_DetailCode
        self.room_DetailCode29 = room_DetailCode29
        self.room_DetailCode32 = room_DetailCode32
        self.room_DetailCode46 = room_DetailCode46
        self.room_DetailCode49 = room_DetailCode49
        self.room_DetailCode73 = room_DetailCode73
        self.room_DetailCode52 = room_DetailCode52
        self.room_DetailCode82 = room_DetailCode82
        self.room_DetailCode85 = room_DetailCode85
        self.room_DetailCode88 = room_DetailCode88
        self.room_DetailCode114 = room_DetailCode114
        self.room_DetailCode128 = room_DetailCode128
        self.room_DetailCode235 = room_DetailCode235
        self.room_DetailCode238 = room_DetailCode238
        self.room_DetailCode241 = room_DetailCode241
        self.room_DetailCode268 = room_DetailCode268
        self.room_DetailCode273 = room_DetailCode273
        self.room_DetailCode275 = room_DetailCode275
        self.room_DetailCode284 = room_DetailCode284
        self.room_DetailCode307 = room_DetailCode307
        
    @property
    def commands(self) -> str:
        return self.__commands

    @commands.setter
    def commands(self, commands: str):
        self.__commands = commands

    @property
    def room_DetailCode49(self):
        return self.__room_DetailCode49

    @room_DetailCode49.setter
    def room_DetailCode49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode49", None)
        self.__room_DetailCode49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass48"):
                opp_val = getattr(old_value, "room_DataClass48", None)
                if opp_val == self:
                    setattr(old_value, "room_DataClass48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass48"):
                opp_val = getattr(value, "room_DataClass48", None)
                setattr(value, "room_DataClass48", self)

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
            if hasattr(old_value, "room_ActorContainerClass26"):
                opp_val = getattr(old_value, "room_ActorContainerClass26", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorContainerClass26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorContainerClass26"):
                opp_val = getattr(value, "room_ActorContainerClass26", None)
                setattr(value, "room_ActorContainerClass26", self)

    @property
    def room_DetailCode273(self):
        return self.__room_DetailCode273

    @room_DetailCode273.setter
    def room_DetailCode273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode273", None)
        self.__room_DetailCode273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_GuardedTransition"):
                opp_val = getattr(old_value, "room_GuardedTransition", None)
                if opp_val == self:
                    setattr(old_value, "room_GuardedTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_GuardedTransition"):
                opp_val = getattr(value, "room_GuardedTransition", None)
                setattr(value, "room_GuardedTransition", self)

    @property
    def room_DetailCode114(self):
        return self.__room_DetailCode114

    @room_DetailCode114.setter
    def room_DetailCode114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode114", None)
        self.__room_DetailCode114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_PortClass113"):
                opp_val = getattr(old_value, "room_PortClass113", None)
                if opp_val == self:
                    setattr(old_value, "room_PortClass113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortClass113"):
                opp_val = getattr(value, "room_PortClass113", None)
                setattr(value, "room_PortClass113", self)

    @property
    def room_DetailCode238(self):
        return self.__room_DetailCode238

    @room_DetailCode238.setter
    def room_DetailCode238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode238", None)
        self.__room_DetailCode238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_State237"):
                opp_val = getattr(old_value, "room_State237", None)
                if opp_val == self:
                    setattr(old_value, "room_State237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_State237"):
                opp_val = getattr(value, "room_State237", None)
                setattr(value, "room_State237", self)

    @property
    def room_DetailCode82(self):
        return self.__room_DetailCode82

    @room_DetailCode82.setter
    def room_DetailCode82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode82", None)
        self.__room_DetailCode82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass81"):
                opp_val = getattr(old_value, "room_ProtocolClass81", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass81"):
                opp_val = getattr(value, "room_ProtocolClass81", None)
                setattr(value, "room_ProtocolClass81", self)

    @property
    def room_DetailCode284(self):
        return self.__room_DetailCode284

    @room_DetailCode284.setter
    def room_DetailCode284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode284", None)
        self.__room_DetailCode284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RefinedTransition283"):
                opp_val = getattr(old_value, "room_RefinedTransition283", None)
                if opp_val == self:
                    setattr(old_value, "room_RefinedTransition283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RefinedTransition283"):
                opp_val = getattr(value, "room_RefinedTransition283", None)
                setattr(value, "room_RefinedTransition283", self)

    @property
    def room_DetailCode275(self):
        return self.__room_DetailCode275

    @room_DetailCode275.setter
    def room_DetailCode275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode275", None)
        self.__room_DetailCode275 = value
        
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
    def room_DetailCode307(self):
        return self.__room_DetailCode307

    @room_DetailCode307.setter
    def room_DetailCode307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode307", None)
        self.__room_DetailCode307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Guard306"):
                opp_val = getattr(old_value, "room_Guard306", None)
                if opp_val == self:
                    setattr(old_value, "room_Guard306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Guard306"):
                opp_val = getattr(value, "room_Guard306", None)
                setattr(value, "room_Guard306", self)

    @property
    def room_DetailCode88(self):
        return self.__room_DetailCode88

    @room_DetailCode88.setter
    def room_DetailCode88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode88", None)
        self.__room_DetailCode88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass87"):
                opp_val = getattr(old_value, "room_ProtocolClass87", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass87"):
                opp_val = getattr(value, "room_ProtocolClass87", None)
                setattr(value, "room_ProtocolClass87", self)

    @property
    def room_DetailCode235(self):
        return self.__room_DetailCode235

    @room_DetailCode235.setter
    def room_DetailCode235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode235", None)
        self.__room_DetailCode235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_State234"):
                opp_val = getattr(old_value, "room_State234", None)
                if opp_val == self:
                    setattr(old_value, "room_State234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_State234"):
                opp_val = getattr(value, "room_State234", None)
                setattr(value, "room_State234", self)

    @property
    def room_DetailCode268(self):
        return self.__room_DetailCode268

    @room_DetailCode268.setter
    def room_DetailCode268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode268", None)
        self.__room_DetailCode268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Transition267"):
                opp_val = getattr(old_value, "room_Transition267", None)
                if opp_val == self:
                    setattr(old_value, "room_Transition267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Transition267"):
                opp_val = getattr(value, "room_Transition267", None)
                setattr(value, "room_Transition267", self)

    @property
    def room_DetailCode52(self):
        return self.__room_DetailCode52

    @room_DetailCode52.setter
    def room_DetailCode52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode52", None)
        self.__room_DetailCode52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass51"):
                opp_val = getattr(old_value, "room_DataClass51", None)
                if opp_val == self:
                    setattr(old_value, "room_DataClass51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass51"):
                opp_val = getattr(value, "room_DataClass51", None)
                setattr(value, "room_DataClass51", self)

    @property
    def room_DetailCode128(self):
        return self.__room_DetailCode128

    @room_DetailCode128.setter
    def room_DetailCode128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode128", None)
        self.__room_DetailCode128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageHandler127"):
                opp_val = getattr(old_value, "room_MessageHandler127", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageHandler127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageHandler127"):
                opp_val = getattr(value, "room_MessageHandler127", None)
                setattr(value, "room_MessageHandler127", self)

    @property
    def room_DetailCode29(self):
        return self.__room_DetailCode29

    @room_DetailCode29.setter
    def room_DetailCode29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode29", None)
        self.__room_DetailCode29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorContainerClass28"):
                opp_val = getattr(old_value, "room_ActorContainerClass28", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorContainerClass28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorContainerClass28"):
                opp_val = getattr(value, "room_ActorContainerClass28", None)
                setattr(value, "room_ActorContainerClass28", self)

    @property
    def room_DetailCode73(self):
        return self.__room_DetailCode73

    @room_DetailCode73.setter
    def room_DetailCode73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode73", None)
        self.__room_DetailCode73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Operation72"):
                opp_val = getattr(old_value, "room_Operation72", None)
                if opp_val == self:
                    setattr(old_value, "room_Operation72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Operation72"):
                opp_val = getattr(value, "room_Operation72", None)
                setattr(value, "room_Operation72", self)

    @property
    def room_DetailCode32(self):
        return self.__room_DetailCode32

    @room_DetailCode32.setter
    def room_DetailCode32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode32", None)
        self.__room_DetailCode32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorContainerClass31"):
                opp_val = getattr(old_value, "room_ActorContainerClass31", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorContainerClass31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorContainerClass31"):
                opp_val = getattr(value, "room_ActorContainerClass31", None)
                setattr(value, "room_ActorContainerClass31", self)

    @property
    def room_DetailCode85(self):
        return self.__room_DetailCode85

    @room_DetailCode85.setter
    def room_DetailCode85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode85", None)
        self.__room_DetailCode85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass84"):
                opp_val = getattr(old_value, "room_ProtocolClass84", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass84"):
                opp_val = getattr(value, "room_ProtocolClass84", None)
                setattr(value, "room_ProtocolClass84", self)

    @property
    def room_DetailCode241(self):
        return self.__room_DetailCode241

    @room_DetailCode241.setter
    def room_DetailCode241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode241", None)
        self.__room_DetailCode241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_State240"):
                opp_val = getattr(old_value, "room_State240", None)
                if opp_val == self:
                    setattr(old_value, "room_State240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_State240"):
                opp_val = getattr(value, "room_State240", None)
                setattr(value, "room_State240", self)

    @property
    def room_DetailCode46(self):
        return self.__room_DetailCode46

    @room_DetailCode46.setter
    def room_DetailCode46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode46", None)
        self.__room_DetailCode46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass45"):
                opp_val = getattr(old_value, "room_DataClass45", None)
                if opp_val == self:
                    setattr(old_value, "room_DataClass45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass45"):
                opp_val = getattr(value, "room_DataClass45", None)
                setattr(value, "room_DataClass45", self)

class room_SPPRef(InterfaceItem):

    pass
class StructureClass:

    pass
class room_ActorContainerClass(StructureClass):

    pass
class room_LayerConnection:

    pass
class RoomClass:

    pass
class room_DataType(RoomClass):

    pass
class room_StructureClass(RoomClass):

    pass
class room_RoomClass:

    def __init__(self, name: str, room_RoomClass: "room_Documentation" = None):
        self.name = name
        self.room_RoomClass = room_RoomClass
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_RoomClass(self):
        return self.__room_RoomClass

    @room_RoomClass.setter
    def room_RoomClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomClass__room_RoomClass", None)
        self.__room_RoomClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation18"):
                opp_val = getattr(old_value, "room_Documentation18", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation18"):
                opp_val = getattr(value, "room_Documentation18", None)
                setattr(value, "room_Documentation18", self)

class room_LogicalSystem(StructureClass):

    pass
class room_SubSystemClass(ActorContainerClass):

    pass
class room_ActorClass(ActorContainerClass):

    def __init__(self, abstract: bool, commType: str, room_ActorClass: "room_RoomModel" = None, room_ActorClass139: "room_ActorClass" = None, room_ActorClass137: "room_ActorClass" = None, room_ActorClass141: set["room_Port"] = None, room_ActorClass146: set["room_Port"] = None, room_ActorClass149: set["room_ExternalPort"] = None, room_ActorClass151: set["room_ServiceImplementation"] = None, room_ActorClass153: set["room_SAPRef"] = None, room_ActorClass155: set["room_Attribute"] = None, room_ActorClass158: "room_Documentation" = None, room_ActorClass161: set["room_Annotation"] = None, room_ActorClass164: set["room_StandardOperation"] = None, room_ActorClass167: "room_StateGraph" = None, room_ActorClass143: "room_Documentation" = None, room_ActorClass230: "room_ActorRef" = None):
        self.abstract = abstract
        self.commType = commType
        self.room_ActorClass = room_ActorClass
        self.room_ActorClass139 = room_ActorClass139
        self.room_ActorClass137 = room_ActorClass137
        self.room_ActorClass141 = room_ActorClass141 if room_ActorClass141 is not None else set()
        self.room_ActorClass146 = room_ActorClass146 if room_ActorClass146 is not None else set()
        self.room_ActorClass149 = room_ActorClass149 if room_ActorClass149 is not None else set()
        self.room_ActorClass151 = room_ActorClass151 if room_ActorClass151 is not None else set()
        self.room_ActorClass153 = room_ActorClass153 if room_ActorClass153 is not None else set()
        self.room_ActorClass155 = room_ActorClass155 if room_ActorClass155 is not None else set()
        self.room_ActorClass158 = room_ActorClass158
        self.room_ActorClass161 = room_ActorClass161 if room_ActorClass161 is not None else set()
        self.room_ActorClass164 = room_ActorClass164 if room_ActorClass164 is not None else set()
        self.room_ActorClass167 = room_ActorClass167
        self.room_ActorClass143 = room_ActorClass143
        self.room_ActorClass230 = room_ActorClass230
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def commType(self) -> str:
        return self.__commType

    @commType.setter
    def commType(self, commType: str):
        self.__commType = commType

    @property
    def room_ActorClass230(self):
        return self.__room_ActorClass230

    @room_ActorClass230.setter
    def room_ActorClass230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass230", None)
        self.__room_ActorClass230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorRef229"):
                opp_val = getattr(old_value, "room_ActorRef229", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorRef229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorRef229"):
                opp_val = getattr(value, "room_ActorRef229", None)
                setattr(value, "room_ActorRef229", self)

    @property
    def room_ActorClass151(self):
        return self.__room_ActorClass151

    @room_ActorClass151.setter
    def room_ActorClass151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass151", None)
        self.__room_ActorClass151 = value if value is not None else set()
        
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
    def room_ActorClass137(self):
        return self.__room_ActorClass137

    @room_ActorClass137.setter
    def room_ActorClass137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass137", None)
        self.__room_ActorClass137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass139"):
                opp_val = getattr(old_value, "room_ActorClass139", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass139"):
                opp_val = getattr(value, "room_ActorClass139", None)
                setattr(value, "room_ActorClass139", self)

    @property
    def room_ActorClass167(self):
        return self.__room_ActorClass167

    @room_ActorClass167.setter
    def room_ActorClass167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass167", None)
        self.__room_ActorClass167 = value
        
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
    def room_ActorClass149(self):
        return self.__room_ActorClass149

    @room_ActorClass149.setter
    def room_ActorClass149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass149", None)
        self.__room_ActorClass149 = value if value is not None else set()
        
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
                    

    @property
    def room_ActorClass161(self):
        return self.__room_ActorClass161

    @room_ActorClass161.setter
    def room_ActorClass161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass161", None)
        self.__room_ActorClass161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Annotation162"):
                    opp_val = getattr(item, "room_Annotation162", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Annotation162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Annotation162"):
                    opp_val = getattr(item, "room_Annotation162", None)
                    
                    setattr(item, "room_Annotation162", self)
                    

    @property
    def room_ActorClass155(self):
        return self.__room_ActorClass155

    @room_ActorClass155.setter
    def room_ActorClass155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass155", None)
        self.__room_ActorClass155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Attribute156"):
                    opp_val = getattr(item, "room_Attribute156", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Attribute156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Attribute156"):
                    opp_val = getattr(item, "room_Attribute156", None)
                    
                    setattr(item, "room_Attribute156", self)
                    

    @property
    def room_ActorClass164(self):
        return self.__room_ActorClass164

    @room_ActorClass164.setter
    def room_ActorClass164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass164", None)
        self.__room_ActorClass164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_StandardOperation165"):
                    opp_val = getattr(item, "room_StandardOperation165", None)
                    
                    if opp_val == self:
                        setattr(item, "room_StandardOperation165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_StandardOperation165"):
                    opp_val = getattr(item, "room_StandardOperation165", None)
                    
                    setattr(item, "room_StandardOperation165", self)
                    

    @property
    def room_ActorClass141(self):
        return self.__room_ActorClass141

    @room_ActorClass141.setter
    def room_ActorClass141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass141", None)
        self.__room_ActorClass141 = value if value is not None else set()
        
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
    def room_ActorClass146(self):
        return self.__room_ActorClass146

    @room_ActorClass146.setter
    def room_ActorClass146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass146", None)
        self.__room_ActorClass146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Port147"):
                    opp_val = getattr(item, "room_Port147", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Port147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Port147"):
                    opp_val = getattr(item, "room_Port147", None)
                    
                    setattr(item, "room_Port147", self)
                    

    @property
    def room_ActorClass143(self):
        return self.__room_ActorClass143

    @room_ActorClass143.setter
    def room_ActorClass143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass143", None)
        self.__room_ActorClass143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation144"):
                opp_val = getattr(old_value, "room_Documentation144", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation144"):
                opp_val = getattr(value, "room_Documentation144", None)
                setattr(value, "room_Documentation144", self)

    @property
    def room_ActorClass158(self):
        return self.__room_ActorClass158

    @room_ActorClass158.setter
    def room_ActorClass158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass158", None)
        self.__room_ActorClass158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation159"):
                opp_val = getattr(old_value, "room_Documentation159", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation159"):
                opp_val = getattr(value, "room_Documentation159", None)
                setattr(value, "room_Documentation159", self)

    @property
    def room_ActorClass153(self):
        return self.__room_ActorClass153

    @room_ActorClass153.setter
    def room_ActorClass153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass153", None)
        self.__room_ActorClass153 = value if value is not None else set()
        
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
    def room_ActorClass139(self):
        return self.__room_ActorClass139

    @room_ActorClass139.setter
    def room_ActorClass139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass139", None)
        self.__room_ActorClass139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass137"):
                opp_val = getattr(old_value, "room_ActorClass137", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass137"):
                opp_val = getattr(value, "room_ActorClass137", None)
                setattr(value, "room_ActorClass137", self)

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
            if hasattr(old_value, "room_RoomModel12"):
                opp_val = getattr(old_value, "room_RoomModel12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RoomModel12"):
                opp_val = getattr(value, "room_RoomModel12", None)
                if opp_val is None:
                    setattr(value, "room_RoomModel12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_GeneralProtocolClass(RoomClass):

    pass
class room_DataClass(ComplexType):

    pass
class room_ExternalType(ComplexType):

    def __init__(self, targetName: str, room_ExternalType: "room_RoomModel" = None):
        self.targetName = targetName
        self.room_ExternalType = room_ExternalType
        
    @property
    def targetName(self) -> str:
        return self.__targetName

    @targetName.setter
    def targetName(self, targetName: str):
        self.__targetName = targetName

    @property
    def room_ExternalType(self):
        return self.__room_ExternalType

    @room_ExternalType.setter
    def room_ExternalType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ExternalType__room_ExternalType", None)
        self.__room_ExternalType = value
        
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

class room_PrimitiveType(DataType):

    def __init__(self, type: str, targetName: str, castName: str, defaultValueLiteral: str, room_PrimitiveType: "room_RoomModel" = None):
        self.type = type
        self.targetName = targetName
        self.castName = castName
        self.defaultValueLiteral = defaultValueLiteral
        self.room_PrimitiveType = room_PrimitiveType
        
    @property
    def castName(self) -> str:
        return self.__castName

    @castName.setter
    def castName(self, castName: str):
        self.__castName = castName

    @property
    def targetName(self) -> str:
        return self.__targetName

    @targetName.setter
    def targetName(self, targetName: str):
        self.__targetName = targetName

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

    @property
    def room_PrimitiveType(self):
        return self.__room_PrimitiveType

    @room_PrimitiveType.setter
    def room_PrimitiveType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_PrimitiveType__room_PrimitiveType", None)
        self.__room_PrimitiveType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RoomModel4"):
                opp_val = getattr(old_value, "room_RoomModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RoomModel4"):
                opp_val = getattr(value, "room_RoomModel4", None)
                if opp_val is None:
                    setattr(value, "room_RoomModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_Import:

    def __init__(self, importURI: str, importedNamespace: str, room_Import: "room_RoomModel" = None):
        self.importURI = importURI
        self.importedNamespace = importedNamespace
        self.room_Import = room_Import
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

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
            if hasattr(old_value, "room_RoomModel2"):
                opp_val = getattr(old_value, "room_RoomModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RoomModel2"):
                opp_val = getattr(value, "room_RoomModel2", None)
                if opp_val is None:
                    setattr(value, "room_RoomModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_Documentation:

    def __init__(self, text: str, room_Documentation: "room_RoomModel" = None, room_Documentation18: "room_RoomClass" = None, room_Documentation62: "room_Attribute" = None, room_Documentation70: "room_Operation" = None, room_Documentation111: "room_Message" = None, room_Documentation159: "room_ActorClass" = None, room_Documentation144: "room_ActorClass" = None, room_Documentation189: "room_ActorContainerRef" = None, room_Documentation173: "room_Port" = None, room_Documentation232: "room_State" = None, room_Documentation260: "room_ChoicePoint" = None, room_Documentation265: "room_Transition" = None, room_Documentation281: "room_RefinedTransition" = None):
        self.text = text
        self.room_Documentation = room_Documentation
        self.room_Documentation18 = room_Documentation18
        self.room_Documentation62 = room_Documentation62
        self.room_Documentation70 = room_Documentation70
        self.room_Documentation111 = room_Documentation111
        self.room_Documentation159 = room_Documentation159
        self.room_Documentation144 = room_Documentation144
        self.room_Documentation189 = room_Documentation189
        self.room_Documentation173 = room_Documentation173
        self.room_Documentation232 = room_Documentation232
        self.room_Documentation260 = room_Documentation260
        self.room_Documentation265 = room_Documentation265
        self.room_Documentation281 = room_Documentation281
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def room_Documentation159(self):
        return self.__room_Documentation159

    @room_Documentation159.setter
    def room_Documentation159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation159", None)
        self.__room_Documentation159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass158"):
                opp_val = getattr(old_value, "room_ActorClass158", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass158"):
                opp_val = getattr(value, "room_ActorClass158", None)
                setattr(value, "room_ActorClass158", self)

    @property
    def room_Documentation232(self):
        return self.__room_Documentation232

    @room_Documentation232.setter
    def room_Documentation232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation232", None)
        self.__room_Documentation232 = value
        
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

    @property
    def room_Documentation144(self):
        return self.__room_Documentation144

    @room_Documentation144.setter
    def room_Documentation144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation144", None)
        self.__room_Documentation144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass143"):
                opp_val = getattr(old_value, "room_ActorClass143", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass143"):
                opp_val = getattr(value, "room_ActorClass143", None)
                setattr(value, "room_ActorClass143", self)

    @property
    def room_Documentation62(self):
        return self.__room_Documentation62

    @room_Documentation62.setter
    def room_Documentation62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation62", None)
        self.__room_Documentation62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Attribute61"):
                opp_val = getattr(old_value, "room_Attribute61", None)
                if opp_val == self:
                    setattr(old_value, "room_Attribute61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Attribute61"):
                opp_val = getattr(value, "room_Attribute61", None)
                setattr(value, "room_Attribute61", self)

    @property
    def room_Documentation173(self):
        return self.__room_Documentation173

    @room_Documentation173.setter
    def room_Documentation173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation173", None)
        self.__room_Documentation173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Port172"):
                opp_val = getattr(old_value, "room_Port172", None)
                if opp_val == self:
                    setattr(old_value, "room_Port172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Port172"):
                opp_val = getattr(value, "room_Port172", None)
                setattr(value, "room_Port172", self)

    @property
    def room_Documentation281(self):
        return self.__room_Documentation281

    @room_Documentation281.setter
    def room_Documentation281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation281", None)
        self.__room_Documentation281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RefinedTransition280"):
                opp_val = getattr(old_value, "room_RefinedTransition280", None)
                if opp_val == self:
                    setattr(old_value, "room_RefinedTransition280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RefinedTransition280"):
                opp_val = getattr(value, "room_RefinedTransition280", None)
                setattr(value, "room_RefinedTransition280", self)

    @property
    def room_Documentation(self):
        return self.__room_Documentation

    @room_Documentation.setter
    def room_Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation", None)
        self.__room_Documentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RoomModel"):
                opp_val = getattr(old_value, "room_RoomModel", None)
                if opp_val == self:
                    setattr(old_value, "room_RoomModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RoomModel"):
                opp_val = getattr(value, "room_RoomModel", None)
                setattr(value, "room_RoomModel", self)

    @property
    def room_Documentation260(self):
        return self.__room_Documentation260

    @room_Documentation260.setter
    def room_Documentation260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation260", None)
        self.__room_Documentation260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ChoicePoint259"):
                opp_val = getattr(old_value, "room_ChoicePoint259", None)
                if opp_val == self:
                    setattr(old_value, "room_ChoicePoint259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ChoicePoint259"):
                opp_val = getattr(value, "room_ChoicePoint259", None)
                setattr(value, "room_ChoicePoint259", self)

    @property
    def room_Documentation189(self):
        return self.__room_Documentation189

    @room_Documentation189.setter
    def room_Documentation189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation189", None)
        self.__room_Documentation189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorContainerRef"):
                opp_val = getattr(old_value, "room_ActorContainerRef", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorContainerRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorContainerRef"):
                opp_val = getattr(value, "room_ActorContainerRef", None)
                setattr(value, "room_ActorContainerRef", self)

    @property
    def room_Documentation70(self):
        return self.__room_Documentation70

    @room_Documentation70.setter
    def room_Documentation70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation70", None)
        self.__room_Documentation70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Operation69"):
                opp_val = getattr(old_value, "room_Operation69", None)
                if opp_val == self:
                    setattr(old_value, "room_Operation69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Operation69"):
                opp_val = getattr(value, "room_Operation69", None)
                setattr(value, "room_Operation69", self)

    @property
    def room_Documentation111(self):
        return self.__room_Documentation111

    @room_Documentation111.setter
    def room_Documentation111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation111", None)
        self.__room_Documentation111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Message110"):
                opp_val = getattr(old_value, "room_Message110", None)
                if opp_val == self:
                    setattr(old_value, "room_Message110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Message110"):
                opp_val = getattr(value, "room_Message110", None)
                setattr(value, "room_Message110", self)

    @property
    def room_Documentation265(self):
        return self.__room_Documentation265

    @room_Documentation265.setter
    def room_Documentation265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation265", None)
        self.__room_Documentation265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Transition264"):
                opp_val = getattr(old_value, "room_Transition264", None)
                if opp_val == self:
                    setattr(old_value, "room_Transition264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Transition264"):
                opp_val = getattr(value, "room_Transition264", None)
                setattr(value, "room_Transition264", self)

    @property
    def room_Documentation18(self):
        return self.__room_Documentation18

    @room_Documentation18.setter
    def room_Documentation18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation18", None)
        self.__room_Documentation18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RoomClass"):
                opp_val = getattr(old_value, "room_RoomClass", None)
                if opp_val == self:
                    setattr(old_value, "room_RoomClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RoomClass"):
                opp_val = getattr(value, "room_RoomClass", None)
                setattr(value, "room_RoomClass", self)

class room_RoomModel:

    def __init__(self, name: str, room_RoomModel: "room_Documentation" = None, room_RoomModel2: set["room_Import"] = None, room_RoomModel4: set["room_PrimitiveType"] = None, room_RoomModel6: set["room_ExternalType"] = None, room_RoomModel8: set["room_DataClass"] = None, room_RoomModel10: set["room_GeneralProtocolClass"] = None, room_RoomModel12: set["room_ActorClass"] = None, room_RoomModel14: set["room_SubSystemClass"] = None, room_RoomModel16: set["room_LogicalSystem"] = None):
        self.name = name
        self.room_RoomModel = room_RoomModel
        self.room_RoomModel2 = room_RoomModel2 if room_RoomModel2 is not None else set()
        self.room_RoomModel4 = room_RoomModel4 if room_RoomModel4 is not None else set()
        self.room_RoomModel6 = room_RoomModel6 if room_RoomModel6 is not None else set()
        self.room_RoomModel8 = room_RoomModel8 if room_RoomModel8 is not None else set()
        self.room_RoomModel10 = room_RoomModel10 if room_RoomModel10 is not None else set()
        self.room_RoomModel12 = room_RoomModel12 if room_RoomModel12 is not None else set()
        self.room_RoomModel14 = room_RoomModel14 if room_RoomModel14 is not None else set()
        self.room_RoomModel16 = room_RoomModel16 if room_RoomModel16 is not None else set()
        
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
                if hasattr(item, "room_GeneralProtocolClass"):
                    opp_val = getattr(item, "room_GeneralProtocolClass", None)
                    
                    if opp_val == self:
                        setattr(item, "room_GeneralProtocolClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_GeneralProtocolClass"):
                    opp_val = getattr(item, "room_GeneralProtocolClass", None)
                    
                    setattr(item, "room_GeneralProtocolClass", self)
                    

    @property
    def room_RoomModel14(self):
        return self.__room_RoomModel14

    @room_RoomModel14.setter
    def room_RoomModel14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomModel__room_RoomModel14", None)
        self.__room_RoomModel14 = value if value is not None else set()
        
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
                if hasattr(item, "room_ExternalType"):
                    opp_val = getattr(item, "room_ExternalType", None)
                    
                    if opp_val == self:
                        setattr(item, "room_ExternalType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_ExternalType"):
                    opp_val = getattr(item, "room_ExternalType", None)
                    
                    setattr(item, "room_ExternalType", self)
                    

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
    def room_RoomModel12(self):
        return self.__room_RoomModel12

    @room_RoomModel12.setter
    def room_RoomModel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomModel__room_RoomModel12", None)
        self.__room_RoomModel12 = value if value is not None else set()
        
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
    def room_RoomModel16(self):
        return self.__room_RoomModel16

    @room_RoomModel16.setter
    def room_RoomModel16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomModel__room_RoomModel16", None)
        self.__room_RoomModel16 = value if value is not None else set()
        
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
    def room_RoomModel(self):
        return self.__room_RoomModel

    @room_RoomModel.setter
    def room_RoomModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RoomModel__room_RoomModel", None)
        self.__room_RoomModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation"):
                opp_val = getattr(old_value, "room_Documentation", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation"):
                opp_val = getattr(value, "room_Documentation", None)
                setattr(value, "room_Documentation", self)

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
                if hasattr(item, "room_PrimitiveType"):
                    opp_val = getattr(item, "room_PrimitiveType", None)
                    
                    if opp_val == self:
                        setattr(item, "room_PrimitiveType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_PrimitiveType"):
                    opp_val = getattr(item, "room_PrimitiveType", None)
                    
                    setattr(item, "room_PrimitiveType", self)
                    
