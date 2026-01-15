from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Is_Style(Enum):
    style = "style"
    non_style = "non_style"


############################################
# Definition of Classes
############################################

class robotmodel_Role:

    def __init__(self, name: str, robotmodel_Role: "robotmodel_Connector" = None, robotmodel_Role25: "robotmodel_Port" = None):
        self.name = name
        self.robotmodel_Role = robotmodel_Role
        self.robotmodel_Role25 = robotmodel_Role25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robotmodel_Role(self):
        return self.__robotmodel_Role

    @robotmodel_Role.setter
    def robotmodel_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Role__robotmodel_Role", None)
        self.__robotmodel_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Connector22"):
                opp_val = getattr(old_value, "robotmodel_Connector22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Connector22"):
                opp_val = getattr(value, "robotmodel_Connector22", None)
                if opp_val is None:
                    setattr(value, "robotmodel_Connector22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Role25(self):
        return self.__robotmodel_Role25

    @robotmodel_Role25.setter
    def robotmodel_Role25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Role__robotmodel_Role25", None)
        self.__robotmodel_Role25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Port24"):
                opp_val = getattr(old_value, "robotmodel_Port24", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Port24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Port24"):
                opp_val = getattr(value, "robotmodel_Port24", None)
                setattr(value, "robotmodel_Port24", self)

class robotmodel_Action:

    def __init__(self, name: str, robotmodel_Action: "robotmodel_Component" = None, robotmodel_Action48: "robotmodel_Transition" = None, robotmodel_Action51: "robotmodel_Transition" = None, robotmodel_Action33: "robotmodel_State" = None, robotmodel_Action39: "robotmodel_State" = None, robotmodel_Action42: "robotmodel_State" = None):
        self.name = name
        self.robotmodel_Action = robotmodel_Action
        self.robotmodel_Action48 = robotmodel_Action48
        self.robotmodel_Action51 = robotmodel_Action51
        self.robotmodel_Action33 = robotmodel_Action33
        self.robotmodel_Action39 = robotmodel_Action39
        self.robotmodel_Action42 = robotmodel_Action42
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robotmodel_Action51(self):
        return self.__robotmodel_Action51

    @robotmodel_Action51.setter
    def robotmodel_Action51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Action__robotmodel_Action51", None)
        self.__robotmodel_Action51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Transition50"):
                opp_val = getattr(old_value, "robotmodel_Transition50", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Transition50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Transition50"):
                opp_val = getattr(value, "robotmodel_Transition50", None)
                setattr(value, "robotmodel_Transition50", self)

    @property
    def robotmodel_Action48(self):
        return self.__robotmodel_Action48

    @robotmodel_Action48.setter
    def robotmodel_Action48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Action__robotmodel_Action48", None)
        self.__robotmodel_Action48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Transition47"):
                opp_val = getattr(old_value, "robotmodel_Transition47", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Transition47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Transition47"):
                opp_val = getattr(value, "robotmodel_Transition47", None)
                setattr(value, "robotmodel_Transition47", self)

    @property
    def robotmodel_Action(self):
        return self.__robotmodel_Action

    @robotmodel_Action.setter
    def robotmodel_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Action__robotmodel_Action", None)
        self.__robotmodel_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Component17"):
                opp_val = getattr(old_value, "robotmodel_Component17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Component17"):
                opp_val = getattr(value, "robotmodel_Component17", None)
                if opp_val is None:
                    setattr(value, "robotmodel_Component17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Action39(self):
        return self.__robotmodel_Action39

    @robotmodel_Action39.setter
    def robotmodel_Action39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Action__robotmodel_Action39", None)
        self.__robotmodel_Action39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_State38"):
                opp_val = getattr(old_value, "robotmodel_State38", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_State38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_State38"):
                opp_val = getattr(value, "robotmodel_State38", None)
                setattr(value, "robotmodel_State38", self)

    @property
    def robotmodel_Action33(self):
        return self.__robotmodel_Action33

    @robotmodel_Action33.setter
    def robotmodel_Action33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Action__robotmodel_Action33", None)
        self.__robotmodel_Action33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_State32"):
                opp_val = getattr(old_value, "robotmodel_State32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_State32"):
                opp_val = getattr(value, "robotmodel_State32", None)
                if opp_val is None:
                    setattr(value, "robotmodel_State32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Action42(self):
        return self.__robotmodel_Action42

    @robotmodel_Action42.setter
    def robotmodel_Action42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Action__robotmodel_Action42", None)
        self.__robotmodel_Action42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_State41"):
                opp_val = getattr(old_value, "robotmodel_State41", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_State41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_State41"):
                opp_val = getattr(value, "robotmodel_State41", None)
                setattr(value, "robotmodel_State41", self)

class robotmodel_Transition:

    def __init__(self, name: str, robotmodel_Transition: "robotmodel_Component" = None, robotmodel_Transition47: "robotmodel_Action" = None, robotmodel_Transition50: "robotmodel_Action" = None, robotmodel_Transition53: "robotmodel_State" = None, robotmodel_Transition56: "robotmodel_State" = None, robotmodel_Transition60: "robotmodel_Event" = None, robotmodel_Transition36: "robotmodel_State" = None):
        self.name = name
        self.robotmodel_Transition = robotmodel_Transition
        self.robotmodel_Transition47 = robotmodel_Transition47
        self.robotmodel_Transition50 = robotmodel_Transition50
        self.robotmodel_Transition53 = robotmodel_Transition53
        self.robotmodel_Transition56 = robotmodel_Transition56
        self.robotmodel_Transition60 = robotmodel_Transition60
        self.robotmodel_Transition36 = robotmodel_Transition36
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robotmodel_Transition36(self):
        return self.__robotmodel_Transition36

    @robotmodel_Transition36.setter
    def robotmodel_Transition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Transition__robotmodel_Transition36", None)
        self.__robotmodel_Transition36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_State35"):
                opp_val = getattr(old_value, "robotmodel_State35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_State35"):
                opp_val = getattr(value, "robotmodel_State35", None)
                if opp_val is None:
                    setattr(value, "robotmodel_State35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Transition56(self):
        return self.__robotmodel_Transition56

    @robotmodel_Transition56.setter
    def robotmodel_Transition56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Transition__robotmodel_Transition56", None)
        self.__robotmodel_Transition56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_State57"):
                opp_val = getattr(old_value, "robotmodel_State57", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_State57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_State57"):
                opp_val = getattr(value, "robotmodel_State57", None)
                setattr(value, "robotmodel_State57", self)

    @property
    def robotmodel_Transition50(self):
        return self.__robotmodel_Transition50

    @robotmodel_Transition50.setter
    def robotmodel_Transition50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Transition__robotmodel_Transition50", None)
        self.__robotmodel_Transition50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Action51"):
                opp_val = getattr(old_value, "robotmodel_Action51", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Action51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Action51"):
                opp_val = getattr(value, "robotmodel_Action51", None)
                setattr(value, "robotmodel_Action51", self)

    @property
    def robotmodel_Transition47(self):
        return self.__robotmodel_Transition47

    @robotmodel_Transition47.setter
    def robotmodel_Transition47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Transition__robotmodel_Transition47", None)
        self.__robotmodel_Transition47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Action48"):
                opp_val = getattr(old_value, "robotmodel_Action48", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Action48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Action48"):
                opp_val = getattr(value, "robotmodel_Action48", None)
                setattr(value, "robotmodel_Action48", self)

    @property
    def robotmodel_Transition53(self):
        return self.__robotmodel_Transition53

    @robotmodel_Transition53.setter
    def robotmodel_Transition53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Transition__robotmodel_Transition53", None)
        self.__robotmodel_Transition53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_State54"):
                opp_val = getattr(old_value, "robotmodel_State54", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_State54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_State54"):
                opp_val = getattr(value, "robotmodel_State54", None)
                setattr(value, "robotmodel_State54", self)

    @property
    def robotmodel_Transition(self):
        return self.__robotmodel_Transition

    @robotmodel_Transition.setter
    def robotmodel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Transition__robotmodel_Transition", None)
        self.__robotmodel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Component15"):
                opp_val = getattr(old_value, "robotmodel_Component15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Component15"):
                opp_val = getattr(value, "robotmodel_Component15", None)
                if opp_val is None:
                    setattr(value, "robotmodel_Component15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Transition60(self):
        return self.__robotmodel_Transition60

    @robotmodel_Transition60.setter
    def robotmodel_Transition60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Transition__robotmodel_Transition60", None)
        self.__robotmodel_Transition60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Event59"):
                opp_val = getattr(old_value, "robotmodel_Event59", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Event59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Event59"):
                opp_val = getattr(value, "robotmodel_Event59", None)
                setattr(value, "robotmodel_Event59", self)

class robotmodel_Event:

    def __init__(self, name: str, robotmodel_Event: "robotmodel_Component" = None, robotmodel_Event45: "robotmodel_State" = None, robotmodel_Event59: "robotmodel_Transition" = None):
        self.name = name
        self.robotmodel_Event = robotmodel_Event
        self.robotmodel_Event45 = robotmodel_Event45
        self.robotmodel_Event59 = robotmodel_Event59
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robotmodel_Event59(self):
        return self.__robotmodel_Event59

    @robotmodel_Event59.setter
    def robotmodel_Event59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Event__robotmodel_Event59", None)
        self.__robotmodel_Event59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Transition60"):
                opp_val = getattr(old_value, "robotmodel_Transition60", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Transition60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Transition60"):
                opp_val = getattr(value, "robotmodel_Transition60", None)
                setattr(value, "robotmodel_Transition60", self)

    @property
    def robotmodel_Event45(self):
        return self.__robotmodel_Event45

    @robotmodel_Event45.setter
    def robotmodel_Event45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Event__robotmodel_Event45", None)
        self.__robotmodel_Event45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_State44"):
                opp_val = getattr(old_value, "robotmodel_State44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_State44"):
                opp_val = getattr(value, "robotmodel_State44", None)
                if opp_val is None:
                    setattr(value, "robotmodel_State44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Event(self):
        return self.__robotmodel_Event

    @robotmodel_Event.setter
    def robotmodel_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Event__robotmodel_Event", None)
        self.__robotmodel_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Component13"):
                opp_val = getattr(old_value, "robotmodel_Component13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Component13"):
                opp_val = getattr(value, "robotmodel_Component13", None)
                if opp_val is None:
                    setattr(value, "robotmodel_Component13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class robotmodel_State:

    def __init__(self, name: str, robotmodel_State: "robotmodel_Component" = None, robotmodel_State54: "robotmodel_Transition" = None, robotmodel_State57: "robotmodel_Transition" = None, robotmodel_State30: "robotmodel_State" = None, robotmodel_State28: set["robotmodel_State"] = None, robotmodel_State32: set["robotmodel_Action"] = None, robotmodel_State35: set["robotmodel_Transition"] = None, robotmodel_State38: "robotmodel_Action" = None, robotmodel_State41: "robotmodel_Action" = None, robotmodel_State44: set["robotmodel_Event"] = None):
        self.name = name
        self.robotmodel_State = robotmodel_State
        self.robotmodel_State54 = robotmodel_State54
        self.robotmodel_State57 = robotmodel_State57
        self.robotmodel_State30 = robotmodel_State30
        self.robotmodel_State28 = robotmodel_State28 if robotmodel_State28 is not None else set()
        self.robotmodel_State32 = robotmodel_State32 if robotmodel_State32 is not None else set()
        self.robotmodel_State35 = robotmodel_State35 if robotmodel_State35 is not None else set()
        self.robotmodel_State38 = robotmodel_State38
        self.robotmodel_State41 = robotmodel_State41
        self.robotmodel_State44 = robotmodel_State44 if robotmodel_State44 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robotmodel_State41(self):
        return self.__robotmodel_State41

    @robotmodel_State41.setter
    def robotmodel_State41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_State__robotmodel_State41", None)
        self.__robotmodel_State41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Action42"):
                opp_val = getattr(old_value, "robotmodel_Action42", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Action42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Action42"):
                opp_val = getattr(value, "robotmodel_Action42", None)
                setattr(value, "robotmodel_Action42", self)

    @property
    def robotmodel_State54(self):
        return self.__robotmodel_State54

    @robotmodel_State54.setter
    def robotmodel_State54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_State__robotmodel_State54", None)
        self.__robotmodel_State54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Transition53"):
                opp_val = getattr(old_value, "robotmodel_Transition53", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Transition53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Transition53"):
                opp_val = getattr(value, "robotmodel_Transition53", None)
                setattr(value, "robotmodel_Transition53", self)

    @property
    def robotmodel_State28(self):
        return self.__robotmodel_State28

    @robotmodel_State28.setter
    def robotmodel_State28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_State__robotmodel_State28", None)
        self.__robotmodel_State28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_State30"):
                    opp_val = getattr(item, "robotmodel_State30", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_State30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_State30"):
                    opp_val = getattr(item, "robotmodel_State30", None)
                    
                    setattr(item, "robotmodel_State30", self)
                    

    @property
    def robotmodel_State30(self):
        return self.__robotmodel_State30

    @robotmodel_State30.setter
    def robotmodel_State30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_State__robotmodel_State30", None)
        self.__robotmodel_State30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_State28"):
                opp_val = getattr(old_value, "robotmodel_State28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_State28"):
                opp_val = getattr(value, "robotmodel_State28", None)
                if opp_val is None:
                    setattr(value, "robotmodel_State28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_State32(self):
        return self.__robotmodel_State32

    @robotmodel_State32.setter
    def robotmodel_State32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_State__robotmodel_State32", None)
        self.__robotmodel_State32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Action33"):
                    opp_val = getattr(item, "robotmodel_Action33", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Action33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Action33"):
                    opp_val = getattr(item, "robotmodel_Action33", None)
                    
                    setattr(item, "robotmodel_Action33", self)
                    

    @property
    def robotmodel_State44(self):
        return self.__robotmodel_State44

    @robotmodel_State44.setter
    def robotmodel_State44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_State__robotmodel_State44", None)
        self.__robotmodel_State44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Event45"):
                    opp_val = getattr(item, "robotmodel_Event45", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Event45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Event45"):
                    opp_val = getattr(item, "robotmodel_Event45", None)
                    
                    setattr(item, "robotmodel_Event45", self)
                    

    @property
    def robotmodel_State38(self):
        return self.__robotmodel_State38

    @robotmodel_State38.setter
    def robotmodel_State38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_State__robotmodel_State38", None)
        self.__robotmodel_State38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Action39"):
                opp_val = getattr(old_value, "robotmodel_Action39", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Action39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Action39"):
                opp_val = getattr(value, "robotmodel_Action39", None)
                setattr(value, "robotmodel_Action39", self)

    @property
    def robotmodel_State(self):
        return self.__robotmodel_State

    @robotmodel_State.setter
    def robotmodel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_State__robotmodel_State", None)
        self.__robotmodel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Component11"):
                opp_val = getattr(old_value, "robotmodel_Component11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Component11"):
                opp_val = getattr(value, "robotmodel_Component11", None)
                if opp_val is None:
                    setattr(value, "robotmodel_Component11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_State35(self):
        return self.__robotmodel_State35

    @robotmodel_State35.setter
    def robotmodel_State35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_State__robotmodel_State35", None)
        self.__robotmodel_State35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Transition36"):
                    opp_val = getattr(item, "robotmodel_Transition36", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Transition36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Transition36"):
                    opp_val = getattr(item, "robotmodel_Transition36", None)
                    
                    setattr(item, "robotmodel_Transition36", self)
                    

    @property
    def robotmodel_State57(self):
        return self.__robotmodel_State57

    @robotmodel_State57.setter
    def robotmodel_State57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_State__robotmodel_State57", None)
        self.__robotmodel_State57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Transition56"):
                opp_val = getattr(old_value, "robotmodel_Transition56", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Transition56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Transition56"):
                opp_val = getattr(value, "robotmodel_Transition56", None)
                setattr(value, "robotmodel_Transition56", self)

class robotmodel_Property:

    def __init__(self, name: str, type: str, value: str, robotmodel_Property: "robotmodel_Property_List" = None):
        self.name = name
        self.type = type
        self.value = value
        self.robotmodel_Property = robotmodel_Property
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
    def robotmodel_Property(self):
        return self.__robotmodel_Property

    @robotmodel_Property.setter
    def robotmodel_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Property__robotmodel_Property", None)
        self.__robotmodel_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Property_List27"):
                opp_val = getattr(old_value, "robotmodel_Property_List27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Property_List27"):
                opp_val = getattr(value, "robotmodel_Property_List27", None)
                if opp_val is None:
                    setattr(value, "robotmodel_Property_List27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class robotmodel_Connector:

    def __init__(self, atype: str, type: str, name: str, robotmodel_Connector: "robotmodel_System" = None, robotmodel_Connector22: set["robotmodel_Role"] = None, robotmodel_Connector19: set["robotmodel_Property_List"] = None):
        self.atype = atype
        self.type = type
        self.name = name
        self.robotmodel_Connector = robotmodel_Connector
        self.robotmodel_Connector22 = robotmodel_Connector22 if robotmodel_Connector22 is not None else set()
        self.robotmodel_Connector19 = robotmodel_Connector19 if robotmodel_Connector19 is not None else set()
        
    @property
    def atype(self) -> str:
        return self.__atype

    @atype.setter
    def atype(self, atype: str):
        self.__atype = atype

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
    def robotmodel_Connector(self):
        return self.__robotmodel_Connector

    @robotmodel_Connector.setter
    def robotmodel_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Connector__robotmodel_Connector", None)
        self.__robotmodel_Connector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_System2"):
                opp_val = getattr(old_value, "robotmodel_System2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_System2"):
                opp_val = getattr(value, "robotmodel_System2", None)
                if opp_val is None:
                    setattr(value, "robotmodel_System2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Connector19(self):
        return self.__robotmodel_Connector19

    @robotmodel_Connector19.setter
    def robotmodel_Connector19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Connector__robotmodel_Connector19", None)
        self.__robotmodel_Connector19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Property_List20"):
                    opp_val = getattr(item, "robotmodel_Property_List20", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Property_List20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Property_List20"):
                    opp_val = getattr(item, "robotmodel_Property_List20", None)
                    
                    setattr(item, "robotmodel_Property_List20", self)
                    

    @property
    def robotmodel_Connector22(self):
        return self.__robotmodel_Connector22

    @robotmodel_Connector22.setter
    def robotmodel_Connector22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Connector__robotmodel_Connector22", None)
        self.__robotmodel_Connector22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Role"):
                    opp_val = getattr(item, "robotmodel_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Role"):
                    opp_val = getattr(item, "robotmodel_Role", None)
                    
                    setattr(item, "robotmodel_Role", self)
                    

class robotmodel_Component:

    def __init__(self, name: str, atype: str, type: str, depends: str, frequency: float, robotmodel_Component4: set["robotmodel_Port"] = None, robotmodel_Component6: set["robotmodel_Property_List"] = None, robotmodel_Component9: "robotmodel_Component" = None, robotmodel_Component7: set["robotmodel_Component"] = None, robotmodel_Component: "robotmodel_System" = None, robotmodel_Component11: set["robotmodel_State"] = None, robotmodel_Component13: set["robotmodel_Event"] = None, robotmodel_Component15: set["robotmodel_Transition"] = None, robotmodel_Component17: set["robotmodel_Action"] = None):
        self.name = name
        self.atype = atype
        self.type = type
        self.depends = depends
        self.frequency = frequency
        self.robotmodel_Component4 = robotmodel_Component4 if robotmodel_Component4 is not None else set()
        self.robotmodel_Component6 = robotmodel_Component6 if robotmodel_Component6 is not None else set()
        self.robotmodel_Component9 = robotmodel_Component9
        self.robotmodel_Component7 = robotmodel_Component7 if robotmodel_Component7 is not None else set()
        self.robotmodel_Component = robotmodel_Component
        self.robotmodel_Component11 = robotmodel_Component11 if robotmodel_Component11 is not None else set()
        self.robotmodel_Component13 = robotmodel_Component13 if robotmodel_Component13 is not None else set()
        self.robotmodel_Component15 = robotmodel_Component15 if robotmodel_Component15 is not None else set()
        self.robotmodel_Component17 = robotmodel_Component17 if robotmodel_Component17 is not None else set()
        
    @property
    def atype(self) -> str:
        return self.__atype

    @atype.setter
    def atype(self, atype: str):
        self.__atype = atype

    @property
    def depends(self) -> str:
        return self.__depends

    @depends.setter
    def depends(self, depends: str):
        self.__depends = depends

    @property
    def frequency(self) -> float:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: float):
        self.__frequency = frequency

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
    def robotmodel_Component17(self):
        return self.__robotmodel_Component17

    @robotmodel_Component17.setter
    def robotmodel_Component17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Component__robotmodel_Component17", None)
        self.__robotmodel_Component17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Action"):
                    opp_val = getattr(item, "robotmodel_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Action"):
                    opp_val = getattr(item, "robotmodel_Action", None)
                    
                    setattr(item, "robotmodel_Action", self)
                    

    @property
    def robotmodel_Component13(self):
        return self.__robotmodel_Component13

    @robotmodel_Component13.setter
    def robotmodel_Component13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Component__robotmodel_Component13", None)
        self.__robotmodel_Component13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Event"):
                    opp_val = getattr(item, "robotmodel_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Event"):
                    opp_val = getattr(item, "robotmodel_Event", None)
                    
                    setattr(item, "robotmodel_Event", self)
                    

    @property
    def robotmodel_Component(self):
        return self.__robotmodel_Component

    @robotmodel_Component.setter
    def robotmodel_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Component__robotmodel_Component", None)
        self.__robotmodel_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_System"):
                opp_val = getattr(old_value, "robotmodel_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_System"):
                opp_val = getattr(value, "robotmodel_System", None)
                if opp_val is None:
                    setattr(value, "robotmodel_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Component9(self):
        return self.__robotmodel_Component9

    @robotmodel_Component9.setter
    def robotmodel_Component9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Component__robotmodel_Component9", None)
        self.__robotmodel_Component9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Component7"):
                opp_val = getattr(old_value, "robotmodel_Component7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Component7"):
                opp_val = getattr(value, "robotmodel_Component7", None)
                if opp_val is None:
                    setattr(value, "robotmodel_Component7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Component15(self):
        return self.__robotmodel_Component15

    @robotmodel_Component15.setter
    def robotmodel_Component15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Component__robotmodel_Component15", None)
        self.__robotmodel_Component15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Transition"):
                    opp_val = getattr(item, "robotmodel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Transition"):
                    opp_val = getattr(item, "robotmodel_Transition", None)
                    
                    setattr(item, "robotmodel_Transition", self)
                    

    @property
    def robotmodel_Component4(self):
        return self.__robotmodel_Component4

    @robotmodel_Component4.setter
    def robotmodel_Component4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Component__robotmodel_Component4", None)
        self.__robotmodel_Component4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Port"):
                    opp_val = getattr(item, "robotmodel_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Port"):
                    opp_val = getattr(item, "robotmodel_Port", None)
                    
                    setattr(item, "robotmodel_Port", self)
                    

    @property
    def robotmodel_Component7(self):
        return self.__robotmodel_Component7

    @robotmodel_Component7.setter
    def robotmodel_Component7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Component__robotmodel_Component7", None)
        self.__robotmodel_Component7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Component9"):
                    opp_val = getattr(item, "robotmodel_Component9", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Component9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Component9"):
                    opp_val = getattr(item, "robotmodel_Component9", None)
                    
                    setattr(item, "robotmodel_Component9", self)
                    

    @property
    def robotmodel_Component6(self):
        return self.__robotmodel_Component6

    @robotmodel_Component6.setter
    def robotmodel_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Component__robotmodel_Component6", None)
        self.__robotmodel_Component6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Property_List"):
                    opp_val = getattr(item, "robotmodel_Property_List", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Property_List", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Property_List"):
                    opp_val = getattr(item, "robotmodel_Property_List", None)
                    
                    setattr(item, "robotmodel_Property_List", self)
                    

    @property
    def robotmodel_Component11(self):
        return self.__robotmodel_Component11

    @robotmodel_Component11.setter
    def robotmodel_Component11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Component__robotmodel_Component11", None)
        self.__robotmodel_Component11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_State"):
                    opp_val = getattr(item, "robotmodel_State", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_State"):
                    opp_val = getattr(item, "robotmodel_State", None)
                    
                    setattr(item, "robotmodel_State", self)
                    

class robotmodel_System:

    def __init__(self, name: str, depends: str, description: str, author_email: str, author: str, robotmodel_System: set["robotmodel_Component"] = None, robotmodel_System2: set["robotmodel_Connector"] = None):
        self.name = name
        self.depends = depends
        self.description = description
        self.author_email = author_email
        self.author = author
        self.robotmodel_System = robotmodel_System if robotmodel_System is not None else set()
        self.robotmodel_System2 = robotmodel_System2 if robotmodel_System2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def author_email(self) -> str:
        return self.__author_email

    @author_email.setter
    def author_email(self, author_email: str):
        self.__author_email = author_email

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def depends(self) -> str:
        return self.__depends

    @depends.setter
    def depends(self, depends: str):
        self.__depends = depends

    @property
    def robotmodel_System2(self):
        return self.__robotmodel_System2

    @robotmodel_System2.setter
    def robotmodel_System2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_System__robotmodel_System2", None)
        self.__robotmodel_System2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Connector"):
                    opp_val = getattr(item, "robotmodel_Connector", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Connector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Connector"):
                    opp_val = getattr(item, "robotmodel_Connector", None)
                    
                    setattr(item, "robotmodel_Connector", self)
                    

    @property
    def robotmodel_System(self):
        return self.__robotmodel_System

    @robotmodel_System.setter
    def robotmodel_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_System__robotmodel_System", None)
        self.__robotmodel_System = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Component"):
                    opp_val = getattr(item, "robotmodel_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Component"):
                    opp_val = getattr(item, "robotmodel_Component", None)
                    
                    setattr(item, "robotmodel_Component", self)
                    

class robotmodel_Property_List:

    def __init__(self, name: str, robotmodel_Property_List: "robotmodel_Component" = None, robotmodel_Property_List27: set["robotmodel_Property"] = None, robotmodel_Property_List20: "robotmodel_Connector" = None):
        self.name = name
        self.robotmodel_Property_List = robotmodel_Property_List
        self.robotmodel_Property_List27 = robotmodel_Property_List27 if robotmodel_Property_List27 is not None else set()
        self.robotmodel_Property_List20 = robotmodel_Property_List20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robotmodel_Property_List(self):
        return self.__robotmodel_Property_List

    @robotmodel_Property_List.setter
    def robotmodel_Property_List(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Property_List__robotmodel_Property_List", None)
        self.__robotmodel_Property_List = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Component6"):
                opp_val = getattr(old_value, "robotmodel_Component6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Component6"):
                opp_val = getattr(value, "robotmodel_Component6", None)
                if opp_val is None:
                    setattr(value, "robotmodel_Component6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Property_List20(self):
        return self.__robotmodel_Property_List20

    @robotmodel_Property_List20.setter
    def robotmodel_Property_List20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Property_List__robotmodel_Property_List20", None)
        self.__robotmodel_Property_List20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Connector19"):
                opp_val = getattr(old_value, "robotmodel_Connector19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Connector19"):
                opp_val = getattr(value, "robotmodel_Connector19", None)
                if opp_val is None:
                    setattr(value, "robotmodel_Connector19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotmodel_Property_List27(self):
        return self.__robotmodel_Property_List27

    @robotmodel_Property_List27.setter
    def robotmodel_Property_List27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Property_List__robotmodel_Property_List27", None)
        self.__robotmodel_Property_List27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotmodel_Property"):
                    opp_val = getattr(item, "robotmodel_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "robotmodel_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotmodel_Property"):
                    opp_val = getattr(item, "robotmodel_Property", None)
                    
                    setattr(item, "robotmodel_Property", self)
                    

class robotmodel_Port:

    def __init__(self, name: str, robotmodel_Port: "robotmodel_Component" = None, robotmodel_Port24: "robotmodel_Role" = None):
        self.name = name
        self.robotmodel_Port = robotmodel_Port
        self.robotmodel_Port24 = robotmodel_Port24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robotmodel_Port24(self):
        return self.__robotmodel_Port24

    @robotmodel_Port24.setter
    def robotmodel_Port24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Port__robotmodel_Port24", None)
        self.__robotmodel_Port24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Role25"):
                opp_val = getattr(old_value, "robotmodel_Role25", None)
                if opp_val == self:
                    setattr(old_value, "robotmodel_Role25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Role25"):
                opp_val = getattr(value, "robotmodel_Role25", None)
                setattr(value, "robotmodel_Role25", self)

    @property
    def robotmodel_Port(self):
        return self.__robotmodel_Port

    @robotmodel_Port.setter
    def robotmodel_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotmodel_Port__robotmodel_Port", None)
        self.__robotmodel_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotmodel_Component4"):
                opp_val = getattr(old_value, "robotmodel_Component4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotmodel_Component4"):
                opp_val = getattr(value, "robotmodel_Component4", None)
                if opp_val is None:
                    setattr(value, "robotmodel_Component4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
