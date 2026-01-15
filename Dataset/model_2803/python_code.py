from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class vulnerabilityType(Enum):
    Timing = "Timing"
    Isolation = "Isolation"
    ResourceAllocation = "ResourceAllocation"
    Exposure = "Exposure"
    Authentication = "Authentication"
    Concurrency = "Concurrency"
class propagationType(Enum):
    bus = "bus"
    dataFlow = "dataFlow"
    local = "local"
    memory = "memory"
    processor = "processor"
    data = "data"


############################################
# Definition of Classes
############################################

class attacktree_Model:

    def __init__(self, name: str, description: str, attacktree_Model: "attacktree_Node" = None):
        self.name = name
        self.description = description
        self.attacktree_Model = attacktree_Model
        
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
    def attacktree_Model(self):
        return self.__attacktree_Model

    @attacktree_Model.setter
    def attacktree_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attacktree_Model__attacktree_Model", None)
        self.__attacktree_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attacktree_Node7"):
                opp_val = getattr(old_value, "attacktree_Node7", None)
                if opp_val == self:
                    setattr(old_value, "attacktree_Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attacktree_Node7"):
                opp_val = getattr(value, "attacktree_Node7", None)
                setattr(value, "attacktree_Node7", self)

class attacktree_EObject:

    pass
class attacktree_Vulnerability:

    def __init__(self, name: str, description: str, type: str, tags: str, severity: int, attacktree_Vulnerability: "attacktree_Node" = None):
        self.name = name
        self.description = description
        self.type = type
        self.tags = tags
        self.severity = severity
        self.attacktree_Vulnerability = attacktree_Vulnerability
        
    @property
    def severity(self) -> int:
        return self.__severity

    @severity.setter
    def severity(self, severity: int):
        self.__severity = severity

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tags(self) -> str:
        return self.__tags

    @tags.setter
    def tags(self, tags: str):
        self.__tags = tags

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def attacktree_Vulnerability(self):
        return self.__attacktree_Vulnerability

    @attacktree_Vulnerability.setter
    def attacktree_Vulnerability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attacktree_Vulnerability__attacktree_Vulnerability", None)
        self.__attacktree_Vulnerability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attacktree_Node"):
                opp_val = getattr(old_value, "attacktree_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attacktree_Node"):
                opp_val = getattr(value, "attacktree_Node", None)
                if opp_val is None:
                    setattr(value, "attacktree_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class attacktree_Node:

    def __init__(self, name: str, description: str, tags: str, domains: str, attacktree_Node: set["attacktree_Vulnerability"] = None, attacktree_Node3: "attacktree_Node" = None, attacktree_Node1: set["attacktree_Node"] = None, attacktree_Node5: "attacktree_EObject" = None, attacktree_Node7: "attacktree_Model" = None):
        self.name = name
        self.description = description
        self.tags = tags
        self.domains = domains
        self.attacktree_Node = attacktree_Node if attacktree_Node is not None else set()
        self.attacktree_Node3 = attacktree_Node3
        self.attacktree_Node1 = attacktree_Node1 if attacktree_Node1 is not None else set()
        self.attacktree_Node5 = attacktree_Node5
        self.attacktree_Node7 = attacktree_Node7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domains(self) -> str:
        return self.__domains

    @domains.setter
    def domains(self, domains: str):
        self.__domains = domains

    @property
    def tags(self) -> str:
        return self.__tags

    @tags.setter
    def tags(self, tags: str):
        self.__tags = tags

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def attacktree_Node1(self):
        return self.__attacktree_Node1

    @attacktree_Node1.setter
    def attacktree_Node1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attacktree_Node__attacktree_Node1", None)
        self.__attacktree_Node1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attacktree_Node3"):
                    opp_val = getattr(item, "attacktree_Node3", None)
                    
                    if opp_val == self:
                        setattr(item, "attacktree_Node3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attacktree_Node3"):
                    opp_val = getattr(item, "attacktree_Node3", None)
                    
                    setattr(item, "attacktree_Node3", self)
                    

    @property
    def attacktree_Node3(self):
        return self.__attacktree_Node3

    @attacktree_Node3.setter
    def attacktree_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attacktree_Node__attacktree_Node3", None)
        self.__attacktree_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attacktree_Node1"):
                opp_val = getattr(old_value, "attacktree_Node1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attacktree_Node1"):
                opp_val = getattr(value, "attacktree_Node1", None)
                if opp_val is None:
                    setattr(value, "attacktree_Node1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attacktree_Node7(self):
        return self.__attacktree_Node7

    @attacktree_Node7.setter
    def attacktree_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attacktree_Node__attacktree_Node7", None)
        self.__attacktree_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attacktree_Model"):
                opp_val = getattr(old_value, "attacktree_Model", None)
                if opp_val == self:
                    setattr(old_value, "attacktree_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attacktree_Model"):
                opp_val = getattr(value, "attacktree_Model", None)
                setattr(value, "attacktree_Model", self)

    @property
    def attacktree_Node(self):
        return self.__attacktree_Node

    @attacktree_Node.setter
    def attacktree_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attacktree_Node__attacktree_Node", None)
        self.__attacktree_Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attacktree_Vulnerability"):
                    opp_val = getattr(item, "attacktree_Vulnerability", None)
                    
                    if opp_val == self:
                        setattr(item, "attacktree_Vulnerability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attacktree_Vulnerability"):
                    opp_val = getattr(item, "attacktree_Vulnerability", None)
                    
                    setattr(item, "attacktree_Vulnerability", self)
                    

    @property
    def attacktree_Node5(self):
        return self.__attacktree_Node5

    @attacktree_Node5.setter
    def attacktree_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attacktree_Node__attacktree_Node5", None)
        self.__attacktree_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attacktree_EObject"):
                opp_val = getattr(old_value, "attacktree_EObject", None)
                if opp_val == self:
                    setattr(old_value, "attacktree_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attacktree_EObject"):
                opp_val = getattr(value, "attacktree_EObject", None)
                setattr(value, "attacktree_EObject", self)
