from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CommunicationType(Enum):
    EVENT_DRIVEN = "EVENT_DRIVEN"
    DATA_DRIVEN = "DATA_DRIVEN"
    SYNCHRONOUS = "SYNCHRONOUS"
class ActorCommunicationType(Enum):
    EVENT_DRIVEN = "EVENT_DRIVEN"
    DATA_DRIVEN = "DATA_DRIVEN"
    ASYNCHRONOUS = "ASYNCHRONOUS"
    SYNCHRONOUS = "SYNCHRONOUS"


############################################
# Definition of Classes
############################################

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
            if hasattr(old_value, "room_Annotation276"):
                opp_val = getattr(old_value, "room_Annotation276", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Annotation276"):
                opp_val = getattr(value, "room_Annotation276", None)
                if opp_val is None:
                    setattr(value, "room_Annotation276", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_Guard:

    pass
class room_MessageFromIf:

    pass
class TransitionTerminal:

    pass
class room_SubStateTrPointTerminal(TransitionTerminal):

    pass
class room_ChoicepointTerminal(TransitionTerminal):

    pass
class room_TrPointTerminal(TransitionTerminal):

    pass
class room_StateTerminal(TransitionTerminal):

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

    def __init__(self, name: str, room_BaseState: "room_RefinedState" = None, room_BaseState252: "room_StateTerminal" = None, room_BaseState259: "room_SubStateTrPointTerminal" = None):
        self.name = name
        self.room_BaseState = room_BaseState
        self.room_BaseState252 = room_BaseState252
        self.room_BaseState259 = room_BaseState259
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_BaseState259(self):
        return self.__room_BaseState259

    @room_BaseState259.setter
    def room_BaseState259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_BaseState__room_BaseState259", None)
        self.__room_BaseState259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SubStateTrPointTerminal258"):
                opp_val = getattr(old_value, "room_SubStateTrPointTerminal258", None)
                if opp_val == self:
                    setattr(old_value, "room_SubStateTrPointTerminal258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SubStateTrPointTerminal258"):
                opp_val = getattr(value, "room_SubStateTrPointTerminal258", None)
                setattr(value, "room_SubStateTrPointTerminal258", self)

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
    def room_BaseState252(self):
        return self.__room_BaseState252

    @room_BaseState252.setter
    def room_BaseState252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_BaseState__room_BaseState252", None)
        self.__room_BaseState252 = value
        
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

class StateGraphNode:

    pass
class room_ChoicePoint(StateGraphNode):

    def __init__(self, name: str, room_ChoicePoint: "room_StateGraph" = None, room_ChoicePoint234: "room_Documentation" = None, room_ChoicePoint261: "room_ChoicepointTerminal" = None):
        self.name = name
        self.room_ChoicePoint = room_ChoicePoint
        self.room_ChoicePoint234 = room_ChoicePoint234
        self.room_ChoicePoint261 = room_ChoicePoint261
        
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
            if hasattr(old_value, "room_StateGraph229"):
                opp_val = getattr(old_value, "room_StateGraph229", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph229"):
                opp_val = getattr(value, "room_StateGraph229", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph229", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_ChoicePoint261(self):
        return self.__room_ChoicePoint261

    @room_ChoicePoint261.setter
    def room_ChoicePoint261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ChoicePoint__room_ChoicePoint261", None)
        self.__room_ChoicePoint261 = value
        
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
    def room_ChoicePoint234(self):
        return self.__room_ChoicePoint234

    @room_ChoicePoint234.setter
    def room_ChoicePoint234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ChoicePoint__room_ChoicePoint234", None)
        self.__room_ChoicePoint234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation235"):
                opp_val = getattr(old_value, "room_Documentation235", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation235"):
                opp_val = getattr(value, "room_Documentation235", None)
                setattr(value, "room_Documentation235", self)

class room_TrPoint(StateGraphNode):

    def __init__(self, name: str, room_TrPoint: "room_StateGraph" = None, room_TrPoint254: "room_TrPointTerminal" = None, room_TrPoint256: "room_SubStateTrPointTerminal" = None):
        self.name = name
        self.room_TrPoint = room_TrPoint
        self.room_TrPoint254 = room_TrPoint254
        self.room_TrPoint256 = room_TrPoint256
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_TrPoint254(self):
        return self.__room_TrPoint254

    @room_TrPoint254.setter
    def room_TrPoint254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_TrPoint__room_TrPoint254", None)
        self.__room_TrPoint254 = value
        
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
    def room_TrPoint256(self):
        return self.__room_TrPoint256

    @room_TrPoint256.setter
    def room_TrPoint256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_TrPoint__room_TrPoint256", None)
        self.__room_TrPoint256 = value
        
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
            if hasattr(old_value, "room_StateGraph227"):
                opp_val = getattr(old_value, "room_StateGraph227", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph227"):
                opp_val = getattr(value, "room_StateGraph227", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph227", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_State(StateGraphNode):

    def __init__(self, room_State218: "room_DetailCode" = None, room_State: "room_Documentation" = None, room_State212: "room_DetailCode" = None, room_State215: "room_DetailCode" = None, room_State221: "room_StateGraph" = None, room_State225: "room_StateGraph" = None):
        self.room_State218 = room_State218
        self.room_State = room_State
        self.room_State212 = room_State212
        self.room_State215 = room_State215
        self.room_State221 = room_State221
        self.room_State225 = room_State225
        
    @property
    def room_State218(self):
        return self.__room_State218

    @room_State218.setter
    def room_State218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State218", None)
        self.__room_State218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode219"):
                opp_val = getattr(old_value, "room_DetailCode219", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode219"):
                opp_val = getattr(value, "room_DetailCode219", None)
                setattr(value, "room_DetailCode219", self)

    @property
    def room_State215(self):
        return self.__room_State215

    @room_State215.setter
    def room_State215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State215", None)
        self.__room_State215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode216"):
                opp_val = getattr(old_value, "room_DetailCode216", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode216"):
                opp_val = getattr(value, "room_DetailCode216", None)
                setattr(value, "room_DetailCode216", self)

    @property
    def room_State225(self):
        return self.__room_State225

    @room_State225.setter
    def room_State225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State225", None)
        self.__room_State225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph224"):
                opp_val = getattr(old_value, "room_StateGraph224", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph224"):
                opp_val = getattr(value, "room_StateGraph224", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph224", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_State221(self):
        return self.__room_State221

    @room_State221.setter
    def room_State221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State221", None)
        self.__room_State221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_StateGraph222"):
                opp_val = getattr(old_value, "room_StateGraph222", None)
                if opp_val == self:
                    setattr(old_value, "room_StateGraph222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph222"):
                opp_val = getattr(value, "room_StateGraph222", None)
                setattr(value, "room_StateGraph222", self)

    @property
    def room_State212(self):
        return self.__room_State212

    @room_State212.setter
    def room_State212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_State__room_State212", None)
        self.__room_State212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode213"):
                opp_val = getattr(old_value, "room_DetailCode213", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode213"):
                opp_val = getattr(value, "room_DetailCode213", None)
                setattr(value, "room_DetailCode213", self)

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
            if hasattr(old_value, "room_Documentation210"):
                opp_val = getattr(old_value, "room_Documentation210", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation210"):
                opp_val = getattr(value, "room_Documentation210", None)
                setattr(value, "room_Documentation210", self)

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

    def __init__(self, name: str, room_Transition: "room_StateGraph" = None, room_Transition237: "room_TransitionTerminal" = None, room_Transition239: "room_Documentation" = None, room_Transition242: "room_DetailCode" = None):
        self.name = name
        self.room_Transition = room_Transition
        self.room_Transition237 = room_Transition237
        self.room_Transition239 = room_Transition239
        self.room_Transition242 = room_Transition242
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_Transition239(self):
        return self.__room_Transition239

    @room_Transition239.setter
    def room_Transition239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Transition__room_Transition239", None)
        self.__room_Transition239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation240"):
                opp_val = getattr(old_value, "room_Documentation240", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation240"):
                opp_val = getattr(value, "room_Documentation240", None)
                setattr(value, "room_Documentation240", self)

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
            if hasattr(old_value, "room_StateGraph231"):
                opp_val = getattr(old_value, "room_StateGraph231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_StateGraph231"):
                opp_val = getattr(value, "room_StateGraph231", None)
                if opp_val is None:
                    setattr(value, "room_StateGraph231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Transition242(self):
        return self.__room_Transition242

    @room_Transition242.setter
    def room_Transition242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Transition__room_Transition242", None)
        self.__room_Transition242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode243"):
                opp_val = getattr(old_value, "room_DetailCode243", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode243"):
                opp_val = getattr(value, "room_DetailCode243", None)
                setattr(value, "room_DetailCode243", self)

    @property
    def room_Transition237(self):
        return self.__room_Transition237

    @room_Transition237.setter
    def room_Transition237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Transition__room_Transition237", None)
        self.__room_Transition237 = value
        
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
            if hasattr(old_value, "room_LogicalThread180"):
                opp_val = getattr(old_value, "room_LogicalThread180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_LogicalThread180"):
                opp_val = getattr(value, "room_LogicalThread180", None)
                if opp_val is None:
                    setattr(value, "room_LogicalThread180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_LogicalThread:

    def __init__(self, name: str, prio: int, room_LogicalThread: "room_SubSystemClass" = None, room_LogicalThread180: set["room_ActorInstancePath"] = None):
        self.name = name
        self.prio = prio
        self.room_LogicalThread = room_LogicalThread
        self.room_LogicalThread180 = room_LogicalThread180 if room_LogicalThread180 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def prio(self) -> int:
        return self.__prio

    @prio.setter
    def prio(self, prio: int):
        self.__prio = prio

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
            if hasattr(old_value, "room_SubSystemClass178"):
                opp_val = getattr(old_value, "room_SubSystemClass178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SubSystemClass178"):
                opp_val = getattr(value, "room_SubSystemClass178", None)
                if opp_val is None:
                    setattr(value, "room_SubSystemClass178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_LogicalThread180(self):
        return self.__room_LogicalThread180

    @room_LogicalThread180.setter
    def room_LogicalThread180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_LogicalThread__room_LogicalThread180", None)
        self.__room_LogicalThread180 = value if value is not None else set()
        
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

    def __init__(self, name: str, room_ActorContainerRef188: "room_BindingEndPoint" = None, room_ActorContainerRef197: "room_RefSAPoint" = None, room_ActorContainerRef: "room_Documentation" = None, room_ActorContainerRef202: "room_SPPoint" = None):
        self.name = name
        self.room_ActorContainerRef188 = room_ActorContainerRef188
        self.room_ActorContainerRef197 = room_ActorContainerRef197
        self.room_ActorContainerRef = room_ActorContainerRef
        self.room_ActorContainerRef202 = room_ActorContainerRef202
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_ActorContainerRef197(self):
        return self.__room_ActorContainerRef197

    @room_ActorContainerRef197.setter
    def room_ActorContainerRef197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorContainerRef__room_ActorContainerRef197", None)
        self.__room_ActorContainerRef197 = value
        
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
    def room_ActorContainerRef(self):
        return self.__room_ActorContainerRef

    @room_ActorContainerRef.setter
    def room_ActorContainerRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorContainerRef__room_ActorContainerRef", None)
        self.__room_ActorContainerRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation170"):
                opp_val = getattr(old_value, "room_Documentation170", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation170"):
                opp_val = getattr(value, "room_Documentation170", None)
                setattr(value, "room_Documentation170", self)

    @property
    def room_ActorContainerRef202(self):
        return self.__room_ActorContainerRef202

    @room_ActorContainerRef202.setter
    def room_ActorContainerRef202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorContainerRef__room_ActorContainerRef202", None)
        self.__room_ActorContainerRef202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SPPoint201"):
                opp_val = getattr(old_value, "room_SPPoint201", None)
                if opp_val == self:
                    setattr(old_value, "room_SPPoint201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SPPoint201"):
                opp_val = getattr(value, "room_SPPoint201", None)
                setattr(value, "room_SPPoint201", self)

    @property
    def room_ActorContainerRef188(self):
        return self.__room_ActorContainerRef188

    @room_ActorContainerRef188.setter
    def room_ActorContainerRef188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorContainerRef__room_ActorContainerRef188", None)
        self.__room_ActorContainerRef188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_BindingEndPoint187"):
                opp_val = getattr(old_value, "room_BindingEndPoint187", None)
                if opp_val == self:
                    setattr(old_value, "room_BindingEndPoint187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_BindingEndPoint187"):
                opp_val = getattr(value, "room_BindingEndPoint187", None)
                setattr(value, "room_BindingEndPoint187", self)

class room_SubSystemRef(ActorContainerRef):

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
class room_BindingEndPoint:

    pass
class room_StateGraph:

    pass
class room_Annotation:

    def __init__(self, name: str, room_Annotation: "room_ActorClass" = None, room_Annotation276: set["room_KeyValue"] = None):
        self.name = name
        self.room_Annotation = room_Annotation
        self.room_Annotation276 = room_Annotation276 if room_Annotation276 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_Annotation276(self):
        return self.__room_Annotation276

    @room_Annotation276.setter
    def room_Annotation276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Annotation__room_Annotation276", None)
        self.__room_Annotation276 = value if value is not None else set()
        
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
    def room_Annotation(self):
        return self.__room_Annotation

    @room_Annotation.setter
    def room_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Annotation__room_Annotation", None)
        self.__room_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass150"):
                opp_val = getattr(old_value, "room_ActorClass150", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass150"):
                opp_val = getattr(value, "room_ActorClass150", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass150", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class room_ServiceImplementation:

    pass
class room_ExternalPort:

    pass
class InterfaceItem:

    pass
class room_SAPRef(InterfaceItem):

    pass
class room_InterfaceItem:

    def __init__(self, name: str, room_InterfaceItem: "room_ProtocolClass" = None, room_InterfaceItem271: "room_MessageFromIf" = None):
        self.name = name
        self.room_InterfaceItem = room_InterfaceItem
        self.room_InterfaceItem271 = room_InterfaceItem271
        
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
            if hasattr(old_value, "room_ProtocolClass157"):
                opp_val = getattr(old_value, "room_ProtocolClass157", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass157"):
                opp_val = getattr(value, "room_ProtocolClass157", None)
                setattr(value, "room_ProtocolClass157", self)

    @property
    def room_InterfaceItem271(self):
        return self.__room_InterfaceItem271

    @room_InterfaceItem271.setter
    def room_InterfaceItem271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_InterfaceItem__room_InterfaceItem271", None)
        self.__room_InterfaceItem271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageFromIf270"):
                opp_val = getattr(old_value, "room_MessageFromIf270", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageFromIf270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageFromIf270"):
                opp_val = getattr(value, "room_MessageFromIf270", None)
                setattr(value, "room_MessageFromIf270", self)

class room_SemanticsRule:

    pass
class room_Port(InterfaceItem):

    def __init__(self, conjugated: bool, multiplicity: int, room_Port: "room_ActorClass" = None, room_Port159: "room_Documentation" = None, room_Port163: "room_ExternalPort" = None, room_Port136: "room_ActorClass" = None, room_Port191: "room_BindingEndPoint" = None, room_Port176: "room_SubSystemClass" = None):
        self.conjugated = conjugated
        self.multiplicity = multiplicity
        self.room_Port = room_Port
        self.room_Port159 = room_Port159
        self.room_Port163 = room_Port163
        self.room_Port136 = room_Port136
        self.room_Port191 = room_Port191
        self.room_Port176 = room_Port176
        
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
    def room_Port163(self):
        return self.__room_Port163

    @room_Port163.setter
    def room_Port163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port163", None)
        self.__room_Port163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ExternalPort162"):
                opp_val = getattr(old_value, "room_ExternalPort162", None)
                if opp_val == self:
                    setattr(old_value, "room_ExternalPort162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ExternalPort162"):
                opp_val = getattr(value, "room_ExternalPort162", None)
                setattr(value, "room_ExternalPort162", self)

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
            if hasattr(old_value, "room_ActorClass130"):
                opp_val = getattr(old_value, "room_ActorClass130", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass130"):
                opp_val = getattr(value, "room_ActorClass130", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass130", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Port191(self):
        return self.__room_Port191

    @room_Port191.setter
    def room_Port191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port191", None)
        self.__room_Port191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_BindingEndPoint190"):
                opp_val = getattr(old_value, "room_BindingEndPoint190", None)
                if opp_val == self:
                    setattr(old_value, "room_BindingEndPoint190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_BindingEndPoint190"):
                opp_val = getattr(value, "room_BindingEndPoint190", None)
                setattr(value, "room_BindingEndPoint190", self)

    @property
    def room_Port159(self):
        return self.__room_Port159

    @room_Port159.setter
    def room_Port159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port159", None)
        self.__room_Port159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation160"):
                opp_val = getattr(old_value, "room_Documentation160", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation160"):
                opp_val = getattr(value, "room_Documentation160", None)
                setattr(value, "room_Documentation160", self)

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
            if hasattr(old_value, "room_SubSystemClass175"):
                opp_val = getattr(old_value, "room_SubSystemClass175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SubSystemClass175"):
                opp_val = getattr(value, "room_SubSystemClass175", None)
                if opp_val is None:
                    setattr(value, "room_SubSystemClass175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Port136(self):
        return self.__room_Port136

    @room_Port136.setter
    def room_Port136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Port__room_Port136", None)
        self.__room_Port136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass135"):
                opp_val = getattr(old_value, "room_ActorClass135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass135"):
                opp_val = getattr(value, "room_ActorClass135", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isReplicated(self) -> bool:
        # TODO: Implement isReplicated method
        pass

class ActorContainerClass:

    pass
class room_MessageHandler:

    pass
class room_ProtocolSemantics:

    pass
class room_PortClass:

    pass
class room_Operation:

    def __init__(self, name: str, room_Operation67: "room_DetailCode" = None, room_Operation: set["room_VarDecl"] = None, room_Operation61: "room_RefableType" = None, room_Operation64: "room_Documentation" = None):
        self.name = name
        self.room_Operation67 = room_Operation67
        self.room_Operation = room_Operation if room_Operation is not None else set()
        self.room_Operation61 = room_Operation61
        self.room_Operation64 = room_Operation64
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "room_VarDecl59"):
                    opp_val = getattr(item, "room_VarDecl59", None)
                    
                    if opp_val == self:
                        setattr(item, "room_VarDecl59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_VarDecl59"):
                    opp_val = getattr(item, "room_VarDecl59", None)
                    
                    setattr(item, "room_VarDecl59", self)
                    

    @property
    def room_Operation67(self):
        return self.__room_Operation67

    @room_Operation67.setter
    def room_Operation67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation67", None)
        self.__room_Operation67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode68"):
                opp_val = getattr(old_value, "room_DetailCode68", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode68"):
                opp_val = getattr(value, "room_DetailCode68", None)
                setattr(value, "room_DetailCode68", self)

    @property
    def room_Operation61(self):
        return self.__room_Operation61

    @room_Operation61.setter
    def room_Operation61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation61", None)
        self.__room_Operation61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RefableType62"):
                opp_val = getattr(old_value, "room_RefableType62", None)
                if opp_val == self:
                    setattr(old_value, "room_RefableType62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RefableType62"):
                opp_val = getattr(value, "room_RefableType62", None)
                setattr(value, "room_RefableType62", self)

    @property
    def room_Operation64(self):
        return self.__room_Operation64

    @room_Operation64.setter
    def room_Operation64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Operation__room_Operation64", None)
        self.__room_Operation64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation65"):
                opp_val = getattr(old_value, "room_Documentation65", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation65"):
                opp_val = getattr(value, "room_Documentation65", None)
                setattr(value, "room_Documentation65", self)

class room_Message:

    def __init__(self, priv: bool, name: str, room_Message: "room_PortOperation" = None, room_Message87: "room_ProtocolClass" = None, room_Message84: "room_ProtocolClass" = None, room_Message114: "room_MessageHandler" = None, room_Message96: "room_VarDecl" = None, room_Message99: "room_Documentation" = None, room_Message122: "room_SemanticsRule" = None, room_Message268: "room_MessageFromIf" = None):
        self.priv = priv
        self.name = name
        self.room_Message = room_Message
        self.room_Message87 = room_Message87
        self.room_Message84 = room_Message84
        self.room_Message114 = room_Message114
        self.room_Message96 = room_Message96
        self.room_Message99 = room_Message99
        self.room_Message122 = room_Message122
        self.room_Message268 = room_Message268
        
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
    def room_Message87(self):
        return self.__room_Message87

    @room_Message87.setter
    def room_Message87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message87", None)
        self.__room_Message87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass86"):
                opp_val = getattr(old_value, "room_ProtocolClass86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass86"):
                opp_val = getattr(value, "room_ProtocolClass86", None)
                if opp_val is None:
                    setattr(value, "room_ProtocolClass86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Message84(self):
        return self.__room_Message84

    @room_Message84.setter
    def room_Message84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message84", None)
        self.__room_Message84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass83"):
                opp_val = getattr(old_value, "room_ProtocolClass83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass83"):
                opp_val = getattr(value, "room_ProtocolClass83", None)
                if opp_val is None:
                    setattr(value, "room_ProtocolClass83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Message99(self):
        return self.__room_Message99

    @room_Message99.setter
    def room_Message99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message99", None)
        self.__room_Message99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation100"):
                opp_val = getattr(old_value, "room_Documentation100", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation100"):
                opp_val = getattr(value, "room_Documentation100", None)
                setattr(value, "room_Documentation100", self)

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
    def room_Message122(self):
        return self.__room_Message122

    @room_Message122.setter
    def room_Message122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message122", None)
        self.__room_Message122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_SemanticsRule121"):
                opp_val = getattr(old_value, "room_SemanticsRule121", None)
                if opp_val == self:
                    setattr(old_value, "room_SemanticsRule121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_SemanticsRule121"):
                opp_val = getattr(value, "room_SemanticsRule121", None)
                setattr(value, "room_SemanticsRule121", self)

    @property
    def room_Message268(self):
        return self.__room_Message268

    @room_Message268.setter
    def room_Message268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message268", None)
        self.__room_Message268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageFromIf267"):
                opp_val = getattr(old_value, "room_MessageFromIf267", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageFromIf267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageFromIf267"):
                opp_val = getattr(value, "room_MessageFromIf267", None)
                setattr(value, "room_MessageFromIf267", self)

    @property
    def room_Message114(self):
        return self.__room_Message114

    @room_Message114.setter
    def room_Message114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message114", None)
        self.__room_Message114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageHandler113"):
                opp_val = getattr(old_value, "room_MessageHandler113", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageHandler113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageHandler113"):
                opp_val = getattr(value, "room_MessageHandler113", None)
                setattr(value, "room_MessageHandler113", self)

    @property
    def room_Message96(self):
        return self.__room_Message96

    @room_Message96.setter
    def room_Message96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Message__room_Message96", None)
        self.__room_Message96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_VarDecl97"):
                opp_val = getattr(old_value, "room_VarDecl97", None)
                if opp_val == self:
                    setattr(old_value, "room_VarDecl97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_VarDecl97"):
                opp_val = getattr(value, "room_VarDecl97", None)
                setattr(value, "room_VarDecl97", self)

class Operation:

    pass
class room_PortOperation(Operation):

    pass
class ComplexType:

    pass
class room_StandardOperation(Operation):

    pass
class room_Attribute:

    def __init__(self, name: str, size: int, defaultValueLiteral: str, room_Attribute: "room_DataClass" = None, room_Attribute53: "room_RefableType" = None, room_Attribute56: "room_Documentation" = None, room_Attribute106: "room_PortClass" = None, room_Attribute145: "room_ActorClass" = None):
        self.name = name
        self.size = size
        self.defaultValueLiteral = defaultValueLiteral
        self.room_Attribute = room_Attribute
        self.room_Attribute53 = room_Attribute53
        self.room_Attribute56 = room_Attribute56
        self.room_Attribute106 = room_Attribute106
        self.room_Attribute145 = room_Attribute145
        
    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

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
    def room_Attribute145(self):
        return self.__room_Attribute145

    @room_Attribute145.setter
    def room_Attribute145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute145", None)
        self.__room_Attribute145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass144"):
                opp_val = getattr(old_value, "room_ActorClass144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass144"):
                opp_val = getattr(value, "room_ActorClass144", None)
                if opp_val is None:
                    setattr(value, "room_ActorClass144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Attribute53(self):
        return self.__room_Attribute53

    @room_Attribute53.setter
    def room_Attribute53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute53", None)
        self.__room_Attribute53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_RefableType54"):
                opp_val = getattr(old_value, "room_RefableType54", None)
                if opp_val == self:
                    setattr(old_value, "room_RefableType54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RefableType54"):
                opp_val = getattr(value, "room_RefableType54", None)
                setattr(value, "room_RefableType54", self)

    @property
    def room_Attribute106(self):
        return self.__room_Attribute106

    @room_Attribute106.setter
    def room_Attribute106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute106", None)
        self.__room_Attribute106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_PortClass105"):
                opp_val = getattr(old_value, "room_PortClass105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortClass105"):
                opp_val = getattr(value, "room_PortClass105", None)
                if opp_val is None:
                    setattr(value, "room_PortClass105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_Attribute56(self):
        return self.__room_Attribute56

    @room_Attribute56.setter
    def room_Attribute56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Attribute__room_Attribute56", None)
        self.__room_Attribute56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation57"):
                opp_val = getattr(old_value, "room_Documentation57", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation57"):
                opp_val = getattr(value, "room_Documentation57", None)
                setattr(value, "room_Documentation57", self)

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
            if hasattr(old_value, "room_DataClass49"):
                opp_val = getattr(old_value, "room_DataClass49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass49"):
                opp_val = getattr(value, "room_DataClass49", None)
                if opp_val is None:
                    setattr(value, "room_DataClass49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DataType:

    pass
class room_ComplexType(DataType):

    pass
class room_RefableType:

    def __init__(self, ref: bool, room_RefableType: "room_VarDecl" = None, room_RefableType35: "room_DataType" = None, room_RefableType54: "room_Attribute" = None, room_RefableType62: "room_Operation" = None):
        self.ref = ref
        self.room_RefableType = room_RefableType
        self.room_RefableType35 = room_RefableType35
        self.room_RefableType54 = room_RefableType54
        self.room_RefableType62 = room_RefableType62
        
    @property
    def ref(self) -> bool:
        return self.__ref

    @ref.setter
    def ref(self, ref: bool):
        self.__ref = ref

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
    def room_RefableType54(self):
        return self.__room_RefableType54

    @room_RefableType54.setter
    def room_RefableType54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RefableType__room_RefableType54", None)
        self.__room_RefableType54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Attribute53"):
                opp_val = getattr(old_value, "room_Attribute53", None)
                if opp_val == self:
                    setattr(old_value, "room_Attribute53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Attribute53"):
                opp_val = getattr(value, "room_Attribute53", None)
                setattr(value, "room_Attribute53", self)

    @property
    def room_RefableType35(self):
        return self.__room_RefableType35

    @room_RefableType35.setter
    def room_RefableType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RefableType__room_RefableType35", None)
        self.__room_RefableType35 = value
        
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

    @property
    def room_RefableType62(self):
        return self.__room_RefableType62

    @room_RefableType62.setter
    def room_RefableType62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_RefableType__room_RefableType62", None)
        self.__room_RefableType62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Operation61"):
                opp_val = getattr(old_value, "room_Operation61", None)
                if opp_val == self:
                    setattr(old_value, "room_Operation61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Operation61"):
                opp_val = getattr(value, "room_Operation61", None)
                setattr(value, "room_Operation61", self)

class room_VarDecl:

    def __init__(self, name: str, room_VarDecl: "room_RefableType" = None, room_VarDecl59: "room_Operation" = None, room_VarDecl97: "room_Message" = None):
        self.name = name
        self.room_VarDecl = room_VarDecl
        self.room_VarDecl59 = room_VarDecl59
        self.room_VarDecl97 = room_VarDecl97
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_VarDecl97(self):
        return self.__room_VarDecl97

    @room_VarDecl97.setter
    def room_VarDecl97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_VarDecl__room_VarDecl97", None)
        self.__room_VarDecl97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Message96"):
                opp_val = getattr(old_value, "room_Message96", None)
                if opp_val == self:
                    setattr(old_value, "room_Message96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Message96"):
                opp_val = getattr(value, "room_Message96", None)
                setattr(value, "room_Message96", self)

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
    def room_VarDecl59(self):
        return self.__room_VarDecl59

    @room_VarDecl59.setter
    def room_VarDecl59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_VarDecl__room_VarDecl59", None)
        self.__room_VarDecl59 = value
        
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

class room_ActorRef(ActorContainerRef):

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

class room_SubSystemClass(ActorContainerClass):

    pass
class room_ActorClass(ActorContainerClass):

    def __init__(self, abstract: bool, commType: str, room_ActorClass: "room_RoomModel" = None, room_ActorClass128: "room_ActorClass" = None, room_ActorClass126: "room_ActorClass" = None, room_ActorClass130: set["room_Port"] = None, room_ActorClass132: "room_Documentation" = None, room_ActorClass155: "room_StateGraph" = None, room_ActorClass135: set["room_Port"] = None, room_ActorClass138: set["room_ExternalPort"] = None, room_ActorClass140: set["room_ServiceImplementation"] = None, room_ActorClass142: set["room_SAPRef"] = None, room_ActorClass144: set["room_Attribute"] = None, room_ActorClass147: "room_Documentation" = None, room_ActorClass150: set["room_Annotation"] = None, room_ActorClass152: set["room_StandardOperation"] = None, room_ActorClass208: "room_ActorRef" = None):
        self.abstract = abstract
        self.commType = commType
        self.room_ActorClass = room_ActorClass
        self.room_ActorClass128 = room_ActorClass128
        self.room_ActorClass126 = room_ActorClass126
        self.room_ActorClass130 = room_ActorClass130 if room_ActorClass130 is not None else set()
        self.room_ActorClass132 = room_ActorClass132
        self.room_ActorClass155 = room_ActorClass155
        self.room_ActorClass135 = room_ActorClass135 if room_ActorClass135 is not None else set()
        self.room_ActorClass138 = room_ActorClass138 if room_ActorClass138 is not None else set()
        self.room_ActorClass140 = room_ActorClass140 if room_ActorClass140 is not None else set()
        self.room_ActorClass142 = room_ActorClass142 if room_ActorClass142 is not None else set()
        self.room_ActorClass144 = room_ActorClass144 if room_ActorClass144 is not None else set()
        self.room_ActorClass147 = room_ActorClass147
        self.room_ActorClass150 = room_ActorClass150 if room_ActorClass150 is not None else set()
        self.room_ActorClass152 = room_ActorClass152 if room_ActorClass152 is not None else set()
        self.room_ActorClass208 = room_ActorClass208
        
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
    def room_ActorClass132(self):
        return self.__room_ActorClass132

    @room_ActorClass132.setter
    def room_ActorClass132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass132", None)
        self.__room_ActorClass132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation133"):
                opp_val = getattr(old_value, "room_Documentation133", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation133"):
                opp_val = getattr(value, "room_Documentation133", None)
                setattr(value, "room_Documentation133", self)

    @property
    def room_ActorClass152(self):
        return self.__room_ActorClass152

    @room_ActorClass152.setter
    def room_ActorClass152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass152", None)
        self.__room_ActorClass152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_StandardOperation153"):
                    opp_val = getattr(item, "room_StandardOperation153", None)
                    
                    if opp_val == self:
                        setattr(item, "room_StandardOperation153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_StandardOperation153"):
                    opp_val = getattr(item, "room_StandardOperation153", None)
                    
                    setattr(item, "room_StandardOperation153", self)
                    

    @property
    def room_ActorClass138(self):
        return self.__room_ActorClass138

    @room_ActorClass138.setter
    def room_ActorClass138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass138", None)
        self.__room_ActorClass138 = value if value is not None else set()
        
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
    def room_ActorClass130(self):
        return self.__room_ActorClass130

    @room_ActorClass130.setter
    def room_ActorClass130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass130", None)
        self.__room_ActorClass130 = value if value is not None else set()
        
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
    def room_ActorClass135(self):
        return self.__room_ActorClass135

    @room_ActorClass135.setter
    def room_ActorClass135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass135", None)
        self.__room_ActorClass135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Port136"):
                    opp_val = getattr(item, "room_Port136", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Port136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Port136"):
                    opp_val = getattr(item, "room_Port136", None)
                    
                    setattr(item, "room_Port136", self)
                    

    @property
    def room_ActorClass208(self):
        return self.__room_ActorClass208

    @room_ActorClass208.setter
    def room_ActorClass208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass208", None)
        self.__room_ActorClass208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorRef207"):
                opp_val = getattr(old_value, "room_ActorRef207", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorRef207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorRef207"):
                opp_val = getattr(value, "room_ActorRef207", None)
                setattr(value, "room_ActorRef207", self)

    @property
    def room_ActorClass126(self):
        return self.__room_ActorClass126

    @room_ActorClass126.setter
    def room_ActorClass126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass126", None)
        self.__room_ActorClass126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass128"):
                opp_val = getattr(old_value, "room_ActorClass128", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass128"):
                opp_val = getattr(value, "room_ActorClass128", None)
                setattr(value, "room_ActorClass128", self)

    @property
    def room_ActorClass128(self):
        return self.__room_ActorClass128

    @room_ActorClass128.setter
    def room_ActorClass128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass128", None)
        self.__room_ActorClass128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass126"):
                opp_val = getattr(old_value, "room_ActorClass126", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass126"):
                opp_val = getattr(value, "room_ActorClass126", None)
                setattr(value, "room_ActorClass126", self)

    @property
    def room_ActorClass150(self):
        return self.__room_ActorClass150

    @room_ActorClass150.setter
    def room_ActorClass150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass150", None)
        self.__room_ActorClass150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Annotation"):
                    opp_val = getattr(item, "room_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Annotation"):
                    opp_val = getattr(item, "room_Annotation", None)
                    
                    setattr(item, "room_Annotation", self)
                    

    @property
    def room_ActorClass155(self):
        return self.__room_ActorClass155

    @room_ActorClass155.setter
    def room_ActorClass155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass155", None)
        self.__room_ActorClass155 = value
        
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
    def room_ActorClass144(self):
        return self.__room_ActorClass144

    @room_ActorClass144.setter
    def room_ActorClass144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass144", None)
        self.__room_ActorClass144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Attribute145"):
                    opp_val = getattr(item, "room_Attribute145", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Attribute145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Attribute145"):
                    opp_val = getattr(item, "room_Attribute145", None)
                    
                    setattr(item, "room_Attribute145", self)
                    

    @property
    def room_ActorClass147(self):
        return self.__room_ActorClass147

    @room_ActorClass147.setter
    def room_ActorClass147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass147", None)
        self.__room_ActorClass147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Documentation148"):
                opp_val = getattr(old_value, "room_Documentation148", None)
                if opp_val == self:
                    setattr(old_value, "room_Documentation148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Documentation148"):
                opp_val = getattr(value, "room_Documentation148", None)
                setattr(value, "room_Documentation148", self)

    @property
    def room_ActorClass142(self):
        return self.__room_ActorClass142

    @room_ActorClass142.setter
    def room_ActorClass142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass142", None)
        self.__room_ActorClass142 = value if value is not None else set()
        
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
    def room_ActorClass140(self):
        return self.__room_ActorClass140

    @room_ActorClass140.setter
    def room_ActorClass140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ActorClass__room_ActorClass140", None)
        self.__room_ActorClass140 = value if value is not None else set()
        
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

class room_DetailCode:

    def __init__(self, commands: str, room_DetailCode: "room_ActorContainerClass" = None, room_DetailCode27: "room_ActorContainerClass" = None, room_DetailCode30: "room_ActorContainerClass" = None, room_DetailCode47: "room_DataClass" = None, room_DetailCode41: "room_DataClass" = None, room_DetailCode44: "room_DataClass" = None, room_DetailCode68: "room_Operation" = None, room_DetailCode75: "room_ProtocolClass" = None, room_DetailCode78: "room_ProtocolClass" = None, room_DetailCode81: "room_ProtocolClass" = None, room_DetailCode117: "room_MessageHandler" = None, room_DetailCode103: "room_PortClass" = None, room_DetailCode213: "room_State" = None, room_DetailCode216: "room_State" = None, room_DetailCode219: "room_State" = None, room_DetailCode248: "room_GuardedTransition" = None, room_DetailCode243: "room_Transition" = None, room_DetailCode250: "room_CPBranchTransition" = None, room_DetailCode274: "room_Guard" = None):
        self.commands = commands
        self.room_DetailCode = room_DetailCode
        self.room_DetailCode27 = room_DetailCode27
        self.room_DetailCode30 = room_DetailCode30
        self.room_DetailCode47 = room_DetailCode47
        self.room_DetailCode41 = room_DetailCode41
        self.room_DetailCode44 = room_DetailCode44
        self.room_DetailCode68 = room_DetailCode68
        self.room_DetailCode75 = room_DetailCode75
        self.room_DetailCode78 = room_DetailCode78
        self.room_DetailCode81 = room_DetailCode81
        self.room_DetailCode117 = room_DetailCode117
        self.room_DetailCode103 = room_DetailCode103
        self.room_DetailCode213 = room_DetailCode213
        self.room_DetailCode216 = room_DetailCode216
        self.room_DetailCode219 = room_DetailCode219
        self.room_DetailCode248 = room_DetailCode248
        self.room_DetailCode243 = room_DetailCode243
        self.room_DetailCode250 = room_DetailCode250
        self.room_DetailCode274 = room_DetailCode274
        
    @property
    def commands(self) -> str:
        return self.__commands

    @commands.setter
    def commands(self, commands: str):
        self.__commands = commands

    @property
    def room_DetailCode75(self):
        return self.__room_DetailCode75

    @room_DetailCode75.setter
    def room_DetailCode75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode75", None)
        self.__room_DetailCode75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass74"):
                opp_val = getattr(old_value, "room_ProtocolClass74", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass74"):
                opp_val = getattr(value, "room_ProtocolClass74", None)
                setattr(value, "room_ProtocolClass74", self)

    @property
    def room_DetailCode47(self):
        return self.__room_DetailCode47

    @room_DetailCode47.setter
    def room_DetailCode47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode47", None)
        self.__room_DetailCode47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass46"):
                opp_val = getattr(old_value, "room_DataClass46", None)
                if opp_val == self:
                    setattr(old_value, "room_DataClass46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass46"):
                opp_val = getattr(value, "room_DataClass46", None)
                setattr(value, "room_DataClass46", self)

    @property
    def room_DetailCode213(self):
        return self.__room_DetailCode213

    @room_DetailCode213.setter
    def room_DetailCode213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode213", None)
        self.__room_DetailCode213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_State212"):
                opp_val = getattr(old_value, "room_State212", None)
                if opp_val == self:
                    setattr(old_value, "room_State212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_State212"):
                opp_val = getattr(value, "room_State212", None)
                setattr(value, "room_State212", self)

    @property
    def room_DetailCode30(self):
        return self.__room_DetailCode30

    @room_DetailCode30.setter
    def room_DetailCode30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode30", None)
        self.__room_DetailCode30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorContainerClass29"):
                opp_val = getattr(old_value, "room_ActorContainerClass29", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorContainerClass29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorContainerClass29"):
                opp_val = getattr(value, "room_ActorContainerClass29", None)
                setattr(value, "room_ActorContainerClass29", self)

    @property
    def room_DetailCode250(self):
        return self.__room_DetailCode250

    @room_DetailCode250.setter
    def room_DetailCode250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode250", None)
        self.__room_DetailCode250 = value
        
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
    def room_DetailCode78(self):
        return self.__room_DetailCode78

    @room_DetailCode78.setter
    def room_DetailCode78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode78", None)
        self.__room_DetailCode78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass77"):
                opp_val = getattr(old_value, "room_ProtocolClass77", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass77"):
                opp_val = getattr(value, "room_ProtocolClass77", None)
                setattr(value, "room_ProtocolClass77", self)

    @property
    def room_DetailCode103(self):
        return self.__room_DetailCode103

    @room_DetailCode103.setter
    def room_DetailCode103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode103", None)
        self.__room_DetailCode103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_PortClass102"):
                opp_val = getattr(old_value, "room_PortClass102", None)
                if opp_val == self:
                    setattr(old_value, "room_PortClass102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortClass102"):
                opp_val = getattr(value, "room_PortClass102", None)
                setattr(value, "room_PortClass102", self)

    @property
    def room_DetailCode81(self):
        return self.__room_DetailCode81

    @room_DetailCode81.setter
    def room_DetailCode81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode81", None)
        self.__room_DetailCode81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass80"):
                opp_val = getattr(old_value, "room_ProtocolClass80", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass80"):
                opp_val = getattr(value, "room_ProtocolClass80", None)
                setattr(value, "room_ProtocolClass80", self)

    @property
    def room_DetailCode274(self):
        return self.__room_DetailCode274

    @room_DetailCode274.setter
    def room_DetailCode274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode274", None)
        self.__room_DetailCode274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Guard273"):
                opp_val = getattr(old_value, "room_Guard273", None)
                if opp_val == self:
                    setattr(old_value, "room_Guard273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Guard273"):
                opp_val = getattr(value, "room_Guard273", None)
                setattr(value, "room_Guard273", self)

    @property
    def room_DetailCode41(self):
        return self.__room_DetailCode41

    @room_DetailCode41.setter
    def room_DetailCode41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode41", None)
        self.__room_DetailCode41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass40"):
                opp_val = getattr(old_value, "room_DataClass40", None)
                if opp_val == self:
                    setattr(old_value, "room_DataClass40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass40"):
                opp_val = getattr(value, "room_DataClass40", None)
                setattr(value, "room_DataClass40", self)

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
            if hasattr(old_value, "room_ActorContainerClass24"):
                opp_val = getattr(old_value, "room_ActorContainerClass24", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorContainerClass24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorContainerClass24"):
                opp_val = getattr(value, "room_ActorContainerClass24", None)
                setattr(value, "room_ActorContainerClass24", self)

    @property
    def room_DetailCode27(self):
        return self.__room_DetailCode27

    @room_DetailCode27.setter
    def room_DetailCode27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode27", None)
        self.__room_DetailCode27 = value
        
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
    def room_DetailCode219(self):
        return self.__room_DetailCode219

    @room_DetailCode219.setter
    def room_DetailCode219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode219", None)
        self.__room_DetailCode219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_State218"):
                opp_val = getattr(old_value, "room_State218", None)
                if opp_val == self:
                    setattr(old_value, "room_State218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_State218"):
                opp_val = getattr(value, "room_State218", None)
                setattr(value, "room_State218", self)

    @property
    def room_DetailCode117(self):
        return self.__room_DetailCode117

    @room_DetailCode117.setter
    def room_DetailCode117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode117", None)
        self.__room_DetailCode117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_MessageHandler116"):
                opp_val = getattr(old_value, "room_MessageHandler116", None)
                if opp_val == self:
                    setattr(old_value, "room_MessageHandler116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_MessageHandler116"):
                opp_val = getattr(value, "room_MessageHandler116", None)
                setattr(value, "room_MessageHandler116", self)

    @property
    def room_DetailCode243(self):
        return self.__room_DetailCode243

    @room_DetailCode243.setter
    def room_DetailCode243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode243", None)
        self.__room_DetailCode243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Transition242"):
                opp_val = getattr(old_value, "room_Transition242", None)
                if opp_val == self:
                    setattr(old_value, "room_Transition242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Transition242"):
                opp_val = getattr(value, "room_Transition242", None)
                setattr(value, "room_Transition242", self)

    @property
    def room_DetailCode68(self):
        return self.__room_DetailCode68

    @room_DetailCode68.setter
    def room_DetailCode68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode68", None)
        self.__room_DetailCode68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Operation67"):
                opp_val = getattr(old_value, "room_Operation67", None)
                if opp_val == self:
                    setattr(old_value, "room_Operation67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Operation67"):
                opp_val = getattr(value, "room_Operation67", None)
                setattr(value, "room_Operation67", self)

    @property
    def room_DetailCode248(self):
        return self.__room_DetailCode248

    @room_DetailCode248.setter
    def room_DetailCode248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode248", None)
        self.__room_DetailCode248 = value
        
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
    def room_DetailCode44(self):
        return self.__room_DetailCode44

    @room_DetailCode44.setter
    def room_DetailCode44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode44", None)
        self.__room_DetailCode44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DataClass43"):
                opp_val = getattr(old_value, "room_DataClass43", None)
                if opp_val == self:
                    setattr(old_value, "room_DataClass43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DataClass43"):
                opp_val = getattr(value, "room_DataClass43", None)
                setattr(value, "room_DataClass43", self)

    @property
    def room_DetailCode216(self):
        return self.__room_DetailCode216

    @room_DetailCode216.setter
    def room_DetailCode216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_DetailCode__room_DetailCode216", None)
        self.__room_DetailCode216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_State215"):
                opp_val = getattr(old_value, "room_State215", None)
                if opp_val == self:
                    setattr(old_value, "room_State215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_State215"):
                opp_val = getattr(value, "room_State215", None)
                setattr(value, "room_State215", self)

class room_SPPRef(InterfaceItem):

    pass
class StructureClass:

    pass
class room_LogicalSystem(StructureClass):

    pass
class room_ActorContainerClass(StructureClass):

    pass
class room_LayerConnection:

    pass
class room_Binding:

    pass
class RoomClass:

    pass
class room_DataType(RoomClass):

    pass
class room_StructureClass(RoomClass):

    pass
class room_Documentation:

    def __init__(self, text: str, room_Documentation: "room_RoomModel" = None, room_Documentation18: "room_RoomClass" = None, room_Documentation57: "room_Attribute" = None, room_Documentation65: "room_Operation" = None, room_Documentation100: "room_Message" = None, room_Documentation133: "room_ActorClass" = None, room_Documentation160: "room_Port" = None, room_Documentation148: "room_ActorClass" = None, room_Documentation170: "room_ActorContainerRef" = None, room_Documentation210: "room_State" = None, room_Documentation235: "room_ChoicePoint" = None, room_Documentation240: "room_Transition" = None):
        self.text = text
        self.room_Documentation = room_Documentation
        self.room_Documentation18 = room_Documentation18
        self.room_Documentation57 = room_Documentation57
        self.room_Documentation65 = room_Documentation65
        self.room_Documentation100 = room_Documentation100
        self.room_Documentation133 = room_Documentation133
        self.room_Documentation160 = room_Documentation160
        self.room_Documentation148 = room_Documentation148
        self.room_Documentation170 = room_Documentation170
        self.room_Documentation210 = room_Documentation210
        self.room_Documentation235 = room_Documentation235
        self.room_Documentation240 = room_Documentation240
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def room_Documentation148(self):
        return self.__room_Documentation148

    @room_Documentation148.setter
    def room_Documentation148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation148", None)
        self.__room_Documentation148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass147"):
                opp_val = getattr(old_value, "room_ActorClass147", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass147"):
                opp_val = getattr(value, "room_ActorClass147", None)
                setattr(value, "room_ActorClass147", self)

    @property
    def room_Documentation170(self):
        return self.__room_Documentation170

    @room_Documentation170.setter
    def room_Documentation170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation170", None)
        self.__room_Documentation170 = value
        
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
    def room_Documentation240(self):
        return self.__room_Documentation240

    @room_Documentation240.setter
    def room_Documentation240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation240", None)
        self.__room_Documentation240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Transition239"):
                opp_val = getattr(old_value, "room_Transition239", None)
                if opp_val == self:
                    setattr(old_value, "room_Transition239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Transition239"):
                opp_val = getattr(value, "room_Transition239", None)
                setattr(value, "room_Transition239", self)

    @property
    def room_Documentation160(self):
        return self.__room_Documentation160

    @room_Documentation160.setter
    def room_Documentation160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation160", None)
        self.__room_Documentation160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Port159"):
                opp_val = getattr(old_value, "room_Port159", None)
                if opp_val == self:
                    setattr(old_value, "room_Port159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Port159"):
                opp_val = getattr(value, "room_Port159", None)
                setattr(value, "room_Port159", self)

    @property
    def room_Documentation57(self):
        return self.__room_Documentation57

    @room_Documentation57.setter
    def room_Documentation57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation57", None)
        self.__room_Documentation57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Attribute56"):
                opp_val = getattr(old_value, "room_Attribute56", None)
                if opp_val == self:
                    setattr(old_value, "room_Attribute56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Attribute56"):
                opp_val = getattr(value, "room_Attribute56", None)
                setattr(value, "room_Attribute56", self)

    @property
    def room_Documentation210(self):
        return self.__room_Documentation210

    @room_Documentation210.setter
    def room_Documentation210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation210", None)
        self.__room_Documentation210 = value
        
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

    @property
    def room_Documentation235(self):
        return self.__room_Documentation235

    @room_Documentation235.setter
    def room_Documentation235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation235", None)
        self.__room_Documentation235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ChoicePoint234"):
                opp_val = getattr(old_value, "room_ChoicePoint234", None)
                if opp_val == self:
                    setattr(old_value, "room_ChoicePoint234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ChoicePoint234"):
                opp_val = getattr(value, "room_ChoicePoint234", None)
                setattr(value, "room_ChoicePoint234", self)

    @property
    def room_Documentation65(self):
        return self.__room_Documentation65

    @room_Documentation65.setter
    def room_Documentation65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation65", None)
        self.__room_Documentation65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Operation64"):
                opp_val = getattr(old_value, "room_Operation64", None)
                if opp_val == self:
                    setattr(old_value, "room_Operation64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Operation64"):
                opp_val = getattr(value, "room_Operation64", None)
                setattr(value, "room_Operation64", self)

    @property
    def room_Documentation100(self):
        return self.__room_Documentation100

    @room_Documentation100.setter
    def room_Documentation100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation100", None)
        self.__room_Documentation100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_Message99"):
                opp_val = getattr(old_value, "room_Message99", None)
                if opp_val == self:
                    setattr(old_value, "room_Message99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_Message99"):
                opp_val = getattr(value, "room_Message99", None)
                setattr(value, "room_Message99", self)

    @property
    def room_Documentation133(self):
        return self.__room_Documentation133

    @room_Documentation133.setter
    def room_Documentation133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_Documentation__room_Documentation133", None)
        self.__room_Documentation133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ActorClass132"):
                opp_val = getattr(old_value, "room_ActorClass132", None)
                if opp_val == self:
                    setattr(old_value, "room_ActorClass132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ActorClass132"):
                opp_val = getattr(value, "room_ActorClass132", None)
                setattr(value, "room_ActorClass132", self)

class room_RoomModel:

    def __init__(self, name: str, room_RoomModel2: set["room_Import"] = None, room_RoomModel4: set["room_PrimitiveType"] = None, room_RoomModel6: set["room_ExternalType"] = None, room_RoomModel8: set["room_DataClass"] = None, room_RoomModel10: set["room_ProtocolClass"] = None, room_RoomModel: "room_Documentation" = None, room_RoomModel12: set["room_ActorClass"] = None, room_RoomModel14: set["room_SubSystemClass"] = None, room_RoomModel16: set["room_LogicalSystem"] = None):
        self.name = name
        self.room_RoomModel2 = room_RoomModel2 if room_RoomModel2 is not None else set()
        self.room_RoomModel4 = room_RoomModel4 if room_RoomModel4 is not None else set()
        self.room_RoomModel6 = room_RoomModel6 if room_RoomModel6 is not None else set()
        self.room_RoomModel8 = room_RoomModel8 if room_RoomModel8 is not None else set()
        self.room_RoomModel10 = room_RoomModel10 if room_RoomModel10 is not None else set()
        self.room_RoomModel = room_RoomModel
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
                    

class room_ProtocolClass(RoomClass):

    def __init__(self, commType: str, room_ProtocolClass: "room_RoomModel" = None, room_ProtocolClass83: set["room_Message"] = None, room_ProtocolClass86: set["room_Message"] = None, room_ProtocolClass89: "room_PortClass" = None, room_ProtocolClass91: "room_PortClass" = None, room_ProtocolClass94: "room_ProtocolSemantics" = None, room_ProtocolClass72: "room_ProtocolClass" = None, room_ProtocolClass70: "room_ProtocolClass" = None, room_ProtocolClass74: "room_DetailCode" = None, room_ProtocolClass77: "room_DetailCode" = None, room_ProtocolClass80: "room_DetailCode" = None, room_ProtocolClass157: "room_InterfaceItem" = None):
        self.commType = commType
        self.room_ProtocolClass = room_ProtocolClass
        self.room_ProtocolClass83 = room_ProtocolClass83 if room_ProtocolClass83 is not None else set()
        self.room_ProtocolClass86 = room_ProtocolClass86 if room_ProtocolClass86 is not None else set()
        self.room_ProtocolClass89 = room_ProtocolClass89
        self.room_ProtocolClass91 = room_ProtocolClass91
        self.room_ProtocolClass94 = room_ProtocolClass94
        self.room_ProtocolClass72 = room_ProtocolClass72
        self.room_ProtocolClass70 = room_ProtocolClass70
        self.room_ProtocolClass74 = room_ProtocolClass74
        self.room_ProtocolClass77 = room_ProtocolClass77
        self.room_ProtocolClass80 = room_ProtocolClass80
        self.room_ProtocolClass157 = room_ProtocolClass157
        
    @property
    def commType(self) -> str:
        return self.__commType

    @commType.setter
    def commType(self, commType: str):
        self.__commType = commType

    @property
    def room_ProtocolClass83(self):
        return self.__room_ProtocolClass83

    @room_ProtocolClass83.setter
    def room_ProtocolClass83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass83", None)
        self.__room_ProtocolClass83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Message84"):
                    opp_val = getattr(item, "room_Message84", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Message84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Message84"):
                    opp_val = getattr(item, "room_Message84", None)
                    
                    setattr(item, "room_Message84", self)
                    

    @property
    def room_ProtocolClass157(self):
        return self.__room_ProtocolClass157

    @room_ProtocolClass157.setter
    def room_ProtocolClass157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass157", None)
        self.__room_ProtocolClass157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_InterfaceItem"):
                opp_val = getattr(old_value, "room_InterfaceItem", None)
                if opp_val == self:
                    setattr(old_value, "room_InterfaceItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_InterfaceItem"):
                opp_val = getattr(value, "room_InterfaceItem", None)
                setattr(value, "room_InterfaceItem", self)

    @property
    def room_ProtocolClass86(self):
        return self.__room_ProtocolClass86

    @room_ProtocolClass86.setter
    def room_ProtocolClass86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass86", None)
        self.__room_ProtocolClass86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room_Message87"):
                    opp_val = getattr(item, "room_Message87", None)
                    
                    if opp_val == self:
                        setattr(item, "room_Message87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room_Message87"):
                    opp_val = getattr(item, "room_Message87", None)
                    
                    setattr(item, "room_Message87", self)
                    

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
            if hasattr(old_value, "room_RoomModel10"):
                opp_val = getattr(old_value, "room_RoomModel10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_RoomModel10"):
                opp_val = getattr(value, "room_RoomModel10", None)
                if opp_val is None:
                    setattr(value, "room_RoomModel10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room_ProtocolClass72(self):
        return self.__room_ProtocolClass72

    @room_ProtocolClass72.setter
    def room_ProtocolClass72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass72", None)
        self.__room_ProtocolClass72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass70"):
                opp_val = getattr(old_value, "room_ProtocolClass70", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass70"):
                opp_val = getattr(value, "room_ProtocolClass70", None)
                setattr(value, "room_ProtocolClass70", self)

    @property
    def room_ProtocolClass70(self):
        return self.__room_ProtocolClass70

    @room_ProtocolClass70.setter
    def room_ProtocolClass70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass70", None)
        self.__room_ProtocolClass70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_ProtocolClass72"):
                opp_val = getattr(old_value, "room_ProtocolClass72", None)
                if opp_val == self:
                    setattr(old_value, "room_ProtocolClass72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_ProtocolClass72"):
                opp_val = getattr(value, "room_ProtocolClass72", None)
                setattr(value, "room_ProtocolClass72", self)

    @property
    def room_ProtocolClass80(self):
        return self.__room_ProtocolClass80

    @room_ProtocolClass80.setter
    def room_ProtocolClass80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass80", None)
        self.__room_ProtocolClass80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode81"):
                opp_val = getattr(old_value, "room_DetailCode81", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode81"):
                opp_val = getattr(value, "room_DetailCode81", None)
                setattr(value, "room_DetailCode81", self)

    @property
    def room_ProtocolClass77(self):
        return self.__room_ProtocolClass77

    @room_ProtocolClass77.setter
    def room_ProtocolClass77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass77", None)
        self.__room_ProtocolClass77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode78"):
                opp_val = getattr(old_value, "room_DetailCode78", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode78"):
                opp_val = getattr(value, "room_DetailCode78", None)
                setattr(value, "room_DetailCode78", self)

    @property
    def room_ProtocolClass89(self):
        return self.__room_ProtocolClass89

    @room_ProtocolClass89.setter
    def room_ProtocolClass89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass89", None)
        self.__room_ProtocolClass89 = value
        
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
    def room_ProtocolClass91(self):
        return self.__room_ProtocolClass91

    @room_ProtocolClass91.setter
    def room_ProtocolClass91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass91", None)
        self.__room_ProtocolClass91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_PortClass92"):
                opp_val = getattr(old_value, "room_PortClass92", None)
                if opp_val == self:
                    setattr(old_value, "room_PortClass92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_PortClass92"):
                opp_val = getattr(value, "room_PortClass92", None)
                setattr(value, "room_PortClass92", self)

    @property
    def room_ProtocolClass74(self):
        return self.__room_ProtocolClass74

    @room_ProtocolClass74.setter
    def room_ProtocolClass74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass74", None)
        self.__room_ProtocolClass74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room_DetailCode75"):
                opp_val = getattr(old_value, "room_DetailCode75", None)
                if opp_val == self:
                    setattr(old_value, "room_DetailCode75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room_DetailCode75"):
                opp_val = getattr(value, "room_DetailCode75", None)
                setattr(value, "room_DetailCode75", self)

    @property
    def room_ProtocolClass94(self):
        return self.__room_ProtocolClass94

    @room_ProtocolClass94.setter
    def room_ProtocolClass94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room_ProtocolClass__room_ProtocolClass94", None)
        self.__room_ProtocolClass94 = value
        
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

    def __init__(self, targetName: str, castName: str, defaultValueLiteral: str, room_PrimitiveType: "room_RoomModel" = None):
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
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

    @property
    def targetName(self) -> str:
        return self.__targetName

    @targetName.setter
    def targetName(self, targetName: str):
        self.__targetName = targetName

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

    def __init__(self, importedNamespace: str, importURI: str, room_Import: "room_RoomModel" = None):
        self.importedNamespace = importedNamespace
        self.importURI = importURI
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
