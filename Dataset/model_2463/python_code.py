from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MarkerKind(Enum):
    value = "value"
    INTERNALEVENT = "INTERNALEVENT"
    EXTERNALEVENT = "EXTERNALEVENT"
    ACTIONNEEDED = "ACTIONNEEDED"
    THRESHOLDREACHED = "THRESHOLDREACHED"


############################################
# Definition of Classes
############################################

class operators_ResourceMonitor:

    pass
class operators_ResourceForecast:

    pass
class operators_Relationship:

    def __init__(self, name: str, operators_Relationship68: "operators_Node" = None, operators_Relationship71: "operators_Protocol" = None, operators_Relationship: "operators_Node" = None):
        self.name = name
        self.operators_Relationship68 = operators_Relationship68
        self.operators_Relationship71 = operators_Relationship71
        self.operators_Relationship = operators_Relationship
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def operators_Relationship(self):
        return self.__operators_Relationship

    @operators_Relationship.setter
    def operators_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Relationship__operators_Relationship", None)
        self.__operators_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Node66"):
                opp_val = getattr(old_value, "operators_Node66", None)
                if opp_val == self:
                    setattr(old_value, "operators_Node66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Node66"):
                opp_val = getattr(value, "operators_Node66", None)
                setattr(value, "operators_Node66", self)

    @property
    def operators_Relationship71(self):
        return self.__operators_Relationship71

    @operators_Relationship71.setter
    def operators_Relationship71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Relationship__operators_Relationship71", None)
        self.__operators_Relationship71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Protocol"):
                opp_val = getattr(old_value, "operators_Protocol", None)
                if opp_val == self:
                    setattr(old_value, "operators_Protocol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Protocol"):
                opp_val = getattr(value, "operators_Protocol", None)
                setattr(value, "operators_Protocol", self)

    @property
    def operators_Relationship68(self):
        return self.__operators_Relationship68

    @operators_Relationship68.setter
    def operators_Relationship68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Relationship__operators_Relationship68", None)
        self.__operators_Relationship68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Node69"):
                opp_val = getattr(old_value, "operators_Node69", None)
                if opp_val == self:
                    setattr(old_value, "operators_Node69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Node69"):
                opp_val = getattr(value, "operators_Node69", None)
                setattr(value, "operators_Node69", self)

class operators_Protocol:

    pass
class operators_ServiceUser:

    pass
class operators_Service:

    pass
class operators_ResourceExpansion:

    pass
class Company:

    pass
class operators_Operator(Company):

    pass
class operators_Room:

    pass
