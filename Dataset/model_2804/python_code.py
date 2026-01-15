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

class attackimpact_Model:

    def __init__(self, name: str, description: str, attackimpact_Model: set["attackimpact_Node"] = None):
        self.name = name
        self.description = description
        self.attackimpact_Model = attackimpact_Model if attackimpact_Model is not None else set()
        
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
    def attackimpact_Model(self):
        return self.__attackimpact_Model

    @attackimpact_Model.setter
    def attackimpact_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Model__attackimpact_Model", None)
        self.__attackimpact_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attackimpact_Node12"):
                    opp_val = getattr(item, "attackimpact_Node12", None)
                    
                    if opp_val == self:
                        setattr(item, "attackimpact_Node12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attackimpact_Node12"):
                    opp_val = getattr(item, "attackimpact_Node12", None)
                    
                    setattr(item, "attackimpact_Node12", self)
                    

class attackimpact_Propagation:

    def __init__(self, tags: str, type: str, severity: int, attackimpact_Propagation: "attackimpact_Node" = None, attackimpact_Propagation7: "attackimpact_Vulnerability" = None, attackimpact_Propagation9: set["attackimpact_Node"] = None):
        self.tags = tags
        self.type = type
        self.severity = severity
        self.attackimpact_Propagation = attackimpact_Propagation
        self.attackimpact_Propagation7 = attackimpact_Propagation7
        self.attackimpact_Propagation9 = attackimpact_Propagation9 if attackimpact_Propagation9 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def severity(self) -> int:
        return self.__severity

    @severity.setter
    def severity(self, severity: int):
        self.__severity = severity

    @property
    def tags(self) -> str:
        return self.__tags

    @tags.setter
    def tags(self, tags: str):
        self.__tags = tags

    @property
    def attackimpact_Propagation(self):
        return self.__attackimpact_Propagation

    @attackimpact_Propagation.setter
    def attackimpact_Propagation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Propagation__attackimpact_Propagation", None)
        self.__attackimpact_Propagation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attackimpact_Node2"):
                opp_val = getattr(old_value, "attackimpact_Node2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attackimpact_Node2"):
                opp_val = getattr(value, "attackimpact_Node2", None)
                if opp_val is None:
                    setattr(value, "attackimpact_Node2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attackimpact_Propagation9(self):
        return self.__attackimpact_Propagation9

    @attackimpact_Propagation9.setter
    def attackimpact_Propagation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Propagation__attackimpact_Propagation9", None)
        self.__attackimpact_Propagation9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attackimpact_Node10"):
                    opp_val = getattr(item, "attackimpact_Node10", None)
                    
                    if opp_val == self:
                        setattr(item, "attackimpact_Node10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attackimpact_Node10"):
                    opp_val = getattr(item, "attackimpact_Node10", None)
                    
                    setattr(item, "attackimpact_Node10", self)
                    

    @property
    def attackimpact_Propagation7(self):
        return self.__attackimpact_Propagation7

    @attackimpact_Propagation7.setter
    def attackimpact_Propagation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Propagation__attackimpact_Propagation7", None)
        self.__attackimpact_Propagation7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attackimpact_Vulnerability6"):
                opp_val = getattr(old_value, "attackimpact_Vulnerability6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attackimpact_Vulnerability6"):
                opp_val = getattr(value, "attackimpact_Vulnerability6", None)
                if opp_val is None:
                    setattr(value, "attackimpact_Vulnerability6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class attackimpact_Vulnerability:

    def __init__(self, name: str, description: str, type: str, tags: str, severity: int, attackimpact_Vulnerability: "attackimpact_Node" = None, attackimpact_Vulnerability6: set["attackimpact_Propagation"] = None):
        self.name = name
        self.description = description
        self.type = type
        self.tags = tags
        self.severity = severity
        self.attackimpact_Vulnerability = attackimpact_Vulnerability
        self.attackimpact_Vulnerability6 = attackimpact_Vulnerability6 if attackimpact_Vulnerability6 is not None else set()
        
    @property
    def severity(self) -> int:
        return self.__severity

    @severity.setter
    def severity(self, severity: int):
        self.__severity = severity

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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def attackimpact_Vulnerability(self):
        return self.__attackimpact_Vulnerability

    @attackimpact_Vulnerability.setter
    def attackimpact_Vulnerability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Vulnerability__attackimpact_Vulnerability", None)
        self.__attackimpact_Vulnerability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attackimpact_Node"):
                opp_val = getattr(old_value, "attackimpact_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attackimpact_Node"):
                opp_val = getattr(value, "attackimpact_Node", None)
                if opp_val is None:
                    setattr(value, "attackimpact_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attackimpact_Vulnerability6(self):
        return self.__attackimpact_Vulnerability6

    @attackimpact_Vulnerability6.setter
    def attackimpact_Vulnerability6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Vulnerability__attackimpact_Vulnerability6", None)
        self.__attackimpact_Vulnerability6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attackimpact_Propagation7"):
                    opp_val = getattr(item, "attackimpact_Propagation7", None)
                    
                    if opp_val == self:
                        setattr(item, "attackimpact_Propagation7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attackimpact_Propagation7"):
                    opp_val = getattr(item, "attackimpact_Propagation7", None)
                    
                    setattr(item, "attackimpact_Propagation7", self)
                    

class attackimpact_Node:

    def __init__(self, tags: str, domains: str, name: str, description: str, attackimpact_Node4: "attackimpact_EObject" = None, attackimpact_Node: set["attackimpact_Vulnerability"] = None, attackimpact_Node2: set["attackimpact_Propagation"] = None, attackimpact_Node10: "attackimpact_Propagation" = None, attackimpact_Node12: "attackimpact_Model" = None):
        self.tags = tags
        self.domains = domains
        self.name = name
        self.description = description
        self.attackimpact_Node4 = attackimpact_Node4
        self.attackimpact_Node = attackimpact_Node if attackimpact_Node is not None else set()
        self.attackimpact_Node2 = attackimpact_Node2 if attackimpact_Node2 is not None else set()
        self.attackimpact_Node10 = attackimpact_Node10
        self.attackimpact_Node12 = attackimpact_Node12
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def tags(self) -> str:
        return self.__tags

    @tags.setter
    def tags(self, tags: str):
        self.__tags = tags

    @property
    def domains(self) -> str:
        return self.__domains

    @domains.setter
    def domains(self, domains: str):
        self.__domains = domains

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attackimpact_Node(self):
        return self.__attackimpact_Node

    @attackimpact_Node.setter
    def attackimpact_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Node__attackimpact_Node", None)
        self.__attackimpact_Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attackimpact_Vulnerability"):
                    opp_val = getattr(item, "attackimpact_Vulnerability", None)
                    
                    if opp_val == self:
                        setattr(item, "attackimpact_Vulnerability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attackimpact_Vulnerability"):
                    opp_val = getattr(item, "attackimpact_Vulnerability", None)
                    
                    setattr(item, "attackimpact_Vulnerability", self)
                    

    @property
    def attackimpact_Node4(self):
        return self.__attackimpact_Node4

    @attackimpact_Node4.setter
    def attackimpact_Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Node__attackimpact_Node4", None)
        self.__attackimpact_Node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attackimpact_EObject"):
                opp_val = getattr(old_value, "attackimpact_EObject", None)
                if opp_val == self:
                    setattr(old_value, "attackimpact_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attackimpact_EObject"):
                opp_val = getattr(value, "attackimpact_EObject", None)
                setattr(value, "attackimpact_EObject", self)

    @property
    def attackimpact_Node2(self):
        return self.__attackimpact_Node2

    @attackimpact_Node2.setter
    def attackimpact_Node2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Node__attackimpact_Node2", None)
        self.__attackimpact_Node2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attackimpact_Propagation"):
                    opp_val = getattr(item, "attackimpact_Propagation", None)
                    
                    if opp_val == self:
                        setattr(item, "attackimpact_Propagation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attackimpact_Propagation"):
                    opp_val = getattr(item, "attackimpact_Propagation", None)
                    
                    setattr(item, "attackimpact_Propagation", self)
                    

    @property
    def attackimpact_Node10(self):
        return self.__attackimpact_Node10

    @attackimpact_Node10.setter
    def attackimpact_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Node__attackimpact_Node10", None)
        self.__attackimpact_Node10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attackimpact_Propagation9"):
                opp_val = getattr(old_value, "attackimpact_Propagation9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attackimpact_Propagation9"):
                opp_val = getattr(value, "attackimpact_Propagation9", None)
                if opp_val is None:
                    setattr(value, "attackimpact_Propagation9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attackimpact_Node12(self):
        return self.__attackimpact_Node12

    @attackimpact_Node12.setter
    def attackimpact_Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attackimpact_Node__attackimpact_Node12", None)
        self.__attackimpact_Node12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attackimpact_Model"):
                opp_val = getattr(old_value, "attackimpact_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attackimpact_Model"):
                opp_val = getattr(value, "attackimpact_Model", None)
                if opp_val is None:
                    setattr(value, "attackimpact_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class attackimpact_EObject:

    pass