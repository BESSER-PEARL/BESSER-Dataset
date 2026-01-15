from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Comparation(Enum):
    Equal = "Equal"
    NotEqual = "NotEqual"
    Less = "Less"
    Greater = "Greater"
class Protocol(Enum):
    Paho = "Paho"
    Akka = "Akka"


############################################
# Definition of Classes
############################################

class dataflownet_Token:

    def __init__(self, value: str, dataflownet_Token: "dataflownet_FiringRule" = None, dataflownet_Token38: "dataflownet_Type" = None):
        self.value = value
        self.dataflownet_Token = dataflownet_Token
        self.dataflownet_Token38 = dataflownet_Token38
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def dataflownet_Token(self):
        return self.__dataflownet_Token

    @dataflownet_Token.setter
    def dataflownet_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_Token__dataflownet_Token", None)
        self.__dataflownet_Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflownet_FiringRule36"):
                opp_val = getattr(old_value, "dataflownet_FiringRule36", None)
                if opp_val == self:
                    setattr(old_value, "dataflownet_FiringRule36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflownet_FiringRule36"):
                opp_val = getattr(value, "dataflownet_FiringRule36", None)
                setattr(value, "dataflownet_FiringRule36", self)

    @property
    def dataflownet_Token38(self):
        return self.__dataflownet_Token38

    @dataflownet_Token38.setter
    def dataflownet_Token38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_Token__dataflownet_Token38", None)
        self.__dataflownet_Token38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflownet_Type39"):
                opp_val = getattr(old_value, "dataflownet_Type39", None)
                if opp_val == self:
                    setattr(old_value, "dataflownet_Type39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflownet_Type39"):
                opp_val = getattr(value, "dataflownet_Type39", None)
                setattr(value, "dataflownet_Type39", self)

class dataflownet_Type:

    pass
class NamedElement:

    pass
