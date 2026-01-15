from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operators(Enum):
    equal = "equal"
    lessThan = "lessThan"
    moreThan = "moreThan"
    lessEqualThan = "lessEqualThan"
    moreEqualThan = "moreEqualThan"
    and = "and"
    or = "or"
    between = "between"
    in = "in"
    not = "not"
    notIn = "notIn"
    plus = "plus"
    minus = "minus"
    multiplication = "multiplication"
    isnot = "isnot"


############################################
# Definition of Classes
############################################

class esper_ExtraParenthesisRule:

    pass
class ExtraParenthesisRule:

    pass
class esper_Timer:

    pass
class esper_KindOfEvent:

    def __init__(self, name: str, esper_KindOfEvent: "esper_SingleDefinition" = None):
        self.name = name
        self.esper_KindOfEvent = esper_KindOfEvent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esper_KindOfEvent(self):
        return self.__esper_KindOfEvent

    @esper_KindOfEvent.setter
    def esper_KindOfEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_KindOfEvent__esper_KindOfEvent", None)
        self.__esper_KindOfEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_SingleDefinition66"):
                opp_val = getattr(old_value, "esper_SingleDefinition66", None)
                if opp_val == self:
                    setattr(old_value, "esper_SingleDefinition66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_SingleDefinition66"):
                opp_val = getattr(value, "esper_SingleDefinition66", None)
                setattr(value, "esper_SingleDefinition66", self)

