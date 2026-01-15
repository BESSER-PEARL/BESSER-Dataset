from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Actuate:

    pass
class farrusco_Motors(Actuate):

    def __init__(self, MotorLeft: int, MotorRight: int):
        self.MotorLeft = MotorLeft
        self.MotorRight = MotorRight
        
    @property
    def MotorRight(self) -> int:
        return self.__MotorRight

    @MotorRight.setter
    def MotorRight(self, MotorRight: int):
        self.__MotorRight = MotorRight

    @property
    def MotorLeft(self) -> int:
        return self.__MotorLeft

    @MotorLeft.setter
    def MotorLeft(self, MotorLeft: int):
        self.__MotorLeft = MotorLeft

class Condition:

    pass
class farrusco_Wait(Condition):

    def __init__(self, time: int):
        self.time = time
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

class farrusco_LeftBumper(Condition):

    pass
class farrusco_RightBumper(Condition):

    pass
class farrusco_IRdist(Condition):

    def __init__(self, distancia: int, how_sucess: bool):
        self.distancia = distancia
        self.how_sucess = how_sucess
        
    @property
    def how_sucess(self) -> bool:
        return self.__how_sucess

    @how_sucess.setter
    def how_sucess(self, how_sucess: bool):
        self.__how_sucess = how_sucess

    @property
    def distancia(self) -> int:
        return self.__distancia

    @distancia.setter
    def distancia(self, distancia: int):
        self.__distancia = distancia

class Action:

    pass
class farrusco_Actuate(Action):

    pass
class farrusco_Condition(Action):

    pass
class farrusco_LED(Actuate):

    def __init__(self, on_off: bool):
        self.on_off = on_off
        
    @property
    def on_off(self) -> bool:
        return self.__on_off

    @on_off.setter
    def on_off(self, on_off: bool):
        self.__on_off = on_off

class farrusco_ServoRange(Actuate):

    def __init__(self, min: int, max: int, inc: int):
        self.min = min
        self.max = max
        self.inc = inc
        
    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def inc(self) -> int:
        return self.__inc

    @inc.setter
    def inc(self, inc: int):
        self.__inc = inc

class Behavior:

    pass
class farrusco_Paralell(Behavior):

    pass
class farrusco_Prior(Behavior):

    pass
class Node:

    pass
