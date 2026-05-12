from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statechart00_Transition:

    def __init__(self, name: str, expression: str, statechart00_Transition: "statechart00_State" = None, statechart00_Transition9: "statechart00_State" = None, statechart00_Transition12: "statechart00_State" = None):
        self.name = name
        self.expression = expression
        self.statechart00_Transition = statechart00_Transition
        self.statechart00_Transition9 = statechart00_Transition9
        self.statechart00_Transition12 = statechart00_Transition12
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def statechart00_Transition(self):
        return self.__statechart00_Transition

    @statechart00_Transition.setter
    def statechart00_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_Transition__statechart00_Transition", None)
        self.__statechart00_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart00_State7"):
                opp_val = getattr(old_value, "statechart00_State7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart00_State7"):
                opp_val = getattr(value, "statechart00_State7", None)
                if opp_val is None:
                    setattr(value, "statechart00_State7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statechart00_Transition9(self):
        return self.__statechart00_Transition9

    @statechart00_Transition9.setter
    def statechart00_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_Transition__statechart00_Transition9", None)
        self.__statechart00_Transition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart00_State10"):
                opp_val = getattr(old_value, "statechart00_State10", None)
                if opp_val == self:
                    setattr(old_value, "statechart00_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart00_State10"):
                opp_val = getattr(value, "statechart00_State10", None)
                setattr(value, "statechart00_State10", self)

    @property
    def statechart00_Transition12(self):
        return self.__statechart00_Transition12

    @statechart00_Transition12.setter
    def statechart00_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_Transition__statechart00_Transition12", None)
        self.__statechart00_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart00_State13"):
                opp_val = getattr(old_value, "statechart00_State13", None)
                if opp_val == self:
                    setattr(old_value, "statechart00_State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart00_State13"):
                opp_val = getattr(value, "statechart00_State13", None)
                setattr(value, "statechart00_State13", self)

class statechart00_Variable:

    def __init__(self, name: str, type: str, value: str, statechart00_Variable: "statechart00_State" = None):
        self.name = name
        self.type = type
        self.value = value
        self.statechart00_Variable = statechart00_Variable
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def statechart00_Variable(self):
        return self.__statechart00_Variable

    @statechart00_Variable.setter
    def statechart00_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_Variable__statechart00_Variable", None)
        self.__statechart00_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart00_State"):
                opp_val = getattr(old_value, "statechart00_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart00_State"):
                opp_val = getattr(value, "statechart00_State", None)
                if opp_val is None:
                    setattr(value, "statechart00_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statechart00_State:

    def __init__(self, name: str, label: str, type: str, activity: str, statechart00_State7: set["statechart00_Transition"] = None, statechart00_State10: "statechart00_Transition" = None, statechart00_State13: "statechart00_Transition" = None, State: "statechart00_State" = None, parentstate: set["statechart00_State"] = None, State4: "statechart00_State" = None, substates: "statechart00_State" = None, statechart00_State: set["statechart00_Variable"] = None):
        self.name = name
        self.label = label
        self.type = type
        self.activity = activity
        self.statechart00_State7 = statechart00_State7 if statechart00_State7 is not None else set()
        self.statechart00_State10 = statechart00_State10
        self.statechart00_State13 = statechart00_State13
        self.State = State
        self.parentstate = parentstate if parentstate is not None else set()
        self.State4 = State4
        self.substates = substates
        self.statechart00_State = statechart00_State if statechart00_State is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def statechart00_State13(self):
        return self.__statechart00_State13

    @statechart00_State13.setter
    def statechart00_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_State__statechart00_State13", None)
        self.__statechart00_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart00_Transition12"):
                opp_val = getattr(old_value, "statechart00_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "statechart00_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart00_Transition12"):
                opp_val = getattr(value, "statechart00_Transition12", None)
                setattr(value, "statechart00_Transition12", self)

    @property
    def statechart00_State(self):
        return self.__statechart00_State

    @statechart00_State.setter
    def statechart00_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_State__statechart00_State", None)
        self.__statechart00_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statechart00_Variable"):
                    opp_val = getattr(item, "statechart00_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "statechart00_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statechart00_Variable"):
                    opp_val = getattr(item, "statechart00_Variable", None)
                    
                    setattr(item, "statechart00_Variable", self)
                    

    @property
    def State4(self):
        return self.__State4

    @State4.setter
    def State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_State__State4", None)
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
    def substates(self):
        return self.__substates

    @substates.setter
    def substates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_State__substates", None)
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
    def statechart00_State10(self):
        return self.__statechart00_State10

    @statechart00_State10.setter
    def statechart00_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_State__statechart00_State10", None)
        self.__statechart00_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart00_Transition9"):
                opp_val = getattr(old_value, "statechart00_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "statechart00_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart00_Transition9"):
                opp_val = getattr(value, "statechart00_Transition9", None)
                setattr(value, "statechart00_Transition9", self)

    @property
    def parentstate(self):
        return self.__parentstate

    @parentstate.setter
    def parentstate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_State__parentstate", None)
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
    def statechart00_State7(self):
        return self.__statechart00_State7

    @statechart00_State7.setter
    def statechart00_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_State__statechart00_State7", None)
        self.__statechart00_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statechart00_Transition"):
                    opp_val = getattr(item, "statechart00_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statechart00_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statechart00_Transition"):
                    opp_val = getattr(item, "statechart00_Transition", None)
                    
                    setattr(item, "statechart00_Transition", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart00_State__State", None)
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
