from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudoStateTypes(Enum):
    initial = "initial"
    entry = "entry"
    choice = "choice"
class LanguageTypes(Enum):
    java = "java"
    groovy = "groovy"
    relogo = "relogo"
class MessageCheckerTypes(Enum):
    conditional = "conditional"
    equals = "equals"
    unconditional = "unconditional"
    always = "always"
class TriggerTypes(Enum):
    always = "always"
    timed = "timed"
    exponential = "exponential"
    probability = "probability"
    condition = "condition"
    message = "message"


############################################
# Definition of Classes
############################################

class State:

    pass
class scmodel_History(State):

    def __init__(self, shallow: bool):
        self.shallow = shallow
        
    @property
    def shallow(self) -> bool:
        return self.__shallow

    @shallow.setter
    def shallow(self, shallow: bool):
        self.__shallow = shallow

class scmodel_FinalState(State):

    pass
class AbstractState:

    pass
class scmodel_PseudoState(AbstractState):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class scmodel_CompositeState(AbstractState):

    pass
class scmodel_State(AbstractState):

    pass
class scmodel_StateMachine:

    def __init__(self, agentType: str, package: str, className: str, language: str, nextID: int, id: str, uuid: str, priority: float, scmodel_StateMachine: set["scmodel_AbstractState"] = None, scmodel_StateMachine2: set["scmodel_Transition"] = None):
        self.agentType = agentType
        self.package = package
        self.className = className
        self.language = language
        self.nextID = nextID
        self.id = id
        self.uuid = uuid
        self.priority = priority
        self.scmodel_StateMachine = scmodel_StateMachine if scmodel_StateMachine is not None else set()
        self.scmodel_StateMachine2 = scmodel_StateMachine2 if scmodel_StateMachine2 is not None else set()
        
    @property
    def priority(self) -> float:
        return self.__priority

    @priority.setter
    def priority(self, priority: float):
        self.__priority = priority

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def agentType(self) -> str:
        return self.__agentType

    @agentType.setter
    def agentType(self, agentType: str):
        self.__agentType = agentType

    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def nextID(self) -> int:
        return self.__nextID

    @nextID.setter
    def nextID(self, nextID: int):
        self.__nextID = nextID

    @property
    def scmodel_StateMachine2(self):
        return self.__scmodel_StateMachine2

    @scmodel_StateMachine2.setter
    def scmodel_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scmodel_StateMachine__scmodel_StateMachine2", None)
        self.__scmodel_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scmodel_Transition"):
                    opp_val = getattr(item, "scmodel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "scmodel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scmodel_Transition"):
                    opp_val = getattr(item, "scmodel_Transition", None)
                    
                    setattr(item, "scmodel_Transition", self)
                    

    @property
    def scmodel_StateMachine(self):
        return self.__scmodel_StateMachine

    @scmodel_StateMachine.setter
    def scmodel_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scmodel_StateMachine__scmodel_StateMachine", None)
        self.__scmodel_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scmodel_AbstractState"):
                    opp_val = getattr(item, "scmodel_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "scmodel_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scmodel_AbstractState"):
                    opp_val = getattr(item, "scmodel_AbstractState", None)
                    
                    setattr(item, "scmodel_AbstractState", self)
                    

class scmodel_Transition:

    def __init__(self, onTransitionImports: str, outOfBranch: bool, defaultTransition: bool, triggerType: str, triggerTime: float, triggerConditionCode: str, triggerConditionCodeImports: str, triggerCodeLanguage: str, messageCheckerType: str, messageCheckerClass: str, priority: float, onTransition: str, triggerProbCode: str, triggerProbCodeImports: str, messageCheckerCode: str, messageCheckerCodeImports: str, messageCheckerConditionLanguage: str, id: str, guard: str, guardImports: str, triggerTimedCode: str, triggerTimedCodeImports: str, triggerExpRateCode: str, triggerExpRateCodeImports: str, uuid: str, selfTransition: bool, scmodel_Transition: "scmodel_StateMachine" = None, scmodel_Transition4: "scmodel_AbstractState" = None, scmodel_Transition7: "scmodel_AbstractState" = None):
        self.onTransitionImports = onTransitionImports
        self.outOfBranch = outOfBranch
        self.defaultTransition = defaultTransition
        self.triggerType = triggerType
        self.triggerTime = triggerTime
        self.triggerConditionCode = triggerConditionCode
        self.triggerConditionCodeImports = triggerConditionCodeImports
        self.triggerCodeLanguage = triggerCodeLanguage
        self.messageCheckerType = messageCheckerType
        self.messageCheckerClass = messageCheckerClass
        self.priority = priority
        self.onTransition = onTransition
        self.triggerProbCode = triggerProbCode
        self.triggerProbCodeImports = triggerProbCodeImports
        self.messageCheckerCode = messageCheckerCode
        self.messageCheckerCodeImports = messageCheckerCodeImports
        self.messageCheckerConditionLanguage = messageCheckerConditionLanguage
        self.id = id
        self.guard = guard
        self.guardImports = guardImports
        self.triggerTimedCode = triggerTimedCode
        self.triggerTimedCodeImports = triggerTimedCodeImports
        self.triggerExpRateCode = triggerExpRateCode
        self.triggerExpRateCodeImports = triggerExpRateCodeImports
        self.uuid = uuid
        self.selfTransition = selfTransition
        self.scmodel_Transition = scmodel_Transition
        self.scmodel_Transition4 = scmodel_Transition4
        self.scmodel_Transition7 = scmodel_Transition7
        
    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def triggerTime(self) -> float:
        return self.__triggerTime

    @triggerTime.setter
    def triggerTime(self, triggerTime: float):
        self.__triggerTime = triggerTime

    @property
    def triggerType(self) -> str:
        return self.__triggerType

    @triggerType.setter
    def triggerType(self, triggerType: str):
        self.__triggerType = triggerType

    @property
    def messageCheckerConditionLanguage(self) -> str:
        return self.__messageCheckerConditionLanguage

    @messageCheckerConditionLanguage.setter
    def messageCheckerConditionLanguage(self, messageCheckerConditionLanguage: str):
        self.__messageCheckerConditionLanguage = messageCheckerConditionLanguage

    @property
    def triggerCodeLanguage(self) -> str:
        return self.__triggerCodeLanguage

    @triggerCodeLanguage.setter
    def triggerCodeLanguage(self, triggerCodeLanguage: str):
        self.__triggerCodeLanguage = triggerCodeLanguage

    @property
    def triggerExpRateCodeImports(self) -> str:
        return self.__triggerExpRateCodeImports

    @triggerExpRateCodeImports.setter
    def triggerExpRateCodeImports(self, triggerExpRateCodeImports: str):
        self.__triggerExpRateCodeImports = triggerExpRateCodeImports

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def guardImports(self) -> str:
        return self.__guardImports

    @guardImports.setter
    def guardImports(self, guardImports: str):
        self.__guardImports = guardImports

    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

    @property
    def messageCheckerCode(self) -> str:
        return self.__messageCheckerCode

    @messageCheckerCode.setter
    def messageCheckerCode(self, messageCheckerCode: str):
        self.__messageCheckerCode = messageCheckerCode

    @property
    def triggerTimedCodeImports(self) -> str:
        return self.__triggerTimedCodeImports

    @triggerTimedCodeImports.setter
    def triggerTimedCodeImports(self, triggerTimedCodeImports: str):
        self.__triggerTimedCodeImports = triggerTimedCodeImports

    @property
    def priority(self) -> float:
        return self.__priority

    @priority.setter
    def priority(self, priority: float):
        self.__priority = priority

    @property
    def messageCheckerCodeImports(self) -> str:
        return self.__messageCheckerCodeImports

    @messageCheckerCodeImports.setter
    def messageCheckerCodeImports(self, messageCheckerCodeImports: str):
        self.__messageCheckerCodeImports = messageCheckerCodeImports

    @property
    def outOfBranch(self) -> bool:
        return self.__outOfBranch

    @outOfBranch.setter
    def outOfBranch(self, outOfBranch: bool):
        self.__outOfBranch = outOfBranch

    @property
    def triggerProbCodeImports(self) -> str:
        return self.__triggerProbCodeImports

    @triggerProbCodeImports.setter
    def triggerProbCodeImports(self, triggerProbCodeImports: str):
        self.__triggerProbCodeImports = triggerProbCodeImports

    @property
    def triggerProbCode(self) -> str:
        return self.__triggerProbCode

    @triggerProbCode.setter
    def triggerProbCode(self, triggerProbCode: str):
        self.__triggerProbCode = triggerProbCode

    @property
    def messageCheckerClass(self) -> str:
        return self.__messageCheckerClass

    @messageCheckerClass.setter
    def messageCheckerClass(self, messageCheckerClass: str):
        self.__messageCheckerClass = messageCheckerClass

    @property
    def triggerTimedCode(self) -> str:
        return self.__triggerTimedCode

    @triggerTimedCode.setter
    def triggerTimedCode(self, triggerTimedCode: str):
        self.__triggerTimedCode = triggerTimedCode

    @property
    def triggerConditionCodeImports(self) -> str:
        return self.__triggerConditionCodeImports

    @triggerConditionCodeImports.setter
    def triggerConditionCodeImports(self, triggerConditionCodeImports: str):
        self.__triggerConditionCodeImports = triggerConditionCodeImports

    @property
    def defaultTransition(self) -> bool:
        return self.__defaultTransition

    @defaultTransition.setter
    def defaultTransition(self, defaultTransition: bool):
        self.__defaultTransition = defaultTransition

    @property
    def triggerExpRateCode(self) -> str:
        return self.__triggerExpRateCode

    @triggerExpRateCode.setter
    def triggerExpRateCode(self, triggerExpRateCode: str):
        self.__triggerExpRateCode = triggerExpRateCode

    @property
    def messageCheckerType(self) -> str:
        return self.__messageCheckerType

    @messageCheckerType.setter
    def messageCheckerType(self, messageCheckerType: str):
        self.__messageCheckerType = messageCheckerType

    @property
    def onTransitionImports(self) -> str:
        return self.__onTransitionImports

    @onTransitionImports.setter
    def onTransitionImports(self, onTransitionImports: str):
        self.__onTransitionImports = onTransitionImports

    @property
    def triggerConditionCode(self) -> str:
        return self.__triggerConditionCode

    @triggerConditionCode.setter
    def triggerConditionCode(self, triggerConditionCode: str):
        self.__triggerConditionCode = triggerConditionCode

    @property
    def onTransition(self) -> str:
        return self.__onTransition

    @onTransition.setter
    def onTransition(self, onTransition: str):
        self.__onTransition = onTransition

    @property
    def selfTransition(self) -> bool:
        return self.__selfTransition

    @selfTransition.setter
    def selfTransition(self, selfTransition: bool):
        self.__selfTransition = selfTransition

    @property
    def scmodel_Transition(self):
        return self.__scmodel_Transition

    @scmodel_Transition.setter
    def scmodel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scmodel_Transition__scmodel_Transition", None)
        self.__scmodel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scmodel_StateMachine2"):
                opp_val = getattr(old_value, "scmodel_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scmodel_StateMachine2"):
                opp_val = getattr(value, "scmodel_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "scmodel_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scmodel_Transition4(self):
        return self.__scmodel_Transition4

    @scmodel_Transition4.setter
    def scmodel_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scmodel_Transition__scmodel_Transition4", None)
        self.__scmodel_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scmodel_AbstractState5"):
                opp_val = getattr(old_value, "scmodel_AbstractState5", None)
                if opp_val == self:
                    setattr(old_value, "scmodel_AbstractState5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scmodel_AbstractState5"):
                opp_val = getattr(value, "scmodel_AbstractState5", None)
                setattr(value, "scmodel_AbstractState5", self)

    @property
    def scmodel_Transition7(self):
        return self.__scmodel_Transition7

    @scmodel_Transition7.setter
    def scmodel_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scmodel_Transition__scmodel_Transition7", None)
        self.__scmodel_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scmodel_AbstractState8"):
                opp_val = getattr(old_value, "scmodel_AbstractState8", None)
                if opp_val == self:
                    setattr(old_value, "scmodel_AbstractState8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scmodel_AbstractState8"):
                opp_val = getattr(value, "scmodel_AbstractState8", None)
                setattr(value, "scmodel_AbstractState8", self)

class scmodel_AbstractState(ABC):

    def __init__(self, id: str, onEnter: str, onExit: str, language: str, uuid: str, onEnterImports: str, onExitImports: str, scmodel_AbstractState: "scmodel_StateMachine" = None, scmodel_AbstractState5: "scmodel_Transition" = None, scmodel_AbstractState8: "scmodel_Transition" = None, scmodel_AbstractState10: "scmodel_CompositeState" = None):
        self.id = id
        self.onEnter = onEnter
        self.onExit = onExit
        self.language = language
        self.uuid = uuid
        self.onEnterImports = onEnterImports
        self.onExitImports = onExitImports
        self.scmodel_AbstractState = scmodel_AbstractState
        self.scmodel_AbstractState5 = scmodel_AbstractState5
        self.scmodel_AbstractState8 = scmodel_AbstractState8
        self.scmodel_AbstractState10 = scmodel_AbstractState10
        
    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

    @property
    def onExit(self) -> str:
        return self.__onExit

    @onExit.setter
    def onExit(self, onExit: str):
        self.__onExit = onExit

    @property
    def onEnter(self) -> str:
        return self.__onEnter

    @onEnter.setter
    def onEnter(self, onEnter: str):
        self.__onEnter = onEnter

    @property
    def onEnterImports(self) -> str:
        return self.__onEnterImports

    @onEnterImports.setter
    def onEnterImports(self, onEnterImports: str):
        self.__onEnterImports = onEnterImports

    @property
    def onExitImports(self) -> str:
        return self.__onExitImports

    @onExitImports.setter
    def onExitImports(self, onExitImports: str):
        self.__onExitImports = onExitImports

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def scmodel_AbstractState10(self):
        return self.__scmodel_AbstractState10

    @scmodel_AbstractState10.setter
    def scmodel_AbstractState10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scmodel_AbstractState__scmodel_AbstractState10", None)
        self.__scmodel_AbstractState10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scmodel_CompositeState"):
                opp_val = getattr(old_value, "scmodel_CompositeState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scmodel_CompositeState"):
                opp_val = getattr(value, "scmodel_CompositeState", None)
                if opp_val is None:
                    setattr(value, "scmodel_CompositeState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scmodel_AbstractState5(self):
        return self.__scmodel_AbstractState5

    @scmodel_AbstractState5.setter
    def scmodel_AbstractState5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scmodel_AbstractState__scmodel_AbstractState5", None)
        self.__scmodel_AbstractState5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scmodel_Transition4"):
                opp_val = getattr(old_value, "scmodel_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "scmodel_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scmodel_Transition4"):
                opp_val = getattr(value, "scmodel_Transition4", None)
                setattr(value, "scmodel_Transition4", self)

    @property
    def scmodel_AbstractState(self):
        return self.__scmodel_AbstractState

    @scmodel_AbstractState.setter
    def scmodel_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scmodel_AbstractState__scmodel_AbstractState", None)
        self.__scmodel_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scmodel_StateMachine"):
                opp_val = getattr(old_value, "scmodel_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scmodel_StateMachine"):
                opp_val = getattr(value, "scmodel_StateMachine", None)
                if opp_val is None:
                    setattr(value, "scmodel_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scmodel_AbstractState8(self):
        return self.__scmodel_AbstractState8

    @scmodel_AbstractState8.setter
    def scmodel_AbstractState8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scmodel_AbstractState__scmodel_AbstractState8", None)
        self.__scmodel_AbstractState8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scmodel_Transition7"):
                opp_val = getattr(old_value, "scmodel_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "scmodel_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scmodel_Transition7"):
                opp_val = getattr(value, "scmodel_Transition7", None)
                setattr(value, "scmodel_Transition7", self)
