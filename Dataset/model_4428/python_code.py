from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Condition:

    pass
class farrusco_Distancia(Condition):

    def __init__(self, how_sucess: bool, distancia: int):
        self.how_sucess = how_sucess
        self.distancia = distancia
        
        pass
    @property
    def how_sucess(self):
        return self.__how_sucess

    @how_sucess.setter
    def how_sucess(self, how_sucess: bool):
        self.__how_sucess = how_sucess


    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, distancia: int):
        self.__distancia = distancia


class Action:

    pass
class farrusco_Condition(Action):

    pass
class Actuate:

    pass
class farrusco_Servo(Actuate):

    def __init__(self, max: int, inc: int, min: int):
        self.max = max
        self.inc = inc
        self.min = min
        
        pass
    @property
    def inc(self):
        return self.__inc

    @inc.setter
    def inc(self, inc: int):
        self.__inc = inc


    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max


    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min


class farrusco_LED(Actuate):

    def __init__(self, on_off: bool):
        self.on_off = on_off
        
        pass
    @property
    def on_off(self):
        return self.__on_off

    @on_off.setter
    def on_off(self, on_off: bool):
        self.__on_off = on_off


class farrusco_Motor(Actuate):

    def __init__(self, MotorLeft: int, MotorRight: int):
        self.MotorLeft = MotorLeft
        self.MotorRight = MotorRight
        
        pass
    @property
    def MotorLeft(self):
        return self.__MotorLeft

    @MotorLeft.setter
    def MotorLeft(self, MotorLeft: int):
        self.__MotorLeft = MotorLeft


    @property
    def MotorRight(self):
        return self.__MotorRight

    @MotorRight.setter
    def MotorRight(self, MotorRight: int):
        self.__MotorRight = MotorRight


class farrusco_Actuate(Action):

    pass
class farrusco_Espera(Condition):

    def __init__(self, time: int):
        self.time = time
        
        pass
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time


class farrusco_BumperEsquerdo(Condition):

    pass
class farrusco_BumperDireito(Condition):

    pass
class Behavior:

    pass
class farrusco_Paralelo(Behavior):

    pass
class farrusco_Prioridade(Behavior):

    pass
class farrusco_AlterarEstado(Behavior):

    def __init__(self, succ_policy: int, fail_policy: int, runn_policy: int):
        self.succ_policy = succ_policy
        self.fail_policy = fail_policy
        self.runn_policy = runn_policy
        
        pass
    @property
    def fail_policy(self):
        return self.__fail_policy

    @fail_policy.setter
    def fail_policy(self, fail_policy: int):
        self.__fail_policy = fail_policy


    @property
    def succ_policy(self):
        return self.__succ_policy

    @succ_policy.setter
    def succ_policy(self, succ_policy: int):
        self.__succ_policy = succ_policy


    @property
    def runn_policy(self):
        return self.__runn_policy

    @runn_policy.setter
    def runn_policy(self, runn_policy: int):
        self.__runn_policy = runn_policy


class Node:

    pass
class farrusco_Behavior(Node):

    def __init__(self, Name: str, farrusco_Behavior: "farrusco_Filho" = None):
        self.Name = Name
        self.farrusco_Behavior = farrusco_Behavior
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


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
            if hasattr(old_value, "farrusco_Filho6"):
                opp_val = getattr(old_value, "farrusco_Filho6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "farrusco_Filho6"):
                opp_val = getattr(value, "farrusco_Filho6", None)
                if opp_val is None:
                    setattr(value, "farrusco_Filho6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class farrusco_Action(Node):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class farrusco_Robot:

    def __init__(self, Name: str, farrusco_Robot: set["farrusco_Node"] = None, farrusco_Robot2: set["farrusco_Filho"] = None, farrusco_Robot4: set["farrusco_Irmao"] = None):
        self.Name = Name
        self.farrusco_Robot = farrusco_Robot if farrusco_Robot is not None else set()
        self.farrusco_Robot2 = farrusco_Robot2 if farrusco_Robot2 is not None else set()
        self.farrusco_Robot4 = farrusco_Robot4 if farrusco_Robot4 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


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
                if hasattr(item, "farrusco_Filho"):
                    opp_val = getattr(item, "farrusco_Filho", None)
                    
                    if opp_val == self:
                        setattr(item, "farrusco_Filho", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farrusco_Filho"):
                    opp_val = getattr(item, "farrusco_Filho", None)
                    
                    setattr(item, "farrusco_Filho", self)
                    

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
                if hasattr(item, "farrusco_Irmao"):
                    opp_val = getattr(item, "farrusco_Irmao", None)
                    
                    if opp_val == self:
                        setattr(item, "farrusco_Irmao", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farrusco_Irmao"):
                    opp_val = getattr(item, "farrusco_Irmao", None)
                    
                    setattr(item, "farrusco_Irmao", self)
                    

class farrusco_Irmao:

    pass
class farrusco_Filho:

    pass
class farrusco_Node:

    pass