from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class MDAIntermediateStateMachine_Value:

    def __init__(self, value: str, MDAIntermediateStateMachine_Value: "MDAIntermediateStateMachine_Transition" = None, MDAIntermediateStateMachine_Value41: "MDAIntermediateStateMachine_Message" = None):
        self.value = value
        self.MDAIntermediateStateMachine_Value = MDAIntermediateStateMachine_Value
        self.MDAIntermediateStateMachine_Value41 = MDAIntermediateStateMachine_Value41
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def MDAIntermediateStateMachine_Value41(self):
        return self.__MDAIntermediateStateMachine_Value41

    @MDAIntermediateStateMachine_Value41.setter
    def MDAIntermediateStateMachine_Value41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Value__MDAIntermediateStateMachine_Value41", None)
        self.__MDAIntermediateStateMachine_Value41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Message40"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Message40", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_Message40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Message40"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Message40", None)
                setattr(value, "MDAIntermediateStateMachine_Message40", self)

    @property
    def MDAIntermediateStateMachine_Value(self):
        return self.__MDAIntermediateStateMachine_Value

    @MDAIntermediateStateMachine_Value.setter
    def MDAIntermediateStateMachine_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Value__MDAIntermediateStateMachine_Value", None)
        self.__MDAIntermediateStateMachine_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Transition32"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Transition32", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_Transition32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Transition32"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Transition32", None)
                setattr(value, "MDAIntermediateStateMachine_Transition32", self)

class MDAIntermediateStateMachine_Transition:

    pass
class MDAIntermediateStateMachine_MessageSequence:

    pass
class MDAIntermediateStateMachine_Message:

    pass
class MDAIntermediateStateMachine_Participant:

    def __init__(self, name: str, MDAIntermediateStateMachine_Participant: "MDAIntermediateStateMachine_Content" = None, MDAIntermediateStateMachine_Participant21: "MDAIntermediateStateMachine_Automaton" = None, MDAIntermediateStateMachine_Participant38: "MDAIntermediateStateMachine_Message" = None):
        self.name = name
        self.MDAIntermediateStateMachine_Participant = MDAIntermediateStateMachine_Participant
        self.MDAIntermediateStateMachine_Participant21 = MDAIntermediateStateMachine_Participant21
        self.MDAIntermediateStateMachine_Participant38 = MDAIntermediateStateMachine_Participant38
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MDAIntermediateStateMachine_Participant(self):
        return self.__MDAIntermediateStateMachine_Participant

    @MDAIntermediateStateMachine_Participant.setter
    def MDAIntermediateStateMachine_Participant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Participant__MDAIntermediateStateMachine_Participant", None)
        self.__MDAIntermediateStateMachine_Participant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Content6"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Content6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Content6"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Content6", None)
                if opp_val is None:
                    setattr(value, "MDAIntermediateStateMachine_Content6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MDAIntermediateStateMachine_Participant38(self):
        return self.__MDAIntermediateStateMachine_Participant38

    @MDAIntermediateStateMachine_Participant38.setter
    def MDAIntermediateStateMachine_Participant38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Participant__MDAIntermediateStateMachine_Participant38", None)
        self.__MDAIntermediateStateMachine_Participant38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Message37"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Message37", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_Message37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Message37"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Message37", None)
                setattr(value, "MDAIntermediateStateMachine_Message37", self)

    @property
    def MDAIntermediateStateMachine_Participant21(self):
        return self.__MDAIntermediateStateMachine_Participant21

    @MDAIntermediateStateMachine_Participant21.setter
    def MDAIntermediateStateMachine_Participant21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Participant__MDAIntermediateStateMachine_Participant21", None)
        self.__MDAIntermediateStateMachine_Participant21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Automaton20"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Automaton20", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_Automaton20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Automaton20"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Automaton20", None)
                setattr(value, "MDAIntermediateStateMachine_Automaton20", self)