class esper_TerminalExpression:

    def __init__(self, every: bool, parenthesis: bool, esper_TerminalExpression: "esper_FollowBy" = None, esper_TerminalExpression55: "esper_FollowBy" = None, esper_TerminalExpression57: "esper_FollowBy" = None, esper_TerminalExpression60: "esper_FollowBy" = None, esper_TerminalExpression63: "esper_SingleDefinition" = None):
        self.every = every
        self.parenthesis = parenthesis
        self.esper_TerminalExpression = esper_TerminalExpression
        self.esper_TerminalExpression55 = esper_TerminalExpression55
        self.esper_TerminalExpression57 = esper_TerminalExpression57
        self.esper_TerminalExpression60 = esper_TerminalExpression60
        self.esper_TerminalExpression63 = esper_TerminalExpression63
        
    @property
    def every(self) -> bool:
        return self.__every

    @every.setter
    def every(self, every: bool):
        self.__every = every

    @property
    def parenthesis(self) -> bool:
        return self.__parenthesis

    @parenthesis.setter
    def parenthesis(self, parenthesis: bool):
        self.__parenthesis = parenthesis

    @property
    def esper_TerminalExpression63(self):
        return self.__esper_TerminalExpression63

    @esper_TerminalExpression63.setter
    def esper_TerminalExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_TerminalExpression__esper_TerminalExpression63", None)
        self.__esper_TerminalExpression63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_SingleDefinition64"):
                opp_val = getattr(old_value, "esper_SingleDefinition64", None)
                if opp_val == self:
                    setattr(old_value, "esper_SingleDefinition64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_SingleDefinition64"):
                opp_val = getattr(value, "esper_SingleDefinition64", None)
                setattr(value, "esper_SingleDefinition64", self)

    @property
    def esper_TerminalExpression55(self):
        return self.__esper_TerminalExpression55

    @esper_TerminalExpression55.setter
    def esper_TerminalExpression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_TerminalExpression__esper_TerminalExpression55", None)
        self.__esper_TerminalExpression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_FollowBy54"):
                opp_val = getattr(old_value, "esper_FollowBy54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_FollowBy54"):
                opp_val = getattr(value, "esper_FollowBy54", None)
                if opp_val is None:
                    setattr(value, "esper_FollowBy54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def esper_TerminalExpression57(self):
        return self.__esper_TerminalExpression57

    @esper_TerminalExpression57.setter
    def esper_TerminalExpression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_TerminalExpression__esper_TerminalExpression57", None)
        self.__esper_TerminalExpression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_FollowBy58"):
                opp_val = getattr(old_value, "esper_FollowBy58", None)
                if opp_val == self:
                    setattr(old_value, "esper_FollowBy58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_FollowBy58"):
                opp_val = getattr(value, "esper_FollowBy58", None)
                setattr(value, "esper_FollowBy58", self)

    @property
    def esper_TerminalExpression60(self):
        return self.__esper_TerminalExpression60

    @esper_TerminalExpression60.setter
    def esper_TerminalExpression60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_TerminalExpression__esper_TerminalExpression60", None)
        self.__esper_TerminalExpression60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_FollowBy61"):
                opp_val = getattr(old_value, "esper_FollowBy61", None)
                if opp_val == self:
                    setattr(old_value, "esper_FollowBy61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_FollowBy61"):
                opp_val = getattr(value, "esper_FollowBy61", None)
                setattr(value, "esper_FollowBy61", self)

    @property
    def esper_TerminalExpression(self):
        return self.__esper_TerminalExpression

    @esper_TerminalExpression.setter
    def esper_TerminalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_TerminalExpression__esper_TerminalExpression", None)
        self.__esper_TerminalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_FollowBy52"):
                opp_val = getattr(old_value, "esper_FollowBy52", None)
                if opp_val == self:
                    setattr(old_value, "esper_FollowBy52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_FollowBy52"):
                opp_val = getattr(value, "esper_FollowBy52", None)
                setattr(value, "esper_FollowBy52", self)

class esper_FollowByWhere:

    pass
class esper_FollowBy:

    pass
class esper_AbstractFollowBy:

    pass
class esper_Win:

    pass
class esper_JoinFollowBy:

    def __init__(self, operator: str, esper_JoinFollowBy: "esper_Pattern" = None, esper_JoinFollowBy46: set["esper_AbstractFollowBy"] = None):
        self.operator = operator
        self.esper_JoinFollowBy = esper_JoinFollowBy
        self.esper_JoinFollowBy46 = esper_JoinFollowBy46 if esper_JoinFollowBy46 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def esper_JoinFollowBy(self):
        return self.__esper_JoinFollowBy

    @esper_JoinFollowBy.setter
    def esper_JoinFollowBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_JoinFollowBy__esper_JoinFollowBy", None)
        self.__esper_JoinFollowBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_Pattern42"):
                opp_val = getattr(old_value, "esper_Pattern42", None)
                if opp_val == self:
                    setattr(old_value, "esper_Pattern42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_Pattern42"):
                opp_val = getattr(value, "esper_Pattern42", None)
                setattr(value, "esper_Pattern42", self)

    @property
    def esper_JoinFollowBy46(self):
        return self.__esper_JoinFollowBy46

    @esper_JoinFollowBy46.setter
    def esper_JoinFollowBy46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_JoinFollowBy__esper_JoinFollowBy46", None)
        self.__esper_JoinFollowBy46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "esper_AbstractFollowBy"):
                    opp_val = getattr(item, "esper_AbstractFollowBy", None)
                    
                    if opp_val == self:
                        setattr(item, "esper_AbstractFollowBy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "esper_AbstractFollowBy"):
                    opp_val = getattr(item, "esper_AbstractFollowBy", None)
                    
                    setattr(item, "esper_AbstractFollowBy", self)
                    

class esper_Pattern:

    pass
class esper_Anything(ExtraParenthesisRule):

    def __init__(self, operator: str, esper_Anything: "esper_From" = None, esper_Anything69: "esper_SingleDefinition" = None, esper_Anything80: "esper_GroupBy" = None, esper_Anything86: "esper_Having" = None, esper_Anything89: "esper_DefaultMethods" = None, esper_Anything91: set["esper_ExtraParenthesisRule"] = None):
        self.operator = operator
        self.esper_Anything = esper_Anything
        self.esper_Anything69 = esper_Anything69
        self.esper_Anything80 = esper_Anything80
        self.esper_Anything86 = esper_Anything86
        self.esper_Anything89 = esper_Anything89
        self.esper_Anything91 = esper_Anything91 if esper_Anything91 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def esper_Anything69(self):
        return self.__esper_Anything69

    @esper_Anything69.setter
    def esper_Anything69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Anything__esper_Anything69", None)
        self.__esper_Anything69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_SingleDefinition68"):
                opp_val = getattr(old_value, "esper_SingleDefinition68", None)
                if opp_val == self:
                    setattr(old_value, "esper_SingleDefinition68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_SingleDefinition68"):
                opp_val = getattr(value, "esper_SingleDefinition68", None)
                setattr(value, "esper_SingleDefinition68", self)

    @property
    def esper_Anything89(self):
        return self.__esper_Anything89

    @esper_Anything89.setter
    def esper_Anything89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Anything__esper_Anything89", None)
        self.__esper_Anything89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_DefaultMethods88"):
                opp_val = getattr(old_value, "esper_DefaultMethods88", None)
                if opp_val == self:
                    setattr(old_value, "esper_DefaultMethods88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_DefaultMethods88"):
                opp_val = getattr(value, "esper_DefaultMethods88", None)
                setattr(value, "esper_DefaultMethods88", self)

    @property
    def esper_Anything86(self):
        return self.__esper_Anything86

    @esper_Anything86.setter
    def esper_Anything86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Anything__esper_Anything86", None)
        self.__esper_Anything86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_Having85"):
                opp_val = getattr(old_value, "esper_Having85", None)
                if opp_val == self:
                    setattr(old_value, "esper_Having85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_Having85"):
                opp_val = getattr(value, "esper_Having85", None)
                setattr(value, "esper_Having85", self)

    @property
    def esper_Anything(self):
        return self.__esper_Anything

    @esper_Anything.setter
    def esper_Anything(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Anything__esper_Anything", None)
        self.__esper_Anything = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_From38"):
                opp_val = getattr(old_value, "esper_From38", None)
                if opp_val == self:
                    setattr(old_value, "esper_From38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_From38"):
                opp_val = getattr(value, "esper_From38", None)
                setattr(value, "esper_From38", self)

    @property
    def esper_Anything80(self):
        return self.__esper_Anything80

    @esper_Anything80.setter
    def esper_Anything80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Anything__esper_Anything80", None)
        self.__esper_Anything80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_GroupBy79"):
                opp_val = getattr(old_value, "esper_GroupBy79", None)
                if opp_val == self:
                    setattr(old_value, "esper_GroupBy79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_GroupBy79"):
                opp_val = getattr(value, "esper_GroupBy79", None)
                setattr(value, "esper_GroupBy79", self)

    @property
    def esper_Anything91(self):
        return self.__esper_Anything91

    @esper_Anything91.setter
    def esper_Anything91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Anything__esper_Anything91", None)
        self.__esper_Anything91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "esper_ExtraParenthesisRule"):
                    opp_val = getattr(item, "esper_ExtraParenthesisRule", None)
                    
                    if opp_val == self:
                        setattr(item, "esper_ExtraParenthesisRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "esper_ExtraParenthesisRule"):
                    opp_val = getattr(item, "esper_ExtraParenthesisRule", None)
                    
                    setattr(item, "esper_ExtraParenthesisRule", self)
                    

class esper_SingleDefinition:

    def __init__(self, name: str, esper_SingleDefinition: "esper_SingleSelectDefinition" = None, esper_SingleDefinition64: "esper_TerminalExpression" = None, esper_SingleDefinition66: "esper_KindOfEvent" = None, esper_SingleDefinition68: "esper_Anything" = None):
        self.name = name
        self.esper_SingleDefinition = esper_SingleDefinition
        self.esper_SingleDefinition64 = esper_SingleDefinition64
        self.esper_SingleDefinition66 = esper_SingleDefinition66
        self.esper_SingleDefinition68 = esper_SingleDefinition68
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esper_SingleDefinition64(self):
        return self.__esper_SingleDefinition64

    @esper_SingleDefinition64.setter
    def esper_SingleDefinition64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_SingleDefinition__esper_SingleDefinition64", None)
        self.__esper_SingleDefinition64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_TerminalExpression63"):
                opp_val = getattr(old_value, "esper_TerminalExpression63", None)
                if opp_val == self:
                    setattr(old_value, "esper_TerminalExpression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_TerminalExpression63"):
                opp_val = getattr(value, "esper_TerminalExpression63", None)
                setattr(value, "esper_TerminalExpression63", self)

    @property
    def esper_SingleDefinition66(self):
        return self.__esper_SingleDefinition66

    @esper_SingleDefinition66.setter
    def esper_SingleDefinition66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_SingleDefinition__esper_SingleDefinition66", None)
        self.__esper_SingleDefinition66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_KindOfEvent"):
                opp_val = getattr(old_value, "esper_KindOfEvent", None)
                if opp_val == self:
                    setattr(old_value, "esper_KindOfEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_KindOfEvent"):
                opp_val = getattr(value, "esper_KindOfEvent", None)
                setattr(value, "esper_KindOfEvent", self)

    @property
    def esper_SingleDefinition(self):
        return self.__esper_SingleDefinition

    @esper_SingleDefinition.setter
    def esper_SingleDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_SingleDefinition__esper_SingleDefinition", None)
        self.__esper_SingleDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_SingleSelectDefinition33"):
                opp_val = getattr(old_value, "esper_SingleSelectDefinition33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_SingleSelectDefinition33"):
                opp_val = getattr(value, "esper_SingleSelectDefinition33", None)
                if opp_val is None:
                    setattr(value, "esper_SingleSelectDefinition33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def esper_SingleDefinition68(self):
        return self.__esper_SingleDefinition68

    @esper_SingleDefinition68.setter
    def esper_SingleDefinition68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_SingleDefinition__esper_SingleDefinition68", None)
        self.__esper_SingleDefinition68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_Anything69"):
                opp_val = getattr(old_value, "esper_Anything69", None)
                if opp_val == self:
                    setattr(old_value, "esper_Anything69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_Anything69"):
                opp_val = getattr(value, "esper_Anything69", None)
                setattr(value, "esper_Anything69", self)

class esper_DefaultMethods:

    def __init__(self, name: str, esper_DefaultMethods: "esper_KindSelectAttributesDefinition" = None, esper_DefaultMethods72: "esper_Win" = None, esper_DefaultMethods77: "esper_Timer" = None, esper_DefaultMethods83: "esper_Having" = None, esper_DefaultMethods88: "esper_Anything" = None):
        self.name = name
        self.esper_DefaultMethods = esper_DefaultMethods
        self.esper_DefaultMethods72 = esper_DefaultMethods72
        self.esper_DefaultMethods77 = esper_DefaultMethods77
        self.esper_DefaultMethods83 = esper_DefaultMethods83
        self.esper_DefaultMethods88 = esper_DefaultMethods88
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esper_DefaultMethods83(self):
        return self.__esper_DefaultMethods83

    @esper_DefaultMethods83.setter
    def esper_DefaultMethods83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_DefaultMethods__esper_DefaultMethods83", None)
        self.__esper_DefaultMethods83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_Having82"):
                opp_val = getattr(old_value, "esper_Having82", None)
                if opp_val == self:
                    setattr(old_value, "esper_Having82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_Having82"):
                opp_val = getattr(value, "esper_Having82", None)
                setattr(value, "esper_Having82", self)

    @property
    def esper_DefaultMethods72(self):
        return self.__esper_DefaultMethods72

    @esper_DefaultMethods72.setter
    def esper_DefaultMethods72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_DefaultMethods__esper_DefaultMethods72", None)
        self.__esper_DefaultMethods72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_Win71"):
                opp_val = getattr(old_value, "esper_Win71", None)
                if opp_val == self:
                    setattr(old_value, "esper_Win71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_Win71"):
                opp_val = getattr(value, "esper_Win71", None)
                setattr(value, "esper_Win71", self)

    @property
    def esper_DefaultMethods77(self):
        return self.__esper_DefaultMethods77

    @esper_DefaultMethods77.setter
    def esper_DefaultMethods77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_DefaultMethods__esper_DefaultMethods77", None)
        self.__esper_DefaultMethods77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_Timer76"):
                opp_val = getattr(old_value, "esper_Timer76", None)
                if opp_val == self:
                    setattr(old_value, "esper_Timer76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_Timer76"):
                opp_val = getattr(value, "esper_Timer76", None)
                setattr(value, "esper_Timer76", self)

    @property
    def esper_DefaultMethods(self):
        return self.__esper_DefaultMethods

    @esper_DefaultMethods.setter
    def esper_DefaultMethods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_DefaultMethods__esper_DefaultMethods", None)
        self.__esper_DefaultMethods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_KindSelectAttributesDefinition25"):
                opp_val = getattr(old_value, "esper_KindSelectAttributesDefinition25", None)
                if opp_val == self:
                    setattr(old_value, "esper_KindSelectAttributesDefinition25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_KindSelectAttributesDefinition25"):
                opp_val = getattr(value, "esper_KindSelectAttributesDefinition25", None)
                setattr(value, "esper_KindSelectAttributesDefinition25", self)

    @property
    def esper_DefaultMethods88(self):
        return self.__esper_DefaultMethods88

    @esper_DefaultMethods88.setter
    def esper_DefaultMethods88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_DefaultMethods__esper_DefaultMethods88", None)
        self.__esper_DefaultMethods88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_Anything89"):
                opp_val = getattr(old_value, "esper_Anything89", None)
                if opp_val == self:
                    setattr(old_value, "esper_Anything89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_Anything89"):
                opp_val = getattr(value, "esper_Anything89", None)
                setattr(value, "esper_Anything89", self)

class esper_SingleSelectDefinition:

    def __init__(self, attribute: str, esper_SingleSelectDefinition: "esper_KindSelectAttributesDefinition" = None, esper_SingleSelectDefinition33: set["esper_SingleDefinition"] = None):
        self.attribute = attribute
        self.esper_SingleSelectDefinition = esper_SingleSelectDefinition
        self.esper_SingleSelectDefinition33 = esper_SingleSelectDefinition33 if esper_SingleSelectDefinition33 is not None else set()
        
    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def esper_SingleSelectDefinition33(self):
        return self.__esper_SingleSelectDefinition33

    @esper_SingleSelectDefinition33.setter
    def esper_SingleSelectDefinition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_SingleSelectDefinition__esper_SingleSelectDefinition33", None)
        self.__esper_SingleSelectDefinition33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "esper_SingleDefinition"):
                    opp_val = getattr(item, "esper_SingleDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "esper_SingleDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "esper_SingleDefinition"):
                    opp_val = getattr(item, "esper_SingleDefinition", None)
                    
                    setattr(item, "esper_SingleDefinition", self)
                    

    @property
    def esper_SingleSelectDefinition(self):
        return self.__esper_SingleSelectDefinition

    @esper_SingleSelectDefinition.setter
    def esper_SingleSelectDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_SingleSelectDefinition__esper_SingleSelectDefinition", None)
        self.__esper_SingleSelectDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_KindSelectAttributesDefinition"):
                opp_val = getattr(old_value, "esper_KindSelectAttributesDefinition", None)
                if opp_val == self:
                    setattr(old_value, "esper_KindSelectAttributesDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_KindSelectAttributesDefinition"):
                opp_val = getattr(value, "esper_KindSelectAttributesDefinition", None)
                setattr(value, "esper_KindSelectAttributesDefinition", self)

class esper_KindSelectAttributesDefinition:

    def __init__(self, int: int, string: str, esper_KindSelectAttributesDefinition: "esper_SingleSelectDefinition" = None, esper_KindSelectAttributesDefinition25: "esper_DefaultMethods" = None, esper_KindSelectAttributesDefinition28: "esper_SelectAttributesDefinition" = None, esper_KindSelectAttributesDefinition31: "esper_SelectAttributesDefinition" = None):
        self.int = int
        self.string = string
        self.esper_KindSelectAttributesDefinition = esper_KindSelectAttributesDefinition
        self.esper_KindSelectAttributesDefinition25 = esper_KindSelectAttributesDefinition25
        self.esper_KindSelectAttributesDefinition28 = esper_KindSelectAttributesDefinition28
        self.esper_KindSelectAttributesDefinition31 = esper_KindSelectAttributesDefinition31
        
    @property
    def int(self) -> int:
        return self.__int

    @int.setter
    def int(self, int: int):
        self.__int = int

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def esper_KindSelectAttributesDefinition31(self):
        return self.__esper_KindSelectAttributesDefinition31

    @esper_KindSelectAttributesDefinition31.setter
    def esper_KindSelectAttributesDefinition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_KindSelectAttributesDefinition__esper_KindSelectAttributesDefinition31", None)
        self.__esper_KindSelectAttributesDefinition31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_SelectAttributesDefinition30"):
                opp_val = getattr(old_value, "esper_SelectAttributesDefinition30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_SelectAttributesDefinition30"):
                opp_val = getattr(value, "esper_SelectAttributesDefinition30", None)
                if opp_val is None:
                    setattr(value, "esper_SelectAttributesDefinition30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def esper_KindSelectAttributesDefinition28(self):
        return self.__esper_KindSelectAttributesDefinition28

    @esper_KindSelectAttributesDefinition28.setter
    def esper_KindSelectAttributesDefinition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_KindSelectAttributesDefinition__esper_KindSelectAttributesDefinition28", None)
        self.__esper_KindSelectAttributesDefinition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_SelectAttributesDefinition27"):
                opp_val = getattr(old_value, "esper_SelectAttributesDefinition27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_SelectAttributesDefinition27"):
                opp_val = getattr(value, "esper_SelectAttributesDefinition27", None)
                if opp_val is None:
                    setattr(value, "esper_SelectAttributesDefinition27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def esper_KindSelectAttributesDefinition25(self):
        return self.__esper_KindSelectAttributesDefinition25

    @esper_KindSelectAttributesDefinition25.setter
    def esper_KindSelectAttributesDefinition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_KindSelectAttributesDefinition__esper_KindSelectAttributesDefinition25", None)
        self.__esper_KindSelectAttributesDefinition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_DefaultMethods"):
                opp_val = getattr(old_value, "esper_DefaultMethods", None)
                if opp_val == self:
                    setattr(old_value, "esper_DefaultMethods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_DefaultMethods"):
                opp_val = getattr(value, "esper_DefaultMethods", None)
                setattr(value, "esper_DefaultMethods", self)

    @property
    def esper_KindSelectAttributesDefinition(self):
        return self.__esper_KindSelectAttributesDefinition

    @esper_KindSelectAttributesDefinition.setter
    def esper_KindSelectAttributesDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_KindSelectAttributesDefinition__esper_KindSelectAttributesDefinition", None)
        self.__esper_KindSelectAttributesDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_SingleSelectDefinition"):
                opp_val = getattr(old_value, "esper_SingleSelectDefinition", None)
                if opp_val == self:
                    setattr(old_value, "esper_SingleSelectDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_SingleSelectDefinition"):
                opp_val = getattr(value, "esper_SingleSelectDefinition", None)
                setattr(value, "esper_SingleSelectDefinition", self)

class esper_SelectAttributesDefinition:

    def __init__(self, operator: str, esper_SelectAttributesDefinition: "esper_Select" = None, esper_SelectAttributesDefinition27: set["esper_KindSelectAttributesDefinition"] = None, esper_SelectAttributesDefinition30: set["esper_KindSelectAttributesDefinition"] = None):
        self.operator = operator
        self.esper_SelectAttributesDefinition = esper_SelectAttributesDefinition
        self.esper_SelectAttributesDefinition27 = esper_SelectAttributesDefinition27 if esper_SelectAttributesDefinition27 is not None else set()
        self.esper_SelectAttributesDefinition30 = esper_SelectAttributesDefinition30 if esper_SelectAttributesDefinition30 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def esper_SelectAttributesDefinition(self):
        return self.__esper_SelectAttributesDefinition

    @esper_SelectAttributesDefinition.setter
    def esper_SelectAttributesDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_SelectAttributesDefinition__esper_SelectAttributesDefinition", None)
        self.__esper_SelectAttributesDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_Select22"):
                opp_val = getattr(old_value, "esper_Select22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_Select22"):
                opp_val = getattr(value, "esper_Select22", None)
                if opp_val is None:
                    setattr(value, "esper_Select22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def esper_SelectAttributesDefinition27(self):
        return self.__esper_SelectAttributesDefinition27

    @esper_SelectAttributesDefinition27.setter
    def esper_SelectAttributesDefinition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_SelectAttributesDefinition__esper_SelectAttributesDefinition27", None)
        self.__esper_SelectAttributesDefinition27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "esper_KindSelectAttributesDefinition28"):
                    opp_val = getattr(item, "esper_KindSelectAttributesDefinition28", None)
                    
                    if opp_val == self:
                        setattr(item, "esper_KindSelectAttributesDefinition28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "esper_KindSelectAttributesDefinition28"):
                    opp_val = getattr(item, "esper_KindSelectAttributesDefinition28", None)
                    
                    setattr(item, "esper_KindSelectAttributesDefinition28", self)
                    

    @property
    def esper_SelectAttributesDefinition30(self):
        return self.__esper_SelectAttributesDefinition30

    @esper_SelectAttributesDefinition30.setter
    def esper_SelectAttributesDefinition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_SelectAttributesDefinition__esper_SelectAttributesDefinition30", None)
        self.__esper_SelectAttributesDefinition30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "esper_KindSelectAttributesDefinition31"):
                    opp_val = getattr(item, "esper_KindSelectAttributesDefinition31", None)
                    
                    if opp_val == self:
                        setattr(item, "esper_KindSelectAttributesDefinition31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "esper_KindSelectAttributesDefinition31"):
                    opp_val = getattr(item, "esper_KindSelectAttributesDefinition31", None)
                    
                    setattr(item, "esper_KindSelectAttributesDefinition31", self)
                    

class esper_Having:

    def __init__(self, operator: str, esper_Having: "esper_RuleParts" = None, esper_Having82: "esper_DefaultMethods" = None, esper_Having85: "esper_Anything" = None):
        self.operator = operator
        self.esper_Having = esper_Having
        self.esper_Having82 = esper_Having82
        self.esper_Having85 = esper_Having85
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def esper_Having(self):
        return self.__esper_Having

    @esper_Having.setter
    def esper_Having(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Having__esper_Having", None)
        self.__esper_Having = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_RuleParts20"):
                opp_val = getattr(old_value, "esper_RuleParts20", None)
                if opp_val == self:
                    setattr(old_value, "esper_RuleParts20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_RuleParts20"):
                opp_val = getattr(value, "esper_RuleParts20", None)
                setattr(value, "esper_RuleParts20", self)

    @property
    def esper_Having82(self):
        return self.__esper_Having82

    @esper_Having82.setter
    def esper_Having82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Having__esper_Having82", None)
        self.__esper_Having82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_DefaultMethods83"):
                opp_val = getattr(old_value, "esper_DefaultMethods83", None)
                if opp_val == self:
                    setattr(old_value, "esper_DefaultMethods83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_DefaultMethods83"):
                opp_val = getattr(value, "esper_DefaultMethods83", None)
                setattr(value, "esper_DefaultMethods83", self)

    @property
    def esper_Having85(self):
        return self.__esper_Having85

    @esper_Having85.setter
    def esper_Having85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Having__esper_Having85", None)
        self.__esper_Having85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_Anything86"):
                opp_val = getattr(old_value, "esper_Anything86", None)
                if opp_val == self:
                    setattr(old_value, "esper_Anything86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_Anything86"):
                opp_val = getattr(value, "esper_Anything86", None)
                setattr(value, "esper_Anything86", self)

class esper_GroupBy:

    pass
class esper_From:

    pass
class esper_Select:

    def __init__(self, alias: str, asterisk: bool, esper_Select: "esper_RuleParts" = None, esper_Select22: set["esper_SelectAttributesDefinition"] = None):
        self.alias = alias
        self.asterisk = asterisk
        self.esper_Select = esper_Select
        self.esper_Select22 = esper_Select22 if esper_Select22 is not None else set()
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def asterisk(self) -> bool:
        return self.__asterisk

    @asterisk.setter
    def asterisk(self, asterisk: bool):
        self.__asterisk = asterisk

    @property
    def esper_Select(self):
        return self.__esper_Select

    @esper_Select.setter
    def esper_Select(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Select__esper_Select", None)
        self.__esper_Select = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_RuleParts14"):
                opp_val = getattr(old_value, "esper_RuleParts14", None)
                if opp_val == self:
                    setattr(old_value, "esper_RuleParts14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_RuleParts14"):
                opp_val = getattr(value, "esper_RuleParts14", None)
                setattr(value, "esper_RuleParts14", self)

    @property
    def esper_Select22(self):
        return self.__esper_Select22

    @esper_Select22.setter
    def esper_Select22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Select__esper_Select22", None)
        self.__esper_Select22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "esper_SelectAttributesDefinition"):
                    opp_val = getattr(item, "esper_SelectAttributesDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "esper_SelectAttributesDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "esper_SelectAttributesDefinition"):
                    opp_val = getattr(item, "esper_SelectAttributesDefinition", None)
                    
                    setattr(item, "esper_SelectAttributesDefinition", self)
                    

class esper_Priority:

    def __init__(self, priorityInt: int, esper_Priority: "esper_RuleParts" = None):
        self.priorityInt = priorityInt
        self.esper_Priority = esper_Priority
        
    @property
    def priorityInt(self) -> int:
        return self.__priorityInt

    @priorityInt.setter
    def priorityInt(self, priorityInt: int):
        self.__priorityInt = priorityInt

    @property
    def esper_Priority(self):
        return self.__esper_Priority

    @esper_Priority.setter
    def esper_Priority(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Priority__esper_Priority", None)
        self.__esper_Priority = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_RuleParts12"):
                opp_val = getattr(old_value, "esper_RuleParts12", None)
                if opp_val == self:
                    setattr(old_value, "esper_RuleParts12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_RuleParts12"):
                opp_val = getattr(value, "esper_RuleParts12", None)
                setattr(value, "esper_RuleParts12", self)

class esper_Name:

    def __init__(self, name: str, esper_Name: "esper_RuleParts" = None):
        self.name = name
        self.esper_Name = esper_Name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esper_Name(self):
        return self.__esper_Name

    @esper_Name.setter
    def esper_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_Name__esper_Name", None)
        self.__esper_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_RuleParts8"):
                opp_val = getattr(old_value, "esper_RuleParts8", None)
                if opp_val == self:
                    setattr(old_value, "esper_RuleParts8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_RuleParts8"):
                opp_val = getattr(value, "esper_RuleParts8", None)
                setattr(value, "esper_RuleParts8", self)

class esper_AttributesDefinition:

    def __init__(self, name: str, type: str, esper_AttributesDefinition: "esper_Attributes" = None):
        self.name = name
        self.type = type
        self.esper_AttributesDefinition = esper_AttributesDefinition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def esper_AttributesDefinition(self):
        return self.__esper_AttributesDefinition

    @esper_AttributesDefinition.setter
    def esper_AttributesDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esper_AttributesDefinition__esper_AttributesDefinition", None)
        self.__esper_AttributesDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esper_Attributes6"):
                opp_val = getattr(old_value, "esper_Attributes6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esper_Attributes6"):
                opp_val = getattr(value, "esper_Attributes6", None)
                if opp_val is None:
                    setattr(value, "esper_Attributes6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class esper_Attributes:

    pass
class KindOfEvent:

    pass
class esper_Insert(KindOfEvent):

    pass
class esper_Event(KindOfEvent):

    pass
class esper_RuleParts:

    pass
class esper_Domainmodel:

    pass