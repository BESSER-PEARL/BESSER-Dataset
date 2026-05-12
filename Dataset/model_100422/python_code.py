from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class statechart101_Thing:

    pass
class statechart101_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Thing:

    pass
class NamedElement:

    pass
class statechart101_Variable(NamedElement, Thing):

    def __init__(self, type: str, value: str, statechart101_Variable: "statechart101_State" = None):
        self.type = type
        self.value = value
        self.statechart101_Variable = statechart101_Variable
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def statechart101_Variable(self):
        return self.__statechart101_Variable

    @statechart101_Variable.setter
    def statechart101_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_Variable__statechart101_Variable", None)
        self.__statechart101_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart101_State"):
                opp_val = getattr(old_value, "statechart101_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart101_State"):
                opp_val = getattr(value, "statechart101_State", None)
                if opp_val is None:
                    setattr(value, "statechart101_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statechart101_Transition(NamedElement):

    def __init__(self, expression: str, statechart101_Transition: "statechart101_State" = None, statechart101_Transition9: "statechart101_State" = None, statechart101_Transition12: "statechart101_State" = None):
        self.expression = expression
        self.statechart101_Transition = statechart101_Transition
        self.statechart101_Transition9 = statechart101_Transition9
        self.statechart101_Transition12 = statechart101_Transition12
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


    @property
    def statechart101_Transition12(self):
        return self.__statechart101_Transition12

    @statechart101_Transition12.setter
    def statechart101_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_Transition__statechart101_Transition12", None)
        self.__statechart101_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart101_State13"):
                opp_val = getattr(old_value, "statechart101_State13", None)
                if opp_val == self:
                    setattr(old_value, "statechart101_State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart101_State13"):
                opp_val = getattr(value, "statechart101_State13", None)
                setattr(value, "statechart101_State13", self)

    @property
    def statechart101_Transition9(self):
        return self.__statechart101_Transition9

    @statechart101_Transition9.setter
    def statechart101_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_Transition__statechart101_Transition9", None)
        self.__statechart101_Transition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart101_State10"):
                opp_val = getattr(old_value, "statechart101_State10", None)
                if opp_val == self:
                    setattr(old_value, "statechart101_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart101_State10"):
                opp_val = getattr(value, "statechart101_State10", None)
                setattr(value, "statechart101_State10", self)

    @property
    def statechart101_Transition(self):
        return self.__statechart101_Transition

    @statechart101_Transition.setter
    def statechart101_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_Transition__statechart101_Transition", None)
        self.__statechart101_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart101_State7"):
                opp_val = getattr(old_value, "statechart101_State7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart101_State7"):
                opp_val = getattr(value, "statechart101_State7", None)
                if opp_val is None:
                    setattr(value, "statechart101_State7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statechart101_State(NamedElement):

    def __init__(self, label: str, type: str, activity: str, statechart101_State: set["statechart101_Variable"] = None, statechart101_State7: set["statechart101_Transition"] = None, State: "statechart101_State" = None, parentstate: set["statechart101_State"] = None, statechart101_State10: "statechart101_Transition" = None, statechart101_State13: "statechart101_Transition" = None, State4: "statechart101_State" = None, substates: "statechart101_State" = None):
        self.label = label
        self.type = type
        self.activity = activity
        self.statechart101_State = statechart101_State if statechart101_State is not None else set()
        self.statechart101_State7 = statechart101_State7 if statechart101_State7 is not None else set()
        self.State = State
        self.parentstate = parentstate if parentstate is not None else set()
        self.statechart101_State10 = statechart101_State10
        self.statechart101_State13 = statechart101_State13
        self.State4 = State4
        self.substates = substates
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity


    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentstate"):
                opp_val = getattr(old_value, "parentstate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentstate"):
                opp_val = getattr(value, "parentstate", None)
                if opp_val is None:
                    setattr(value, "parentstate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parentstate(self):
        return self.__parentstate

    @parentstate.setter
    def parentstate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_State__parentstate", None)
        self.__parentstate = value if value is not None else set()
        
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
    def substates(self):
        return self.__substates

    @substates.setter
    def substates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_State__substates", None)
        self.__substates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State4"):
                opp_val = getattr(old_value, "State4", None)
                if opp_val == self:
                    setattr(old_value, "State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State4"):
                opp_val = getattr(value, "State4", None)
                setattr(value, "State4", self)

    @property
    def statechart101_State7(self):
        return self.__statechart101_State7

    @statechart101_State7.setter
    def statechart101_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_State__statechart101_State7", None)
        self.__statechart101_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statechart101_Transition"):
                    opp_val = getattr(item, "statechart101_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statechart101_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statechart101_Transition"):
                    opp_val = getattr(item, "statechart101_Transition", None)
                    
                    setattr(item, "statechart101_Transition", self)
                    

    @property
    def statechart101_State(self):
        return self.__statechart101_State

    @statechart101_State.setter
    def statechart101_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_State__statechart101_State", None)
        self.__statechart101_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statechart101_Variable"):
                    opp_val = getattr(item, "statechart101_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "statechart101_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statechart101_Variable"):
                    opp_val = getattr(item, "statechart101_Variable", None)
                    
                    setattr(item, "statechart101_Variable", self)
                    

    @property
    def State4(self):
        return self.__State4

    @State4.setter
    def State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_State__State4", None)
        self.__State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "substates"):
                opp_val = getattr(old_value, "substates", None)
                if opp_val == self:
                    setattr(old_value, "substates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "substates"):
                opp_val = getattr(value, "substates", None)
                setattr(value, "substates", self)

    @property
    def statechart101_State13(self):
        return self.__statechart101_State13

    @statechart101_State13.setter
    def statechart101_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_State__statechart101_State13", None)
        self.__statechart101_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart101_Transition12"):
                opp_val = getattr(old_value, "statechart101_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "statechart101_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart101_Transition12"):
                opp_val = getattr(value, "statechart101_Transition12", None)
                setattr(value, "statechart101_Transition12", self)

    @property
    def statechart101_State10(self):
        return self.__statechart101_State10

    @statechart101_State10.setter
    def statechart101_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart101_State__statechart101_State10", None)
        self.__statechart101_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart101_Transition9"):
                opp_val = getattr(old_value, "statechart101_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "statechart101_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart101_Transition9"):
                opp_val = getattr(value, "statechart101_Transition9", None)
                setattr(value, "statechart101_Transition9", self)