class MDAIntermediateStateMachine_Automaton:

    def __init__(self, name: str, MDAIntermediateStateMachine_Automaton: "MDAIntermediateStateMachine_Content" = None, MDAIntermediateStateMachine_Automaton15: set["MDAIntermediateStateMachine_State"] = None, MDAIntermediateStateMachine_Automaton12: "MDAIntermediateStateMachine_State" = None, MDAIntermediateStateMachine_Automaton18: set["MDAIntermediateStateMachine_Transition"] = None, MDAIntermediateStateMachine_Automaton20: "MDAIntermediateStateMachine_Participant" = None):
        self.name = name
        self.MDAIntermediateStateMachine_Automaton = MDAIntermediateStateMachine_Automaton
        self.MDAIntermediateStateMachine_Automaton15 = MDAIntermediateStateMachine_Automaton15 if MDAIntermediateStateMachine_Automaton15 is not None else set()
        self.MDAIntermediateStateMachine_Automaton12 = MDAIntermediateStateMachine_Automaton12
        self.MDAIntermediateStateMachine_Automaton18 = MDAIntermediateStateMachine_Automaton18 if MDAIntermediateStateMachine_Automaton18 is not None else set()
        self.MDAIntermediateStateMachine_Automaton20 = MDAIntermediateStateMachine_Automaton20
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MDAIntermediateStateMachine_Automaton20(self):
        return self.__MDAIntermediateStateMachine_Automaton20

    @MDAIntermediateStateMachine_Automaton20.setter
    def MDAIntermediateStateMachine_Automaton20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton20", None)
        self.__MDAIntermediateStateMachine_Automaton20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Participant21"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Participant21", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_Participant21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Participant21"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Participant21", None)
                setattr(value, "MDAIntermediateStateMachine_Participant21", self)

    @property
    def MDAIntermediateStateMachine_Automaton15(self):
        return self.__MDAIntermediateStateMachine_Automaton15

    @MDAIntermediateStateMachine_Automaton15.setter
    def MDAIntermediateStateMachine_Automaton15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton15", None)
        self.__MDAIntermediateStateMachine_Automaton15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MDAIntermediateStateMachine_State16"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_State16", None)
                    
                    if opp_val == self:
                        setattr(item, "MDAIntermediateStateMachine_State16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MDAIntermediateStateMachine_State16"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_State16", None)
                    
                    setattr(item, "MDAIntermediateStateMachine_State16", self)
                    

    @property
    def MDAIntermediateStateMachine_Automaton(self):
        return self.__MDAIntermediateStateMachine_Automaton

    @MDAIntermediateStateMachine_Automaton.setter
    def MDAIntermediateStateMachine_Automaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton", None)
        self.__MDAIntermediateStateMachine_Automaton = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Content2"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Content2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Content2"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Content2", None)
                if opp_val is None:
                    setattr(value, "MDAIntermediateStateMachine_Content2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MDAIntermediateStateMachine_Automaton12(self):
        return self.__MDAIntermediateStateMachine_Automaton12

    @MDAIntermediateStateMachine_Automaton12.setter
    def MDAIntermediateStateMachine_Automaton12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton12", None)
        self.__MDAIntermediateStateMachine_Automaton12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_State13"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_State13", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_State13"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_State13", None)
                setattr(value, "MDAIntermediateStateMachine_State13", self)

    @property
    def MDAIntermediateStateMachine_Automaton18(self):
        return self.__MDAIntermediateStateMachine_Automaton18

    @MDAIntermediateStateMachine_Automaton18.setter
    def MDAIntermediateStateMachine_Automaton18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Automaton__MDAIntermediateStateMachine_Automaton18", None)
        self.__MDAIntermediateStateMachine_Automaton18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MDAIntermediateStateMachine_Transition"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "MDAIntermediateStateMachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MDAIntermediateStateMachine_Transition"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_Transition", None)
                    
                    setattr(item, "MDAIntermediateStateMachine_Transition", self)
                    

