from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class smDsl_Command:

    def __init__(self, name: str, smDsl_Command11: "smDsl_State" = None, smDsl_Command16: "smDsl_State" = None, smDsl_Command22: "smDsl_EventHandlingDescription" = None, smDsl_Command: "smDsl_CommandsSection" = None):
        self.name = name
        self.smDsl_Command11 = smDsl_Command11
        self.smDsl_Command16 = smDsl_Command16
        self.smDsl_Command22 = smDsl_Command22
        self.smDsl_Command = smDsl_Command
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smDsl_Command(self):
        return self.__smDsl_Command

    @smDsl_Command.setter
    def smDsl_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_Command__smDsl_Command", None)
        self.__smDsl_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smDsl_CommandsSection8"):
                opp_val = getattr(old_value, "smDsl_CommandsSection8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smDsl_CommandsSection8"):
                opp_val = getattr(value, "smDsl_CommandsSection8", None)
                if opp_val is None:
                    setattr(value, "smDsl_CommandsSection8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smDsl_Command11(self):
        return self.__smDsl_Command11

    @smDsl_Command11.setter
    def smDsl_Command11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_Command__smDsl_Command11", None)
        self.__smDsl_Command11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smDsl_State10"):
                opp_val = getattr(old_value, "smDsl_State10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smDsl_State10"):
                opp_val = getattr(value, "smDsl_State10", None)
                if opp_val is None:
                    setattr(value, "smDsl_State10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smDsl_Command16(self):
        return self.__smDsl_Command16

    @smDsl_Command16.setter
    def smDsl_Command16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_Command__smDsl_Command16", None)
        self.__smDsl_Command16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smDsl_State15"):
                opp_val = getattr(old_value, "smDsl_State15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smDsl_State15"):
                opp_val = getattr(value, "smDsl_State15", None)
                if opp_val is None:
                    setattr(value, "smDsl_State15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smDsl_Command22(self):
        return self.__smDsl_Command22

    @smDsl_Command22.setter
    def smDsl_Command22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_Command__smDsl_Command22", None)
        self.__smDsl_Command22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smDsl_EventHandlingDescription21"):
                opp_val = getattr(old_value, "smDsl_EventHandlingDescription21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smDsl_EventHandlingDescription21"):
                opp_val = getattr(value, "smDsl_EventHandlingDescription21", None)
                if opp_val is None:
                    setattr(value, "smDsl_EventHandlingDescription21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smDsl_Event:

    def __init__(self, name: str, smDsl_Event19: "smDsl_EventHandlingDescription" = None, smDsl_Event: "smDsl_EventsSection" = None):
        self.name = name
        self.smDsl_Event19 = smDsl_Event19
        self.smDsl_Event = smDsl_Event
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smDsl_Event19(self):
        return self.__smDsl_Event19

    @smDsl_Event19.setter
    def smDsl_Event19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_Event__smDsl_Event19", None)
        self.__smDsl_Event19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smDsl_EventHandlingDescription18"):
                opp_val = getattr(old_value, "smDsl_EventHandlingDescription18", None)
                if opp_val == self:
                    setattr(old_value, "smDsl_EventHandlingDescription18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smDsl_EventHandlingDescription18"):
                opp_val = getattr(value, "smDsl_EventHandlingDescription18", None)
                setattr(value, "smDsl_EventHandlingDescription18", self)

    @property
    def smDsl_Event(self):
        return self.__smDsl_Event

    @smDsl_Event.setter
    def smDsl_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_Event__smDsl_Event", None)
        self.__smDsl_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smDsl_EventsSection6"):
                opp_val = getattr(old_value, "smDsl_EventsSection6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smDsl_EventsSection6"):
                opp_val = getattr(value, "smDsl_EventsSection6", None)
                if opp_val is None:
                    setattr(value, "smDsl_EventsSection6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smDsl_EventHandlingDescription:

    pass
class smDsl_State:

    def __init__(self, initial: bool, name: str, smDsl_State: "smDsl_Model" = None, smDsl_State10: set["smDsl_Command"] = None, smDsl_State13: set["smDsl_EventHandlingDescription"] = None, smDsl_State15: set["smDsl_Command"] = None, smDsl_State25: "smDsl_EventHandlingDescription" = None):
        self.initial = initial
        self.name = name
        self.smDsl_State = smDsl_State
        self.smDsl_State10 = smDsl_State10 if smDsl_State10 is not None else set()
        self.smDsl_State13 = smDsl_State13 if smDsl_State13 is not None else set()
        self.smDsl_State15 = smDsl_State15 if smDsl_State15 is not None else set()
        self.smDsl_State25 = smDsl_State25
        
    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smDsl_State15(self):
        return self.__smDsl_State15

    @smDsl_State15.setter
    def smDsl_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_State__smDsl_State15", None)
        self.__smDsl_State15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smDsl_Command16"):
                    opp_val = getattr(item, "smDsl_Command16", None)
                    
                    if opp_val == self:
                        setattr(item, "smDsl_Command16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smDsl_Command16"):
                    opp_val = getattr(item, "smDsl_Command16", None)
                    
                    setattr(item, "smDsl_Command16", self)
                    

    @property
    def smDsl_State(self):
        return self.__smDsl_State

    @smDsl_State.setter
    def smDsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_State__smDsl_State", None)
        self.__smDsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smDsl_Model4"):
                opp_val = getattr(old_value, "smDsl_Model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smDsl_Model4"):
                opp_val = getattr(value, "smDsl_Model4", None)
                if opp_val is None:
                    setattr(value, "smDsl_Model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smDsl_State13(self):
        return self.__smDsl_State13

    @smDsl_State13.setter
    def smDsl_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_State__smDsl_State13", None)
        self.__smDsl_State13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smDsl_EventHandlingDescription"):
                    opp_val = getattr(item, "smDsl_EventHandlingDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "smDsl_EventHandlingDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smDsl_EventHandlingDescription"):
                    opp_val = getattr(item, "smDsl_EventHandlingDescription", None)
                    
                    setattr(item, "smDsl_EventHandlingDescription", self)
                    

    @property
    def smDsl_State10(self):
        return self.__smDsl_State10

    @smDsl_State10.setter
    def smDsl_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_State__smDsl_State10", None)
        self.__smDsl_State10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smDsl_Command11"):
                    opp_val = getattr(item, "smDsl_Command11", None)
                    
                    if opp_val == self:
                        setattr(item, "smDsl_Command11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smDsl_Command11"):
                    opp_val = getattr(item, "smDsl_Command11", None)
                    
                    setattr(item, "smDsl_Command11", self)
                    

    @property
    def smDsl_State25(self):
        return self.__smDsl_State25

    @smDsl_State25.setter
    def smDsl_State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_State__smDsl_State25", None)
        self.__smDsl_State25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smDsl_EventHandlingDescription24"):
                opp_val = getattr(old_value, "smDsl_EventHandlingDescription24", None)
                if opp_val == self:
                    setattr(old_value, "smDsl_EventHandlingDescription24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smDsl_EventHandlingDescription24"):
                opp_val = getattr(value, "smDsl_EventHandlingDescription24", None)
                setattr(value, "smDsl_EventHandlingDescription24", self)

class smDsl_CommandsSection:

    pass
class smDsl_EventsSection:

    pass
class smDsl_Model:

    def __init__(self, name: str, smDsl_Model: "smDsl_EventsSection" = None, smDsl_Model2: "smDsl_CommandsSection" = None, smDsl_Model4: set["smDsl_State"] = None):
        self.name = name
        self.smDsl_Model = smDsl_Model
        self.smDsl_Model2 = smDsl_Model2
        self.smDsl_Model4 = smDsl_Model4 if smDsl_Model4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smDsl_Model(self):
        return self.__smDsl_Model

    @smDsl_Model.setter
    def smDsl_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_Model__smDsl_Model", None)
        self.__smDsl_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smDsl_EventsSection"):
                opp_val = getattr(old_value, "smDsl_EventsSection", None)
                if opp_val == self:
                    setattr(old_value, "smDsl_EventsSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smDsl_EventsSection"):
                opp_val = getattr(value, "smDsl_EventsSection", None)
                setattr(value, "smDsl_EventsSection", self)

    @property
    def smDsl_Model2(self):
        return self.__smDsl_Model2

    @smDsl_Model2.setter
    def smDsl_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_Model__smDsl_Model2", None)
        self.__smDsl_Model2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smDsl_CommandsSection"):
                opp_val = getattr(old_value, "smDsl_CommandsSection", None)
                if opp_val == self:
                    setattr(old_value, "smDsl_CommandsSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smDsl_CommandsSection"):
                opp_val = getattr(value, "smDsl_CommandsSection", None)
                setattr(value, "smDsl_CommandsSection", self)

    @property
    def smDsl_Model4(self):
        return self.__smDsl_Model4

    @smDsl_Model4.setter
    def smDsl_Model4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smDsl_Model__smDsl_Model4", None)
        self.__smDsl_Model4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smDsl_State"):
                    opp_val = getattr(item, "smDsl_State", None)
                    
                    if opp_val == self:
                        setattr(item, "smDsl_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smDsl_State"):
                    opp_val = getattr(item, "smDsl_State", None)
                    
                    setattr(item, "smDsl_State", self)
                    