class farrusco_Action(Node):

    def __init__(self, name: str, farrusco_Action: "farrusco_ActionChild" = None):
        self.name = name
        self.farrusco_Action = farrusco_Action
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def farrusco_Action(self):
        return self.__farrusco_Action

    @farrusco_Action.setter
    def farrusco_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Action__farrusco_Action", None)
        self.__farrusco_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "farrusco_ActionChild22"):
                opp_val = getattr(old_value, "farrusco_ActionChild22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "farrusco_ActionChild22"):
                opp_val = getattr(value, "farrusco_ActionChild22", None)
                if opp_val is None:
                    setattr(value, "farrusco_ActionChild22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class farrusco_StateOverride(Behavior):

    def __init__(self, succ_policy: int, fail_policy: int, runn_policy: int):
        self.succ_policy = succ_policy
        self.fail_policy = fail_policy
        self.runn_policy = runn_policy
        
    @property
    def succ_policy(self) -> int:
        return self.__succ_policy

    @succ_policy.setter
    def succ_policy(self, succ_policy: int):
        self.__succ_policy = succ_policy

    @property
    def fail_policy(self) -> int:
        return self.__fail_policy

    @fail_policy.setter
    def fail_policy(self, fail_policy: int):
        self.__fail_policy = fail_policy

    @property
    def runn_policy(self) -> int:
        return self.__runn_policy

    @runn_policy.setter
    def runn_policy(self, runn_policy: int):
        self.__runn_policy = runn_policy

class farrusco_Sequential(Behavior):

    pass
class farrusco_Child:

    pass
class farrusco_ActionChild:

    pass
class farrusco_Node:

    pass
class farrusco_Robot:

    def __init__(self, Name: str, farrusco_Robot4: set["farrusco_Child"] = None, farrusco_Robot6: set["farrusco_Next"] = None, farrusco_Robot: set["farrusco_Node"] = None, farrusco_Robot2: set["farrusco_ActionChild"] = None):
        self.Name = Name
        self.farrusco_Robot4 = farrusco_Robot4 if farrusco_Robot4 is not None else set()
        self.farrusco_Robot6 = farrusco_Robot6 if farrusco_Robot6 is not None else set()
        self.farrusco_Robot = farrusco_Robot if farrusco_Robot is not None else set()
        self.farrusco_Robot2 = farrusco_Robot2 if farrusco_Robot2 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def farrusco_Robot4(self):
        return self.__farrusco_Robot4

    @farrusco_Robot4.setter
    def farrusco_Robot4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Robot__farrusco_Robot4", None)
        self.__farrusco_Robot4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "farrusco_Child"):
                    opp_val = getattr(item, "farrusco_Child", None)
                    
                    if opp_val == self:
                        setattr(item, "farrusco_Child", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farrusco_Child"):
                    opp_val = getattr(item, "farrusco_Child", None)
                    
                    setattr(item, "farrusco_Child", self)
                    

    @property
    def farrusco_Robot2(self):
        return self.__farrusco_Robot2

    @farrusco_Robot2.setter
    def farrusco_Robot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Robot__farrusco_Robot2", None)
        self.__farrusco_Robot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "farrusco_ActionChild"):
                    opp_val = getattr(item, "farrusco_ActionChild", None)
                    
                    if opp_val == self:
                        setattr(item, "farrusco_ActionChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farrusco_ActionChild"):
                    opp_val = getattr(item, "farrusco_ActionChild", None)
                    
                    setattr(item, "farrusco_ActionChild", self)
                    

    @property
    def farrusco_Robot6(self):
        return self.__farrusco_Robot6

    @farrusco_Robot6.setter
    def farrusco_Robot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Robot__farrusco_Robot6", None)
        self.__farrusco_Robot6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "farrusco_Next"):
                    opp_val = getattr(item, "farrusco_Next", None)
                    
                    if opp_val == self:
                        setattr(item, "farrusco_Next", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farrusco_Next"):
                    opp_val = getattr(item, "farrusco_Next", None)
                    
                    setattr(item, "farrusco_Next", self)
                    

    @property
    def farrusco_Robot(self):
        return self.__farrusco_Robot

    @farrusco_Robot.setter
    def farrusco_Robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Robot__farrusco_Robot", None)
        self.__farrusco_Robot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "farrusco_Node"):
                    opp_val = getattr(item, "farrusco_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "farrusco_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farrusco_Node"):
                    opp_val = getattr(item, "farrusco_Node", None)
                    
                    setattr(item, "farrusco_Node", self)
                    

class farrusco_Behavior(Node):

    def __init__(self, Name: str, farrusco_Behavior: "farrusco_Child" = None, farrusco_Behavior11: "farrusco_Child" = None, farrusco_Behavior20: "farrusco_ActionChild" = None):
        self.Name = Name
        self.farrusco_Behavior = farrusco_Behavior
        self.farrusco_Behavior11 = farrusco_Behavior11
        self.farrusco_Behavior20 = farrusco_Behavior20
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def farrusco_Behavior11(self):
        return self.__farrusco_Behavior11

    @farrusco_Behavior11.setter
    def farrusco_Behavior11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Behavior__farrusco_Behavior11", None)
        self.__farrusco_Behavior11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "farrusco_Child10"):
                opp_val = getattr(old_value, "farrusco_Child10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "farrusco_Child10"):
                opp_val = getattr(value, "farrusco_Child10", None)
                if opp_val is None:
                    setattr(value, "farrusco_Child10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def farrusco_Behavior20(self):
        return self.__farrusco_Behavior20

    @farrusco_Behavior20.setter
    def farrusco_Behavior20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Behavior__farrusco_Behavior20", None)
        self.__farrusco_Behavior20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "farrusco_ActionChild19"):
                opp_val = getattr(old_value, "farrusco_ActionChild19", None)
                if opp_val == self:
                    setattr(old_value, "farrusco_ActionChild19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "farrusco_ActionChild19"):
                opp_val = getattr(value, "farrusco_ActionChild19", None)
                setattr(value, "farrusco_ActionChild19", self)

    @property
    def farrusco_Behavior(self):
        return self.__farrusco_Behavior

    @farrusco_Behavior.setter
    def farrusco_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farrusco_Behavior__farrusco_Behavior", None)
        self.__farrusco_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "farrusco_Child8"):
                opp_val = getattr(old_value, "farrusco_Child8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "farrusco_Child8"):
                opp_val = getattr(value, "farrusco_Child8", None)
                if opp_val is None:
                    setattr(value, "farrusco_Child8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class farrusco_Next:

    pass