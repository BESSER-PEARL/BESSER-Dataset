from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TimeUnit(Enum):
    ms = "ms"
    s = "s"
    m = "m"
    h = "h"


############################################
# Definition of Classes
############################################

class ResourceImport:

    pass
class scxmlxt_DomainDataImport(ResourceImport):

    pass
class scxmlxt_DomainModelImport(ResourceImport):

    pass
class IntLiteral:

    pass
class scxmlxt_DelayLiteral(IntLiteral):

    def __init__(self, timeUnit: str):
        self.timeUnit = timeUnit
        
        pass
    @property
    def timeUnit(self):
        return self.__timeUnit

    @timeUnit.setter
    def timeUnit(self, timeUnit: str):
        self.__timeUnit = timeUnit


class scxmlxt_EObject:

    pass
class scxmlxt_EObjectReference:

    pass
class ResourceUriLiteral:

    pass
class scxmlxt_EObjectUriLiteral(ResourceUriLiteral):

    def __init__(self, uriFragment: str):
        self.uriFragment = uriFragment
        
        pass
    @property
    def uriFragment(self):
        return self.__uriFragment

    @uriFragment.setter
    def uriFragment(self, uriFragment: str):
        self.__uriFragment = uriFragment


class AbstractUriLiteral:

    pass
class scxmlxt_ResourceUriLiteral(AbstractUriLiteral):

    def __init__(self, resourceUri: str):
        self.resourceUri = resourceUri
        
        pass
    @property
    def resourceUri(self):
        return self.__resourceUri

    @resourceUri.setter
    def resourceUri(self, resourceUri: str):
        self.__resourceUri = resourceUri


class scxmlxt_UriLiteral(AbstractUriLiteral):

    def __init__(self, uriValue: str):
        self.uriValue = uriValue
        
        pass
    @property
    def uriValue(self):
        return self.__uriValue

    @uriValue.setter
    def uriValue(self, uriValue: str):
        self.__uriValue = uriValue


class Expression:

    pass
class scxmlxt_VarRef(Expression):

    pass
class Literal:

    pass
class scxmlxt_FloatLiteral(Literal):

    def __init__(self, floatValue: float):
        self.floatValue = floatValue
        
        pass
    @property
    def floatValue(self):
        return self.__floatValue

    @floatValue.setter
    def floatValue(self, floatValue: float):
        self.__floatValue = floatValue


class scxmlxt_StringLiteral(Literal):

    def __init__(self, stringValue: str):
        self.stringValue = stringValue
        
        pass
    @property
    def stringValue(self):
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue


class scxmlxt_IntLiteral(Literal):

    def __init__(self, intValue: int):
        self.intValue = intValue
        
        pass
    @property
    def intValue(self):
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: int):
        self.__intValue = intValue


class scxmlxt_AbstractUriLiteral(Literal):

    def __init__(self, uri: str):
        self.uri = uri
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


class scxmlxt_BooleanLiteral(Literal):

    def __init__(self, booleanValue: bool):
        self.booleanValue = booleanValue
        
        pass
    @property
    def booleanValue(self):
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: bool):
        self.__booleanValue = booleanValue


class scxmlxt_Literal(Expression):

    pass