class MDAIntermediateStateMachine_State:

    def __init__(self, name: str, MDAIntermediateStateMachine_State: "MDAIntermediateStateMachine_Content" = None, MDAIntermediateStateMachine_State16: "MDAIntermediateStateMachine_Automaton" = None, MDAIntermediateStateMachine_State10: set["MDAIntermediateStateMachine_MessageSequence"] = None, MDAIntermediateStateMachine_State13: "MDAIntermediateStateMachine_Automaton" = None, MDAIntermediateStateMachine_State24: "MDAIntermediateStateMachine_Transition" = None, MDAIntermediateStateMachine_State27: "MDAIntermediateStateMachine_Transition" = None):
        self.name = name
        self.MDAIntermediateStateMachine_State = MDAIntermediateStateMachine_State
        self.MDAIntermediateStateMachine_State16 = MDAIntermediateStateMachine_State16
        self.MDAIntermediateStateMachine_State10 = MDAIntermediateStateMachine_State10 if MDAIntermediateStateMachine_State10 is not None else set()
        self.MDAIntermediateStateMachine_State13 = MDAIntermediateStateMachine_State13
        self.MDAIntermediateStateMachine_State24 = MDAIntermediateStateMachine_State24
        self.MDAIntermediateStateMachine_State27 = MDAIntermediateStateMachine_State27
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MDAIntermediateStateMachine_State13(self):
        return self.__MDAIntermediateStateMachine_State13

    @MDAIntermediateStateMachine_State13.setter
    def MDAIntermediateStateMachine_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State13", None)
        self.__MDAIntermediateStateMachine_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Automaton12"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Automaton12", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_Automaton12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Automaton12"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Automaton12", None)
                setattr(value, "MDAIntermediateStateMachine_Automaton12", self)

    @property
    def MDAIntermediateStateMachine_State24(self):
        return self.__MDAIntermediateStateMachine_State24

    @MDAIntermediateStateMachine_State24.setter
    def MDAIntermediateStateMachine_State24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State24", None)
        self.__MDAIntermediateStateMachine_State24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Transition23"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Transition23", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_Transition23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Transition23"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Transition23", None)
                setattr(value, "MDAIntermediateStateMachine_Transition23", self)

    @property
    def MDAIntermediateStateMachine_State27(self):
        return self.__MDAIntermediateStateMachine_State27

    @MDAIntermediateStateMachine_State27.setter
    def MDAIntermediateStateMachine_State27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State27", None)
        self.__MDAIntermediateStateMachine_State27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Transition26"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Transition26", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_Transition26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Transition26"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Transition26", None)
                setattr(value, "MDAIntermediateStateMachine_Transition26", self)

    @property
    def MDAIntermediateStateMachine_State10(self):
        return self.__MDAIntermediateStateMachine_State10

    @MDAIntermediateStateMachine_State10.setter
    def MDAIntermediateStateMachine_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State10", None)
        self.__MDAIntermediateStateMachine_State10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MDAIntermediateStateMachine_MessageSequence"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_MessageSequence", None)
                    
                    if opp_val == self:
                        setattr(item, "MDAIntermediateStateMachine_MessageSequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MDAIntermediateStateMachine_MessageSequence"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_MessageSequence", None)
                    
                    setattr(item, "MDAIntermediateStateMachine_MessageSequence", self)
                    

    @property
    def MDAIntermediateStateMachine_State16(self):
        return self.__MDAIntermediateStateMachine_State16

    @MDAIntermediateStateMachine_State16.setter
    def MDAIntermediateStateMachine_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State16", None)
        self.__MDAIntermediateStateMachine_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Automaton15"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Automaton15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Automaton15"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Automaton15", None)
                if opp_val is None:
                    setattr(value, "MDAIntermediateStateMachine_Automaton15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MDAIntermediateStateMachine_State(self):
        return self.__MDAIntermediateStateMachine_State

    @MDAIntermediateStateMachine_State.setter
    def MDAIntermediateStateMachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_State__MDAIntermediateStateMachine_State", None)
        self.__MDAIntermediateStateMachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Content"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Content", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Content"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Content", None)
                if opp_val is None:
                    setattr(value, "MDAIntermediateStateMachine_Content", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MDAIntermediateStateMachine_Content:

    def __init__(self, name: str, MDAIntermediateStateMachine_Content: set["MDAIntermediateStateMachine_State"] = None, MDAIntermediateStateMachine_Content2: set["MDAIntermediateStateMachine_Automaton"] = None, MDAIntermediateStateMachine_Content4: set["MDAIntermediateStateMachine_Operation"] = None, MDAIntermediateStateMachine_Content6: set["MDAIntermediateStateMachine_Participant"] = None, MDAIntermediateStateMachine_Content8: set["MDAIntermediateStateMachine_Message"] = None):
        self.name = name
        self.MDAIntermediateStateMachine_Content = MDAIntermediateStateMachine_Content if MDAIntermediateStateMachine_Content is not None else set()
        self.MDAIntermediateStateMachine_Content2 = MDAIntermediateStateMachine_Content2 if MDAIntermediateStateMachine_Content2 is not None else set()
        self.MDAIntermediateStateMachine_Content4 = MDAIntermediateStateMachine_Content4 if MDAIntermediateStateMachine_Content4 is not None else set()
        self.MDAIntermediateStateMachine_Content6 = MDAIntermediateStateMachine_Content6 if MDAIntermediateStateMachine_Content6 is not None else set()
        self.MDAIntermediateStateMachine_Content8 = MDAIntermediateStateMachine_Content8 if MDAIntermediateStateMachine_Content8 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MDAIntermediateStateMachine_Content2(self):
        return self.__MDAIntermediateStateMachine_Content2

    @MDAIntermediateStateMachine_Content2.setter
    def MDAIntermediateStateMachine_Content2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content2", None)
        self.__MDAIntermediateStateMachine_Content2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MDAIntermediateStateMachine_Automaton"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_Automaton", None)
                    
                    if opp_val == self:
                        setattr(item, "MDAIntermediateStateMachine_Automaton", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MDAIntermediateStateMachine_Automaton"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_Automaton", None)
                    
                    setattr(item, "MDAIntermediateStateMachine_Automaton", self)
                    

    @property
    def MDAIntermediateStateMachine_Content6(self):
        return self.__MDAIntermediateStateMachine_Content6

    @MDAIntermediateStateMachine_Content6.setter
    def MDAIntermediateStateMachine_Content6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content6", None)
        self.__MDAIntermediateStateMachine_Content6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MDAIntermediateStateMachine_Participant"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_Participant", None)
                    
                    if opp_val == self:
                        setattr(item, "MDAIntermediateStateMachine_Participant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MDAIntermediateStateMachine_Participant"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_Participant", None)
                    
                    setattr(item, "MDAIntermediateStateMachine_Participant", self)
                    

    @property
    def MDAIntermediateStateMachine_Content8(self):
        return self.__MDAIntermediateStateMachine_Content8

    @MDAIntermediateStateMachine_Content8.setter
    def MDAIntermediateStateMachine_Content8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content8", None)
        self.__MDAIntermediateStateMachine_Content8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MDAIntermediateStateMachine_Message"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "MDAIntermediateStateMachine_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MDAIntermediateStateMachine_Message"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_Message", None)
                    
                    setattr(item, "MDAIntermediateStateMachine_Message", self)
                    

    @property
    def MDAIntermediateStateMachine_Content(self):
        return self.__MDAIntermediateStateMachine_Content

    @MDAIntermediateStateMachine_Content.setter
    def MDAIntermediateStateMachine_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content", None)
        self.__MDAIntermediateStateMachine_Content = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MDAIntermediateStateMachine_State"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_State", None)
                    
                    if opp_val == self:
                        setattr(item, "MDAIntermediateStateMachine_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MDAIntermediateStateMachine_State"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_State", None)
                    
                    setattr(item, "MDAIntermediateStateMachine_State", self)
                    

    @property
    def MDAIntermediateStateMachine_Content4(self):
        return self.__MDAIntermediateStateMachine_Content4

    @MDAIntermediateStateMachine_Content4.setter
    def MDAIntermediateStateMachine_Content4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Content__MDAIntermediateStateMachine_Content4", None)
        self.__MDAIntermediateStateMachine_Content4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MDAIntermediateStateMachine_Operation"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "MDAIntermediateStateMachine_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MDAIntermediateStateMachine_Operation"):
                    opp_val = getattr(item, "MDAIntermediateStateMachine_Operation", None)
                    
                    setattr(item, "MDAIntermediateStateMachine_Operation", self)
                    

class MDAIntermediateStateMachine_Operation:

    def __init__(self, name: str, MDAIntermediateStateMachine_Operation: "MDAIntermediateStateMachine_Content" = None, MDAIntermediateStateMachine_Operation30: "MDAIntermediateStateMachine_Transition" = None, MDAIntermediateStateMachine_Operation35: "MDAIntermediateStateMachine_Message" = None):
        self.name = name
        self.MDAIntermediateStateMachine_Operation = MDAIntermediateStateMachine_Operation
        self.MDAIntermediateStateMachine_Operation30 = MDAIntermediateStateMachine_Operation30
        self.MDAIntermediateStateMachine_Operation35 = MDAIntermediateStateMachine_Operation35
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MDAIntermediateStateMachine_Operation(self):
        return self.__MDAIntermediateStateMachine_Operation

    @MDAIntermediateStateMachine_Operation.setter
    def MDAIntermediateStateMachine_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation", None)
        self.__MDAIntermediateStateMachine_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Content4"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Content4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Content4"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Content4", None)
                if opp_val is None:
                    setattr(value, "MDAIntermediateStateMachine_Content4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MDAIntermediateStateMachine_Operation35(self):
        return self.__MDAIntermediateStateMachine_Operation35

    @MDAIntermediateStateMachine_Operation35.setter
    def MDAIntermediateStateMachine_Operation35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation35", None)
        self.__MDAIntermediateStateMachine_Operation35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Message34"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Message34", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_Message34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Message34"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Message34", None)
                setattr(value, "MDAIntermediateStateMachine_Message34", self)

    @property
    def MDAIntermediateStateMachine_Operation30(self):
        return self.__MDAIntermediateStateMachine_Operation30

    @MDAIntermediateStateMachine_Operation30.setter
    def MDAIntermediateStateMachine_Operation30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MDAIntermediateStateMachine_Operation__MDAIntermediateStateMachine_Operation30", None)
        self.__MDAIntermediateStateMachine_Operation30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MDAIntermediateStateMachine_Transition29"):
                opp_val = getattr(old_value, "MDAIntermediateStateMachine_Transition29", None)
                if opp_val == self:
                    setattr(old_value, "MDAIntermediateStateMachine_Transition29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MDAIntermediateStateMachine_Transition29"):
                opp_val = getattr(value, "MDAIntermediateStateMachine_Transition29", None)
                setattr(value, "MDAIntermediateStateMachine_Transition29", self)