class operators_Warehouse:

    def __init__(self, equipments: str, description: str, name: str, operators_Warehouse: "operators_Operator" = None, operators_Warehouse86: set["operators_Node"] = None):
        self.equipments = equipments
        self.description = description
        self.name = name
        self.operators_Warehouse = operators_Warehouse
        self.operators_Warehouse86 = operators_Warehouse86 if operators_Warehouse86 is not None else set()
        
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
    def equipments(self) -> str:
        return self.__equipments

    @equipments.setter
    def equipments(self, equipments: str):
        self.__equipments = equipments

    @property
    def operators_Warehouse86(self):
        return self.__operators_Warehouse86

    @operators_Warehouse86.setter
    def operators_Warehouse86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Warehouse__operators_Warehouse86", None)
        self.__operators_Warehouse86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_Node87"):
                    opp_val = getattr(item, "operators_Node87", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_Node87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_Node87"):
                    opp_val = getattr(item, "operators_Node87", None)
                    
                    setattr(item, "operators_Node87", self)
                    

    @property
    def operators_Warehouse(self):
        return self.__operators_Warehouse

    @operators_Warehouse.setter
    def operators_Warehouse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Warehouse__operators_Warehouse", None)
        self.__operators_Warehouse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Operator55"):
                opp_val = getattr(old_value, "operators_Operator55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Operator55"):
                opp_val = getattr(value, "operators_Operator55", None)
                if opp_val is None:
                    setattr(value, "operators_Operator55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class operators_Lifecycle:

    pass
class operators_Person:

    pass
class operators_MetricSource:

    pass
class operators_DiagramInfo:

    pass
class operators_Network:

    def __init__(self, createdDate: str, description: str, name: str, operators_Network19: set["operators_Node"] = None, operators_Network22: "operators_Network" = None, operators_Network20: set["operators_Network"] = None, operators_Network: set["operators_DiagramInfo"] = None, operators_Network30: set["operators_MetricSource"] = None, operators_Network32: "operators_Person" = None, operators_Network24: set["operators_FunctionRelationship"] = None, operators_Network27: set["operators_EquipmentRelationship"] = None, operators_Network53: "operators_Operator" = None):
        self.createdDate = createdDate
        self.description = description
        self.name = name
        self.operators_Network19 = operators_Network19 if operators_Network19 is not None else set()
        self.operators_Network22 = operators_Network22
        self.operators_Network20 = operators_Network20 if operators_Network20 is not None else set()
        self.operators_Network = operators_Network if operators_Network is not None else set()
        self.operators_Network30 = operators_Network30 if operators_Network30 is not None else set()
        self.operators_Network32 = operators_Network32
        self.operators_Network24 = operators_Network24 if operators_Network24 is not None else set()
        self.operators_Network27 = operators_Network27 if operators_Network27 is not None else set()
        self.operators_Network53 = operators_Network53
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def createdDate(self) -> str:
        return self.__createdDate

    @createdDate.setter
    def createdDate(self, createdDate: str):
        self.__createdDate = createdDate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def operators_Network22(self):
        return self.__operators_Network22

    @operators_Network22.setter
    def operators_Network22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network22", None)
        self.__operators_Network22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Network20"):
                opp_val = getattr(old_value, "operators_Network20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Network20"):
                opp_val = getattr(value, "operators_Network20", None)
                if opp_val is None:
                    setattr(value, "operators_Network20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Network(self):
        return self.__operators_Network

    @operators_Network.setter
    def operators_Network(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network", None)
        self.__operators_Network = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_DiagramInfo"):
                    opp_val = getattr(item, "operators_DiagramInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_DiagramInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_DiagramInfo"):
                    opp_val = getattr(item, "operators_DiagramInfo", None)
                    
                    setattr(item, "operators_DiagramInfo", self)
                    

    @property
    def operators_Network19(self):
        return self.__operators_Network19

    @operators_Network19.setter
    def operators_Network19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network19", None)
        self.__operators_Network19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_Node"):
                    opp_val = getattr(item, "operators_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_Node"):
                    opp_val = getattr(item, "operators_Node", None)
                    
                    setattr(item, "operators_Node", self)
                    

    @property
    def operators_Network32(self):
        return self.__operators_Network32

    @operators_Network32.setter
    def operators_Network32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network32", None)
        self.__operators_Network32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Person"):
                opp_val = getattr(old_value, "operators_Person", None)
                if opp_val == self:
                    setattr(old_value, "operators_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Person"):
                opp_val = getattr(value, "operators_Person", None)
                setattr(value, "operators_Person", self)

    @property
    def operators_Network53(self):
        return self.__operators_Network53

    @operators_Network53.setter
    def operators_Network53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network53", None)
        self.__operators_Network53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Operator"):
                opp_val = getattr(old_value, "operators_Operator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Operator"):
                opp_val = getattr(value, "operators_Operator", None)
                if opp_val is None:
                    setattr(value, "operators_Operator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Network27(self):
        return self.__operators_Network27

    @operators_Network27.setter
    def operators_Network27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network27", None)
        self.__operators_Network27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_EquipmentRelationship28"):
                    opp_val = getattr(item, "operators_EquipmentRelationship28", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_EquipmentRelationship28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_EquipmentRelationship28"):
                    opp_val = getattr(item, "operators_EquipmentRelationship28", None)
                    
                    setattr(item, "operators_EquipmentRelationship28", self)
                    

    @property
    def operators_Network24(self):
        return self.__operators_Network24

    @operators_Network24.setter
    def operators_Network24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network24", None)
        self.__operators_Network24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_FunctionRelationship25"):
                    opp_val = getattr(item, "operators_FunctionRelationship25", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_FunctionRelationship25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_FunctionRelationship25"):
                    opp_val = getattr(item, "operators_FunctionRelationship25", None)
                    
                    setattr(item, "operators_FunctionRelationship25", self)
                    

    @property
    def operators_Network30(self):
        return self.__operators_Network30

    @operators_Network30.setter
    def operators_Network30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network30", None)
        self.__operators_Network30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_MetricSource"):
                    opp_val = getattr(item, "operators_MetricSource", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_MetricSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_MetricSource"):
                    opp_val = getattr(item, "operators_MetricSource", None)
                    
                    setattr(item, "operators_MetricSource", self)
                    

    @property
    def operators_Network20(self):
        return self.__operators_Network20

    @operators_Network20.setter
    def operators_Network20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network20", None)
        self.__operators_Network20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_Network22"):
                    opp_val = getattr(item, "operators_Network22", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_Network22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_Network22"):
                    opp_val = getattr(item, "operators_Network22", None)
                    
                    setattr(item, "operators_Network22", self)
                    

class operators_Node:

    def __init__(self, nodeID: str, operators_Node: "operators_Network" = None, operators_Node34: "operators_Lifecycle" = None, operators_Node36: set["operators_Function"] = None, operators_Node45: "operators_Equipment" = None, operators_Node48: "operators_Function" = None, operators_Node39: set["operators_Equipment"] = None, operators_Node42: "operators_Person" = None, operators_Node51: "operators_Room" = None, operators_Node69: "operators_Relationship" = None, operators_Node66: "operators_Relationship" = None, operators_Node74: "operators_ResourceExpansion" = None, operators_Node87: "operators_Warehouse" = None):
        self.nodeID = nodeID
        self.operators_Node = operators_Node
        self.operators_Node34 = operators_Node34
        self.operators_Node36 = operators_Node36 if operators_Node36 is not None else set()
        self.operators_Node45 = operators_Node45
        self.operators_Node48 = operators_Node48
        self.operators_Node39 = operators_Node39 if operators_Node39 is not None else set()
        self.operators_Node42 = operators_Node42
        self.operators_Node51 = operators_Node51
        self.operators_Node69 = operators_Node69
        self.operators_Node66 = operators_Node66
        self.operators_Node74 = operators_Node74
        self.operators_Node87 = operators_Node87
        
    @property
    def nodeID(self) -> str:
        return self.__nodeID

    @nodeID.setter
    def nodeID(self, nodeID: str):
        self.__nodeID = nodeID

    @property
    def operators_Node(self):
        return self.__operators_Node

    @operators_Node.setter
    def operators_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node", None)
        self.__operators_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Network19"):
                opp_val = getattr(old_value, "operators_Network19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Network19"):
                opp_val = getattr(value, "operators_Network19", None)
                if opp_val is None:
                    setattr(value, "operators_Network19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Node36(self):
        return self.__operators_Node36

    @operators_Node36.setter
    def operators_Node36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node36", None)
        self.__operators_Node36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_Function37"):
                    opp_val = getattr(item, "operators_Function37", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_Function37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_Function37"):
                    opp_val = getattr(item, "operators_Function37", None)
                    
                    setattr(item, "operators_Function37", self)
                    

    @property
    def operators_Node69(self):
        return self.__operators_Node69

    @operators_Node69.setter
    def operators_Node69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node69", None)
        self.__operators_Node69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Relationship68"):
                opp_val = getattr(old_value, "operators_Relationship68", None)
                if opp_val == self:
                    setattr(old_value, "operators_Relationship68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Relationship68"):
                opp_val = getattr(value, "operators_Relationship68", None)
                setattr(value, "operators_Relationship68", self)

    @property
    def operators_Node66(self):
        return self.__operators_Node66

    @operators_Node66.setter
    def operators_Node66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node66", None)
        self.__operators_Node66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Relationship"):
                opp_val = getattr(old_value, "operators_Relationship", None)
                if opp_val == self:
                    setattr(old_value, "operators_Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Relationship"):
                opp_val = getattr(value, "operators_Relationship", None)
                setattr(value, "operators_Relationship", self)

    @property
    def operators_Node39(self):
        return self.__operators_Node39

    @operators_Node39.setter
    def operators_Node39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node39", None)
        self.__operators_Node39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_Equipment40"):
                    opp_val = getattr(item, "operators_Equipment40", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_Equipment40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_Equipment40"):
                    opp_val = getattr(item, "operators_Equipment40", None)
                    
                    setattr(item, "operators_Equipment40", self)
                    

    @property
    def operators_Node74(self):
        return self.__operators_Node74

    @operators_Node74.setter
    def operators_Node74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node74", None)
        self.__operators_Node74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_ResourceExpansion73"):
                opp_val = getattr(old_value, "operators_ResourceExpansion73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_ResourceExpansion73"):
                opp_val = getattr(value, "operators_ResourceExpansion73", None)
                if opp_val is None:
                    setattr(value, "operators_ResourceExpansion73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Node51(self):
        return self.__operators_Node51

    @operators_Node51.setter
    def operators_Node51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node51", None)
        self.__operators_Node51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Room"):
                opp_val = getattr(old_value, "operators_Room", None)
                if opp_val == self:
                    setattr(old_value, "operators_Room", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Room"):
                opp_val = getattr(value, "operators_Room", None)
                setattr(value, "operators_Room", self)

    @property
    def operators_Node48(self):
        return self.__operators_Node48

    @operators_Node48.setter
    def operators_Node48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node48", None)
        self.__operators_Node48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Function49"):
                opp_val = getattr(old_value, "operators_Function49", None)
                if opp_val == self:
                    setattr(old_value, "operators_Function49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Function49"):
                opp_val = getattr(value, "operators_Function49", None)
                setattr(value, "operators_Function49", self)

    @property
    def operators_Node34(self):
        return self.__operators_Node34

    @operators_Node34.setter
    def operators_Node34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node34", None)
        self.__operators_Node34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Lifecycle"):
                opp_val = getattr(old_value, "operators_Lifecycle", None)
                if opp_val == self:
                    setattr(old_value, "operators_Lifecycle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Lifecycle"):
                opp_val = getattr(value, "operators_Lifecycle", None)
                setattr(value, "operators_Lifecycle", self)

    @property
    def operators_Node87(self):
        return self.__operators_Node87

    @operators_Node87.setter
    def operators_Node87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node87", None)
        self.__operators_Node87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Warehouse86"):
                opp_val = getattr(old_value, "operators_Warehouse86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Warehouse86"):
                opp_val = getattr(value, "operators_Warehouse86", None)
                if opp_val is None:
                    setattr(value, "operators_Warehouse86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Node45(self):
        return self.__operators_Node45

    @operators_Node45.setter
    def operators_Node45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node45", None)
        self.__operators_Node45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Equipment46"):
                opp_val = getattr(old_value, "operators_Equipment46", None)
                if opp_val == self:
                    setattr(old_value, "operators_Equipment46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Equipment46"):
                opp_val = getattr(value, "operators_Equipment46", None)
                setattr(value, "operators_Equipment46", self)

    @property
    def operators_Node42(self):
        return self.__operators_Node42

    @operators_Node42.setter
    def operators_Node42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node42", None)
        self.__operators_Node42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Person43"):
                opp_val = getattr(old_value, "operators_Person43", None)
                if opp_val == self:
                    setattr(old_value, "operators_Person43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Person43"):
                opp_val = getattr(value, "operators_Person43", None)
                setattr(value, "operators_Person43", self)

class operators_Value:

    pass
class operators_Function:

    pass
class operators_Marker:

    def __init__(self, kind: str, description: str, operators_Marker: "operators_Equipment" = None, operators_Marker13: "operators_Function" = None, operators_Marker16: "operators_Value" = None, operators_Marker82: "operators_ResourceForecast" = None, operators_Marker84: "operators_ResourceMonitor" = None):
        self.kind = kind
        self.description = description
        self.operators_Marker = operators_Marker
        self.operators_Marker13 = operators_Marker13
        self.operators_Marker16 = operators_Marker16
        self.operators_Marker82 = operators_Marker82
        self.operators_Marker84 = operators_Marker84
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def operators_Marker13(self):
        return self.__operators_Marker13

    @operators_Marker13.setter
    def operators_Marker13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Marker__operators_Marker13", None)
        self.__operators_Marker13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Function14"):
                opp_val = getattr(old_value, "operators_Function14", None)
                if opp_val == self:
                    setattr(old_value, "operators_Function14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Function14"):
                opp_val = getattr(value, "operators_Function14", None)
                setattr(value, "operators_Function14", self)

    @property
    def operators_Marker16(self):
        return self.__operators_Marker16

    @operators_Marker16.setter
    def operators_Marker16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Marker__operators_Marker16", None)
        self.__operators_Marker16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Value"):
                opp_val = getattr(old_value, "operators_Value", None)
                if opp_val == self:
                    setattr(old_value, "operators_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Value"):
                opp_val = getattr(value, "operators_Value", None)
                setattr(value, "operators_Value", self)

    @property
    def operators_Marker82(self):
        return self.__operators_Marker82

    @operators_Marker82.setter
    def operators_Marker82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Marker__operators_Marker82", None)
        self.__operators_Marker82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_ResourceForecast"):
                opp_val = getattr(old_value, "operators_ResourceForecast", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_ResourceForecast"):
                opp_val = getattr(value, "operators_ResourceForecast", None)
                if opp_val is None:
                    setattr(value, "operators_ResourceForecast", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Marker84(self):
        return self.__operators_Marker84

    @operators_Marker84.setter
    def operators_Marker84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Marker__operators_Marker84", None)
        self.__operators_Marker84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_ResourceMonitor"):
                opp_val = getattr(old_value, "operators_ResourceMonitor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_ResourceMonitor"):
                opp_val = getattr(value, "operators_ResourceMonitor", None)
                if opp_val is None:
                    setattr(value, "operators_ResourceMonitor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Marker(self):
        return self.__operators_Marker

    @operators_Marker.setter
    def operators_Marker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Marker__operators_Marker", None)
        self.__operators_Marker = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Equipment11"):
                opp_val = getattr(old_value, "operators_Equipment11", None)
                if opp_val == self:
                    setattr(old_value, "operators_Equipment11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Equipment11"):
                opp_val = getattr(value, "operators_Equipment11", None)
                setattr(value, "operators_Equipment11", self)

class operators_ExpansionExperience:

    def __init__(self, duration: str, operators_ExpansionExperience: "operators_Equipment" = None, operators_ExpansionExperience64: "operators_Operator" = None):
        self.duration = duration
        self.operators_ExpansionExperience = operators_ExpansionExperience
        self.operators_ExpansionExperience64 = operators_ExpansionExperience64
        
    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def operators_ExpansionExperience(self):
        return self.__operators_ExpansionExperience

    @operators_ExpansionExperience.setter
    def operators_ExpansionExperience(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_ExpansionExperience__operators_ExpansionExperience", None)
        self.__operators_ExpansionExperience = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Equipment5"):
                opp_val = getattr(old_value, "operators_Equipment5", None)
                if opp_val == self:
                    setattr(old_value, "operators_Equipment5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Equipment5"):
                opp_val = getattr(value, "operators_Equipment5", None)
                setattr(value, "operators_Equipment5", self)

    @property
    def operators_ExpansionExperience64(self):
        return self.__operators_ExpansionExperience64

    @operators_ExpansionExperience64.setter
    def operators_ExpansionExperience64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_ExpansionExperience__operators_ExpansionExperience64", None)
        self.__operators_ExpansionExperience64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Operator63"):
                opp_val = getattr(old_value, "operators_Operator63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Operator63"):
                opp_val = getattr(value, "operators_Operator63", None)
                if opp_val is None:
                    setattr(value, "operators_Operator63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class operators_Equipment:

    pass
class Relationship:

    pass
class operators_FunctionRelationship(Relationship):

    pass
class operators_EquipmentRelationship(Relationship):

    pass