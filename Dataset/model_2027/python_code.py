from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class uisut_UISUTElement(ABC):

    def __init__(self, name: str, description: str, id: str):
        self.name = name
        self.description = description
        self.id = id
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class UITrigger:

    pass
class uisut_ComponentTrigger(UITrigger):

    pass
class uisut_UserTrigger(UITrigger):

    pass
class AbstractState:

    pass
class uisut_FinalState(AbstractState):

    pass
class uisut_InitialState(AbstractState):

    pass
class uisut_UIState(AbstractState):

    def __init__(self, isInitial: bool, pic: str, uisut_UIState: set["uisut_UIControl"] = None, uisut_UIState11: set["uisut_UIDataVariable"] = None, uisut_UIState14: set["uisut_UIDataVariable"] = None):
        self.isInitial = isInitial
        self.pic = pic
        self.uisut_UIState = uisut_UIState if uisut_UIState is not None else set()
        self.uisut_UIState11 = uisut_UIState11 if uisut_UIState11 is not None else set()
        self.uisut_UIState14 = uisut_UIState14 if uisut_UIState14 is not None else set()
        
    @property
    def pic(self) -> str:
        return self.__pic

    @pic.setter
    def pic(self, pic: str):
        self.__pic = pic

    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def uisut_UIState11(self):
        return self.__uisut_UIState11

    @uisut_UIState11.setter
    def uisut_UIState11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIState__uisut_UIState11", None)
        self.__uisut_UIState11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uisut_UIDataVariable12"):
                    opp_val = getattr(item, "uisut_UIDataVariable12", None)
                    
                    if opp_val == self:
                        setattr(item, "uisut_UIDataVariable12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uisut_UIDataVariable12"):
                    opp_val = getattr(item, "uisut_UIDataVariable12", None)
                    
                    setattr(item, "uisut_UIDataVariable12", self)
                    

    @property
    def uisut_UIState14(self):
        return self.__uisut_UIState14

    @uisut_UIState14.setter
    def uisut_UIState14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIState__uisut_UIState14", None)
        self.__uisut_UIState14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uisut_UIDataVariable15"):
                    opp_val = getattr(item, "uisut_UIDataVariable15", None)
                    
                    if opp_val == self:
                        setattr(item, "uisut_UIDataVariable15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uisut_UIDataVariable15"):
                    opp_val = getattr(item, "uisut_UIDataVariable15", None)
                    
                    setattr(item, "uisut_UIDataVariable15", self)
                    

    @property
    def uisut_UIState(self):
        return self.__uisut_UIState

    @uisut_UIState.setter
    def uisut_UIState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIState__uisut_UIState", None)
        self.__uisut_UIState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uisut_UIControl"):
                    opp_val = getattr(item, "uisut_UIControl", None)
                    
                    if opp_val == self:
                        setattr(item, "uisut_UIControl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uisut_UIControl"):
                    opp_val = getattr(item, "uisut_UIControl", None)
                    
                    setattr(item, "uisut_UIControl", self)
                    

class UISUTElement:

    pass
