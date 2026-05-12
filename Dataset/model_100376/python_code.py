from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class IOAutomaton_ReturnValue:

    def __init__(self, name: str, isVoid: bool, IOAutomaton_ReturnValue: "IOAutomaton_Activation" = None, IOAutomaton_ReturnValue35: "IOAutomaton_Output" = None):
        self.name = name
        self.isVoid = isVoid
        self.IOAutomaton_ReturnValue = IOAutomaton_ReturnValue
        self.IOAutomaton_ReturnValue35 = IOAutomaton_ReturnValue35
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def isVoid(self):
        return self.__isVoid

    @isVoid.setter
    def isVoid(self, isVoid: bool):
        self.__isVoid = isVoid


    @property
    def IOAutomaton_ReturnValue(self):
        return self.__IOAutomaton_ReturnValue

    @IOAutomaton_ReturnValue.setter
    def IOAutomaton_ReturnValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_ReturnValue__IOAutomaton_ReturnValue", None)
        self.__IOAutomaton_ReturnValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Activation25"):
                opp_val = getattr(old_value, "IOAutomaton_Activation25", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Activation25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Activation25"):
                opp_val = getattr(value, "IOAutomaton_Activation25", None)
                setattr(value, "IOAutomaton_Activation25", self)

    @property
    def IOAutomaton_ReturnValue35(self):
        return self.__IOAutomaton_ReturnValue35

    @IOAutomaton_ReturnValue35.setter
    def IOAutomaton_ReturnValue35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_ReturnValue__IOAutomaton_ReturnValue35", None)
        self.__IOAutomaton_ReturnValue35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Output34"):
                opp_val = getattr(old_value, "IOAutomaton_Output34", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Output34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Output34"):
                opp_val = getattr(value, "IOAutomaton_Output34", None)
                setattr(value, "IOAutomaton_Output34", self)

class IOAutomaton_Object:

    def __init__(self, name: str, IOAutomaton_Object: "IOAutomaton_Output" = None):
        self.name = name
        self.IOAutomaton_Object = IOAutomaton_Object
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def IOAutomaton_Object(self):
        return self.__IOAutomaton_Object

    @IOAutomaton_Object.setter
    def IOAutomaton_Object(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Object__IOAutomaton_Object", None)
        self.__IOAutomaton_Object = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Output32"):
                opp_val = getattr(old_value, "IOAutomaton_Output32", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Output32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Output32"):
                opp_val = getattr(value, "IOAutomaton_Output32", None)
                setattr(value, "IOAutomaton_Output32", self)

class IOAutomaton_Operation:

    def __init__(self, name: str, IOAutomaton_Operation: "IOAutomaton_Input" = None, IOAutomaton_Operation30: "IOAutomaton_Output" = None):
        self.name = name
        self.IOAutomaton_Operation = IOAutomaton_Operation
        self.IOAutomaton_Operation30 = IOAutomaton_Operation30
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def IOAutomaton_Operation(self):
        return self.__IOAutomaton_Operation

    @IOAutomaton_Operation.setter
    def IOAutomaton_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Operation__IOAutomaton_Operation", None)
        self.__IOAutomaton_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Input27"):
                opp_val = getattr(old_value, "IOAutomaton_Input27", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Input27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Input27"):
                opp_val = getattr(value, "IOAutomaton_Input27", None)
                setattr(value, "IOAutomaton_Input27", self)

    @property
    def IOAutomaton_Operation30(self):
        return self.__IOAutomaton_Operation30

    @IOAutomaton_Operation30.setter
    def IOAutomaton_Operation30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Operation__IOAutomaton_Operation30", None)
        self.__IOAutomaton_Operation30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Output29"):
                opp_val = getattr(old_value, "IOAutomaton_Output29", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Output29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Output29"):
                opp_val = getattr(value, "IOAutomaton_Output29", None)
                setattr(value, "IOAutomaton_Output29", self)

class IOAutomaton_Output:

    def __init__(self, name: str, IOAutomaton_Output29: "IOAutomaton_Operation" = None, IOAutomaton_Output32: "IOAutomaton_Object" = None, IOAutomaton_Output: "IOAutomaton_Activation" = None, IOAutomaton_Output34: "IOAutomaton_ReturnValue" = None):
        self.name = name
        self.IOAutomaton_Output29 = IOAutomaton_Output29
        self.IOAutomaton_Output32 = IOAutomaton_Output32
        self.IOAutomaton_Output = IOAutomaton_Output
        self.IOAutomaton_Output34 = IOAutomaton_Output34
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def IOAutomaton_Output(self):
        return self.__IOAutomaton_Output

    @IOAutomaton_Output.setter
    def IOAutomaton_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Output__IOAutomaton_Output", None)
        self.__IOAutomaton_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Activation23"):
                opp_val = getattr(old_value, "IOAutomaton_Activation23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Activation23"):
                opp_val = getattr(value, "IOAutomaton_Activation23", None)
                if opp_val is None:
                    setattr(value, "IOAutomaton_Activation23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def IOAutomaton_Output29(self):
        return self.__IOAutomaton_Output29

    @IOAutomaton_Output29.setter
    def IOAutomaton_Output29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Output__IOAutomaton_Output29", None)
        self.__IOAutomaton_Output29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Operation30"):
                opp_val = getattr(old_value, "IOAutomaton_Operation30", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Operation30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Operation30"):
                opp_val = getattr(value, "IOAutomaton_Operation30", None)
                setattr(value, "IOAutomaton_Operation30", self)

    @property
    def IOAutomaton_Output32(self):
        return self.__IOAutomaton_Output32

    @IOAutomaton_Output32.setter
    def IOAutomaton_Output32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Output__IOAutomaton_Output32", None)
        self.__IOAutomaton_Output32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Object"):
                opp_val = getattr(old_value, "IOAutomaton_Object", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Object", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Object"):
                opp_val = getattr(value, "IOAutomaton_Object", None)
                setattr(value, "IOAutomaton_Object", self)

    @property
    def IOAutomaton_Output34(self):
        return self.__IOAutomaton_Output34

    @IOAutomaton_Output34.setter
    def IOAutomaton_Output34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Output__IOAutomaton_Output34", None)
        self.__IOAutomaton_Output34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_ReturnValue35"):
                opp_val = getattr(old_value, "IOAutomaton_ReturnValue35", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_ReturnValue35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_ReturnValue35"):
                opp_val = getattr(value, "IOAutomaton_ReturnValue35", None)
                setattr(value, "IOAutomaton_ReturnValue35", self)

class IOAutomaton_Transition:

    def __init__(self, name: str, IOAutomaton_Transition17: "IOAutomaton_Input" = None, IOAutomaton_Transition20: "IOAutomaton_Activation" = None, IOAutomaton_Transition: "IOAutomaton_Automaton" = None, IOAutomaton_Transition11: "IOAutomaton_State" = None, IOAutomaton_Transition14: "IOAutomaton_State" = None):
        self.name = name
        self.IOAutomaton_Transition17 = IOAutomaton_Transition17
        self.IOAutomaton_Transition20 = IOAutomaton_Transition20
        self.IOAutomaton_Transition = IOAutomaton_Transition
        self.IOAutomaton_Transition11 = IOAutomaton_Transition11
        self.IOAutomaton_Transition14 = IOAutomaton_Transition14
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def IOAutomaton_Transition17(self):
        return self.__IOAutomaton_Transition17

    @IOAutomaton_Transition17.setter
    def IOAutomaton_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Transition__IOAutomaton_Transition17", None)
        self.__IOAutomaton_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Input18"):
                opp_val = getattr(old_value, "IOAutomaton_Input18", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Input18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Input18"):
                opp_val = getattr(value, "IOAutomaton_Input18", None)
                setattr(value, "IOAutomaton_Input18", self)

    @property
    def IOAutomaton_Transition11(self):
        return self.__IOAutomaton_Transition11

    @IOAutomaton_Transition11.setter
    def IOAutomaton_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Transition__IOAutomaton_Transition11", None)
        self.__IOAutomaton_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_State12"):
                opp_val = getattr(old_value, "IOAutomaton_State12", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_State12"):
                opp_val = getattr(value, "IOAutomaton_State12", None)
                setattr(value, "IOAutomaton_State12", self)

    @property
    def IOAutomaton_Transition(self):
        return self.__IOAutomaton_Transition

    @IOAutomaton_Transition.setter
    def IOAutomaton_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Transition__IOAutomaton_Transition", None)
        self.__IOAutomaton_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Automaton6"):
                opp_val = getattr(old_value, "IOAutomaton_Automaton6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Automaton6"):
                opp_val = getattr(value, "IOAutomaton_Automaton6", None)
                if opp_val is None:
                    setattr(value, "IOAutomaton_Automaton6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def IOAutomaton_Transition20(self):
        return self.__IOAutomaton_Transition20

    @IOAutomaton_Transition20.setter
    def IOAutomaton_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Transition__IOAutomaton_Transition20", None)
        self.__IOAutomaton_Transition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Activation21"):
                opp_val = getattr(old_value, "IOAutomaton_Activation21", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Activation21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Activation21"):
                opp_val = getattr(value, "IOAutomaton_Activation21", None)
                setattr(value, "IOAutomaton_Activation21", self)

    @property
    def IOAutomaton_Transition14(self):
        return self.__IOAutomaton_Transition14

    @IOAutomaton_Transition14.setter
    def IOAutomaton_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Transition__IOAutomaton_Transition14", None)
        self.__IOAutomaton_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_State15"):
                opp_val = getattr(old_value, "IOAutomaton_State15", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_State15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_State15"):
                opp_val = getattr(value, "IOAutomaton_State15", None)
                setattr(value, "IOAutomaton_State15", self)

class IOAutomaton_Activation:

    def __init__(self, name: str, IOAutomaton_Activation21: "IOAutomaton_Transition" = None, IOAutomaton_Activation23: set["IOAutomaton_Output"] = None, IOAutomaton_Activation25: "IOAutomaton_ReturnValue" = None, IOAutomaton_Activation: "IOAutomaton_Automaton" = None):
        self.name = name
        self.IOAutomaton_Activation21 = IOAutomaton_Activation21
        self.IOAutomaton_Activation23 = IOAutomaton_Activation23 if IOAutomaton_Activation23 is not None else set()
        self.IOAutomaton_Activation25 = IOAutomaton_Activation25
        self.IOAutomaton_Activation = IOAutomaton_Activation
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def IOAutomaton_Activation21(self):
        return self.__IOAutomaton_Activation21

    @IOAutomaton_Activation21.setter
    def IOAutomaton_Activation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Activation__IOAutomaton_Activation21", None)
        self.__IOAutomaton_Activation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Transition20"):
                opp_val = getattr(old_value, "IOAutomaton_Transition20", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Transition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Transition20"):
                opp_val = getattr(value, "IOAutomaton_Transition20", None)
                setattr(value, "IOAutomaton_Transition20", self)

    @property
    def IOAutomaton_Activation25(self):
        return self.__IOAutomaton_Activation25

    @IOAutomaton_Activation25.setter
    def IOAutomaton_Activation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Activation__IOAutomaton_Activation25", None)
        self.__IOAutomaton_Activation25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_ReturnValue"):
                opp_val = getattr(old_value, "IOAutomaton_ReturnValue", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_ReturnValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_ReturnValue"):
                opp_val = getattr(value, "IOAutomaton_ReturnValue", None)
                setattr(value, "IOAutomaton_ReturnValue", self)

    @property
    def IOAutomaton_Activation23(self):
        return self.__IOAutomaton_Activation23

    @IOAutomaton_Activation23.setter
    def IOAutomaton_Activation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Activation__IOAutomaton_Activation23", None)
        self.__IOAutomaton_Activation23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IOAutomaton_Output"):
                    opp_val = getattr(item, "IOAutomaton_Output", None)
                    
                    if opp_val == self:
                        setattr(item, "IOAutomaton_Output", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IOAutomaton_Output"):
                    opp_val = getattr(item, "IOAutomaton_Output", None)
                    
                    setattr(item, "IOAutomaton_Output", self)
                    

    @property
    def IOAutomaton_Activation(self):
        return self.__IOAutomaton_Activation

    @IOAutomaton_Activation.setter
    def IOAutomaton_Activation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Activation__IOAutomaton_Activation", None)
        self.__IOAutomaton_Activation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Automaton4"):
                opp_val = getattr(old_value, "IOAutomaton_Automaton4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Automaton4"):
                opp_val = getattr(value, "IOAutomaton_Automaton4", None)
                if opp_val is None:
                    setattr(value, "IOAutomaton_Automaton4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IOAutomaton_Input:

    def __init__(self, name: str, IOAutomaton_Input27: "IOAutomaton_Operation" = None, IOAutomaton_Input: "IOAutomaton_Automaton" = None, IOAutomaton_Input18: "IOAutomaton_Transition" = None):
        self.name = name
        self.IOAutomaton_Input27 = IOAutomaton_Input27
        self.IOAutomaton_Input = IOAutomaton_Input
        self.IOAutomaton_Input18 = IOAutomaton_Input18
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def IOAutomaton_Input18(self):
        return self.__IOAutomaton_Input18

    @IOAutomaton_Input18.setter
    def IOAutomaton_Input18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Input__IOAutomaton_Input18", None)
        self.__IOAutomaton_Input18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Transition17"):
                opp_val = getattr(old_value, "IOAutomaton_Transition17", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Transition17"):
                opp_val = getattr(value, "IOAutomaton_Transition17", None)
                setattr(value, "IOAutomaton_Transition17", self)

    @property
    def IOAutomaton_Input27(self):
        return self.__IOAutomaton_Input27

    @IOAutomaton_Input27.setter
    def IOAutomaton_Input27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Input__IOAutomaton_Input27", None)
        self.__IOAutomaton_Input27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Operation"):
                opp_val = getattr(old_value, "IOAutomaton_Operation", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Operation"):
                opp_val = getattr(value, "IOAutomaton_Operation", None)
                setattr(value, "IOAutomaton_Operation", self)

    @property
    def IOAutomaton_Input(self):
        return self.__IOAutomaton_Input

    @IOAutomaton_Input.setter
    def IOAutomaton_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Input__IOAutomaton_Input", None)
        self.__IOAutomaton_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Automaton2"):
                opp_val = getattr(old_value, "IOAutomaton_Automaton2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Automaton2"):
                opp_val = getattr(value, "IOAutomaton_Automaton2", None)
                if opp_val is None:
                    setattr(value, "IOAutomaton_Automaton2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IOAutomaton_State:

    def __init__(self, name: str, IOAutomaton_State9: "IOAutomaton_Automaton" = None, IOAutomaton_State: "IOAutomaton_Automaton" = None, IOAutomaton_State12: "IOAutomaton_Transition" = None, IOAutomaton_State15: "IOAutomaton_Transition" = None):
        self.name = name
        self.IOAutomaton_State9 = IOAutomaton_State9
        self.IOAutomaton_State = IOAutomaton_State
        self.IOAutomaton_State12 = IOAutomaton_State12
        self.IOAutomaton_State15 = IOAutomaton_State15
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def IOAutomaton_State12(self):
        return self.__IOAutomaton_State12

    @IOAutomaton_State12.setter
    def IOAutomaton_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_State__IOAutomaton_State12", None)
        self.__IOAutomaton_State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Transition11"):
                opp_val = getattr(old_value, "IOAutomaton_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Transition11"):
                opp_val = getattr(value, "IOAutomaton_Transition11", None)
                setattr(value, "IOAutomaton_Transition11", self)

    @property
    def IOAutomaton_State(self):
        return self.__IOAutomaton_State

    @IOAutomaton_State.setter
    def IOAutomaton_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_State__IOAutomaton_State", None)
        self.__IOAutomaton_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Automaton"):
                opp_val = getattr(old_value, "IOAutomaton_Automaton", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Automaton"):
                opp_val = getattr(value, "IOAutomaton_Automaton", None)
                if opp_val is None:
                    setattr(value, "IOAutomaton_Automaton", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def IOAutomaton_State9(self):
        return self.__IOAutomaton_State9

    @IOAutomaton_State9.setter
    def IOAutomaton_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_State__IOAutomaton_State9", None)
        self.__IOAutomaton_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Automaton8"):
                opp_val = getattr(old_value, "IOAutomaton_Automaton8", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Automaton8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Automaton8"):
                opp_val = getattr(value, "IOAutomaton_Automaton8", None)
                setattr(value, "IOAutomaton_Automaton8", self)

    @property
    def IOAutomaton_State15(self):
        return self.__IOAutomaton_State15

    @IOAutomaton_State15.setter
    def IOAutomaton_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_State__IOAutomaton_State15", None)
        self.__IOAutomaton_State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_Transition14"):
                opp_val = getattr(old_value, "IOAutomaton_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_Transition14"):
                opp_val = getattr(value, "IOAutomaton_Transition14", None)
                setattr(value, "IOAutomaton_Transition14", self)

class IOAutomaton_Automaton:

    def __init__(self, name: str, IOAutomaton_Automaton8: "IOAutomaton_State" = None, IOAutomaton_Automaton: set["IOAutomaton_State"] = None, IOAutomaton_Automaton2: set["IOAutomaton_Input"] = None, IOAutomaton_Automaton4: set["IOAutomaton_Activation"] = None, IOAutomaton_Automaton6: set["IOAutomaton_Transition"] = None):
        self.name = name
        self.IOAutomaton_Automaton8 = IOAutomaton_Automaton8
        self.IOAutomaton_Automaton = IOAutomaton_Automaton if IOAutomaton_Automaton is not None else set()
        self.IOAutomaton_Automaton2 = IOAutomaton_Automaton2 if IOAutomaton_Automaton2 is not None else set()
        self.IOAutomaton_Automaton4 = IOAutomaton_Automaton4 if IOAutomaton_Automaton4 is not None else set()
        self.IOAutomaton_Automaton6 = IOAutomaton_Automaton6 if IOAutomaton_Automaton6 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def IOAutomaton_Automaton4(self):
        return self.__IOAutomaton_Automaton4

    @IOAutomaton_Automaton4.setter
    def IOAutomaton_Automaton4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Automaton__IOAutomaton_Automaton4", None)
        self.__IOAutomaton_Automaton4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IOAutomaton_Activation"):
                    opp_val = getattr(item, "IOAutomaton_Activation", None)
                    
                    if opp_val == self:
                        setattr(item, "IOAutomaton_Activation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IOAutomaton_Activation"):
                    opp_val = getattr(item, "IOAutomaton_Activation", None)
                    
                    setattr(item, "IOAutomaton_Activation", self)
                    

    @property
    def IOAutomaton_Automaton(self):
        return self.__IOAutomaton_Automaton

    @IOAutomaton_Automaton.setter
    def IOAutomaton_Automaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Automaton__IOAutomaton_Automaton", None)
        self.__IOAutomaton_Automaton = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IOAutomaton_State"):
                    opp_val = getattr(item, "IOAutomaton_State", None)
                    
                    if opp_val == self:
                        setattr(item, "IOAutomaton_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IOAutomaton_State"):
                    opp_val = getattr(item, "IOAutomaton_State", None)
                    
                    setattr(item, "IOAutomaton_State", self)
                    

    @property
    def IOAutomaton_Automaton6(self):
        return self.__IOAutomaton_Automaton6

    @IOAutomaton_Automaton6.setter
    def IOAutomaton_Automaton6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Automaton__IOAutomaton_Automaton6", None)
        self.__IOAutomaton_Automaton6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IOAutomaton_Transition"):
                    opp_val = getattr(item, "IOAutomaton_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "IOAutomaton_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IOAutomaton_Transition"):
                    opp_val = getattr(item, "IOAutomaton_Transition", None)
                    
                    setattr(item, "IOAutomaton_Transition", self)
                    

    @property
    def IOAutomaton_Automaton8(self):
        return self.__IOAutomaton_Automaton8

    @IOAutomaton_Automaton8.setter
    def IOAutomaton_Automaton8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Automaton__IOAutomaton_Automaton8", None)
        self.__IOAutomaton_Automaton8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IOAutomaton_State9"):
                opp_val = getattr(old_value, "IOAutomaton_State9", None)
                if opp_val == self:
                    setattr(old_value, "IOAutomaton_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IOAutomaton_State9"):
                opp_val = getattr(value, "IOAutomaton_State9", None)
                setattr(value, "IOAutomaton_State9", self)

    @property
    def IOAutomaton_Automaton2(self):
        return self.__IOAutomaton_Automaton2

    @IOAutomaton_Automaton2.setter
    def IOAutomaton_Automaton2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IOAutomaton_Automaton__IOAutomaton_Automaton2", None)
        self.__IOAutomaton_Automaton2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IOAutomaton_Input"):
                    opp_val = getattr(item, "IOAutomaton_Input", None)
                    
                    if opp_val == self:
                        setattr(item, "IOAutomaton_Input", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IOAutomaton_Input"):
                    opp_val = getattr(item, "IOAutomaton_Input", None)
                    
                    setattr(item, "IOAutomaton_Input", self)
                    
