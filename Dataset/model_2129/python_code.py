from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class UserInstructionEnum(Enum):
    SetUIValue = "SetUIValue"
    SendUITrigger = "SendUITrigger"
    ManipulateUIControl = "ManipulateUIControl"
    AssertUIValue = "AssertUIValue"
    AssertUIState = "AssertUIState"
    InstantiateUISUT = "InstantiateUISUT"


############################################
# Definition of Classes
############################################

class uitf_UIControl:

    def __init__(self, id: str, uitf_UIControl13: "uitf_Variable" = None, uitf_UIControl: "uitf_UISUT" = None):
        self.id = id
        self.uitf_UIControl13 = uitf_UIControl13
        self.uitf_UIControl = uitf_UIControl
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def uitf_UIControl13(self):
        return self.__uitf_UIControl13

    @uitf_UIControl13.setter
    def uitf_UIControl13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_UIControl__uitf_UIControl13", None)
        self.__uitf_UIControl13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uitf_Variable14"):
                opp_val = getattr(old_value, "uitf_Variable14", None)
                if opp_val == self:
                    setattr(old_value, "uitf_Variable14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uitf_Variable14"):
                opp_val = getattr(value, "uitf_Variable14", None)
                setattr(value, "uitf_Variable14", self)

    @property
    def uitf_UIControl(self):
        return self.__uitf_UIControl

    @uitf_UIControl.setter
    def uitf_UIControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_UIControl__uitf_UIControl", None)
        self.__uitf_UIControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uitf_UISUT8"):
                opp_val = getattr(old_value, "uitf_UISUT8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uitf_UISUT8"):
                opp_val = getattr(value, "uitf_UISUT8", None)
                if opp_val is None:
                    setattr(value, "uitf_UISUT8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Statement:

    pass
class uitf_TriggeredTransition(Statement):

    def __init__(self, scriptStr: str, transitionId: str):
        self.scriptStr = scriptStr
        self.transitionId = transitionId
        
    @property
    def scriptStr(self) -> str:
        return self.__scriptStr

    @scriptStr.setter
    def scriptStr(self, scriptStr: str):
        self.__scriptStr = scriptStr

    @property
    def transitionId(self) -> str:
        return self.__transitionId

    @transitionId.setter
    def transitionId(self, transitionId: str):
        self.__transitionId = transitionId

class uitf_AssertInState(Statement):

    def __init__(self, stateId: str):
        self.stateId = stateId
        
    @property
    def stateId(self) -> str:
        return self.__stateId

    @stateId.setter
    def stateId(self, stateId: str):
        self.__stateId = stateId

class uitf_TestSuite:

    def __init__(self, id: str, uitf_TestSuite: set["uitf_TestCase"] = None):
        self.id = id
        self.uitf_TestSuite = uitf_TestSuite if uitf_TestSuite is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def uitf_TestSuite(self):
        return self.__uitf_TestSuite

    @uitf_TestSuite.setter
    def uitf_TestSuite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_TestSuite__uitf_TestSuite", None)
        self.__uitf_TestSuite = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uitf_TestCase4"):
                    opp_val = getattr(item, "uitf_TestCase4", None)
                    
                    if opp_val == self:
                        setattr(item, "uitf_TestCase4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uitf_TestCase4"):
                    opp_val = getattr(item, "uitf_TestCase4", None)
                    
                    setattr(item, "uitf_TestCase4", self)
                    

    def stop(self):
        # TODO: Implement stop method
        pass

    def start(self):
        # TODO: Implement start method
        pass

class uitf_Statement:

    def __init__(self, description: str, kind: str, uitf_Statement: "uitf_TestCase" = None, uitf_Statement10: "uitf_Variable" = None):
        self.description = description
        self.kind = kind
        self.uitf_Statement = uitf_Statement
        self.uitf_Statement10 = uitf_Statement10
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def uitf_Statement(self):
        return self.__uitf_Statement

    @uitf_Statement.setter
    def uitf_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_Statement__uitf_Statement", None)
        self.__uitf_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uitf_TestCase2"):
                opp_val = getattr(old_value, "uitf_TestCase2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uitf_TestCase2"):
                opp_val = getattr(value, "uitf_TestCase2", None)
                if opp_val is None:
                    setattr(value, "uitf_TestCase2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uitf_Statement10(self):
        return self.__uitf_Statement10

    @uitf_Statement10.setter
    def uitf_Statement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_Statement__uitf_Statement10", None)
        self.__uitf_Statement10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uitf_Variable11"):
                opp_val = getattr(old_value, "uitf_Variable11", None)
                if opp_val == self:
                    setattr(old_value, "uitf_Variable11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uitf_Variable11"):
                opp_val = getattr(value, "uitf_Variable11", None)
                setattr(value, "uitf_Variable11", self)

class Variable:

    pass
class uitf_UIControlVariable(Variable):

    pass
class uitf_UISUT(Variable):

    def __init__(self, objectURI: str, uitf_UISUT: "uitf_TestCase" = None, uitf_UISUT6: set["uitf_Variable"] = None, uitf_UISUT8: set["uitf_UIControl"] = None):
        self.objectURI = objectURI
        self.uitf_UISUT = uitf_UISUT
        self.uitf_UISUT6 = uitf_UISUT6 if uitf_UISUT6 is not None else set()
        self.uitf_UISUT8 = uitf_UISUT8 if uitf_UISUT8 is not None else set()
        
    @property
    def objectURI(self) -> str:
        return self.__objectURI

    @objectURI.setter
    def objectURI(self, objectURI: str):
        self.__objectURI = objectURI

    @property
    def uitf_UISUT(self):
        return self.__uitf_UISUT

    @uitf_UISUT.setter
    def uitf_UISUT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_UISUT__uitf_UISUT", None)
        self.__uitf_UISUT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uitf_TestCase"):
                opp_val = getattr(old_value, "uitf_TestCase", None)
                if opp_val == self:
                    setattr(old_value, "uitf_TestCase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uitf_TestCase"):
                opp_val = getattr(value, "uitf_TestCase", None)
                setattr(value, "uitf_TestCase", self)

    @property
    def uitf_UISUT8(self):
        return self.__uitf_UISUT8

    @uitf_UISUT8.setter
    def uitf_UISUT8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_UISUT__uitf_UISUT8", None)
        self.__uitf_UISUT8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uitf_UIControl"):
                    opp_val = getattr(item, "uitf_UIControl", None)
                    
                    if opp_val == self:
                        setattr(item, "uitf_UIControl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uitf_UIControl"):
                    opp_val = getattr(item, "uitf_UIControl", None)
                    
                    setattr(item, "uitf_UIControl", self)
                    

    @property
    def uitf_UISUT6(self):
        return self.__uitf_UISUT6

    @uitf_UISUT6.setter
    def uitf_UISUT6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_UISUT__uitf_UISUT6", None)
        self.__uitf_UISUT6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uitf_Variable"):
                    opp_val = getattr(item, "uitf_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "uitf_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uitf_Variable"):
                    opp_val = getattr(item, "uitf_Variable", None)
                    
                    setattr(item, "uitf_Variable", self)
                    

    def onManipulateUIControl(self, manipulationKind: str, controlPath: str):
        # TODO: Implement onManipulateUIControl method
        pass

    def assertInState(self):
        # TODO: Implement assertInState method
        pass

    def onUITrigger(self, trigger: str):
        # TODO: Implement onUITrigger method
        pass

    def onManipulateUIControlData(self, controlPropertyKey: str, controlPath: str, controlPropertyVal: str):
        # TODO: Implement onManipulateUIControlData method
        pass

class uitf_Variable:

    def __init__(self, id: str, uitf_Variable14: "uitf_UIControl" = None, uitf_Variable: "uitf_UISUT" = None, uitf_Variable11: "uitf_Statement" = None):
        self.id = id
        self.uitf_Variable14 = uitf_Variable14
        self.uitf_Variable = uitf_Variable
        self.uitf_Variable11 = uitf_Variable11
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def uitf_Variable(self):
        return self.__uitf_Variable

    @uitf_Variable.setter
    def uitf_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_Variable__uitf_Variable", None)
        self.__uitf_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uitf_UISUT6"):
                opp_val = getattr(old_value, "uitf_UISUT6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uitf_UISUT6"):
                opp_val = getattr(value, "uitf_UISUT6", None)
                if opp_val is None:
                    setattr(value, "uitf_UISUT6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uitf_Variable11(self):
        return self.__uitf_Variable11

    @uitf_Variable11.setter
    def uitf_Variable11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_Variable__uitf_Variable11", None)
        self.__uitf_Variable11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uitf_Statement10"):
                opp_val = getattr(old_value, "uitf_Statement10", None)
                if opp_val == self:
                    setattr(old_value, "uitf_Statement10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uitf_Statement10"):
                opp_val = getattr(value, "uitf_Statement10", None)
                setattr(value, "uitf_Statement10", self)

    @property
    def uitf_Variable14(self):
        return self.__uitf_Variable14

    @uitf_Variable14.setter
    def uitf_Variable14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_Variable__uitf_Variable14", None)
        self.__uitf_Variable14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uitf_UIControl13"):
                opp_val = getattr(old_value, "uitf_UIControl13", None)
                if opp_val == self:
                    setattr(old_value, "uitf_UIControl13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uitf_UIControl13"):
                opp_val = getattr(value, "uitf_UIControl13", None)
                setattr(value, "uitf_UIControl13", self)

    def getValue(self) -> str:
        # TODO: Implement getValue method
        pass

    def assertValue(self):
        # TODO: Implement assertValue method
        pass

    def setValue(self, val: str):
        # TODO: Implement setValue method
        pass

class uitf_TestCase:

    def __init__(self, id: str, uitf_TestCase: "uitf_UISUT" = None, uitf_TestCase2: set["uitf_Statement"] = None, uitf_TestCase4: "uitf_TestSuite" = None):
        self.id = id
        self.uitf_TestCase = uitf_TestCase
        self.uitf_TestCase2 = uitf_TestCase2 if uitf_TestCase2 is not None else set()
        self.uitf_TestCase4 = uitf_TestCase4
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def uitf_TestCase4(self):
        return self.__uitf_TestCase4

    @uitf_TestCase4.setter
    def uitf_TestCase4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_TestCase__uitf_TestCase4", None)
        self.__uitf_TestCase4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uitf_TestSuite"):
                opp_val = getattr(old_value, "uitf_TestSuite", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uitf_TestSuite"):
                opp_val = getattr(value, "uitf_TestSuite", None)
                if opp_val is None:
                    setattr(value, "uitf_TestSuite", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uitf_TestCase2(self):
        return self.__uitf_TestCase2

    @uitf_TestCase2.setter
    def uitf_TestCase2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_TestCase__uitf_TestCase2", None)
        self.__uitf_TestCase2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uitf_Statement"):
                    opp_val = getattr(item, "uitf_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "uitf_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uitf_Statement"):
                    opp_val = getattr(item, "uitf_Statement", None)
                    
                    setattr(item, "uitf_Statement", self)
                    

    @property
    def uitf_TestCase(self):
        return self.__uitf_TestCase

    @uitf_TestCase.setter
    def uitf_TestCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uitf_TestCase__uitf_TestCase", None)
        self.__uitf_TestCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uitf_UISUT"):
                opp_val = getattr(old_value, "uitf_UISUT", None)
                if opp_val == self:
                    setattr(old_value, "uitf_UISUT", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uitf_UISUT"):
                opp_val = getattr(value, "uitf_UISUT", None)
                setattr(value, "uitf_UISUT", self)

    def stop(self):
        # TODO: Implement stop method
        pass

    def start(self):
        # TODO: Implement start method
        pass