class dataflownet_Process(NamedElement):

    def __init__(self, host: str, dataflownet_Process: "dataflownet_DataflowNet" = None, dataflownet_Process50: "dataflownet_DataflowSystem" = None):
        self.host = host
        self.dataflownet_Process = dataflownet_Process
        self.dataflownet_Process50 = dataflownet_Process50
        
    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def host(self, host: str):
        self.__host = host

    @property
    def dataflownet_Process50(self):
        return self.__dataflownet_Process50

    @dataflownet_Process50.setter
    def dataflownet_Process50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_Process__dataflownet_Process50", None)
        self.__dataflownet_Process50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflownet_DataflowSystem49"):
                opp_val = getattr(old_value, "dataflownet_DataflowSystem49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflownet_DataflowSystem49"):
                opp_val = getattr(value, "dataflownet_DataflowSystem49", None)
                if opp_val is None:
                    setattr(value, "dataflownet_DataflowSystem49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflownet_Process(self):
        return self.__dataflownet_Process

    @dataflownet_Process.setter
    def dataflownet_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_Process__dataflownet_Process", None)
        self.__dataflownet_Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflownet_DataflowNet15"):
                opp_val = getattr(old_value, "dataflownet_DataflowNet15", None)
                if opp_val == self:
                    setattr(old_value, "dataflownet_DataflowNet15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflownet_DataflowNet15"):
                opp_val = getattr(value, "dataflownet_DataflowNet15", None)
                setattr(value, "dataflownet_DataflowNet15", self)

class dataflownet_DataflowSystem(NamedElement):

    def __init__(self, protocol: str, dataflownet_DataflowSystem43: set["dataflownet_DataflowNet"] = None, dataflownet_DataflowSystem46: set["dataflownet_Channel"] = None, dataflownet_DataflowSystem49: set["dataflownet_Process"] = None, dataflownet_DataflowSystem: set["dataflownet_Type"] = None):
        self.protocol = protocol
        self.dataflownet_DataflowSystem43 = dataflownet_DataflowSystem43 if dataflownet_DataflowSystem43 is not None else set()
        self.dataflownet_DataflowSystem46 = dataflownet_DataflowSystem46 if dataflownet_DataflowSystem46 is not None else set()
        self.dataflownet_DataflowSystem49 = dataflownet_DataflowSystem49 if dataflownet_DataflowSystem49 is not None else set()
        self.dataflownet_DataflowSystem = dataflownet_DataflowSystem if dataflownet_DataflowSystem is not None else set()
        
    @property
    def protocol(self) -> str:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol

    @property
    def dataflownet_DataflowSystem46(self):
        return self.__dataflownet_DataflowSystem46

    @dataflownet_DataflowSystem46.setter
    def dataflownet_DataflowSystem46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_DataflowSystem__dataflownet_DataflowSystem46", None)
        self.__dataflownet_DataflowSystem46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflownet_Channel47"):
                    opp_val = getattr(item, "dataflownet_Channel47", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflownet_Channel47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflownet_Channel47"):
                    opp_val = getattr(item, "dataflownet_Channel47", None)
                    
                    setattr(item, "dataflownet_Channel47", self)
                    

    @property
    def dataflownet_DataflowSystem49(self):
        return self.__dataflownet_DataflowSystem49

    @dataflownet_DataflowSystem49.setter
    def dataflownet_DataflowSystem49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_DataflowSystem__dataflownet_DataflowSystem49", None)
        self.__dataflownet_DataflowSystem49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflownet_Process50"):
                    opp_val = getattr(item, "dataflownet_Process50", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflownet_Process50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflownet_Process50"):
                    opp_val = getattr(item, "dataflownet_Process50", None)
                    
                    setattr(item, "dataflownet_Process50", self)
                    

    @property
    def dataflownet_DataflowSystem43(self):
        return self.__dataflownet_DataflowSystem43

    @dataflownet_DataflowSystem43.setter
    def dataflownet_DataflowSystem43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_DataflowSystem__dataflownet_DataflowSystem43", None)
        self.__dataflownet_DataflowSystem43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflownet_DataflowNet44"):
                    opp_val = getattr(item, "dataflownet_DataflowNet44", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflownet_DataflowNet44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflownet_DataflowNet44"):
                    opp_val = getattr(item, "dataflownet_DataflowNet44", None)
                    
                    setattr(item, "dataflownet_DataflowNet44", self)
                    

    @property
    def dataflownet_DataflowSystem(self):
        return self.__dataflownet_DataflowSystem

    @dataflownet_DataflowSystem.setter
    def dataflownet_DataflowSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_DataflowSystem__dataflownet_DataflowSystem", None)
        self.__dataflownet_DataflowSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflownet_Type41"):
                    opp_val = getattr(item, "dataflownet_Type41", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflownet_Type41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflownet_Type41"):
                    opp_val = getattr(item, "dataflownet_Type41", None)
                    
                    setattr(item, "dataflownet_Type41", self)
                    

class dataflownet_StateMachineTransition(NamedElement):

    def __init__(self, priority: int, StateMachineTransition: "dataflownet_StateMachineState" = None, StateMachineTransition18: "dataflownet_StateMachineState" = None, dataflownet_StateMachineTransition28: set["dataflownet_FiringRule"] = None, outputTransitions: "dataflownet_StateMachineState" = None, inputTransitions: "dataflownet_StateMachineState" = None, dataflownet_StateMachineTransition: set["dataflownet_FiringRule"] = None):
        self.priority = priority
        self.StateMachineTransition = StateMachineTransition
        self.StateMachineTransition18 = StateMachineTransition18
        self.dataflownet_StateMachineTransition28 = dataflownet_StateMachineTransition28 if dataflownet_StateMachineTransition28 is not None else set()
        self.outputTransitions = outputTransitions
        self.inputTransitions = inputTransitions
        self.dataflownet_StateMachineTransition = dataflownet_StateMachineTransition if dataflownet_StateMachineTransition is not None else set()
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def outputTransitions(self):
        return self.__outputTransitions

    @outputTransitions.setter
    def outputTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_StateMachineTransition__outputTransitions", None)
        self.__outputTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineState22"):
                opp_val = getattr(old_value, "StateMachineState22", None)
                if opp_val == self:
                    setattr(old_value, "StateMachineState22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineState22"):
                opp_val = getattr(value, "StateMachineState22", None)
                setattr(value, "StateMachineState22", self)

    @property
    def inputTransitions(self):
        return self.__inputTransitions

    @inputTransitions.setter
    def inputTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_StateMachineTransition__inputTransitions", None)
        self.__inputTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineState24"):
                opp_val = getattr(old_value, "StateMachineState24", None)
                if opp_val == self:
                    setattr(old_value, "StateMachineState24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineState24"):
                opp_val = getattr(value, "StateMachineState24", None)
                setattr(value, "StateMachineState24", self)

    @property
    def StateMachineTransition(self):
        return self.__StateMachineTransition

    @StateMachineTransition.setter
    def StateMachineTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_StateMachineTransition__StateMachineTransition", None)
        self.__StateMachineTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fromState"):
                opp_val = getattr(old_value, "fromState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fromState"):
                opp_val = getattr(value, "fromState", None)
                if opp_val is None:
                    setattr(value, "fromState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflownet_StateMachineTransition28(self):
        return self.__dataflownet_StateMachineTransition28

    @dataflownet_StateMachineTransition28.setter
    def dataflownet_StateMachineTransition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_StateMachineTransition__dataflownet_StateMachineTransition28", None)
        self.__dataflownet_StateMachineTransition28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflownet_FiringRule29"):
                    opp_val = getattr(item, "dataflownet_FiringRule29", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflownet_FiringRule29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflownet_FiringRule29"):
                    opp_val = getattr(item, "dataflownet_FiringRule29", None)
                    
                    setattr(item, "dataflownet_FiringRule29", self)
                    

    @property
    def dataflownet_StateMachineTransition(self):
        return self.__dataflownet_StateMachineTransition

    @dataflownet_StateMachineTransition.setter
    def dataflownet_StateMachineTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_StateMachineTransition__dataflownet_StateMachineTransition", None)
        self.__dataflownet_StateMachineTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataflownet_FiringRule26"):
                    opp_val = getattr(item, "dataflownet_FiringRule26", None)
                    
                    if opp_val == self:
                        setattr(item, "dataflownet_FiringRule26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataflownet_FiringRule26"):
                    opp_val = getattr(item, "dataflownet_FiringRule26", None)
                    
                    setattr(item, "dataflownet_FiringRule26", self)
                    

    @property
    def StateMachineTransition18(self):
        return self.__StateMachineTransition18

    @StateMachineTransition18.setter
    def StateMachineTransition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_StateMachineTransition__StateMachineTransition18", None)
        self.__StateMachineTransition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toState"):
                opp_val = getattr(old_value, "toState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toState"):
                opp_val = getattr(value, "toState", None)
                if opp_val is None:
                    setattr(value, "toState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dataflownet_Node(NamedElement):

    pass
class dataflownet_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class dataflownet_Channel(NamedElement):

    pass
class dataflownet_FiringRule(NamedElement):

    def __init__(self, compType: str, dataflownet_FiringRule: "dataflownet_StateMachine" = None, dataflownet_FiringRule29: "dataflownet_StateMachineTransition" = None, dataflownet_FiringRule33: "dataflownet_Channel" = None, dataflownet_FiringRule36: "dataflownet_Token" = None, dataflownet_FiringRule26: "dataflownet_StateMachineTransition" = None):
        self.compType = compType
        self.dataflownet_FiringRule = dataflownet_FiringRule
        self.dataflownet_FiringRule29 = dataflownet_FiringRule29
        self.dataflownet_FiringRule33 = dataflownet_FiringRule33
        self.dataflownet_FiringRule36 = dataflownet_FiringRule36
        self.dataflownet_FiringRule26 = dataflownet_FiringRule26
        
    @property
    def compType(self) -> str:
        return self.__compType

    @compType.setter
    def compType(self, compType: str):
        self.__compType = compType

    @property
    def dataflownet_FiringRule29(self):
        return self.__dataflownet_FiringRule29

    @dataflownet_FiringRule29.setter
    def dataflownet_FiringRule29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_FiringRule__dataflownet_FiringRule29", None)
        self.__dataflownet_FiringRule29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflownet_StateMachineTransition28"):
                opp_val = getattr(old_value, "dataflownet_StateMachineTransition28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflownet_StateMachineTransition28"):
                opp_val = getattr(value, "dataflownet_StateMachineTransition28", None)
                if opp_val is None:
                    setattr(value, "dataflownet_StateMachineTransition28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflownet_FiringRule36(self):
        return self.__dataflownet_FiringRule36

    @dataflownet_FiringRule36.setter
    def dataflownet_FiringRule36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_FiringRule__dataflownet_FiringRule36", None)
        self.__dataflownet_FiringRule36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflownet_Token"):
                opp_val = getattr(old_value, "dataflownet_Token", None)
                if opp_val == self:
                    setattr(old_value, "dataflownet_Token", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflownet_Token"):
                opp_val = getattr(value, "dataflownet_Token", None)
                setattr(value, "dataflownet_Token", self)

    @property
    def dataflownet_FiringRule26(self):
        return self.__dataflownet_FiringRule26

    @dataflownet_FiringRule26.setter
    def dataflownet_FiringRule26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_FiringRule__dataflownet_FiringRule26", None)
        self.__dataflownet_FiringRule26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflownet_StateMachineTransition"):
                opp_val = getattr(old_value, "dataflownet_StateMachineTransition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflownet_StateMachineTransition"):
                opp_val = getattr(value, "dataflownet_StateMachineTransition", None)
                if opp_val is None:
                    setattr(value, "dataflownet_StateMachineTransition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataflownet_FiringRule33(self):
        return self.__dataflownet_FiringRule33

    @dataflownet_FiringRule33.setter
    def dataflownet_FiringRule33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_FiringRule__dataflownet_FiringRule33", None)
        self.__dataflownet_FiringRule33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflownet_Channel34"):
                opp_val = getattr(old_value, "dataflownet_Channel34", None)
                if opp_val == self:
                    setattr(old_value, "dataflownet_Channel34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflownet_Channel34"):
                opp_val = getattr(value, "dataflownet_Channel34", None)
                setattr(value, "dataflownet_Channel34", self)

    @property
    def dataflownet_FiringRule(self):
        return self.__dataflownet_FiringRule

    @dataflownet_FiringRule.setter
    def dataflownet_FiringRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dataflownet_FiringRule__dataflownet_FiringRule", None)
        self.__dataflownet_FiringRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataflownet_StateMachine4"):
                opp_val = getattr(old_value, "dataflownet_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataflownet_StateMachine4"):
                opp_val = getattr(value, "dataflownet_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "dataflownet_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dataflownet_StateMachineState(NamedElement):

    pass
class Node:

    pass
class dataflownet_DataflowNet(Node):

    pass
class dataflownet_StateMachine(Node):

    pass