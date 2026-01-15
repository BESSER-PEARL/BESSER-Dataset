from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class smarthome_FilterConnection:

    pass
class smarthome_CommandConnection:

    pass
class smarthome_SmartHome:

    def __init__(self, name: str, smarthome_SmartHome: set["smarthome_Item"] = None, smarthome_SmartHome2: set["smarthome_EvaluatingNode"] = None):
        self.name = name
        self.smarthome_SmartHome = smarthome_SmartHome if smarthome_SmartHome is not None else set()
        self.smarthome_SmartHome2 = smarthome_SmartHome2 if smarthome_SmartHome2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smarthome_SmartHome2(self):
        return self.__smarthome_SmartHome2

    @smarthome_SmartHome2.setter
    def smarthome_SmartHome2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_SmartHome__smarthome_SmartHome2", None)
        self.__smarthome_SmartHome2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smarthome_EvaluatingNode"):
                    opp_val = getattr(item, "smarthome_EvaluatingNode", None)
                    
                    if opp_val == self:
                        setattr(item, "smarthome_EvaluatingNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smarthome_EvaluatingNode"):
                    opp_val = getattr(item, "smarthome_EvaluatingNode", None)
                    
                    setattr(item, "smarthome_EvaluatingNode", self)
                    

    @property
    def smarthome_SmartHome(self):
        return self.__smarthome_SmartHome

    @smarthome_SmartHome.setter
    def smarthome_SmartHome(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_SmartHome__smarthome_SmartHome", None)
        self.__smarthome_SmartHome = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smarthome_Item"):
                    opp_val = getattr(item, "smarthome_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "smarthome_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smarthome_Item"):
                    opp_val = getattr(item, "smarthome_Item", None)
                    
                    setattr(item, "smarthome_Item", self)
                    

class smarthome_StateChangeConnection:

    pass
class Item:

    pass
class smarthome_DimmerItem(Item):

    pass
class smarthome_SwitchItem(Item):

    pass
class smarthome_NumberItem(Item):

    pass
class smarthome_ContactItem(Item):

    pass
class smarthome_Command:

    def __init__(self, command: str, smarthome_Command: "smarthome_Item" = None, smarthome_Command18: "smarthome_CommandConnection" = None):
        self.command = command
        self.smarthome_Command = smarthome_Command
        self.smarthome_Command18 = smarthome_Command18
        
    @property
    def command(self) -> str:
        return self.__command

    @command.setter
    def command(self, command: str):
        self.__command = command

    @property
    def smarthome_Command(self):
        return self.__smarthome_Command

    @smarthome_Command.setter
    def smarthome_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Command__smarthome_Command", None)
        self.__smarthome_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_Item6"):
                opp_val = getattr(old_value, "smarthome_Item6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_Item6"):
                opp_val = getattr(value, "smarthome_Item6", None)
                if opp_val is None:
                    setattr(value, "smarthome_Item6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smarthome_Command18(self):
        return self.__smarthome_Command18

    @smarthome_Command18.setter
    def smarthome_Command18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Command__smarthome_Command18", None)
        self.__smarthome_Command18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_CommandConnection17"):
                opp_val = getattr(old_value, "smarthome_CommandConnection17", None)
                if opp_val == self:
                    setattr(old_value, "smarthome_CommandConnection17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_CommandConnection17"):
                opp_val = getattr(value, "smarthome_CommandConnection17", None)
                setattr(value, "smarthome_CommandConnection17", self)

class smarthome_State:

    def __init__(self, state: str, smarthome_State: "smarthome_Item" = None, smarthome_State21: "smarthome_StateChangeConnection" = None, smarthome_State27: "smarthome_FilterConnection" = None):
        self.state = state
        self.smarthome_State = smarthome_State
        self.smarthome_State21 = smarthome_State21
        self.smarthome_State27 = smarthome_State27
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def smarthome_State21(self):
        return self.__smarthome_State21

    @smarthome_State21.setter
    def smarthome_State21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_State__smarthome_State21", None)
        self.__smarthome_State21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_StateChangeConnection20"):
                opp_val = getattr(old_value, "smarthome_StateChangeConnection20", None)
                if opp_val == self:
                    setattr(old_value, "smarthome_StateChangeConnection20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_StateChangeConnection20"):
                opp_val = getattr(value, "smarthome_StateChangeConnection20", None)
                setattr(value, "smarthome_StateChangeConnection20", self)

    @property
    def smarthome_State27(self):
        return self.__smarthome_State27

    @smarthome_State27.setter
    def smarthome_State27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_State__smarthome_State27", None)
        self.__smarthome_State27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_FilterConnection26"):
                opp_val = getattr(old_value, "smarthome_FilterConnection26", None)
                if opp_val == self:
                    setattr(old_value, "smarthome_FilterConnection26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_FilterConnection26"):
                opp_val = getattr(value, "smarthome_FilterConnection26", None)
                setattr(value, "smarthome_FilterConnection26", self)

    @property
    def smarthome_State(self):
        return self.__smarthome_State

    @smarthome_State.setter
    def smarthome_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_State__smarthome_State", None)
        self.__smarthome_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_Item4"):
                opp_val = getattr(old_value, "smarthome_Item4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_Item4"):
                opp_val = getattr(value, "smarthome_Item4", None)
                if opp_val is None:
                    setattr(value, "smarthome_Item4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smarthome_EvaluatingNode:

    pass
class smarthome_Item(ABC):

    def __init__(self, name: str, smarthome_Item: "smarthome_SmartHome" = None, smarthome_Item4: set["smarthome_State"] = None, smarthome_Item6: set["smarthome_Command"] = None, smarthome_Item15: "smarthome_CommandConnection" = None, smarthome_Item24: "smarthome_StateChangeConnection" = None, smarthome_Item30: "smarthome_FilterConnection" = None):
        self.name = name
        self.smarthome_Item = smarthome_Item
        self.smarthome_Item4 = smarthome_Item4 if smarthome_Item4 is not None else set()
        self.smarthome_Item6 = smarthome_Item6 if smarthome_Item6 is not None else set()
        self.smarthome_Item15 = smarthome_Item15
        self.smarthome_Item24 = smarthome_Item24
        self.smarthome_Item30 = smarthome_Item30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smarthome_Item6(self):
        return self.__smarthome_Item6

    @smarthome_Item6.setter
    def smarthome_Item6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Item__smarthome_Item6", None)
        self.__smarthome_Item6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smarthome_Command"):
                    opp_val = getattr(item, "smarthome_Command", None)
                    
                    if opp_val == self:
                        setattr(item, "smarthome_Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smarthome_Command"):
                    opp_val = getattr(item, "smarthome_Command", None)
                    
                    setattr(item, "smarthome_Command", self)
                    

    @property
    def smarthome_Item(self):
        return self.__smarthome_Item

    @smarthome_Item.setter
    def smarthome_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Item__smarthome_Item", None)
        self.__smarthome_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_SmartHome"):
                opp_val = getattr(old_value, "smarthome_SmartHome", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_SmartHome"):
                opp_val = getattr(value, "smarthome_SmartHome", None)
                if opp_val is None:
                    setattr(value, "smarthome_SmartHome", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smarthome_Item24(self):
        return self.__smarthome_Item24

    @smarthome_Item24.setter
    def smarthome_Item24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Item__smarthome_Item24", None)
        self.__smarthome_Item24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_StateChangeConnection23"):
                opp_val = getattr(old_value, "smarthome_StateChangeConnection23", None)
                if opp_val == self:
                    setattr(old_value, "smarthome_StateChangeConnection23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_StateChangeConnection23"):
                opp_val = getattr(value, "smarthome_StateChangeConnection23", None)
                setattr(value, "smarthome_StateChangeConnection23", self)

    @property
    def smarthome_Item15(self):
        return self.__smarthome_Item15

    @smarthome_Item15.setter
    def smarthome_Item15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Item__smarthome_Item15", None)
        self.__smarthome_Item15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_CommandConnection14"):
                opp_val = getattr(old_value, "smarthome_CommandConnection14", None)
                if opp_val == self:
                    setattr(old_value, "smarthome_CommandConnection14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_CommandConnection14"):
                opp_val = getattr(value, "smarthome_CommandConnection14", None)
                setattr(value, "smarthome_CommandConnection14", self)

    @property
    def smarthome_Item30(self):
        return self.__smarthome_Item30

    @smarthome_Item30.setter
    def smarthome_Item30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Item__smarthome_Item30", None)
        self.__smarthome_Item30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_FilterConnection29"):
                opp_val = getattr(old_value, "smarthome_FilterConnection29", None)
                if opp_val == self:
                    setattr(old_value, "smarthome_FilterConnection29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_FilterConnection29"):
                opp_val = getattr(value, "smarthome_FilterConnection29", None)
                setattr(value, "smarthome_FilterConnection29", self)

    @property
    def smarthome_Item4(self):
        return self.__smarthome_Item4

    @smarthome_Item4.setter
    def smarthome_Item4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Item__smarthome_Item4", None)
        self.__smarthome_Item4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smarthome_State"):
                    opp_val = getattr(item, "smarthome_State", None)
                    
                    if opp_val == self:
                        setattr(item, "smarthome_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smarthome_State"):
                    opp_val = getattr(item, "smarthome_State", None)
                    
                    setattr(item, "smarthome_State", self)
                    
