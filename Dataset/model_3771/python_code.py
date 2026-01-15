from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statespace_EObject:

    pass
class statespace_Storage:

    def __init__(self, data: str):
        self.data = data
        
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    def getData(self, endIndex: int, beginIndex: int) -> str:
        # TODO: Implement getData method
        pass

    def getData(self, index: int) -> int:
        # TODO: Implement getData method
        pass

    def setData(self, value: int, index: int):
        # TODO: Implement setData method
        pass

    def setData(self, beginIndex: int, value: str):
        # TODO: Implement setData method
        pass

    def setData(self, beginIndex: int, value: str, endIndex: int):
        # TODO: Implement setData method
        pass

class statespace_EClass:

    pass
class statespace_EAttribute:

    pass
class statespace_EObjectIntegerMapEntry:

    def __init__(self, value: str, statespace_EObjectIntegerMapEntry: "statespace_Model" = None, statespace_EObjectIntegerMapEntry21: "statespace_Model" = None, statespace_EObjectIntegerMapEntry33: "statespace_EObject" = None):
        self.value = value
        self.statespace_EObjectIntegerMapEntry = statespace_EObjectIntegerMapEntry
        self.statespace_EObjectIntegerMapEntry21 = statespace_EObjectIntegerMapEntry21
        self.statespace_EObjectIntegerMapEntry33 = statespace_EObjectIntegerMapEntry33
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def statespace_EObjectIntegerMapEntry(self):
        return self.__statespace_EObjectIntegerMapEntry

    @statespace_EObjectIntegerMapEntry.setter
    def statespace_EObjectIntegerMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_EObjectIntegerMapEntry__statespace_EObjectIntegerMapEntry", None)
        self.__statespace_EObjectIntegerMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statespace_Model18"):
                opp_val = getattr(old_value, "statespace_Model18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statespace_Model18"):
                opp_val = getattr(value, "statespace_Model18", None)
                if opp_val is None:
                    setattr(value, "statespace_Model18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statespace_EObjectIntegerMapEntry21(self):
        return self.__statespace_EObjectIntegerMapEntry21

    @statespace_EObjectIntegerMapEntry21.setter
    def statespace_EObjectIntegerMapEntry21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_EObjectIntegerMapEntry__statespace_EObjectIntegerMapEntry21", None)
        self.__statespace_EObjectIntegerMapEntry21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statespace_Model20"):
                opp_val = getattr(old_value, "statespace_Model20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statespace_Model20"):
                opp_val = getattr(value, "statespace_Model20", None)
                if opp_val is None:
                    setattr(value, "statespace_Model20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statespace_EObjectIntegerMapEntry33(self):
        return self.__statespace_EObjectIntegerMapEntry33

    @statespace_EObjectIntegerMapEntry33.setter
    def statespace_EObjectIntegerMapEntry33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_EObjectIntegerMapEntry__statespace_EObjectIntegerMapEntry33", None)
        self.__statespace_EObjectIntegerMapEntry33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statespace_EObject"):
                opp_val = getattr(old_value, "statespace_EObject", None)
                if opp_val == self:
                    setattr(old_value, "statespace_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statespace_EObject"):
                opp_val = getattr(value, "statespace_EObject", None)
                setattr(value, "statespace_EObject", self)

class statespace_Model:

    def __init__(self, objectKeys: str, resource: str, eGraph: str, objectCount: int, statespace_Model: "statespace_State" = None, statespace_Model18: set["statespace_EObjectIntegerMapEntry"] = None, statespace_Model20: set["statespace_EObjectIntegerMapEntry"] = None):
        self.objectKeys = objectKeys
        self.resource = resource
        self.eGraph = eGraph
        self.objectCount = objectCount
        self.statespace_Model = statespace_Model
        self.statespace_Model18 = statespace_Model18 if statespace_Model18 is not None else set()
        self.statespace_Model20 = statespace_Model20 if statespace_Model20 is not None else set()
        
    @property
    def eGraph(self) -> str:
        return self.__eGraph

    @eGraph.setter
    def eGraph(self, eGraph: str):
        self.__eGraph = eGraph

    @property
    def resource(self) -> str:
        return self.__resource

    @resource.setter
    def resource(self, resource: str):
        self.__resource = resource

    @property
    def objectKeys(self) -> str:
        return self.__objectKeys

    @objectKeys.setter
    def objectKeys(self, objectKeys: str):
        self.__objectKeys = objectKeys

    @property
    def objectCount(self) -> int:
        return self.__objectCount

    @objectCount.setter
    def objectCount(self, objectCount: int):
        self.__objectCount = objectCount

    @property
    def statespace_Model(self):
        return self.__statespace_Model

    @statespace_Model.setter
    def statespace_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_Model__statespace_Model", None)
        self.__statespace_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statespace_State16"):
                opp_val = getattr(old_value, "statespace_State16", None)
                if opp_val == self:
                    setattr(old_value, "statespace_State16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statespace_State16"):
                opp_val = getattr(value, "statespace_State16", None)
                setattr(value, "statespace_State16", self)

    @property
    def statespace_Model18(self):
        return self.__statespace_Model18

    @statespace_Model18.setter
    def statespace_Model18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_Model__statespace_Model18", None)
        self.__statespace_Model18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statespace_EObjectIntegerMapEntry"):
                    opp_val = getattr(item, "statespace_EObjectIntegerMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "statespace_EObjectIntegerMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statespace_EObjectIntegerMapEntry"):
                    opp_val = getattr(item, "statespace_EObjectIntegerMapEntry", None)
                    
                    setattr(item, "statespace_EObjectIntegerMapEntry", self)
                    

    @property
    def statespace_Model20(self):
        return self.__statespace_Model20

    @statespace_Model20.setter
    def statespace_Model20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_Model__statespace_Model20", None)
        self.__statespace_Model20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statespace_EObjectIntegerMapEntry21"):
                    opp_val = getattr(item, "statespace_EObjectIntegerMapEntry21", None)
                    
                    if opp_val == self:
                        setattr(item, "statespace_EObjectIntegerMapEntry21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statespace_EObjectIntegerMapEntry21"):
                    opp_val = getattr(item, "statespace_EObjectIntegerMapEntry21", None)
                    
                    setattr(item, "statespace_EObjectIntegerMapEntry21", self)
                    

    def collectMissingRootObjects(self):
        # TODO: Implement collectMissingRootObjects method
        pass

    def getCopy(self, match: str) -> str:
        # TODO: Implement getCopy method
        pass

    def updateObjectKeys(self, identityTypes: str) -> bool:
        # TODO: Implement updateObjectKeys method
        pass

class statespace_EStringToStringMapEntry:

    pass
class statespace_EqualityHelper:

    def __init__(self, checkLinkOrder: bool, statespace_EqualityHelper: "statespace_StateSpace" = None, statespace_EqualityHelper29: set["statespace_EAttribute"] = None, statespace_EqualityHelper31: set["statespace_EClass"] = None):
        self.checkLinkOrder = checkLinkOrder
        self.statespace_EqualityHelper = statespace_EqualityHelper
        self.statespace_EqualityHelper29 = statespace_EqualityHelper29 if statespace_EqualityHelper29 is not None else set()
        self.statespace_EqualityHelper31 = statespace_EqualityHelper31 if statespace_EqualityHelper31 is not None else set()
        
    @property
    def checkLinkOrder(self) -> bool:
        return self.__checkLinkOrder

    @checkLinkOrder.setter
    def checkLinkOrder(self, checkLinkOrder: bool):
        self.__checkLinkOrder = checkLinkOrder

    @property
    def statespace_EqualityHelper(self):
        return self.__statespace_EqualityHelper

    @statespace_EqualityHelper.setter
    def statespace_EqualityHelper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_EqualityHelper__statespace_EqualityHelper", None)
        self.__statespace_EqualityHelper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statespace_StateSpace8"):
                opp_val = getattr(old_value, "statespace_StateSpace8", None)
                if opp_val == self:
                    setattr(old_value, "statespace_StateSpace8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statespace_StateSpace8"):
                opp_val = getattr(value, "statespace_StateSpace8", None)
                setattr(value, "statespace_StateSpace8", self)

    @property
    def statespace_EqualityHelper29(self):
        return self.__statespace_EqualityHelper29

    @statespace_EqualityHelper29.setter
    def statespace_EqualityHelper29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_EqualityHelper__statespace_EqualityHelper29", None)
        self.__statespace_EqualityHelper29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statespace_EAttribute"):
                    opp_val = getattr(item, "statespace_EAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "statespace_EAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statespace_EAttribute"):
                    opp_val = getattr(item, "statespace_EAttribute", None)
                    
                    setattr(item, "statespace_EAttribute", self)
                    

    @property
    def statespace_EqualityHelper31(self):
        return self.__statespace_EqualityHelper31

    @statespace_EqualityHelper31.setter
    def statespace_EqualityHelper31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_EqualityHelper__statespace_EqualityHelper31", None)
        self.__statespace_EqualityHelper31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statespace_EClass"):
                    opp_val = getattr(item, "statespace_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "statespace_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statespace_EClass"):
                    opp_val = getattr(item, "statespace_EClass", None)
                    
                    setattr(item, "statespace_EClass", self)
                    

    def equals(self, model1: str, model2: str) -> bool:
        # TODO: Implement equals method
        pass

    def hashCode(self, model: str) -> int:
        # TODO: Implement hashCode method
        pass

    def setStateSpace(self, stateSpace: str):
        # TODO: Implement setStateSpace method
        pass

class Storage:

    pass
class statespace_Transition(Storage):

    def __init__(self, parameterCount: int, parameterKeys: str, match: int, Transition13: "statespace_State" = None, Transition: "statespace_State" = None, outgoing: "statespace_State" = None, incoming: "statespace_State" = None, statespace_Transition: "statespace_Rule" = None):
        self.parameterCount = parameterCount
        self.parameterKeys = parameterKeys
        self.match = match
        self.Transition13 = Transition13
        self.Transition = Transition
        self.outgoing = outgoing
        self.incoming = incoming
        self.statespace_Transition = statespace_Transition
        
    @property
    def parameterCount(self) -> int:
        return self.__parameterCount

    @parameterCount.setter
    def parameterCount(self, parameterCount: int):
        self.__parameterCount = parameterCount

    @property
    def parameterKeys(self) -> str:
        return self.__parameterKeys

    @parameterKeys.setter
    def parameterKeys(self, parameterKeys: str):
        self.__parameterKeys = parameterKeys

    @property
    def match(self) -> int:
        return self.__match

    @match.setter
    def match(self, match: int):
        self.__match = match

    @property
    def statespace_Transition(self):
        return self.__statespace_Transition

    @statespace_Transition.setter
    def statespace_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_Transition__statespace_Transition", None)
        self.__statespace_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statespace_Rule27"):
                opp_val = getattr(old_value, "statespace_Rule27", None)
                if opp_val == self:
                    setattr(old_value, "statespace_Rule27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statespace_Rule27"):
                opp_val = getattr(value, "statespace_Rule27", None)
                setattr(value, "statespace_Rule27", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State23"):
                opp_val = getattr(old_value, "State23", None)
                if opp_val == self:
                    setattr(old_value, "State23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State23"):
                opp_val = getattr(value, "State23", None)
                setattr(value, "State23", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State25"):
                opp_val = getattr(old_value, "State25", None)
                if opp_val == self:
                    setattr(old_value, "State25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State25"):
                opp_val = getattr(value, "State25", None)
                setattr(value, "State25", self)

    @property
    def Transition13(self):
        return self.__Transition13

    @Transition13.setter
    def Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_Transition__Transition13", None)
        self.__Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getLabel(self) -> str:
        # TODO: Implement getLabel method
        pass

class statespace_State(Storage):

    def __init__(self, index: int, open: bool, goal: bool, pruned: bool, location: str, objectCount: int, hashCode: int, derivedFrom: int, objectKeys: str, State: "statespace_StateSpace" = None, statespace_State: "statespace_StateSpace" = None, statespace_State6: "statespace_StateSpace" = None, source: set["statespace_Transition"] = None, states: "statespace_StateSpace" = None, target: set["statespace_Transition"] = None, statespace_State16: "statespace_Model" = None, State23: "statespace_Transition" = None, State25: "statespace_Transition" = None):
        self.index = index
        self.open = open
        self.goal = goal
        self.pruned = pruned
        self.location = location
        self.objectCount = objectCount
        self.hashCode = hashCode
        self.derivedFrom = derivedFrom
        self.objectKeys = objectKeys
        self.State = State
        self.statespace_State = statespace_State
        self.statespace_State6 = statespace_State6
        self.source = source if source is not None else set()
        self.states = states
        self.target = target if target is not None else set()
        self.statespace_State16 = statespace_State16
        self.State23 = State23
        self.State25 = State25
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def derivedFrom(self) -> int:
        return self.__derivedFrom

    @derivedFrom.setter
    def derivedFrom(self, derivedFrom: int):
        self.__derivedFrom = derivedFrom

    @property
    def pruned(self) -> bool:
        return self.__pruned

    @pruned.setter
    def pruned(self, pruned: bool):
        self.__pruned = pruned

    @property
    def goal(self) -> bool:
        return self.__goal

    @goal.setter
    def goal(self, goal: bool):
        self.__goal = goal

    @property
    def open(self) -> bool:
        return self.__open

    @open.setter
    def open(self, open: bool):
        self.__open = open

    @property
    def hashCode(self) -> int:
        return self.__hashCode

    @hashCode.setter
    def hashCode(self, hashCode: int):
        self.__hashCode = hashCode

    @property
    def objectCount(self) -> int:
        return self.__objectCount

    @objectCount.setter
    def objectCount(self, objectCount: int):
        self.__objectCount = objectCount

    @property
    def objectKeys(self) -> str:
        return self.__objectKeys

    @objectKeys.setter
    def objectKeys(self, objectKeys: str):
        self.__objectKeys = objectKeys

    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition13"):
                    opp_val = getattr(item, "Transition13", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition13"):
                    opp_val = getattr(item, "Transition13", None)
                    
                    setattr(item, "Transition13", self)
                    

    @property
    def State23(self):
        return self.__State23

    @State23.setter
    def State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_State__State23", None)
        self.__State23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateSpace"):
                opp_val = getattr(old_value, "stateSpace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateSpace"):
                opp_val = getattr(value, "stateSpace", None)
                if opp_val is None:
                    setattr(value, "stateSpace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State25(self):
        return self.__State25

    @State25.setter
    def State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_State__State25", None)
        self.__State25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateSpace"):
                opp_val = getattr(old_value, "StateSpace", None)
                if opp_val == self:
                    setattr(old_value, "StateSpace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateSpace"):
                opp_val = getattr(value, "StateSpace", None)
                setattr(value, "StateSpace", self)

    @property
    def statespace_State(self):
        return self.__statespace_State

    @statespace_State.setter
    def statespace_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_State__statespace_State", None)
        self.__statespace_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statespace_StateSpace3"):
                opp_val = getattr(old_value, "statespace_StateSpace3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statespace_StateSpace3"):
                opp_val = getattr(value, "statespace_StateSpace3", None)
                if opp_val is None:
                    setattr(value, "statespace_StateSpace3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statespace_State6(self):
        return self.__statespace_State6

    @statespace_State6.setter
    def statespace_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_State__statespace_State6", None)
        self.__statespace_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statespace_StateSpace5"):
                opp_val = getattr(old_value, "statespace_StateSpace5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statespace_StateSpace5"):
                opp_val = getattr(value, "statespace_StateSpace5", None)
                if opp_val is None:
                    setattr(value, "statespace_StateSpace5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_State__target", None)
        self.__target = value if value is not None else set()
        
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
    def statespace_State16(self):
        return self.__statespace_State16

    @statespace_State16.setter
    def statespace_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_State__statespace_State16", None)
        self.__statespace_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statespace_Model"):
                opp_val = getattr(old_value, "statespace_Model", None)
                if opp_val == self:
                    setattr(old_value, "statespace_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statespace_Model"):
                opp_val = getattr(value, "statespace_Model", None)
                setattr(value, "statespace_Model", self)

    def getOutgoing(self, match: int, target: str, rule: str, paramIDs: str) -> str:
        # TODO: Implement getOutgoing method
        pass

    def isInitial(self) -> bool:
        # TODO: Implement isInitial method
        pass

class statespace_StateSpace(Storage):

    def __init__(self, stateCount: int, transitionCount: int, layoutZoomLevel: int, layoutHideLabels: bool, layoutHideIndizes: bool, maxStateDistance: int, layoutStateRepulsion: int, layoutTransitionAttraction: int, allParameterKeys: str, stateSpace: set["statespace_State"] = None, statespace_StateSpace3: set["statespace_State"] = None, statespace_StateSpace: set["statespace_Rule"] = None, statespace_StateSpace8: "statespace_EqualityHelper" = None, statespace_StateSpace5: set["statespace_State"] = None, statespace_StateSpace10: set["statespace_EStringToStringMapEntry"] = None, StateSpace: "statespace_State" = None):
        self.stateCount = stateCount
        self.transitionCount = transitionCount
        self.layoutZoomLevel = layoutZoomLevel
        self.layoutHideLabels = layoutHideLabels
        self.layoutHideIndizes = layoutHideIndizes
        self.maxStateDistance = maxStateDistance
        self.layoutStateRepulsion = layoutStateRepulsion
        self.layoutTransitionAttraction = layoutTransitionAttraction
        self.allParameterKeys = allParameterKeys
        self.stateSpace = stateSpace if stateSpace is not None else set()
        self.statespace_StateSpace3 = statespace_StateSpace3 if statespace_StateSpace3 is not None else set()
        self.statespace_StateSpace = statespace_StateSpace if statespace_StateSpace is not None else set()
        self.statespace_StateSpace8 = statespace_StateSpace8
        self.statespace_StateSpace5 = statespace_StateSpace5 if statespace_StateSpace5 is not None else set()
        self.statespace_StateSpace10 = statespace_StateSpace10 if statespace_StateSpace10 is not None else set()
        self.StateSpace = StateSpace
        
    @property
    def stateCount(self) -> int:
        return self.__stateCount

    @stateCount.setter
    def stateCount(self, stateCount: int):
        self.__stateCount = stateCount

    @property
    def layoutStateRepulsion(self) -> int:
        return self.__layoutStateRepulsion

    @layoutStateRepulsion.setter
    def layoutStateRepulsion(self, layoutStateRepulsion: int):
        self.__layoutStateRepulsion = layoutStateRepulsion

    @property
    def transitionCount(self) -> int:
        return self.__transitionCount

    @transitionCount.setter
    def transitionCount(self, transitionCount: int):
        self.__transitionCount = transitionCount

    @property
    def layoutHideLabels(self) -> bool:
        return self.__layoutHideLabels

    @layoutHideLabels.setter
    def layoutHideLabels(self, layoutHideLabels: bool):
        self.__layoutHideLabels = layoutHideLabels

    @property
    def maxStateDistance(self) -> int:
        return self.__maxStateDistance

    @maxStateDistance.setter
    def maxStateDistance(self, maxStateDistance: int):
        self.__maxStateDistance = maxStateDistance

    @property
    def layoutZoomLevel(self) -> int:
        return self.__layoutZoomLevel

    @layoutZoomLevel.setter
    def layoutZoomLevel(self, layoutZoomLevel: int):
        self.__layoutZoomLevel = layoutZoomLevel

    @property
    def layoutHideIndizes(self) -> bool:
        return self.__layoutHideIndizes

    @layoutHideIndizes.setter
    def layoutHideIndizes(self, layoutHideIndizes: bool):
        self.__layoutHideIndizes = layoutHideIndizes

    @property
    def layoutTransitionAttraction(self) -> int:
        return self.__layoutTransitionAttraction

    @layoutTransitionAttraction.setter
    def layoutTransitionAttraction(self, layoutTransitionAttraction: int):
        self.__layoutTransitionAttraction = layoutTransitionAttraction

    @property
    def allParameterKeys(self) -> str:
        return self.__allParameterKeys

    @allParameterKeys.setter
    def allParameterKeys(self, allParameterKeys: str):
        self.__allParameterKeys = allParameterKeys

    @property
    def stateSpace(self):
        return self.__stateSpace

    @stateSpace.setter
    def stateSpace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_StateSpace__stateSpace", None)
        self.__stateSpace = value if value is not None else set()
        
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
    def statespace_StateSpace3(self):
        return self.__statespace_StateSpace3

    @statespace_StateSpace3.setter
    def statespace_StateSpace3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_StateSpace__statespace_StateSpace3", None)
        self.__statespace_StateSpace3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statespace_State"):
                    opp_val = getattr(item, "statespace_State", None)
                    
                    if opp_val == self:
                        setattr(item, "statespace_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statespace_State"):
                    opp_val = getattr(item, "statespace_State", None)
                    
                    setattr(item, "statespace_State", self)
                    

    @property
    def StateSpace(self):
        return self.__StateSpace

    @StateSpace.setter
    def StateSpace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_StateSpace__StateSpace", None)
        self.__StateSpace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states"):
                opp_val = getattr(old_value, "states", None)
                if opp_val == self:
                    setattr(old_value, "states", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states"):
                opp_val = getattr(value, "states", None)
                setattr(value, "states", self)

    @property
    def statespace_StateSpace(self):
        return self.__statespace_StateSpace

    @statespace_StateSpace.setter
    def statespace_StateSpace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_StateSpace__statespace_StateSpace", None)
        self.__statespace_StateSpace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statespace_Rule"):
                    opp_val = getattr(item, "statespace_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "statespace_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statespace_Rule"):
                    opp_val = getattr(item, "statespace_Rule", None)
                    
                    setattr(item, "statespace_Rule", self)
                    

    @property
    def statespace_StateSpace5(self):
        return self.__statespace_StateSpace5

    @statespace_StateSpace5.setter
    def statespace_StateSpace5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_StateSpace__statespace_StateSpace5", None)
        self.__statespace_StateSpace5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statespace_State6"):
                    opp_val = getattr(item, "statespace_State6", None)
                    
                    if opp_val == self:
                        setattr(item, "statespace_State6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statespace_State6"):
                    opp_val = getattr(item, "statespace_State6", None)
                    
                    setattr(item, "statespace_State6", self)
                    

    @property
    def statespace_StateSpace8(self):
        return self.__statespace_StateSpace8

    @statespace_StateSpace8.setter
    def statespace_StateSpace8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_StateSpace__statespace_StateSpace8", None)
        self.__statespace_StateSpace8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statespace_EqualityHelper"):
                opp_val = getattr(old_value, "statespace_EqualityHelper", None)
                if opp_val == self:
                    setattr(old_value, "statespace_EqualityHelper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statespace_EqualityHelper"):
                opp_val = getattr(value, "statespace_EqualityHelper", None)
                setattr(value, "statespace_EqualityHelper", self)

    @property
    def statespace_StateSpace10(self):
        return self.__statespace_StateSpace10

    @statespace_StateSpace10.setter
    def statespace_StateSpace10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statespace_StateSpace__statespace_StateSpace10", None)
        self.__statespace_StateSpace10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statespace_EStringToStringMapEntry"):
                    opp_val = getattr(item, "statespace_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "statespace_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statespace_EStringToStringMapEntry"):
                    opp_val = getattr(item, "statespace_EStringToStringMapEntry", None)
                    
                    setattr(item, "statespace_EStringToStringMapEntry", self)
                    

    def removeState(self, state: str) -> bool:
        # TODO: Implement removeState method
        pass

    def incTransitionCount(self) -> int:
        # TODO: Implement incTransitionCount method
        pass

    def updateEqualityHelper(self):
        # TODO: Implement updateEqualityHelper method
        pass

class statespace_Rule:

    pass