class uisut_UIControl(UISUTElement):

    def __init__(self, valueExpression: str, variableName: str, uisut_UIControl: "uisut_UIState" = None, uisut_UIControl29: "uisut_UIDataVariable" = None, uisut_UIControl32: "uisut_UIDataVariable" = None):
        self.valueExpression = valueExpression
        self.variableName = variableName
        self.uisut_UIControl = uisut_UIControl
        self.uisut_UIControl29 = uisut_UIControl29
        self.uisut_UIControl32 = uisut_UIControl32
        
    @property
    def valueExpression(self) -> str:
        return self.__valueExpression

    @valueExpression.setter
    def valueExpression(self, valueExpression: str):
        self.__valueExpression = valueExpression

    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def uisut_UIControl29(self):
        return self.__uisut_UIControl29

    @uisut_UIControl29.setter
    def uisut_UIControl29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIControl__uisut_UIControl29", None)
        self.__uisut_UIControl29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UIDataVariable30"):
                opp_val = getattr(old_value, "uisut_UIDataVariable30", None)
                if opp_val == self:
                    setattr(old_value, "uisut_UIDataVariable30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UIDataVariable30"):
                opp_val = getattr(value, "uisut_UIDataVariable30", None)
                setattr(value, "uisut_UIDataVariable30", self)

    @property
    def uisut_UIControl(self):
        return self.__uisut_UIControl

    @uisut_UIControl.setter
    def uisut_UIControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIControl__uisut_UIControl", None)
        self.__uisut_UIControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UIState"):
                opp_val = getattr(old_value, "uisut_UIState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UIState"):
                opp_val = getattr(value, "uisut_UIState", None)
                if opp_val is None:
                    setattr(value, "uisut_UIState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uisut_UIControl32(self):
        return self.__uisut_UIControl32

    @uisut_UIControl32.setter
    def uisut_UIControl32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIControl__uisut_UIControl32", None)
        self.__uisut_UIControl32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UIDataVariable33"):
                opp_val = getattr(old_value, "uisut_UIDataVariable33", None)
                if opp_val == self:
                    setattr(old_value, "uisut_UIDataVariable33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UIDataVariable33"):
                opp_val = getattr(value, "uisut_UIDataVariable33", None)
                setattr(value, "uisut_UIDataVariable33", self)

class uisut_UICondition(UISUTElement):

    pass
class uisut_UIDataVariable(UISUTElement):

    def __init__(self, constraintRE: str, uisut_UIDataVariable12: "uisut_UIState" = None, uisut_UIDataVariable15: "uisut_UIState" = None, uisut_UIDataVariable: "uisut_UIStatemachine" = None, uisut_UIDataVariable30: "uisut_UIControl" = None, uisut_UIDataVariable27: "uisut_UITransition" = None, uisut_UIDataVariable33: "uisut_UIControl" = None):
        self.constraintRE = constraintRE
        self.uisut_UIDataVariable12 = uisut_UIDataVariable12
        self.uisut_UIDataVariable15 = uisut_UIDataVariable15
        self.uisut_UIDataVariable = uisut_UIDataVariable
        self.uisut_UIDataVariable30 = uisut_UIDataVariable30
        self.uisut_UIDataVariable27 = uisut_UIDataVariable27
        self.uisut_UIDataVariable33 = uisut_UIDataVariable33
        
    @property
    def constraintRE(self) -> str:
        return self.__constraintRE

    @constraintRE.setter
    def constraintRE(self, constraintRE: str):
        self.__constraintRE = constraintRE

    @property
    def uisut_UIDataVariable30(self):
        return self.__uisut_UIDataVariable30

    @uisut_UIDataVariable30.setter
    def uisut_UIDataVariable30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIDataVariable__uisut_UIDataVariable30", None)
        self.__uisut_UIDataVariable30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UIControl29"):
                opp_val = getattr(old_value, "uisut_UIControl29", None)
                if opp_val == self:
                    setattr(old_value, "uisut_UIControl29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UIControl29"):
                opp_val = getattr(value, "uisut_UIControl29", None)
                setattr(value, "uisut_UIControl29", self)

    @property
    def uisut_UIDataVariable33(self):
        return self.__uisut_UIDataVariable33

    @uisut_UIDataVariable33.setter
    def uisut_UIDataVariable33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIDataVariable__uisut_UIDataVariable33", None)
        self.__uisut_UIDataVariable33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UIControl32"):
                opp_val = getattr(old_value, "uisut_UIControl32", None)
                if opp_val == self:
                    setattr(old_value, "uisut_UIControl32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UIControl32"):
                opp_val = getattr(value, "uisut_UIControl32", None)
                setattr(value, "uisut_UIControl32", self)

    @property
    def uisut_UIDataVariable27(self):
        return self.__uisut_UIDataVariable27

    @uisut_UIDataVariable27.setter
    def uisut_UIDataVariable27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIDataVariable__uisut_UIDataVariable27", None)
        self.__uisut_UIDataVariable27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UITransition26"):
                opp_val = getattr(old_value, "uisut_UITransition26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UITransition26"):
                opp_val = getattr(value, "uisut_UITransition26", None)
                if opp_val is None:
                    setattr(value, "uisut_UITransition26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uisut_UIDataVariable12(self):
        return self.__uisut_UIDataVariable12

    @uisut_UIDataVariable12.setter
    def uisut_UIDataVariable12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIDataVariable__uisut_UIDataVariable12", None)
        self.__uisut_UIDataVariable12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UIState11"):
                opp_val = getattr(old_value, "uisut_UIState11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UIState11"):
                opp_val = getattr(value, "uisut_UIState11", None)
                if opp_val is None:
                    setattr(value, "uisut_UIState11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uisut_UIDataVariable(self):
        return self.__uisut_UIDataVariable

    @uisut_UIDataVariable.setter
    def uisut_UIDataVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIDataVariable__uisut_UIDataVariable", None)
        self.__uisut_UIDataVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UIStatemachine8"):
                opp_val = getattr(old_value, "uisut_UIStatemachine8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UIStatemachine8"):
                opp_val = getattr(value, "uisut_UIStatemachine8", None)
                if opp_val is None:
                    setattr(value, "uisut_UIStatemachine8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uisut_UIDataVariable15(self):
        return self.__uisut_UIDataVariable15

    @uisut_UIDataVariable15.setter
    def uisut_UIDataVariable15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UIDataVariable__uisut_UIDataVariable15", None)
        self.__uisut_UIDataVariable15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UIState14"):
                opp_val = getattr(old_value, "uisut_UIState14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UIState14"):
                opp_val = getattr(value, "uisut_UIState14", None)
                if opp_val is None:
                    setattr(value, "uisut_UIState14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uisut_UITrigger(UISUTElement):

    pass
class uisut_UIStatemachine(UISUTElement):

    pass
class uisut_Action(UISUTElement):

    pass
class uisut_UISUT(UISUTElement):

    pass
class uisut_UITransition(UISUTElement):

    def __init__(self, triggerStr: str, guardStr: str, scriptStr: str, actionStr: str, uisut_UITransition: "uisut_UIStatemachine" = None, itsOutTransition: "uisut_AbstractState" = None, uisut_UITransition20: "uisut_UITrigger" = None, uisut_UITransition22: "uisut_UICondition" = None, uisut_UITransition24: "uisut_Action" = None, itsInTransition: "uisut_AbstractState" = None, uisut_UITransition26: set["uisut_UIDataVariable"] = None, UITransition36: "uisut_AbstractState" = None, UITransition: "uisut_AbstractState" = None):
        self.triggerStr = triggerStr
        self.guardStr = guardStr
        self.scriptStr = scriptStr
        self.actionStr = actionStr
        self.uisut_UITransition = uisut_UITransition
        self.itsOutTransition = itsOutTransition
        self.uisut_UITransition20 = uisut_UITransition20
        self.uisut_UITransition22 = uisut_UITransition22
        self.uisut_UITransition24 = uisut_UITransition24
        self.itsInTransition = itsInTransition
        self.uisut_UITransition26 = uisut_UITransition26 if uisut_UITransition26 is not None else set()
        self.UITransition36 = UITransition36
        self.UITransition = UITransition
        
    @property
    def scriptStr(self) -> str:
        return self.__scriptStr

    @scriptStr.setter
    def scriptStr(self, scriptStr: str):
        self.__scriptStr = scriptStr

    @property
    def guardStr(self) -> str:
        return self.__guardStr

    @guardStr.setter
    def guardStr(self, guardStr: str):
        self.__guardStr = guardStr

    @property
    def actionStr(self) -> str:
        return self.__actionStr

    @actionStr.setter
    def actionStr(self, actionStr: str):
        self.__actionStr = actionStr

    @property
    def triggerStr(self) -> str:
        return self.__triggerStr

    @triggerStr.setter
    def triggerStr(self, triggerStr: str):
        self.__triggerStr = triggerStr

    @property
    def uisut_UITransition(self):
        return self.__uisut_UITransition

    @uisut_UITransition.setter
    def uisut_UITransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UITransition__uisut_UITransition", None)
        self.__uisut_UITransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UIStatemachine6"):
                opp_val = getattr(old_value, "uisut_UIStatemachine6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UIStatemachine6"):
                opp_val = getattr(value, "uisut_UIStatemachine6", None)
                if opp_val is None:
                    setattr(value, "uisut_UIStatemachine6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uisut_UITransition24(self):
        return self.__uisut_UITransition24

    @uisut_UITransition24.setter
    def uisut_UITransition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UITransition__uisut_UITransition24", None)
        self.__uisut_UITransition24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_Action"):
                opp_val = getattr(old_value, "uisut_Action", None)
                if opp_val == self:
                    setattr(old_value, "uisut_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_Action"):
                opp_val = getattr(value, "uisut_Action", None)
                setattr(value, "uisut_Action", self)

    @property
    def itsInTransition(self):
        return self.__itsInTransition

    @itsInTransition.setter
    def itsInTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UITransition__itsInTransition", None)
        self.__itsInTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractState"):
                opp_val = getattr(old_value, "AbstractState", None)
                if opp_val == self:
                    setattr(old_value, "AbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractState"):
                opp_val = getattr(value, "AbstractState", None)
                setattr(value, "AbstractState", self)

    @property
    def uisut_UITransition26(self):
        return self.__uisut_UITransition26

    @uisut_UITransition26.setter
    def uisut_UITransition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UITransition__uisut_UITransition26", None)
        self.__uisut_UITransition26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uisut_UIDataVariable27"):
                    opp_val = getattr(item, "uisut_UIDataVariable27", None)
                    
                    if opp_val == self:
                        setattr(item, "uisut_UIDataVariable27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uisut_UIDataVariable27"):
                    opp_val = getattr(item, "uisut_UIDataVariable27", None)
                    
                    setattr(item, "uisut_UIDataVariable27", self)
                    

    @property
    def itsOutTransition(self):
        return self.__itsOutTransition

    @itsOutTransition.setter
    def itsOutTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UITransition__itsOutTransition", None)
        self.__itsOutTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractState18"):
                opp_val = getattr(old_value, "AbstractState18", None)
                if opp_val == self:
                    setattr(old_value, "AbstractState18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractState18"):
                opp_val = getattr(value, "AbstractState18", None)
                setattr(value, "AbstractState18", self)

    @property
    def uisut_UITransition22(self):
        return self.__uisut_UITransition22

    @uisut_UITransition22.setter
    def uisut_UITransition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UITransition__uisut_UITransition22", None)
        self.__uisut_UITransition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UICondition"):
                opp_val = getattr(old_value, "uisut_UICondition", None)
                if opp_val == self:
                    setattr(old_value, "uisut_UICondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UICondition"):
                opp_val = getattr(value, "uisut_UICondition", None)
                setattr(value, "uisut_UICondition", self)

    @property
    def UITransition(self):
        return self.__UITransition

    @UITransition.setter
    def UITransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UITransition__UITransition", None)
        self.__UITransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itsTrgtState"):
                opp_val = getattr(old_value, "itsTrgtState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itsTrgtState"):
                opp_val = getattr(value, "itsTrgtState", None)
                if opp_val is None:
                    setattr(value, "itsTrgtState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uisut_UITransition20(self):
        return self.__uisut_UITransition20

    @uisut_UITransition20.setter
    def uisut_UITransition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UITransition__uisut_UITransition20", None)
        self.__uisut_UITransition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uisut_UITrigger"):
                opp_val = getattr(old_value, "uisut_UITrigger", None)
                if opp_val == self:
                    setattr(old_value, "uisut_UITrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uisut_UITrigger"):
                opp_val = getattr(value, "uisut_UITrigger", None)
                setattr(value, "uisut_UITrigger", self)

    @property
    def UITransition36(self):
        return self.__UITransition36

    @UITransition36.setter
    def UITransition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uisut_UITransition__UITransition36", None)
        self.__UITransition36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itsSrcState"):
                opp_val = getattr(old_value, "itsSrcState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itsSrcState"):
                opp_val = getattr(value, "itsSrcState", None)
                if opp_val is None:
                    setattr(value, "itsSrcState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uisut_AbstractState(UISUTElement):

    pass
class uisut_ApplicationSystem(UISUTElement):

    pass