class scxmlxt_ScriptExpression(Expression):

    def __init__(self, script: str, scxmlxt_ScriptExpression: "scxmlxt_EStepFilter" = None):
        self.script = script
        self.scxmlxt_ScriptExpression = scxmlxt_ScriptExpression
        
        pass
    @property
    def script(self):
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script


    @property
    def scxmlxt_ScriptExpression(self):
        return self.__scxmlxt_ScriptExpression

    @scxmlxt_ScriptExpression.setter
    def scxmlxt_ScriptExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_ScriptExpression__scxmlxt_ScriptExpression", None)
        self.__scxmlxt_ScriptExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_EStepFilter51"):
                opp_val = getattr(old_value, "scxmlxt_EStepFilter51", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_EStepFilter51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_EStepFilter51"):
                opp_val = getattr(value, "scxmlxt_EStepFilter51", None)
                setattr(value, "scxmlxt_EStepFilter51", self)

class scxmlxt_EStepFilter:

    def __init__(self, freeVarName: str, scxmlxt_EStepFilter: "scxmlxt_EStep" = None, scxmlxt_EStepFilter51: "scxmlxt_ScriptExpression" = None):
        self.freeVarName = freeVarName
        self.scxmlxt_EStepFilter = scxmlxt_EStepFilter
        self.scxmlxt_EStepFilter51 = scxmlxt_EStepFilter51
        
        pass
    @property
    def freeVarName(self):
        return self.__freeVarName

    @freeVarName.setter
    def freeVarName(self, freeVarName: str):
        self.__freeVarName = freeVarName


    @property
    def scxmlxt_EStepFilter(self):
        return self.__scxmlxt_EStepFilter

    @scxmlxt_EStepFilter.setter
    def scxmlxt_EStepFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_EStepFilter__scxmlxt_EStepFilter", None)
        self.__scxmlxt_EStepFilter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_EStep49"):
                opp_val = getattr(old_value, "scxmlxt_EStep49", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_EStep49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_EStep49"):
                opp_val = getattr(value, "scxmlxt_EStep49", None)
                setattr(value, "scxmlxt_EStep49", self)

    @property
    def scxmlxt_EStepFilter51(self):
        return self.__scxmlxt_EStepFilter51

    @scxmlxt_EStepFilter51.setter
    def scxmlxt_EStepFilter51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_EStepFilter__scxmlxt_EStepFilter51", None)
        self.__scxmlxt_EStepFilter51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_ScriptExpression"):
                opp_val = getattr(old_value, "scxmlxt_ScriptExpression", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_ScriptExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_ScriptExpression"):
                opp_val = getattr(value, "scxmlxt_ScriptExpression", None)
                setattr(value, "scxmlxt_ScriptExpression", self)

class scxmlxt_EStep:

    def __init__(self, featureName: str, scxmlxt_EStep: "scxmlxt_EPath" = None, scxmlxt_EStep49: "scxmlxt_EStepFilter" = None):
        self.featureName = featureName
        self.scxmlxt_EStep = scxmlxt_EStep
        self.scxmlxt_EStep49 = scxmlxt_EStep49
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def scxmlxt_EStep49(self):
        return self.__scxmlxt_EStep49

    @scxmlxt_EStep49.setter
    def scxmlxt_EStep49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_EStep__scxmlxt_EStep49", None)
        self.__scxmlxt_EStep49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_EStepFilter"):
                opp_val = getattr(old_value, "scxmlxt_EStepFilter", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_EStepFilter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_EStepFilter"):
                opp_val = getattr(value, "scxmlxt_EStepFilter", None)
                setattr(value, "scxmlxt_EStepFilter", self)

    @property
    def scxmlxt_EStep(self):
        return self.__scxmlxt_EStep

    @scxmlxt_EStep.setter
    def scxmlxt_EStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_EStep__scxmlxt_EStep", None)
        self.__scxmlxt_EStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_EPath47"):
                opp_val = getattr(old_value, "scxmlxt_EPath47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_EPath47"):
                opp_val = getattr(value, "scxmlxt_EPath47", None)
                if opp_val is None:
                    setattr(value, "scxmlxt_EPath47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxmlxt_EPath(Expression):

    pass
class Typed:

    pass
class scxmlxt_EClassifier:

    pass
class scxmlxt_Typed:

    def __init__(self, many: bool, scxmlxt_Typed: "scxmlxt_EClassifier" = None):
        self.many = many
        self.scxmlxt_Typed = scxmlxt_Typed
        
        pass
    @property
    def many(self):
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many


    @property
    def scxmlxt_Typed(self):
        return self.__scxmlxt_Typed

    @scxmlxt_Typed.setter
    def scxmlxt_Typed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_Typed__scxmlxt_Typed", None)
        self.__scxmlxt_Typed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_EClassifier"):
                opp_val = getattr(old_value, "scxmlxt_EClassifier", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_EClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_EClassifier"):
                opp_val = getattr(value, "scxmlxt_EClassifier", None)
                setattr(value, "scxmlxt_EClassifier", self)

class Action:

    pass
class scxmlxt_AssignmentAction(Action):

    pass
class scxmlxt_ScriptAction(Action):

    def __init__(self, script: str):
        self.script = script
        
        pass
    @property
    def script(self):
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script


class scxmlxt_SymbolicAction(Action):

    def __init__(self, name: str, scxmlxt_SymbolicAction: "scxmlxt_Expression" = None):
        self.name = name
        self.scxmlxt_SymbolicAction = scxmlxt_SymbolicAction
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def scxmlxt_SymbolicAction(self):
        return self.__scxmlxt_SymbolicAction

    @scxmlxt_SymbolicAction.setter
    def scxmlxt_SymbolicAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_SymbolicAction__scxmlxt_SymbolicAction", None)
        self.__scxmlxt_SymbolicAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_Expression32"):
                opp_val = getattr(old_value, "scxmlxt_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_Expression32"):
                opp_val = getattr(value, "scxmlxt_Expression32", None)
                setattr(value, "scxmlxt_Expression32", self)

class scxmlxt_Expression(ABC):

    pass
class AbstractTransitionEvent:

    pass
class scxmlxt_EnterEvent(AbstractTransitionEvent):

    pass
class scxmlxt_ExitEvent(AbstractTransitionEvent):

    pass
class scxmlxt_TransitionEvent(AbstractTransitionEvent):

    pass
class Event:

    pass
class scxmlxt_ScriptEvent(Event):

    def __init__(self, script: str):
        self.script = script
        
        pass
    @property
    def script(self):
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script


class scxmlxt_AbstractTransitionEvent(Event):

    def __init__(self):
        
        pass
    def getSource(self) :
        # TODO: Implement getSource method
        pass

    def getTarget(self) :
        # TODO: Implement getTarget method
        pass

class scxmlxt_TimerEvent(Event):

    pass
class scxmlxt_SymbolicEvent(Event):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class AbstractTransition:

    pass
class scxmlxt_InternalTransition(AbstractTransition):

    pass
class scxmlxt_Transition(AbstractTransition):

    pass
class scxmlxt_Condition:

    def __init__(self, script: str, scxmlxt_Condition: "scxmlxt_AbstractTransition" = None):
        self.script = script
        self.scxmlxt_Condition = scxmlxt_Condition
        
        pass
    @property
    def script(self):
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script


    @property
    def scxmlxt_Condition(self):
        return self.__scxmlxt_Condition

    @scxmlxt_Condition.setter
    def scxmlxt_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_Condition__scxmlxt_Condition", None)
        self.__scxmlxt_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_AbstractTransition16"):
                opp_val = getattr(old_value, "scxmlxt_AbstractTransition16", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_AbstractTransition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_AbstractTransition16"):
                opp_val = getattr(value, "scxmlxt_AbstractTransition16", None)
                setattr(value, "scxmlxt_AbstractTransition16", self)

class scxmlxt_Event(ABC):

    pass
class scxmlxt_VarDef(Typed):

    def __init__(self, name: str, scxmlxt_VarDef: "scxmlxt_AbstractState" = None, scxmlxt_VarDef35: "scxmlxt_Expression" = None, scxmlxt_VarDef38: "scxmlxt_AssignmentAction" = None, scxmlxt_VarDef43: "scxmlxt_VarRef" = None):
        self.name = name
        self.scxmlxt_VarDef = scxmlxt_VarDef
        self.scxmlxt_VarDef35 = scxmlxt_VarDef35
        self.scxmlxt_VarDef38 = scxmlxt_VarDef38
        self.scxmlxt_VarDef43 = scxmlxt_VarDef43
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def scxmlxt_VarDef43(self):
        return self.__scxmlxt_VarDef43

    @scxmlxt_VarDef43.setter
    def scxmlxt_VarDef43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_VarDef__scxmlxt_VarDef43", None)
        self.__scxmlxt_VarDef43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_VarRef"):
                opp_val = getattr(old_value, "scxmlxt_VarRef", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_VarRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_VarRef"):
                opp_val = getattr(value, "scxmlxt_VarRef", None)
                setattr(value, "scxmlxt_VarRef", self)

    @property
    def scxmlxt_VarDef35(self):
        return self.__scxmlxt_VarDef35

    @scxmlxt_VarDef35.setter
    def scxmlxt_VarDef35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_VarDef__scxmlxt_VarDef35", None)
        self.__scxmlxt_VarDef35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_Expression36"):
                opp_val = getattr(old_value, "scxmlxt_Expression36", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_Expression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_Expression36"):
                opp_val = getattr(value, "scxmlxt_Expression36", None)
                setattr(value, "scxmlxt_Expression36", self)

    @property
    def scxmlxt_VarDef(self):
        return self.__scxmlxt_VarDef

    @scxmlxt_VarDef.setter
    def scxmlxt_VarDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_VarDef__scxmlxt_VarDef", None)
        self.__scxmlxt_VarDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_AbstractState12"):
                opp_val = getattr(old_value, "scxmlxt_AbstractState12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_AbstractState12"):
                opp_val = getattr(value, "scxmlxt_AbstractState12", None)
                if opp_val is None:
                    setattr(value, "scxmlxt_AbstractState12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxmlxt_VarDef38(self):
        return self.__scxmlxt_VarDef38

    @scxmlxt_VarDef38.setter
    def scxmlxt_VarDef38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_VarDef__scxmlxt_VarDef38", None)
        self.__scxmlxt_VarDef38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_AssignmentAction"):
                opp_val = getattr(old_value, "scxmlxt_AssignmentAction", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_AssignmentAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_AssignmentAction"):
                opp_val = getattr(value, "scxmlxt_AssignmentAction", None)
                setattr(value, "scxmlxt_AssignmentAction", self)

class scxmlxt_AbstractTransition(ABC):

    pass
class scxmlxt_AbstractState(ABC):

    pass
class scxmlxt_Action(ABC):

    pass
class scxmlxt_InitialTransition:

    pass
class scxmlxt_ResourceImport(ABC):

    def __init__(self, importURI: str, scxmlxt_ResourceImport: "scxmlxt_StateMachine" = None):
        self.importURI = importURI
        self.scxmlxt_ResourceImport = scxmlxt_ResourceImport
        
        pass
    @property
    def importURI(self):
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI


    @property
    def scxmlxt_ResourceImport(self):
        return self.__scxmlxt_ResourceImport

    @scxmlxt_ResourceImport.setter
    def scxmlxt_ResourceImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_ResourceImport__scxmlxt_ResourceImport", None)
        self.__scxmlxt_ResourceImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_StateMachine"):
                opp_val = getattr(old_value, "scxmlxt_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_StateMachine"):
                opp_val = getattr(value, "scxmlxt_StateMachine", None)
                if opp_val is None:
                    setattr(value, "scxmlxt_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractState:

    pass
class scxmlxt_State(AbstractState):

    def __init__(self, name: str, scxmlxt_State: "scxmlxt_StateMachine" = None, scxmlxt_State4: "scxmlxt_InitialTransition" = None, scxmlxt_State8: "scxmlxt_AbstractState" = None, scxmlxt_State21: "scxmlxt_Transition" = None, scxmlxt_State26: "scxmlxt_TransitionEvent" = None, scxmlxt_State23: "scxmlxt_TransitionEvent" = None):
        self.name = name
        self.scxmlxt_State = scxmlxt_State
        self.scxmlxt_State4 = scxmlxt_State4
        self.scxmlxt_State8 = scxmlxt_State8
        self.scxmlxt_State21 = scxmlxt_State21
        self.scxmlxt_State26 = scxmlxt_State26
        self.scxmlxt_State23 = scxmlxt_State23
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def scxmlxt_State21(self):
        return self.__scxmlxt_State21

    @scxmlxt_State21.setter
    def scxmlxt_State21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_State__scxmlxt_State21", None)
        self.__scxmlxt_State21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_Transition"):
                opp_val = getattr(old_value, "scxmlxt_Transition", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_Transition"):
                opp_val = getattr(value, "scxmlxt_Transition", None)
                setattr(value, "scxmlxt_Transition", self)

    @property
    def scxmlxt_State(self):
        return self.__scxmlxt_State

    @scxmlxt_State.setter
    def scxmlxt_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_State__scxmlxt_State", None)
        self.__scxmlxt_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_StateMachine2"):
                opp_val = getattr(old_value, "scxmlxt_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_StateMachine2"):
                opp_val = getattr(value, "scxmlxt_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "scxmlxt_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxmlxt_State26(self):
        return self.__scxmlxt_State26

    @scxmlxt_State26.setter
    def scxmlxt_State26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_State__scxmlxt_State26", None)
        self.__scxmlxt_State26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_TransitionEvent25"):
                opp_val = getattr(old_value, "scxmlxt_TransitionEvent25", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_TransitionEvent25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_TransitionEvent25"):
                opp_val = getattr(value, "scxmlxt_TransitionEvent25", None)
                setattr(value, "scxmlxt_TransitionEvent25", self)

    @property
    def scxmlxt_State8(self):
        return self.__scxmlxt_State8

    @scxmlxt_State8.setter
    def scxmlxt_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_State__scxmlxt_State8", None)
        self.__scxmlxt_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_AbstractState"):
                opp_val = getattr(old_value, "scxmlxt_AbstractState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_AbstractState"):
                opp_val = getattr(value, "scxmlxt_AbstractState", None)
                if opp_val is None:
                    setattr(value, "scxmlxt_AbstractState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxmlxt_State4(self):
        return self.__scxmlxt_State4

    @scxmlxt_State4.setter
    def scxmlxt_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_State__scxmlxt_State4", None)
        self.__scxmlxt_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_InitialTransition"):
                opp_val = getattr(old_value, "scxmlxt_InitialTransition", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_InitialTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_InitialTransition"):
                opp_val = getattr(value, "scxmlxt_InitialTransition", None)
                setattr(value, "scxmlxt_InitialTransition", self)

    @property
    def scxmlxt_State23(self):
        return self.__scxmlxt_State23

    @scxmlxt_State23.setter
    def scxmlxt_State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxmlxt_State__scxmlxt_State23", None)
        self.__scxmlxt_State23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxmlxt_TransitionEvent"):
                opp_val = getattr(old_value, "scxmlxt_TransitionEvent", None)
                if opp_val == self:
                    setattr(old_value, "scxmlxt_TransitionEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxmlxt_TransitionEvent"):
                opp_val = getattr(value, "scxmlxt_TransitionEvent", None)
                setattr(value, "scxmlxt_TransitionEvent", self)

class scxmlxt_StateMachine(AbstractState):

    pass